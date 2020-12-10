
## code for: The influence of long-term memory on working memory: Age-differences in proactive facilitation and interference

# combine the data sets from the different conditions (distraction: yes/no; interval: 2/10)
# this will only work if the "read-...R" scripts in each subfolder of "data/" have been run

library(plyr)

setwd(dirname(rstudioapi::getActiveDocumentContext()$path))

### ### ### ### ### ### ### ### ### ### 
### read in different conditions ----
### ### ### ### ### ### ### ### ### ### 
no2_wm = read.csv("no-2/no2_wm.csv", stringsAsFactors = F)
no2_learn = read.csv("no-2/no2_learn.csv", stringsAsFactors = F)

yes2_wm = read.csv("yes-2/yes2_wm.csv", stringsAsFactors = F)
yes2_learn = read.csv("yes-2/yes2_learn.csv", stringsAsFactors = F)
yes2_search = read.csv("yes-2/yes2_search.csv", stringsAsFactors = F)

yes10_search = read.csv("yes-10/yes10_search.csv", stringsAsFactors = F)
yes10_wm = read.csv("yes-10/yes10_wm.csv", stringsAsFactors = F)
yes10_learn = read.csv("yes-10/yes10_learn.csv", stringsAsFactors = F)

no10_wm = read.csv("no-10/no10_wm.csv", stringsAsFactors = F)
no10_learn = read.csv("no-10/no10_learn.csv", stringsAsFactors = F)

## info
no2_info_y = read.csv("no-2/prolific_export_5f035e5afe130c270d6ae6dd-younger.csv")
no2_info_o = read.csv("no-2/prolific_export_5f073de81c76c3308c0e4fb3-older.csv")

yes2_info_y = read.csv("yes-2/prolific_export_5f341be081b9052c55068110-younger.csv")
yes2_info_o = read.csv("yes-2/prolific_export_5f5126bb654d4b30ee6923d8-older.csv")

yes10_info_y = read.csv("yes-10/prolific_export_5f47c29a48bd2a1e651a6eb7-younger-dist.csv")
no10_info_y = read.csv("no-10/prolific_export_5f47c0b9b035471e11593a5c-younger-blan.csv")
yes10_info_o = read.csv("yes-10/prolific_export_5f599a131af4471f3d752b7b-older-dist.csv")
no10_info_o = read.csv("no-10/prolific_export_5f5adea66120081ea0f57a61-older-blan.csv")

# new columns 
no2_wm$distraction = no2_learn$distraction = "no"
yes2_wm$distraction = yes2_learn$distraction = "yes"

no2_info_y$distraction = no2_info_o$distraction = "no"
yes2_info_y$distraction = yes2_info_o$distraction = "yes"

no2_wm$interval = no2_learn$interval = "2 s"
yes2_wm$interval = yes2_learn$interval = "2 s"

no2_info_y$interval = no2_info_o$interval = "2 s"
yes2_info_y$interval = yes2_info_o$interval = "2 s"

yes10_wm$distraction = yes10_learn$distraction = "yes"
no10_wm$distraction = no10_learn$distraction = "no"

yes10_info_y$distraction = yes10_info_o$distraction = "yes"
no10_info_y$distraction = no10_info_o$distraction = "no"

yes10_wm$interval = yes10_learn$interval = "10 s"
no10_wm$interval = no10_learn$interval = "10 s"

yes10_info_y$interval = yes10_info_o$interval = "10 s"
no10_info_y$interval = no10_info_o$interval = "10 s"

yes2_search$interval = "2 s"
yes10_search$interval = "10 s"

### ### ### ### ### ### ### ### ### ### 
### combine conditions ----
### ### ### ### ### ### ### ### ### ### 
wm_cols = Reduce(intersect, list(colnames(no2_wm), 
                                 colnames(yes2_wm), 
                                 colnames(yes10_wm), 
                                 colnames(no10_wm)))

learn_cols = Reduce(intersect, list(colnames(no2_learn), 
                                    colnames(yes2_learn), 
                                    colnames(yes10_learn), 
                                    colnames(no10_learn)))

search_cols = Reduce(intersect, list(colnames(yes2_search), 
                                    colnames(yes10_search)))

info_cols = Reduce(intersect, list(colnames(no2_info_y),
                                   colnames(no2_info_o),
                                   colnames(yes2_info_y),
                                   colnames(yes2_info_o),
                                   colnames(yes10_info_y),
                                   colnames(yes10_info_o),
                                   colnames(no10_info_y),
                                   colnames(no10_info_o)))

wm_dat = rbind(no2_wm[,wm_cols], 
               yes2_wm[,wm_cols], 
               yes10_wm[,wm_cols], 
               no10_wm[,wm_cols])

learn_dat = rbind(no2_learn[,learn_cols], 
                  yes2_learn[,learn_cols], 
                  yes10_learn[,learn_cols], 
                  no10_learn[,learn_cols])

search_dat = rbind(yes2_search[,search_cols], 
                  yes10_search[,search_cols])

keep_search = c("participant", "group", "section", "wm_trial", "s_respright", 
                "accuracy", "interval", "s_im1", "s_im2", 
                "s_im3", "s_im4", 's_im5', "s_im6", "s_im7", 
                "s_im8",  "s_im1pos", "s_im2pos",  's_im3pos', 
                "s_im4pos", "s_im5pos", "s_im6pos",  's_im7pos', 
                "s_im8pos",  "s_tarright", "search_resp.keys", 
                "search_resp.rt", "search_loop.thisRepN", 
               "search_loop.thisTrialN",  "search_loop.thisN", 
                "search_loop.thisIndex", "search_loop.ran")

