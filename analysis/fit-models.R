
## code for: The influence of long-term memory on working memory: Age-differences in proactive facilitation and interference
# run analyses

# read in combined data files (run "read-...R" and "combine-dataset.R" scripts first)

rm(list=ls())

library(plyr)
library(brms)
library(HDInterval)
library(vioplot)
library(ggplot2)

mh = function(x) c(m=mean(x), hdi(x))

options(mc.cores = parallel::detectCores())

nchains=4
nwarm=1000
niter=3500

(niter- nwarm)*nchains # total samples

setwd(dirname(rstudioapi::getActiveDocumentContext()$path))

wm_dat = read.csv("../data/all_wm.csv")
learn_dat = read.csv("../data/all_learn.csv")
search_dat = read.csv("../data/all_search.csv")
info = read.csv("../data/ppt-info-clean.csv")
info_all = read.csv("../data/ppt-info-all.csv")

source("useful_functions.R")

# participant info table
info_tab = ddply(info, c("interval", "distraction", "group"), summarize,
                 N = length(age),
                 N_female = sum(Sex == "Female"),
                 M_age = mean(age), 
                 SD_age = sd(age),
                 min_age = min(age),
                 max_age = max(age)
)

groups = c("younger", "older")
distractions = c("no", "yes")
intervals = c("2 s", "10 s")

ids = list()
for (i in intervals){
  for (d in distractions){
    for (g in groups){
      ids[[i]][[d]][[g]] = unique(wm_dat$participant[with(wm_dat, group==g & distraction==d & interval==i)])
    }
  }
}


### ### ### ### ### ### ### ### ### ### 
### LEARNING ----
### ### ### ### ### ### ### ### ### ### 

# find bad performers
learn_overall = ddply(learn_dat, c("participant", "interval", "distraction", "group"),
                      summarize,
                      N = length(recall_acc), 
                      acc = mean(recall_acc),
                      mean_rt = mean(recalled_rt),
                      prop_noresp = mean(recalled %in% c("?", "")))

#learn_overall[learn_overall$acc < .5,]

learn_agg = ddply(learn_dat, c("participant", "interval", "distraction", "group", "learn_block"), summarize,
                  N = length(recall_acc), 
                  acc = mean(recall_acc),
                  mean_rt = mean(recalled_rt),
                  prop_noresp = mean(recalled %in% c("?", "")))

learn_agg$learn_block = factor(learn_agg$learn_block, levels = c("1", "2", "3", "final test"))

learn_mse = summarySEwithin(data = learn_agg, measurevar = "acc", betweenvars = c("interval", "distraction", "group"), withinvars = "learn_block")


### plot 1: overall performance in each learning block + final test performance

jitts = c("younger" = -.08, "older" = .08)
cols = c("younger" = "deepskyblue4", "older" = "firebrick")

par(mfcol=c(2,2), mar=c(2,2,2,2), oma=c(0,2,0,0))

for (i in intervals){
  for (d in distractions){
    plot(NA, xlim=c(.7,4.3), ylim=c(0,1), xlab="", ylab="Recall Accuracy", axes=F)
    #box()
    axis(1, at = 1:4, labels = c("Block 1", "Block 2", "Block 3", "Final Test"))
    axis(2)
    mtext(paste(i, c("with distraction", "no distraction")[(d=="no")+1]), adj = 0)
    
    for (g in groups){
      l_ply(.data = ids[[i]][[d]][[g]], .fun = function(x) with(subset(learn_agg, participant==x), points(jitter(as.numeric(learn_block)+jitts[g], amount = .025), acc, pch=16, col=faintCol(cols[g]), type='p')))
    }
    for (g in groups){
      # error bars
      with(subset(learn_mse, distraction==d & interval==i & group==g), errBars(means = acc, error = se, xpos = as.numeric(learn_block)+jitts[g]))
      # points
      with(subset(learn_mse, distraction==d & interval==i & group==g), points(as.numeric(learn_block)+jitts[g], acc, pch=16, col=cols[g], type='b'))
    }
  }
}

legend("bottomright", legend = groups, pch=16, col=cols, bty='n')

mtext("Learning Accuracy", 2, outer = T)

par(mfcol=c(1,1))

## analysis
LOAD = F # set to F to (re-)run models

learn_dat = within(learn_dat, {
  distraction = as.factor(distraction)
  interval = as.factor(interval)
  group = as.factor(group)
})

options(contrasts=c("contr.sum", "contr.sum")) # sum-to-zero coding

contrasts(learn_dat$distraction)
contrasts(learn_dat$interval)
contrasts(learn_dat$group)
learn_dat$word_fac = as.factor(learn_dat$word) # for random effect

if (!LOAD){
  # priors
  priors = c(set_prior("cauchy(0, 2.5)", class = "Intercept"),
             set_prior("cauchy(0, 1)", class = "b"),
             set_prior("cauchy(0, 2.5)", class = "sd"))
  
  # fit model
  learn_brm1 = brm(recall_acc ~ distraction*interval*group + 
                     (1 | participant) + (1 | word_fac), 
                   data = subset(learn_dat, learn_block=="final test"), 
                   family = bernoulli(link = "logit"), 
                   prior = priors, 
                   sample_prior = "yes",
                   chains=nchains,
                   iter=niter,
                   warmup=nwarm
  )
  
  saveRDS(learn_brm1, file = "rds-files/learn_brm1.rds")
  
} else {
  learn_brm1 = readRDS("rds-files/learn_brm1.rds")
}

# transform posterior to probabilities
learn_newd = expand.grid(distraction=c("yes", "no"), 
                         interval=c("2 s", "10 s"), 
                         group=c("younger", "older"))

learn_fitp = posterior_epred(learn_brm1, newdata = learn_newd, 
                             re_formula = NA, transform = T)

