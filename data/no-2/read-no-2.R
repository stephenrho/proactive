
## code for: The influence of long-term memory on working memory: Age-differences in proactive facilitation and interference
# read data from the 2 s interval, no distraction condition

exclude_ids = c("5de904d8443d0b01db94ff9b", "5e86c11942701c2ffda5d113") # technical difficulties

setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
datloc <- "raw/"


prolific_files = list.files(pattern = "prolific")

prolific_data = prolific_files[c(grep(pattern = "younger", x = prolific_files),
                                 grep(pattern = "older", x = prolific_files))]

groups = c("younger", "older")

dob = c()

for (i in 1:length(groups)){
  info <- read.csv(prolific_data[i],
                   stringsAsFactors = F)
  
  info$group = groups[i]
  
  assign(x = paste0("info_", groups[i]), value = info)
  
  pids <- info$participant_id[info$status %in% c("AWAITING REVIEW", "APPROVED")]
  
  # exclude people
  pids = pids[!(pids %in% exclude_ids)]
  
  assign(x = paste0("pids_", groups[i]), value = pids)
  
  # find data files for each participant
  files = unlist(lapply(pids, function(x) list.files(path=datloc, pattern = x)))
  
  # keep only csvs
  files = files[grep(pattern = ".csv", x = files)]
  
  full_dat = data.frame()
  
  for (x in files){
    tmp = tryCatch(read.csv(paste0(datloc, x), stringsAsFactors = F), error=function(i) matrix(NA,2,2))
    
    if ("please.enter.your.date.of.birth..dd.mm.yyyy." %in% colnames(tmp)){
      dob = rbind(dob, c(tmp$participant[1], tmp$please.enter.your.date.of.birth..dd.mm.yyyy.[1]))
      
      tmp$please.enter.your.date.of.birth..dd.mm.yyyy. = NULL
    }
    
    if (!(nrow(tmp)%in% c(946, 1306, 1666))){
      cat(paste0(groups[i], ": file ", x, " is incomplete\n"))
    } else {
      full_dat = rbind(full_dat, tmp)
    }
  }
  
  full_dat$group = groups[i]
  
  assign(x = paste0("full_dat_", groups[i]), value = full_dat)
}

info_younger = subset(info_younger, participant_id %in% pids_younger) 
info_older = subset(info_older, participant_id %in% pids_older) 

info = rbind(info_younger[,colnames(info_older)],
             info_older[,colnames(info_older)])

full_dat = rbind(full_dat_younger, full_dat_older)

consent=subset(full_dat, consent_key.keys=="y")

dat=subset(full_dat, list==list_no)

dat$section = NA
dat$section[with(dat, !is.na(learn_study_loop.thisN) || !is.na(learn_test_loop.thisN))] <- "learning"
dat$section[with(dat, !is.na(final_learn_test.thisN))] <- "learn_test"
dat$section[with(dat, !is.na(wm_trial_loop.thisN))] <- "wm"

table(dat$section)

### LEARNING DATA
full_learn_dat = subset(dat, section %in% c("learning", "learn_test"))

full_learn_dat$phase = ifelse(!is.na(full_learn_dat$learn_study_loop.thisN), "study", "test")

learn_dat = subset(full_learn_dat, phase == "test")

aggregate(recall_acc ~ participant, data = learn_dat, FUN = mean)

## here we could match pairs to their study position... (some are missing the very first study event...)

# label learning blocks
learn_dat$learn_block = "final test"

for (ppt in unique(learn_dat$participant)){
  tmp = subset(learn_dat, participant == ppt)
  
  nb = nrow(subset(tmp, section == "learning"))/30
  
  learn_dat$learn_block[with(learn_dat, participant == ppt & section=="learning")] = rep(1:nb, each=30)
}

### WORKING MEMORY DATA
full_wm_dat = subset(dat, section == "wm")

# match item_type to order probed

full_wm_dat$wm_probed_type1 = NA
full_wm_dat$wm_probed_type2 = NA
full_wm_dat$wm_probed_type3 = NA
full_wm_dat$wm_probed_type4 = NA

full_wm_dat$wm_probed_word1 = NA
full_wm_dat$wm_probed_word2 = NA
full_wm_dat$wm_probed_word3 = NA
full_wm_dat$wm_probed_word4 = NA