search_dat = search_dat[,keep_search]

info_all = rbind(no2_info_y[,info_cols], 
                 no2_info_o[,info_cols],
                 yes2_info_y[,info_cols],
                 yes2_info_o[,info_cols],
                 yes10_info_y[,info_cols],
                 yes10_info_o[,info_cols],
                 no10_info_y[,info_cols],
                 no10_info_o[,info_cols])

info_all$group = ifelse(info_all$age > 50, "older", "younger")

info = subset(info_all, participant_id %in% unique(wm_dat$participant))

# get ids of participants in different conditions
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
### response categories ----
### ### ### ### ### ### ### ### ### ### 

# find instances where participant recalled 
# learned associate instead of wm associate

wm_dat$prev_assoc = NA

for (i in 1:nrow(wm_dat)){
  if (wm_dat$item_type[i] %in% c("mis-match", "old-new")){
    s = wm_dat$participant[i]; im = wm_dat$image[i]
    
    prev_words = learn_dat$word[learn_dat$participant == s & learn_dat$image == im]
    if (length(unique(prev_words)) == 1){
      wm_dat$prev_assoc[i] = prev_words[1]
    } else{
      cat("row", i, "different words...\n")
    }
    
  }
}

wm_dat$ltm_intru = with(wm_dat, as.integer(recalled == prev_assoc))

wm_dat$ltm_intru[is.na(wm_dat$recalled) & !is.na(wm_dat$prev_assoc)] = 0 # replace NAs with zero when noting was recalled

# categorize responses
# - omission (no response)
# - correct (the correct word)
# - ltm (a word learned at the beginning of the experiment; for match and old-new this will be an incorrect word)
# - previous (word from the previous wm trial)
# - within (transposition)
# - extra (a response but none of the above...)

wm_dat$study_pos = wm_dat$study_pos + 1

n_trials = max(wm_dat$trial_no)

S = unique(wm_dat$participant)

wm_dat$resp_type = NA
wm_dat$tran_dist = NA

for (s in 1:length(S)){
  for (t in 1:n_trials){
    for (i in 1:4){
      # extract information 
      r = with(wm_dat, which(participant == S[s] & trial_no == t & study_pos == i) ) # row
      w = wm_dat$word[r] # studied 
      re = wm_dat$recalled[r] # recalled
      nt = wm_dat$word[with(wm_dat, participant == S[s] & trial_no == t & word != w)] # non targets
      pt = rep("", 4) # previous trial items (if there were any)
      if (t > 1){
        pt = wm_dat$word[with(wm_dat, participant == S[s] & trial_no == t-1)]
      }
      lw = learn_dat$word[with(learn_dat, participant == S[s] & section == "learn_test")] # learned words
      stopifnot(length(lw) == 30)
      
      if (wm_dat$recall_acc[r] == 1){
        # first check if response is correct
        wm_dat$resp_type[r] = "correct"
      } else if (is.na(re) | re == "" | re == "?") {
        # next, was there a response? 
        wm_dat$resp_type[r] = "omission"
      } else if (re %in% nt){
        # was this a word studied in the same trial?
        wm_dat$resp_type[r] = "within"
        # calculate transposition distance
        # position studied - position of recalled item in sequence
        # e.g., + 1 equals next item in the sequence
        wm_dat$tran_dist[r] = i - wm_dat$study_pos[with(wm_dat, participant == S[s] & trial_no == t & word == re)]
      } else if (re %in% pt){
        # recalled a word from a previous trial
        wm_dat$resp_type[r] = "previous"
      } else if (re %in% lw){
        # recalled a word learned in the first part
        wm_dat$resp_type[r] = "ltm"
      } else {
        # with everything else exhausted...
        wm_dat$resp_type[r] = "extra"
      }
    }
  }
}

wmresps_agg = ddply(wm_dat, c("participant", "group", "item_type", "resp_type"), summarise,
                    count = length(participant))

wmresps_agg$prop = wmresps_agg$count/ifelse(wmresps_agg$item_type == "new-new", 10 + 6*4, 10)

resp_tables = with(wm_dat, table(resp_type, item_type, group))

# proportions
resp_propall = resp_tables
resp_propall[,,"younger"] = t(t(resp_propall[,,"younger"])/ apply(resp_propall[,,"younger"], 2, sum))
resp_propall[,,"older"] = t(t(resp_propall[,,"older"])/ apply(resp_propall[,,"older"], 2, sum))

resp_propin = resp_propall[c("extra", "ltm", "omission", "previous", "within"),,]

par(mfrow=c(1,2), mar=c(3,3,1,1))
barplot(resp_propall[,,"younger"], ylim=c(0,1), beside = T, legend.text = F, cex.names = .8, col = viridis::viridis(6), main = "Younger")
barplot(resp_propall[,,"older"],  ylim=c(0,1), beside = T, legend.text = T, cex.names = .8, col = viridis::viridis(6), main = "Older")

## Write the combined data sets

write.csv(x = wm_dat, file = "all_wm.csv", row.names = F)
write.csv(x = learn_dat, file = "all_learn.csv", row.names = F)
write.csv(x = search_dat, file = "all_search.csv", row.names = F)
write.csv(x = info_all, file = "ppt-info-all.csv", row.names = F)
write.csv(x = info, file = "ppt-info-clean.csv", row.names = F)