colnames(learn_fitp) = with(learn_newd, paste(distraction, interval, group, sep = "-"))

apply(learn_fitp, 2, function(x) c(mean = mean(x), se = sd(x), hdi(x)))

hist(learn_fitp[,"yes-2 s-younger"])
plot(density(learn_fitp[,"yes-2 s-younger"]))

plot(density(learn_fitp[,"yes-2 s-younger"] - learn_fitp[,"yes-2 s-older"]))
plot(density(learn_fitp[,"yes-10 s-younger"] - learn_fitp[,"yes-10 s-older"]))
plot(density(learn_fitp[,"no-2 s-younger"] - learn_fitp[,"no-2 s-older"]))
plot(density(learn_fitp[,"no-10 s-younger"] - learn_fitp[,"no-10 s-older"]))


vioplot2 = function(x, at=1, add=T, col="grey"){
  # wrapper function to plot vioplot and 
  # 95% HDI in same call
  vioplot(x = x, horizontal = T, at = at, 
          add = add, axes=F, drawRect = F, 
          col = col, border = NA)
  
  hdint = hdi(x)
  segments(x0 = hdint["lower"], y0 = at, 
           x1 = hdint["upper"], y1 = at, 
           lwd = 4, lend=2)
  
  points(x = mean(x), y = at, pch=16, cex=1.5)
}

# plot age contrasts across different combinations of conditions
par(mar=c(5, 7, 4, 2)+.1)
plot(NA, xlim=c(-.12, .22), ylim=c(0.5,6.5), xlab="Age difference in learning accuracy", ylab = "", axes=F)
box()
axis(1)
axis(2, at = 6:1, labels = c("no - 2 s", "yes - 2 s", 
                             "no - 10 s", "yes - 10 s",
                             "yes vs. no", "2 s vs. 10 s"), las=1)

vioplot2(learn_fitp[,"no-2 s-younger"] - learn_fitp[,"no-2 s-older"], at = 6)
vioplot2(learn_fitp[,"yes-2 s-younger"] - learn_fitp[,"yes-2 s-older"], at = 5)
vioplot2(learn_fitp[,"no-10 s-younger"] - learn_fitp[,"no-10 s-older"], at = 4)
vioplot2(learn_fitp[,"yes-10 s-younger"] - learn_fitp[,"yes-10 s-older"], at = 3)

yvn = .5*((learn_fitp[,"yes-10 s-younger"] - learn_fitp[,"yes-10 s-older"]) +
            (learn_fitp[,"yes-2 s-younger"] - learn_fitp[,"yes-2 s-older"])) -
  .5*((learn_fitp[,"no-10 s-younger"] - learn_fitp[,"no-10 s-older"]) +
        (learn_fitp[,"no-2 s-younger"] - learn_fitp[,"no-2 s-older"]))

vioplot2(yvn, at = 2)

s2vs10 = .5*((learn_fitp[,"yes-10 s-younger"] - learn_fitp[,"yes-10 s-older"]) +
               (learn_fitp[,"no-10 s-younger"] - learn_fitp[,"no-10 s-older"])) -
  .5*( (learn_fitp[,"yes-2 s-younger"] - learn_fitp[,"yes-2 s-older"])+
         (learn_fitp[,"no-2 s-younger"] - learn_fitp[,"no-2 s-older"]))

vioplot2(s2vs10, at = 1)

abline(v=0, lty=2)

par(mar=c(5, 4, 4, 2)+.1)

### ### ### ### ### ### ### ### ### ### 
### WORKING MEMORY -----
### ### ### ### ### ### ### ### ### ### 

wm_overall = ddply(wm_dat, c("participant", "interval", "distraction", "group"), summarize,
                   N = length(recall_acc),
                   acc = mean(recall_acc),
                   mean_rt = mean(recall_rt))

hist(wm_overall$acc) # overall accuracy across participants

# aggregate for plot
wm_agg = ddply(wm_dat, c("participant", "interval", "distraction", "group", "item_type"), summarize,
               N = length(recall_acc),
               acc = mean(recall_acc),
               mean_rt = mean(recall_rt),
               ltm_int = mean(ltm_intru))

wm_agg$item_type = as.factor(wm_agg$item_type)

wm_mse = summarySEwithin(data = wm_agg, measurevar = "acc", 
                         betweenvars = c("interval", "distraction", "group"), 
                         withinvars = "item_type")

### plot 2: performance in the wm task by item type

par(mfcol=c(2,2), mar=c(2,2,2,2), oma=c(0,2,0,0))

for (i in intervals){
  for (d in distractions){
    plot(NA, xlim=c(.7,4.3), ylim=c(0,1), xlab="", ylab="Recall Accuracy", axes=F)
    #box()
    labs = levels(wm_agg$item_type)
    labs[labs=="new-new"]="new"
    axis(1, at = 1:4, labels = labs)
    axis(2)
    mtext(paste(i, c("with distraction", "no distraction")[(d=="no")+1]), adj = 0)
    
    for (g in groups){
      l_ply(.data = ids[[i]][[d]][[g]], .fun = function(x) with(subset(wm_agg, participant==x), points(jitter(as.numeric(item_type)+jitts[g], amount = .025), acc, pch=16, col=faintCol(cols[g]), type='p')))
    }
    for (g in groups){
      # error bars
      with(subset(wm_mse, distraction==d & interval==i & group==g), errBars(means = acc, error = se, xpos = as.numeric(item_type)+jitts[g]))
      # points
      with(subset(wm_mse, distraction==d & interval==i & group==g), points(as.numeric(item_type)+jitts[g], acc, pch=16, col=cols[g], type='b'))
    }
  }
}

legend("bottomright", legend = groups, pch=16, col=cols, bty='n')

