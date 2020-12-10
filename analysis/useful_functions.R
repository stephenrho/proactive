# useful functions from http://www.cookbook-r.com/Graphs/Plotting_means_and_error_bars_(ggplot2)/

## Gives count, mean, standard deviation, standard error of the mean, and confidence interval (default 95%).
##   data: a data frame.
##   measurevar: the name of a column that contains the variable to be summariezed
##   groupvars: a vector containing names of columns that contain grouping variables
##   na.rm: a boolean that indicates whether to ignore NA's
##   conf.interval: the percent range of the confidence interval (default is 95%)
summarySE <- function(data=NULL, measurevar, groupvars=NULL, na.rm=FALSE,
                      conf.interval=.95, .drop=TRUE) {
  library(plyr)
  
  # New version of length which can handle NA's: if na.rm==T, don't count them
  length2 <- function (x, na.rm=FALSE) {
    if (na.rm) sum(!is.na(x))
    else       length(x)
  }
  
  # This does the summary. For each group's data frame, return a vector with
  # N, mean, and sd
  datac <- ddply(data, groupvars, .drop=.drop,
                 .fun = function(xx, col) {
                   c(N    = length2(xx[[col]], na.rm=na.rm),
                     mean = mean   (xx[[col]], na.rm=na.rm),
                     sd   = sd     (xx[[col]], na.rm=na.rm)
                   )
                 },
                 measurevar
  )
  
  # Rename the "mean" column    
  datac <- rename(datac, c("mean" = measurevar))
  
  datac$se <- datac$sd / sqrt(datac$N)  # Calculate standard error of the mean
  
  # Confidence interval multiplier for standard error
  # Calculate t-statistic for confidence interval: 
  # e.g., if conf.interval is .95, use .975 (above/below), and use df=N-1
  ciMult <- qt(conf.interval/2 + .5, datac$N-1)
  datac$ci <- datac$se * ciMult
  
  return(datac)
}

## Norms the data within specified groups in a data frame; it normalizes each
## subject (identified by idvar) so that they have the same mean, within each group
## specified by betweenvars.
##   data: a data frame.
##   idvar: the name of a column that identifies each subject (or matched subjects)
##   measurevar: the name of a column that contains the variable to be summariezed
##   betweenvars: a vector containing names of columns that are between-subjects variables
##   na.rm: a boolean that indicates whether to ignore NA's
normDataWithin <- function(data=NULL, idvar, measurevar, betweenvars=NULL,
                           na.rm=FALSE, .drop=TRUE) {
  library(plyr)
  
  # Measure var on left, idvar + between vars on right of formula.
  data.subjMean <- ddply(data, c(idvar, betweenvars), .drop=.drop,
                         .fun = function(xx, col, na.rm) {
                           c(subjMean = mean(xx[,col], na.rm=na.rm))
                         },
                         measurevar,
                         na.rm
  )
  
  # Put the subject means with original data
  data <- merge(data, data.subjMean)
  
  # Get the normalized data in a new column
  measureNormedVar <- paste(measurevar, "_norm", sep="")
  data[,measureNormedVar] <- data[,measurevar] - data[,"subjMean"] +
    mean(data[,measurevar], na.rm=na.rm)
  
  # Remove this subject mean column
  data$subjMean <- NULL
  
  return(data)
}

## Summarizes data, handling within-subjects variables by removing inter-subject variability.
## It will still work if there are no within-S variables.
## Gives count, un-normed mean, normed mean (with same between-group mean),
##   standard deviation, standard error of the mean, and confidence interval.
## If there are within-subject variables, calculate adjusted values using method from Morey (2008).
##   data: a data frame.
##   measurevar: the name of a column that contains the variable to be summariezed
##   betweenvars: a vector containing names of columns that are between-subjects variables
##   withinvars: a vector containing names of columns that are within-subjects variables
##   idvar: the name of a column that identifies each subject (or matched subjects)
##   na.rm: a boolean that indicates whether to ignore NA's
##   conf.interval: the percent range of the confidence interval (default is 95%)
summarySEwithin <- function(data=NULL, measurevar, betweenvars=NULL, withinvars=NULL,
                            idvar=NULL, na.rm=FALSE, conf.interval=.95, .drop=TRUE) {
  
  # Ensure that the betweenvars and withinvars are factors
  factorvars <- vapply(data[, c(betweenvars, withinvars), drop=FALSE],
                       FUN=is.factor, FUN.VALUE=logical(1))
  
  if (!all(factorvars)) {
    nonfactorvars <- names(factorvars)[!factorvars]
    message("Automatically converting the following non-factors to factors: ",
            paste(nonfactorvars, collapse = ", "))
    data[nonfactorvars] <- lapply(data[nonfactorvars], factor)
  }
  
  # Get the means from the un-normed data
  datac <- summarySE(data, measurevar, groupvars=c(betweenvars, withinvars),
                     na.rm=na.rm, conf.interval=conf.interval, .drop=.drop)
  
  # Drop all the unused columns (these will be calculated with normed data)
  datac$sd <- NULL
  datac$se <- NULL
  datac$ci <- NULL
  
  # Norm each subject's data
  ndata <- normDataWithin(data, idvar, measurevar, betweenvars, na.rm, .drop=.drop)
  
  # This is the name of the new column
  measurevar_n <- paste(measurevar, "_norm", sep="")
  
  # Collapse the normed data - now we can treat between and within vars the same
  ndatac <- summarySE(ndata, measurevar_n, groupvars=c(betweenvars, withinvars),
                      na.rm=na.rm, conf.interval=conf.interval, .drop=.drop)
  
  # Apply correction from Morey (2008) to the standard error and confidence interval
  #  Get the product of the number of conditions of within-S variables
  nWithinGroups    <- prod(vapply(ndatac[,withinvars, drop=FALSE], FUN=nlevels,
                                  FUN.VALUE=numeric(1)))
  correctionFactor <- sqrt( nWithinGroups / (nWithinGroups-1) )
  
  # Apply the correction factor
  ndatac$sd <- ndatac$sd * correctionFactor
  ndatac$se <- ndatac$se * correctionFactor
  ndatac$ci <- ndatac$ci * correctionFactor
  
  # Combine the un-normed means with the normed results
  merge(datac, ndatac)
}