full_wm_dat$wm_probed_image1 = NA
full_wm_dat$wm_probed_image2 = NA
full_wm_dat$wm_probed_image3 = NA
full_wm_dat$wm_probed_image4 = NA

for (i in 1:nrow(full_wm_dat)){
  # type
  full_wm_dat$wm_probed_type1[i] = full_wm_dat[i, paste0("item_type", full_wm_dat$wm_probed1[i]+1)]
  
  full_wm_dat$wm_probed_type2[i] = full_wm_dat[i, paste0("item_type", full_wm_dat$wm_probed2[i]+1)]
  
  full_wm_dat$wm_probed_type3[i] = full_wm_dat[i, paste0("item_type", full_wm_dat$wm_probed3[i]+1)]
  
  full_wm_dat$wm_probed_type4[i] = full_wm_dat[i, paste0("item_type", full_wm_dat$wm_probed4[i]+1)]
  
  # word
  full_wm_dat$wm_probed_word1[i] = full_wm_dat[i, paste0("word", full_wm_dat$wm_probed1[i]+1)]
  
  full_wm_dat$wm_probed_word2[i] = full_wm_dat[i, paste0("word", full_wm_dat$wm_probed2[i]+1)]
  
  full_wm_dat$wm_probed_word3[i] = full_wm_dat[i, paste0("word", full_wm_dat$wm_probed3[i]+1)]
  
  full_wm_dat$wm_probed_word4[i] = full_wm_dat[i, paste0("word", full_wm_dat$wm_probed4[i]+1)]
  
  # image
  full_wm_dat$wm_probed_image1[i] = full_wm_dat[i, paste0("image", full_wm_dat$wm_probed1[i]+1)]
  
  full_wm_dat$wm_probed_image2[i] = full_wm_dat[i, paste0("image", full_wm_dat$wm_probed2[i]+1)]
  
  full_wm_dat$wm_probed_image3[i] = full_wm_dat[i, paste0("image", full_wm_dat$wm_probed3[i]+1)]
  
  full_wm_dat$wm_probed_image4[i] = full_wm_dat[i, paste0("image", full_wm_dat$wm_probed4[i]+1)]
  
}

full_wm_dat$wm_tested1=1
full_wm_dat$wm_tested2=2
full_wm_dat$wm_tested3=3
full_wm_dat$wm_tested4=4

full_wm_dat$trial_no = rep(1:16)

col_list = list(
  paste0("wm_recalled", 1:4),
  paste0("wm_probed_word", 1:4),
  paste0("wm_recall_acc", 1:4),
  paste0("wm_recall_rt", 1:4),
  paste0("wm_probed", 1:4),
  paste0("wm_tested", 1:4),
  paste0("wm_probed_image", 1:4),
  paste0("wm_probed_type", 1:4)
)

col_names = c("recalled", "word", "recall_acc", "recall_rt", "study_pos", "test_pos", "image", "item_type")

wm_dat = reshape(full_wm_dat[,c("participant", "trial_no", "group", unlist(col_list))], 
                 varying = col_list, v.names = col_names, direction = "long")

# reorder
wm_dat = wm_dat[with(wm_dat, order(participant, trial_no, test_pos)),]


## ARE DOBS CORRECT?

dob = as.data.frame(dob)
colnames(dob) = c("participant", "dob")

dob$age_prolific = NA
dob$date_test = NA

for (i in 1:nrow(dob)){
  dob$age_prolific[i] = info$age[info$participant_id == dob$participant[i]]
  dob$date_test[i] = info$started_datetime[info$participant_id == dob$participant[i]]
}

dob$dob_age = as.numeric(difftime(
  strptime(x = dob$date_test, format = "%Y-%m-%d"), 
  strptime(x = dob$dob, format = "%d/%m/%Y"), units = "days"))/365

dob$age_disc = with(dob, age_prolific - dob_age)

subset(dob, abs(age_disc) > 1)
subset(dob, is.na(dob_age)) # people that entered dob incorrectly...

# write data to csv
write.csv(x = wm_dat, file = "no2_wm.csv", row.names = F)
write.csv(x = learn_dat, file = "no2_learn.csv", row.names = F)