mtext("WM Accuracy", 2, outer = T)

par(mfcol=c(1,1))

## analysis (LOAD is set above)

wm_dat = within(wm_dat, {
  distraction = as.factor(distraction)
  interval = as.factor(interval)
  group = as.factor(group)
  item_type = as.factor(item_type)
})

options(contrasts=c("contr.sum", "contr.sum"))

contrasts(wm_dat$distraction)
contrasts(wm_dat$interval)
contrasts(wm_dat$group)

# specific contrasts of different item types
contrasts(wm_dat$item_type) = cbind(matchVrest = c(1,-1/3,-1/3,-1/3),
                                    newVnonmatch=c(0,-1/2,1,-1/2),
                                    mismatchVoldnew=c(0,1,0,-1))

wm_dat$word_fac = as.factor(wm_dat$word) # for random effect


if (!LOAD){
  # priors
  priors = c(set_prior("cauchy(0, 2.5)", class = "Intercept"),
             set_prior("cauchy(0, 1)", class = "b"),
             set_prior("cauchy(0, 2.5)", class = "sd"),
             set_prior("lkj(1)", class = "cor"))
  
  wm_brm1 = brm(recall_acc ~ distraction*interval*group*item_type + 
                  (1 + item_type | participant) + (1 | word_fac), 
                data = wm_dat, 
                family = bernoulli(link = "logit"), 
                prior = priors, 
                sample_prior = "yes",
                chains=nchains,
                iter=niter,
                warmup=nwarm
  )
  
  # summary(wm_brm1_ml)
  
  saveRDS(wm_brm1, file = "rds-files/wm_brm1.rds")
} else {
  wm_brm1 = readRDS("rds-files/wm_brm1.rds")
}

# transform posterior to probabilities
wm_newd = expand.grid(distraction=NA,
                      interval=NA, 
                      group=c("younger", "older"),
                      item_type = c("match", "mis-match", "new-new", "old-new"))

wm_fitp = posterior_epred(wm_brm1, newdata = wm_newd, re_formula = NA)

colnames(wm_fitp) = with(wm_newd, paste(group, item_type, sep = "-"))

apply(wm_fitp, 2, function(x) c(mean = mean(x), se = sd(x), hdi(x)))

# plot contrasts
par(mar=c(5, 7, 4, 2)+.1)
plot(NA, xlim=c(-.15, .35), ylim=c(0.5,6.5), xlab="Difference in working memory accuracy from new-new", ylab = "", axes=F)
box()
axis(1)
axis(2, at = c(5.5, 3.5, 1.5), 
     labels = c("match", "mis-match", "old-new"), las=1)

you_col = "tomato"; old_col = "dodgerblue"; diff_col = "grey"
vioplot2(wm_fitp[,"younger-match"] - wm_fitp[,"younger-new-new"], at = 6, 
         col = you_col)
vioplot2(wm_fitp[,"older-match"] - wm_fitp[,"older-new-new"], at = 5.5, 
         col = old_col)
vioplot2((wm_fitp[,"younger-match"] - wm_fitp[,"younger-new-new"]) - 
           (wm_fitp[,"older-match"] - wm_fitp[,"older-new-new"]), at = 5, 
         col = diff_col)

vioplot2(wm_fitp[,"younger-mis-match"] - wm_fitp[,"younger-new-new"], at = 4,
         col = you_col)
vioplot2(wm_fitp[,"older-mis-match"] - wm_fitp[,"older-new-new"], at = 3.5,
         col = old_col)

vioplot2((wm_fitp[,"younger-mis-match"] - wm_fitp[,"younger-new-new"]) - 
           (wm_fitp[,"older-mis-match"] - wm_fitp[,"older-new-new"]), at = 3, 
         col = diff_col)

vioplot2(wm_fitp[,"younger-old-new"] - wm_fitp[,"younger-new-new"], at = 2,
         col = you_col)
vioplot2(wm_fitp[,"older-old-new"] - wm_fitp[,"older-new-new"], at = 1.5,
         col = old_col)

vioplot2((wm_fitp[,"younger-old-new"] - wm_fitp[,"younger-new-new"]) - 
           (wm_fitp[,"older-old-new"] - wm_fitp[,"older-new-new"]), at = 1, 
         col = diff_col)

abline(v=0, lty=2, col="grey")

legend(x = 0.35, y = 0.5, legend = c("younger", "older", "younger - older\ndifference"), 
       pch = 15, col = c(you_col, old_col, diff_col), bty="n", xjust = .9, yjust = 0, cex = .8)

par(mar=c(5, 4, 4, 2)+.1)


# Bayes factors

# age-group difference in new vs. recombined effect
hypothesis(x = wm_brm1, "group1:item_typenewVnonmatch > 0")
# all posterior samples are > 0 so Inf support according to hypothesis
# BF should be 
(niter - nwarm)*nchains
# to-1 to account for finite samples

# new vs non-match effect in each group - old then young
hypothesis(x = wm_brm1, "item_typenewVnonmatch + 1 * group1:item_typenewVnonmatch = 0")
hypothesis(x = wm_brm1, "item_typenewVnonmatch + -1 * group1:item_typenewVnonmatch = 0")

# age difference in facilitation
(h = hypothesis(x = wm_brm1, "group1:item_typematchVrest = 0"))

plot(h, plot=F)[[1]] +
  coord_cartesian(xlim = c(-100, 100))

# the default ones don't look right... maybe some way to change bw?
# either way, let's make a base version...

dpri = density(prior_samples(wm_brm1, pars = "b_group1:item_typematchVrest")[[1]], 
               bw = 1/3, from=-10, to=10)
dpost = density(posterior_samples(wm_brm1, pars = "b_group1:item_typematchVrest")[[1]], 
                bw = 1/3, from=-10, to=10)