# for plotting 

errBars <- function(means = NULL, error = NULL, lower = NULL, upper = NULL, xpos = NULL, whiskerWidth = .1){
  # conveniance function for plotting error bars
  # xpos allows user to specify x axis position (i.e. for jittering)
  
  if (is.null(error) & (is.null(lower) | is.null(upper))){
    stop("must specify error or lower and upper")
  }
  
  if (!is.null(error) & is.null(means)){
    stop("if providing error, you must also specify means")
  }
  
  if (is.null(xpos)){
    xpos = 1:length(means)
  }
  
  if (!is.null(error)){
    lower = means - error 
    upper = means + error
  }
  
  # error bar
  segments(x0 = xpos, y0 = lower, x1 = xpos, y1 = upper)
  # bottom whisker
  segments(x0 = xpos - whiskerWidth/2, y0 = lower, x1 = xpos + whiskerWidth/2, y1 = lower)
  # top whisker
  segments(x0 = xpos - whiskerWidth/2, y0 = upper, x1 = xpos + whiskerWidth/2, y1 = upper)
}

logistic <- function(x){
  1/(1 + exp(-x))
}

faintCol <- function(colLabs, alpha = 30){
  colVec = c()
  for (i in colLabs){
    RGB = col2rgb(i)
    newcol = rgb(red = RGB[1], green = RGB[2], blue = RGB[3], alpha = alpha, maxColorValue = 255)
    colVec = c(colVec, newcol)
  }
  return(colVec)
}

print_coef = function(obj, eff=1, dp=2){
  tab = summary(obj)$coefficients
  
  est = format(tab[eff, "Estimate"], digits=0, nsmall=dp)
  se = format(tab[eff, "Std. Error"], digits=0, nsmall=dp)
  z = format(tab[eff, "z value"], digits=0, nsmall=dp)
  pv = tab[eff, "Pr(>|z|)"]
  
  if (pv < 0.05){
    pval = ifelse(pv < 0.01, "< 0.01", "< 0.05")
  } else{
    pval = paste0("= ", format(pv, digits=0, nsmall = dp))
  }
  
  stri = paste0("$b$ = ", est, " (SE = ", se, "), $z$ = ", z, ", $p$ ", pval)
  return(stri)
}

print_chi = function(anov, eff=1, dp=2){
  chi = format(anov[eff, "Chisq"], digits=0, nsmall=dp)
  df = anov[eff, "Df"]
  pv = anov[eff, 3]
  
  if (pv < 0.05){
    pval = ifelse(pv < 0.01, "< 0.01", "< 0.05")
  } else{
    pval = paste0("= ", format(pv, digits=0, nsmall = dp))
  }
  
  stri = paste0("$\\chi^2$", "(", df, ") = ", chi, ", $p$ ", pval)
  return(stri)
}

print_t = function(ttest, addbf=T){
  t = ttest$statistic
  df = ttest$parameter
  p = ttest$p.value
  
  d = t2d(t = t, n = df+1)
  dci = d.ci(d, n = df+1)[c(1,3)]
  
  if (p < 0.05){
    pval = ifelse(p < 0.01, "< 0.01", "< 0.05")
  } else{
    pval = paste0("= ", format(p, digits=0, nsmall = 2))
  }
  
  stri = sprintf("$t$(%i) = %.2f, $p$ %s, $d$ = %.2f [%.2f, %.2f]", df, t, pval, d, dci[1], dci[2])
  
  if (addbf){
    bf = ttest.tstat(t = t, n1 = df+1, simple = T)
    if (p < 0.05){
      bfstr = paste0("$BF_{10}$ = ", format(bf, digits=3))
    } else{
      bfstr = paste0("$BF_{01}$ = ", format(1/bf, digits=3))
    }
    
    stri = paste0(stri, ", ", bfstr)
  }
  
  return(stri)
}

print_bf = function(bfobj, foralt=T){
  # bfobj should reflect evidence in favor of alternative
  bf = extractBF(bfobj, onlybf = T)
  
  if (foralt){
    bfstr = paste0("$BF_{10}$ = ", format(bf, digits=3))
  } else{
    bfstr = paste0("$BF_{01}$ = ", format(1/bf, digits=3))
  }
  return(bfstr)
}