plot(dpost, main="", xlim=c(-5,5), ylim=c(0,1.3), col="violet")
lines(dpri, col = "blue")
abline(v=0, col="grey", lty=2)

legend("topleft", lty=c(1,1), col=c("blue", "violet"),
       text.col = c("blue", "violet"),
       legend = c("prior", "posterior"))

# eval densities at zero
d1 = approx(dpri$x, dpri$y, xout = 0)$y
d2 = approx(dpost$x, dpost$y, xout = 0)$y

d2/d1
# the density method in brms::hypothesis() is different (see https://github.com/paul-buerkner/brms/blob/master/R/hypothesis.R)
# but this gives a similar answer

points(0, d2, col="violet", pch=16)
points(0, d1, col="blue", pch=16)

# other interactions of interest


hypothesis(x = wm_brm1, "distraction1:item_typenewVnonmatch = 0")
hypothesis(x = wm_brm1, "interval1:item_typenewVnonmatch = 0")

hypothesis(x = wm_brm1, "distraction1:group1:item_typenewVnonmatch = 0")
hypothesis(x = wm_brm1, "interval1:group1:item_typenewVnonmatch = 0")

hypothesis(x = wm_brm1, "distraction1:interval1:group1:item_typenewVnonmatch = 0")

## focus on new-new trials

if (!LOAD){
  # priors
  priors = c(set_prior("cauchy(0, 2.5)", class = "Intercept"),
             set_prior("cauchy(0, 1)", class = "b"),
             set_prior("cauchy(0, 2.5)", class = "sd"))
  
  # do new pairs show distraction/interval effects
  wmnew_brm1 = brm(recall_acc ~ distraction*interval*group + 
                     (1 | participant) + (1 | word_fac), 
                   data = subset(wm_dat, item_type == "new-new"), 
                   family = bernoulli(link = "logit"), 
                   prior = priors,
                   sample_prior = "yes",
                   chains=nchains,
                   iter=niter,
                   warmup=nwarm)
  
  saveRDS(wmnew_brm1, file = "rds-files/wmnew_brm1.rds")
  
} else {
  wmnew_brm1 = readRDS("rds-files/wmnew_brm1.rds")
}

### ### ### ### ### ### ### ### ### ### 
### WM: DIFFERENT RESPONSE CATEGORIES -----
### ### ### ### ### ### ### ### ### ### 

if (!LOAD){ # LOAD is set above
  
  # categorical model with all response categories (many priors to set)
  get_prior(resp_type ~ distraction*interval*group*item_type + 
              (1 + item_type | participant) + (1 | word_fac), 
            data = wm_dat, 
            family = categorical(link = "logit"))
  
  priors = c(set_prior("cauchy(0, 2.5)", class = "Intercept"),
             set_prior("cauchy(0, 1)", class = "b"),
             set_prior("cauchy(0, 2.5)", class = "sd", 
                       coef = "Intercept", group = "participant", dpar="muextra"),
             set_prior("cauchy(0, 2.5)", class = "sd", 
                       coef = "item_typematchVrest", group = "participant", dpar="muextra"),
             set_prior("cauchy(0, 2.5)", class = "sd", 
                       coef = "item_typenewVnonmatch", group = "participant", dpar="muextra"),
             set_prior("cauchy(0, 2.5)", class = "sd", 
                       coef = "item_typemismatchVoldnew", group = "participant", dpar="muextra"),
             set_prior("cauchy(0, 2.5)", class = "sd", 
                       coef = "Intercept", group = "word_fac", dpar="muextra"),
             set_prior("cauchy(0, 2.5)", class = "sd", 
                       coef = "Intercept", group = "participant", dpar="multm"),
             set_prior("cauchy(0, 2.5)", class = "sd", 
                       coef = "item_typematchVrest", group = "participant", dpar="multm"),
             set_prior("cauchy(0, 2.5)", class = "sd", 
                       coef = "item_typenewVnonmatch", group = "participant", dpar="multm"),
             set_prior("cauchy(0, 2.5)", class = "sd", 
                       coef = "item_typemismatchVoldnew", group = "participant", dpar="multm"),            
             set_prior("cauchy(0, 2.5)", class = "sd", 
                       coef = "Intercept", group = "word_fac", dpar="multm"),
             set_prior("cauchy(0, 2.5)", class = "sd", 
                       coef = "Intercept", group = "participant", dpar="muomission"),
             set_prior("cauchy(0, 2.5)", class = "sd", 
                       coef = "item_typematchVrest", group = "participant", dpar="muomission"),
             set_prior("cauchy(0, 2.5)", class = "sd", 
                       coef = "item_typenewVnonmatch", group = "participant", dpar="muomission"),
             set_prior("cauchy(0, 2.5)", class = "sd", 
                       coef = "item_typemismatchVoldnew", group = "participant", dpar="muomission"),             
             set_prior("cauchy(0, 2.5)", class = "sd", 
                       coef = "Intercept", group = "word_fac", dpar="muomission"),
             set_prior("cauchy(0, 2.5)", class = "sd", 
                       coef = "Intercept", group = "participant", dpar="muprevious"),
             set_prior("cauchy(0, 2.5)", class = "sd", 
                       coef = "item_typematchVrest", group = "participant", dpar="muprevious"),
             set_prior("cauchy(0, 2.5)", class = "sd", 
                       coef = "item_typenewVnonmatch", group = "participant", dpar="muprevious"),
             set_prior("cauchy(0, 2.5)", class = "sd", 
                       coef = "item_typemismatchVoldnew", group = "participant", dpar="muprevious"),             
             set_prior("cauchy(0, 2.5)", class = "sd", 
                       coef = "Intercept", group = "word_fac", dpar="muprevious"),
             set_prior("cauchy(0, 2.5)", class = "sd", 
                       coef = "Intercept", group = "participant", dpar="muwithin"),
             set_prior("cauchy(0, 2.5)", class = "sd", 
                       coef = "item_typematchVrest", group = "participant", dpar="muwithin"),
             set_prior("cauchy(0, 2.5)", class = "sd", 
                       coef = "item_typenewVnonmatch", group = "participant", dpar="muwithin"),
             set_prior("cauchy(0, 2.5)", class = "sd", 
                       coef = "item_typemismatchVoldnew", group = "participant", dpar="muwithin"),             
             set_prior("cauchy(0, 2.5)", class = "sd", 
                       coef = "Intercept", group = "word_fac", dpar="muwithin"),
             set_prior("lkj(1)", class = "cor"))
  
  # same contrasts as above analysis
  contrasts(wm_dat$item_type)
  contrasts(wm_dat$distraction)
  contrasts(wm_dat$group)
  contrasts(wm_dat$interval)
  
  wmcat_brm1 = brm(resp_type ~ distraction*interval*group*item_type + 
                     (1 + item_type | participant) + (1 | word_fac), 
                   data = wm_dat, 
                   family = categorical(link = "logit"), 
                   prior = priors,
                   control=list(max_treedepth=15),
                   sample_prior = "yes",
                   chains=nchains,
                   iter=niter,
                   warmup=nwarm
                   )
  
  saveRDS(wmcat_brm1, file = "rds-files/wmcat_brm1.rds")
  
} else {
  wmcat_brm1 = readRDS("rds-files/wmcat_brm1.rds")
}

# simplify table of fixed effects
wmcat_fe = as.data.frame(fixef(wmcat_brm1))

# hdi excludes zero
wmcat_fehdi = posterior_samples(wmcat_brm1, pars = paste0("b_", rownames(wmcat_fe)), fixed = T)

wmcat_fehdi = as.data.frame(t(apply(wmcat_fehdi, 2, function(x) c(mh(x), pg0 = mean(x>0) ))))

wmcat_nonz = wmcat_fehdi[with(wmcat_fehdi, sign(lower) == sign(upper)),]

wmcat_nonz = wmcat_fehdi[with(wmcat_fehdi, (lower < -.1 & upper < -.1) | (lower > .1 & upper > .1) ),]

# plot estimated proportions irrespective of interval and distraction
wmcat_newd = expand.grid(
  interval=NA, distraction = NA,#c("yes", "no"), 
  group=c("younger", "older"),
  item_type = c("match", "mis-match", "new-new", "old-new")
)

# posterior samples as probabilities
wmcat_fitp = posterior_epred(wmcat_brm1, newdata=wmcat_newd, re_formula=NA)

resp_types = c("correct", "within", "omission", "extra", "ltm", "previous") # in order of prevelance

# extract means and HDIs
wmcat_mhdis = list()
for (rt in resp_types){
  wmcat_mhdis[[rt]] = cbind(wmcat_newd[,3:4], 
                            t(apply(wmcat_fitp[,,rt], 2, mh))) 
}
colnames(wmcat_fitp) = with(wmcat_newd, paste(group, item_type, sep = "_"))

# difference between young and old
wmcat_yvo = list()
for (rt in resp_types){
  wmcat_yvo[[rt]] = as.data.frame(t(apply(wmcat_fitp[,grep(pattern = "younger", colnames(wmcat_fitp)),rt] - wmcat_fitp[,grep(pattern = "older", colnames(wmcat_fitp)),rt], 2, mh)))
  
  rownames(wmcat_yvo[[rt]]) = gsub("younger_", "",
                                   rownames(wmcat_yvo[[rt]]))
}

# as a proportion of errors (1 - p(responde = correct))
wmcat_fitp2 = wmcat_fitp[,,2:6]
for (i in 1:5){
  wmcat_fitp2[,,i] = wmcat_fitp2[,,i]/(1 - wmcat_fitp[,,1])
}

wmcat_mhdis2 = list()
for (rt in resp_types[2:6]){
  wmcat_mhdis2[[rt]] = cbind(wmcat_newd[,3:4], 
                             t(apply(wmcat_fitp2[,,rt], 2, mh))) 
}

# difference in as a proportion of errors measure
wmcat_yvo2 = list()
for (rt in resp_types[2:6]){
  wmcat_yvo2[[rt]] = as.data.frame(t(apply(wmcat_fitp2[,grep(pattern = "younger", colnames(wmcat_fitp2)),rt] - wmcat_fitp2[,grep(pattern = "older", colnames(wmcat_fitp2)),rt], 2, mh)))
  
  rownames(wmcat_yvo2[[rt]]) = gsub("younger_", "",
                                    rownames(wmcat_yvo2[[rt]]))
}

# plot of estimated probabilities and 95% HDIs of different response types
# plots age difference as text above each pair of points
par(mfrow=c(3,2), mar=c(2,2,2,2), oma=c(0,2,0,0))
for (i in 1:length(resp_types)){
  rt = resp_types[i]
  tmp = wmcat_mhdis[[rt]]
  
  yl = with(tmp,  range(c(lower, upper))) # t=y axis range
  
  yl[1] = ifelse(yl[1] < .1, 0, yl[1]) # if lower range of y is small, round to 0
  
  yl[2] = yl[2] + diff(yl)*.4 # make room for text
  
  plot(NA, xlim=c(.7,4.3), ylim=yl, xlab="", ylab="", axes=F)
  if (yl[2] > 1){
    axis(2, at = round(seq(from=yl[1], to=1, length.out=5), 2))
  } else {
    axis(2)
  }
  
  axis(1, at = 1:4, labels = levels(tmp$item_type))
  mtext(text = rt, adj = 0)
  
  if (rt == "correct"){
    legend("bottomleft", 
           legend = c("younger", "older"), 
           col = c(cols[["younger"]], cols[["older"]]),
           pch = c(16,16), bty="n"
    )
  }
  
  # add data
  for (ag in c("younger", "older")){
    pty = c(16,15)[1]
    lty = c(1,2)[1]
    
    with(subset(tmp, group == ag), 
         errBars(lower=lower, upper=upper, 
                 xpos = as.numeric(item_type)+jitts[[ag]]))
    
    with(subset(tmp, group == ag), 
         points(as.numeric(item_type)+jitts[[ag]], m, pch=pty, lty=lty, 
                type="b", col=cols[[ag]]))
  }
  # add text age differences
  text(x = 1:4, y = yl[2], 
       labels = with(wmcat_yvo[[rt]], sprintf("%.2f\n[%.2f, %.2f]", m, lower, upper)), adj=c(.5, 1), cex=.7)
}

mtext(text = "p(Response)", side = 2, outer = T, line=.7)

# same plot, but as a proportion of errors
par(mfrow=c(3,2), mar=c(2,2,2,2), oma=c(0,2,0,0))

plot(NA, xlim=c(.7,4.3), ylim=yl, xlab="", ylab="", axes=F)
legend("bottomleft", 
       legend = c("younger", "older"), 
       col = c(cols[["younger"]], cols[["older"]]),
       pch = c(16,16), bty="n"
)
for (i in 2:length(resp_types)){
  rt = resp_types[i]
  tmp = wmcat_mhdis2[[rt]]
  
  yl = with(tmp,  range(c(lower, upper)))
  
  yl[1] = ifelse(yl[1] < .1, 0, yl[1])
  
  yl[2] = yl[2] + diff(yl)*.4
  
  plot(NA, xlim=c(.7,4.3), ylim=yl, xlab="", ylab="", axes=F)
  if (yl[2] > 1){
    axis(2, at = round(seq(from=yl[1], to=1, length.out=5), 2))
  } else {
    axis(2)
  }
  
  axis(1, at = 1:4, labels = levels(tmp$item_type))
  mtext(text = rt, adj = 0)
  
  # add data
  for (ag in c("younger", "older")){
    
    pty = c(16,15)[1]
    lty = c(1,2)[1]
    
    with(subset(tmp, group == ag), 
         errBars(lower=lower, upper=upper, 
                 xpos = as.numeric(item_type)+jitts[[ag]]))
    
    with(subset(tmp, group == ag), 
         points(as.numeric(item_type)+jitts[[ag]], m, pch=pty, lty=lty, 
                type="b", col=cols[[ag]]))
  }
  # add text age differences
  text(x = 1:4, y = yl[2], 
       labels = with(wmcat_yvo2[[rt]], sprintf("%.2f\n[%.2f, %.2f]", m, lower, upper)), adj=c(.5, 1), cex=.7)
}

mtext(text = "As proportion of errors: p(Response) / (1 - p(correct))", side = 2, outer = T, line=.7)


### ### ### ### ### ### ### ### ### ### 
### MULTIVARIATE MODEL WITH LEARNING AND WM DATA -----
### ### ### ### ### ### ### ### ### ### 

# https://github.com/paul-buerkner/brms/issues/360

# combine the data sets to fit a mv model
# just use final learning data
learn_final = subset(learn_dat, learn_block == "final test")

wm_dat$learn_block = "0"
learn_final$item_type = "match"

# indicators for subsetting/weighting analyses (see link above)
wm_dat$wm = 1; learn_final$wm = 0
wm_dat$learn = 0; learn_final$learn = 1

multicols = c("participant", "word", "group", "learn_block", "item_type", 
              "recall_acc", "wm", "learn")
multidat = rbind(wm_dat[,multicols], learn_final[,multicols])

# factors
multidat$word_fac = as.factor(multidat$word)
# multidat$block_loop = as.factor(multidat$block_loop)
multidat$participant = as.factor(multidat$participant)
multidat$item_type = as.factor(multidat$item_type)

# responses need to be different columns
multidat$acc_wm = multidat$recall_acc
multidat$acc_learn = multidat$recall_acc

# contrasts
contrasts(multidat$item_type) = cbind(matchVrest = c(1,-1/3,-1/3,-1/3),
                                      newVnonmatch=c(0,-1/2,1,-1/2),
                                      mismatchVoldnew=c(0,1,0,-1))

# contrasts(multidat$item_type) = cbind(match = c(1,0,-1,0), 
#                                         mis=c(0,1,-1,0), 
#                                         oldnew=c(0,0,-1,1))

# contrasts(multidat$block_loop) = cbind(b2 = c(-1,1,0), 
#                                          final=c(-1,0,1))

contrasts(multidat$group) = c(-1,1)

if (!LOAD){
  multi_form = mvbf(
    brms::bf(acc_wm | subset(wm) ~ item_type*group + (1 + item_type |p| participant), 
       family = bernoulli()),
    brms::bf(acc_learn | subset(learn) ~ group + (1 |p| participant), 
       family = bernoulli()), 
    rescor = F
  )
  
  get_prior(multi_form, data = multidat)
  
  multi_priors = c(#set_prior("cauchy(0, 2.5)", class = "Intercept"),
    set_prior("cauchy(0, 2.5)", class = "Intercept", resp = "acclearn"),
    set_prior("cauchy(0, 2.5)", class = "Intercept", resp = "accwm"),
    #set_prior("cauchy(0, 2.5)", class = "b"),
    set_prior("cauchy(0, 1)", class = "b", resp = "acclearn"),
    set_prior("cauchy(0, 1)", class = "b", resp = "accwm"),
    set_prior("cauchy(0, 2.5)", class = "sd", resp = "acclearn"),
    set_prior("cauchy(0, 2.5)", class = "sd", resp = "accwm"),
    set_prior("lkj(1)", class = "cor"))
  
  multi_m1 = brm(multi_form, data = multidat, 
                 prior = multi_priors,
                 control=list(adapt_delta=0.99), 
                 sample_prior = "yes",
                 chains=nchains,
                 iter=niter,
                 warmup=nwarm
                 )
  
  saveRDS(multi_m1, file = "rds-files/multi_m1.rds")
  
} else {
  multi_m1 = readRDS("rds-files/multi_m1.rds")
}

## plot correlation estimates
cor_samps = posterior_samples(multi_m1, pars = "cor")

# make nicer labels
cor_names = colnames(cor_samps)

cor_names = gsub(pattern = "cor_", "Cor(", cor_names)
cor_names = gsub(pattern = "participant__", "", cor_names)
cor_names = gsub(pattern = "accwm_Intercept", "WM Overall", cor_names)
cor_names = gsub(pattern = "accwm_", "WM", cor_names)
cor_names = gsub(pattern = "acclearn_", "Learn", cor_names)
cor_names = gsub(pattern = "Intercept", "", cor_names)
cor_names = gsub(pattern = "item_typematchVrest", " PF", cor_names)
cor_names = gsub(pattern = "item_typenewVnonmatch", " PI", cor_names)
cor_names = gsub(pattern = "item_typemismatchVoldnew", " M vs. O", cor_names)
cor_names = gsub(pattern = "__", ", ", cor_names)
cor_names = paste0(cor_names, ")")

colnames(cor_samps) = cor_names

par(mar=c(5, 14, 4, 2)+.1)
plot(NA, xlim=c(-1, 1), ylim=c(0.5,ncol(cor_samps)+.5), xlab="Correlation", ylab = "", axes=F)
box()
axis(1)
axis(2, at = 1:ncol(cor_samps), 
     labels = colnames(cor_samps), las=1)
l=lapply(1:ncol(cor_samps), FUN = function(x) vioplot2(cor_samps[,x], at = x, col = "lightblue"))
abline(v = 0, lty=2, col="black")

# sd bayes factors

hypothesis(multi_m1, "participant__accwm_Intercept__acclearn_Intercept = 0", class = "cor")
hypothesis(multi_m1, "participant__accwm_item_typematchVrest__acclearn_Intercept = 0", class = "cor")
hypothesis(multi_m1, "participant__accwm_item_typenewVnonmatch__acclearn_Intercept = 0", class = "cor")

### ### ### ### ### ### ### ### ### ### 
### SEARCH TASK PERFORMANCE -----
### ### ### ### ### ### ### ### ### ### 

# take out practice trials for 10 s condition

# wm practice
search_dat = search_dat[!with(search_dat, section=="wm" & wm_trial < 4), ]
# search practice
search_dat = search_dat[!with(search_dat, section=="search_alone" & search_loop.thisRepN < 4), ]

# analysis
search_dat = within(search_dat, {
  group = as.factor(group)
  interval = as.factor(interval)
  section = as.factor(section)
})

# aggregate to speed things up...
search_acc = ddply(search_dat, c("participant", "group", "section", "interval"), summarize,
                   ncor = sum(accuracy),
                   ntrials = length(accuracy))

contrasts(search_dat$section)
contrasts(search_dat$group)
contrasts(search_dat$interval)

contrasts(search_acc$section)
contrasts(search_acc$group)
contrasts(search_acc$interval)

if (!LOAD){
  # priors
  priors = c(set_prior("cauchy(0, 2.5)", class = "Intercept"),
             set_prior("cauchy(0, 1)", class = "b"),
             set_prior("cauchy(0, 2.5)", class = "sd"),
             set_prior("lkj(1)", class = "cor"))
  
  search_acc_brm1 = brm(ncor | trials(ntrials) ~ interval*group*section + 
                          (1 + section | participant), 
                        data = search_acc, 
                        family = binomial(link = "logit"), 
                        prior = priors,
                        sample_prior = "yes",
                        chains=nchains,
                        iter=niter,
                        warmup=nwarm
                        )
  
  saveRDS(search_acc_brm1, file = "rds-files/search_acc_brm1.rds")
  
  priors = c(set_prior("cauchy(1, 1)", class = "Intercept"),
             set_prior("cauchy(0, 1)", class = "b"),
             set_prior("cauchy(0, 1)", class = "sd"),
             set_prior("lkj(1)", class = "cor"))
  
  search_rt_brm1 = brm(search_resp.rt ~ interval*group*section + 
                         (1 + section | participant), 
                       data = search_dat, 
                       family = gaussian(link = "identity"), 
                       prior = priors,
                       sample_prior = "yes",
                       chains=nchains,
                       iter=niter,
                       warmup=nwarm)
  
  saveRDS(search_rt_brm1, file = "rds-files/search_rt_brm1.rds")
  
} else {
  search_acc_brm1 = readRDS("rds-files/search_acc_brm1.rds")
  search_rt_brm1 = readRDS("rds-files/search_rt_brm1.rds")
}


# aggregate to plot
search_agg = ddply(search_dat, c("participant", "group", "section", "interval"), summarize,
                   N = length(accuracy),
                   acc = mean(accuracy),
                   prop_missed = mean(is.na(s_respright)),
                   mean_rt = mean(search_resp.rt, na.rm=T))

search_agg = within(search_agg, {
  interval = as.factor(interval)
  section = as.factor(section)
})

search_acc_mse = summarySEwithin(data = search_agg, measurevar = "acc", withinvars = "section", betweenvars = c("group", "interval"))
search_rt_mse = summarySEwithin(data = na.omit(search_agg), measurevar = "mean_rt", withinvars = "section", betweenvars = c("group", "interval"))

# plot
par(mfrow=c(2,2), mar=c(2,2,2,2), oma=c(0,2,0,0))

d = "yes"
# accuracy
for (i in intervals){
  
  plot(NA, xlim=c(.7,2.3), ylim=c(0,1), xlab="", ylab="Search Accuracy", axes=F)
  #box()
  labs = levels(search_agg$section)
  axis(1, at = 1:2, labels = labs)
  axis(2)
  mtext(i, adj = 0)
  
  if (i == "2 s") mtext("Search Accuracy", 2, line = 2)
  
  for (g in groups){
    l_ply(.data = ids[[i]][[d]][[g]], .fun = function(x) with(subset(search_agg, participant==x), points(jitter(as.numeric(section)+jitts[g], amount = .025), acc, pch=16, col=faintCol(cols[g]), type='p')))
  }
  for (g in groups){
    # error bars + points
    with(subset(search_acc_mse, interval==i & group==g), {
      errBars(means = acc, error = se, xpos = as.numeric(section)+jitts[g])
      points(as.numeric(section)+jitts[g], acc, pch=16, col=cols[g], type='b')
    })
  }
}

# rt
for (i in intervals){
  
  plot(NA, xlim=c(.7,2.3), ylim=range(search_agg$mean_rt, na.rm = T), xlab="", ylab="", axes=F)
  #box()
  labs = levels(search_agg$section)
  axis(1, at = 1:2, labels = labs)
  axis(2)
  mtext(i, adj = 0)
  
  if (i == "2 s") mtext("Search mean RT (s)", 2, line = 2)
  
  for (g in groups){
    l_ply(.data = ids[[i]][[d]][[g]], .fun = function(x) with(subset(search_agg, participant==x), points(jitter(as.numeric(section)+jitts[g], amount = .025), mean_rt, pch=16, col=faintCol(cols[g]), type='p')))
  }
  for (g in groups){
    # error bars + points
    with(subset(search_rt_mse, interval==i & group==g), {
      errBars(means = mean_rt, error = se, xpos = as.numeric(section)+jitts[g])
      points(as.numeric(section)+jitts[g], mean_rt, pch=16, col=cols[g], type='b')
    })
  }
}
legend("bottomright", legend = groups, pch=16, col=cols, bty='n')


# do an analysis with low performers excluded...
# (are results w/ distraction similar when focusing on high search performers?)

search_thresh = .7

high_search = subset(search_agg, acc >= search_thresh & section == "wm")$participant

with(subset(search_agg, participant %in% high_search & section == "wm"), 
     table(group, interval))

if (!LOAD){
  
  # priors
  priors = c(set_prior("cauchy(0, 2.5)", class = "Intercept"),
             set_prior("cauchy(0, 1)", class = "b"),
             set_prior("cauchy(0, 2.5)", class = "sd"),
             set_prior("lkj(1)", class = "cor"))
  
  # all participants
  wm_distraction_brm1 = brm(recall_acc ~ interval*group*item_type + 
                              (1 + item_type | participant) + (1 | word_fac), 
                            data = subset(wm_dat, distraction=="yes"), 
                            family = bernoulli(link = "logit"), 
                            prior = priors,
                            sample_prior = "yes",
                            chains=nchains,
                            iter=niter,
                            warmup=nwarm
                            )
  
  saveRDS(wm_distraction_brm1, file = "rds-files/wm_distraction_brm1.rds")
  
  # exclude low search performers
  wm_distraction_brm2 = brm(recall_acc ~ interval*group*item_type + 
                              (1 + item_type | participant) + (1 | word_fac), 
                            data = subset(wm_dat, distraction=="yes" & 
                                            participant %in% high_search), 
                            family = bernoulli(link = "logit"), 
                            prior = priors,
                            sample_prior = "yes",
                            chains=nchains,
                            iter=niter,
                            warmup=nwarm
                            )
  
  saveRDS(wm_distraction_brm2, file = "rds-files/wm_distraction_brm2.rds")
  
} else {
  wm_distraction_brm1 = readRDS("rds-files/wm_distraction_brm1.rds")
  wm_distraction_brm2 = readRDS("rds-files/wm_distraction_brm2.rds")
}

fe1 = as.data.frame(fixef(wm_distraction_brm1))
fe2 = as.data.frame(fixef(wm_distraction_brm2))

plot(fe1$Estimate, fe2$Estimate, xlim=c(-.8,  1.7), 
     ylim=c(-.8,  1.7), pch=16, col="grey")
abline(0,1)

segments(x0 = fe1$Estimate, y0 = fe2$Q2.5, 
         x1 = fe1$Estimate, y1 = fe2$Q97.5, col="grey")
segments(x0 = fe1$Q2.5, y0 = fe2$Estimate, 
         x1 = fe1$Q97.5, y1 = fe2$Estimate, col="grey")
# one that deviates from 0,1 is the intercept term...
# high search performed perform better at wm task

# zoom
plot(fe1$Estimate, fe2$Estimate, xlim=c(-.3,  .3), 
     ylim=c(-.5, .4), pch=16, col="grey")
abline(0,1)

segments(x0 = fe1$Estimate, y0 = fe2$Q2.5, 
         x1 = fe1$Estimate, y1 = fe2$Q97.5, col="grey")
segments(x0 = fe1$Q2.5, y0 = fe2$Estimate, 
         x1 = fe1$Q97.5, y1 = fe2$Estimate, col="grey")


ci1=with(fe1, (Q2.5 > 0 & Q97.5 > 0) | (Q2.5 < 0 & Q97.5 < 0))
ci2=with(fe2, (Q2.5 > 0 & Q97.5 > 0) | (Q2.5 < 0 & Q97.5 < 0))

all(ci1 == ci2) # doesnt change anything in terms of 0 in 95% CI
