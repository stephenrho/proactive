
from psychopy import visual, core, data, event, gui, monitors, misc
import numpy as np
import pandas as pd
import random, os, string, pickle
from copy import deepcopy

TEST = False ### make sure this is False when running for real!

### EXPERIMENT SETTINGS

if TEST:
    N_PAIRS = 6
    GROUP_INTO = 3
    N_MAX_LEARN_LOOPS = 2
    N_LEARN_PRAC = 2
    N_WM_PRAC = 1
    N_WM_OLD_TRIALS = 2 # int(N_WORDS/5)
    N_WM_NEW_TRIALS = 2
else:
    N_PAIRS = 36
    GROUP_INTO = 9
    N_MAX_LEARN_LOOPS = 3
    N_LEARN_PRAC = 5
    N_WM_PRAC = 3
    N_WM_OLD_TRIALS = 12 # int(N_WORDS/5)
    N_WM_NEW_TRIALS = 6 # trials that only involve new-new pairs

#N_ST_SINGLE = 10

N_LEARN_BLOCK = N_PAIRS/GROUP_INTO
N_LTM = N_WM_OLD_TRIALS*2


if N_PAIRS % 3 != 0 or N_PAIRS % GROUP_INTO != 0:
    raise(Warning("N_PAIRS is incorrect"))

### DISPLAY SETTINGS
WINSIZE = [1280, 1024]
WIDTH = 38
DIST = 60
BACKGROUND=[0,0,0]
FOREGROUND=[-1,-1,-1]
IMSIZE=100
IMSIZE_DEG = 5
WORDSIZE_DEG = 1.5
IMWORD_SEP = 1.2*(IMSIZE_DEG + WORDSIZE_DEG)/2.0
#SYMBOLS = (u"\u2713", u"\u2718") # 0 key = correct/ check symbol, 1 key = incorrect/ x symbol
QUIT='f8'

mon = monitors.Monitor("monitor1", width=WIDTH, distance=DIST)
mon.setSizePix(WINSIZE)
mon.save()

### GUI

data_path = "data-exp2/"
if not os.path.exists(data_path):
    os.makedirs(data_path)

expInfo = {'Participant' : 1, 'Gender': ['M', 'F', "O"], 'Age' : 18, "Start from": ['1','2','3']}
expInfo['dateStr'] = data.getDateStr()

dlg = gui.DlgFromDict(expInfo, title = "Basic Information", fixed = ['dateStr'], order=['Participant', 'Age', 'Gender', 'dateStr', "Start from"])
if dlg.OK:
    log_file = open(data_path + "log-file.csv", 'a')
    log_file.write('%s,%s,%s,%s,%s\n' %(expInfo['Participant'], expInfo['Gender'], expInfo['Age'], expInfo["Start from"], expInfo['dateStr']))
    log_file.close()
else:
    core.quit()

pNo = expInfo["Participant"]
gen =  expInfo["Gender"]
age =  expInfo["Age"]
date = expInfo['dateStr']

if age < 50:
    WM_LIST_LEN = 6
else:
    WM_LIST_LEN = 4

N_WORDS = N_PAIRS + (WM_LIST_LEN - 2)*N_WM_OLD_TRIALS + N_WM_NEW_TRIALS*WM_LIST_LEN
N_IMAGES = N_PAIRS + (WM_LIST_LEN - 3)*N_WM_OLD_TRIALS + N_WM_NEW_TRIALS*WM_LIST_LEN

### READ IN STIMULI

# main
stim_cos = pd.read_csv("stimuli/stim-list.csv")

words = stim_cos["Words"].unique().tolist()
images = stim_cos["Images"].unique().tolist()
files = stim_cos["File"].unique().tolist()

'''
if not TEST:
    if N_WORDS != len(words) or N_IMAGES != len(files):
        raise(Warning("number of stimuli isn't right..."))
'''

image_data = pd.DataFrame({"files": pd.Categorical(files)}, index=images)

# prac
prac_stim_cos = pd.read_csv("stimuli/prac-stim-list.csv")

prac_words = prac_stim_cos["Words"].unique().tolist()
prac_images = prac_stim_cos["Images"].unique().tolist()
prac_files = prac_stim_cos["File"].unique().tolist()

prac_image_data = pd.DataFrame({"files": pd.Categorical(prac_files)}, index=prac_images)

### MAKE BLOCK LISTS

# sample pairs for learning ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

learn_words = random.sample(words, N_PAIRS)
learn_images = random.sample(images, N_PAIRS)

learn_pairs = []
for i in range(N_PAIRS):
    learn_pairs.append({"word": learn_words[i], "image": learn_images[i], "file": image_data.at[learn_images[i], "files"]})

# prac

prac_learn_words = random.sample(prac_words, N_LEARN_PRAC)
prac_learn_images = random.sample(prac_images, N_LEARN_PRAC)

prac_learn_pairs = []
for i in range(N_LEARN_PRAC):
    prac_learn_pairs.append({"word": prac_learn_words[i], "image": prac_learn_images[i], "file": prac_image_data.at[prac_learn_images[i], "files"]})

# construct WM trials ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

new_words = random.sample([x for x in words if x not in learn_words], N_WORDS - N_PAIRS) # items themselves
new_images = random.sample([x for x in images if x not in learn_images], N_IMAGES - N_PAIRS)

match_pairs = random.sample(range(len(learn_pairs)), N_WM_OLD_TRIALS) # indices
mismatch_images = random.sample([x for x in range(len(learn_pairs)) if x not in match_pairs], N_WM_OLD_TRIALS)
oldnew_pairs = random.sample([x for x in range(len(learn_pairs)) if x not in match_pairs and x not in mismatch_images], N_WM_OLD_TRIALS)

def re_pair(list_in):
    l = len(list_in)
    ind = random.sample(range(l), l)
    new_ind = [0 if x+1 >= l else x+1 for x in ind] # serves to repair indices such that none match the original (all shifted by 1)
    list_out = [list_in[ind.index(x)] for x in new_ind]
    return(list_out)

mismatch_words = re_pair(mismatch_images)

used_words = []
used_images = []

wm_trials = dict()
for i in range(N_WM_OLD_TRIALS):
    if WM_LIST_LEN == 4:
        wm_type = random.sample(["match", "mis-match", "old-new", "new-new"], 4)
    elif WM_LIST_LEN == 6:
        wm_type = random.sample(["match", "mis-match", "old-new", "new-new", "new-new", "new-new"], 6)

    trial_items = []
    for j in range(WM_LIST_LEN):
        if wm_type[j] == "match":
            trial_items.append({"word": learn_pairs[match_pairs[i]]["word"], "image": learn_pairs[match_pairs[i]]["image"], "file": learn_pairs[match_pairs[i]]["file"], "item_type": "match"})
            learn_pairs[match_pairs[i]]["wm_type"] = "match"
            learn_pairs[match_pairs[i]]["wm_newword"] = "NA"
        if wm_type[j] == "mis-match":
            trial_items.append({"word": learn_pairs[mismatch_words[i]]["word"], "image": learn_pairs[mismatch_images[i]]["image"], "file": learn_pairs[mismatch_images[i]]["file"], "item_type": "mis-match"})
            learn_pairs[mismatch_images[i]]["wm_type"] = "mis-match"
            learn_pairs[mismatch_images[i]]["wm_newword"] = learn_pairs[mismatch_words[i]]["word"]
            #learn_pairs[mismatch_words[i]]["wm_type"] = "mis-match"
        if wm_type[j] == "old-new":
            new_word = random.choice([x for x in new_words if x not in used_words])
            used_words.append(new_word)
            trial_items.append({"word": new_word, "image": learn_pairs[oldnew_pairs[i]]["image"], "file": learn_pairs[oldnew_pairs[i]]["file"], "item_type": "old-new"})
            learn_pairs[oldnew_pairs[i]]["wm_type"] = "old-new"
            learn_pairs[oldnew_pairs[i]]["wm_newword"] = new_word
        if wm_type[j] == "new-new":
            new_word = random.choice([x for x in new_words if x not in used_words])
            new_image = random.choice([x for x in new_images if x not in used_images])
            used_words.append(new_word)
            used_images.append(new_image)
            trial_items.append({"word": new_word, "image": new_image, "file": image_data.at[new_image, "files"], "item_type": "new-new"})

    wm_trials[i] = trial_items

# add the all new trials
for i in range(N_WM_NEW_TRIALS):
    trial_items = []
    for j in range(WM_LIST_LEN):
        new_word = random.choice([x for x in new_words if x not in used_words])
        new_image = random.choice([x for x in new_images if x not in used_images])
        used_words.append(new_word)
        used_images.append(new_image)
        trial_items.append({"word": new_word, "image": new_image, "file": image_data.at[new_image, "files"], "item_type": "new-new"})

    wm_trials[N_WM_OLD_TRIALS + i] = trial_items

random.shuffle(wm_trials) # randomize order

# wm prac
prac_wm_words = random.sample([x for x in prac_words if x not in prac_learn_words], N_WM_PRAC*WM_LIST_LEN)
prac_wm_images = random.sample([x for x in prac_images if x not in prac_learn_images], N_WM_PRAC*WM_LIST_LEN)

prac_wm_trials = dict()
for i in range(N_WM_PRAC):

    prac_trial_items = []
    r_order = random.sample(range(WM_LIST_LEN), WM_LIST_LEN)
    for j in r_order:
        prac_trial_items.append({"word": prac_wm_words[i*WM_LIST_LEN+j], "image": prac_wm_images[i*WM_LIST_LEN+j], "file": prac_image_data.at[prac_wm_images[i*WM_LIST_LEN+j], "files"], "item_type": "prac"})

    prac_wm_trials[i] = prac_trial_items

print(prac_wm_trials)

# list for LTM test ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
ltm_list = []
for ll in mismatch_images:
    ltm_list.append({"image": learn_pairs[ll]["image"], "file": learn_pairs[ll]["file"], "target": learn_pairs[ll]["word"], "lure": learn_pairs[ll]["wm_newword"], "wm_type": learn_pairs[ll]["wm_type"]})

# pair half of the studied images with new lures
ltm_nonmismatch = [x for x in range(len(learn_pairs)) if x not in mismatch_images]
ltm_images = random.sample(ltm_nonmismatch, N_WM_OLD_TRIALS) # select half of non-mismatch items to serve as cues
ltm_lures = [x for x in ltm_nonmismatch if x not in ltm_images] # find those not used as cues to use as lures

for ll in range(N_WM_OLD_TRIALS):
    ltm_list.append({"image": learn_pairs[ltm_images[ll]]["image"], "file": learn_pairs[ltm_images[ll]]["file"], "target": learn_pairs[ltm_images[ll]]["word"], "lure": learn_pairs[ltm_lures[ll]]["word"], "wm_type": learn_pairs[ltm_images[ll]]["wm_type"]})

random.shuffle(ltm_list)

# example image for instructions
example_word = random.choice([x for x in prac_words if x not in prac_learn_words and x not in prac_wm_words])
example_image = random.choice([x for x in prac_images if x not in prac_learn_images and x not in prac_wm_images])
example_file = prac_image_data.at[example_image, "files"]


### EXPERIMENT FUNCTIONS

## functions for implementing experiment

# presenting stimuli ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

def press_key(text = 'Press SPACE to continue', k_list = ['space']):
    instr.text = text
    instr.draw()
    win.flip()
    k_list.append(QUIT)
    if not TEST:
        key = event.waitKeys(keyList = k_list)[0]
        if key == QUIT:
            core.quit()
        else:
            return(key)
    else:
        core.wait(.1)
        return("space")

def present_instructions(instr_list, forward_key = "space", backward_key = "backspace"):
    n_instr = len(instr_list)

    c_instr = 0
    while c_instr < n_instr:
        k = press_key(text = instr_list[c_instr], k_list = [forward_key, backward_key])
        if k == forward_key:
            c_instr += 1
        if k == backward_key and c_instr > 0:
            c_instr -= 1

def study_pair(image, word, study_time = 4, isi = .5):

    i_stim.image = "stimuli/images/" + image + ".png"
    t_stim.text = word.upper()

    rect.draw()
    i_stim.draw()
    t_stim.draw()
    win.flip()
    core.wait(study_time)

    win.flip()
    core.wait(isi)


def recall_pair(cue_image, correct_word, time_lim = 10, feedback = True, feedback_time = .5, restudy_time = 4, char_lim = 10):
    if not isinstance(cue_image, str) or not isinstance(correct_word, str):
        raise(Warning("in recall_pair - only one cue string at a time"))

    valid_keys = list(string.ascii_lowercase)

    i_stim.image = "stimuli/images/" + cue_image + ".png"

    event.clearEvents()
    prompt = "..."
    input = prompt
    finished = False
    RT.reset()
    while not finished and RT.getTime() <= time_lim:
        t_stim.text = input
        rect.draw()
        i_stim.draw()
        t_stim.draw()
        win.flip()

        n_chars = len(list(input))
        for key in event.getKeys():
            if key in [QUIT]:
                core.quit()
            if key in ['backspace'] and n_chars > 0 and input != prompt:
                input = input[:-1] # remove last char
                if len(list(input)) == 0:
                    input = prompt
            if key in valid_keys and n_chars < char_lim:
                if input == prompt:
                    input = ""
                input = input + key.upper()
            if key in ['return']:
                finished = True

    recall_rt = RT.getTime()
    recalled = input.lower()

    correct = int(recalled == correct_word)

    if feedback:
        if correct == 1:
            t_stim.color = [0,1,0]
            t_stim.text = recalled.upper()
            rect.draw()
            i_stim.draw()
            t_stim.draw()
            win.flip()
            core.wait(feedback_time)
            t_stim.color = FOREGROUND
        else:
            t_stim.color = [1,0,0]
            t_stim.text = recalled.upper()
            rect.draw()
            i_stim.draw()
            t_stim.draw()
            win.flip()
            core.wait(feedback_time)

            t_stim.color = FOREGROUND
            t_stim.text = correct_word.upper()
            rect.draw()
            i_stim.draw()
            t_stim.draw()
            win.flip()
            core.wait(restudy_time)

    win.flip()
    core.wait(.25)

    if recalled == prompt:
        recalled = "NA"

    return(recalled, correct, recall_rt)


# function for final ltm test ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

def tafc(cue_image, target, lure):

    i_stim.image = "stimuli/images/" + cue_image + ".png"

    target_right = random.choice([0,1])

    if target_right == 1:
        test_str = lure.upper() + "  -  " + target.upper()
    else:
        test_str = target.upper() + "  -  " + lure.upper()

    t_stim.text = test_str

    rect.draw()
    i_stim.draw()
    t_stim.draw()
    win.flip()

    event.clearEvents()
    finished = False
    RT.reset()
    while not finished:
        for key in event.getKeys():
            if key in [QUIT]:
                core.quit()
            if key in ['right']:
                resp_right = 1
                finished = True
            if key in ['left']:
                resp_right = 0
                finished = True

    tafc_rt = RT.getTime()
    tafc_acc = int(target_right == resp_right)

    return(tafc_acc, tafc_rt, target_right, resp_right)


# function for secondary task ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
def secondary_task(n_items, total_duration = 10, start_delay = 1, keys=['0','1'], key_map = [1,0], isi = .25):

    duration = total_duration - start_delay # time taken by the task

    all_digits = [[x,y] for x in range(1,10,1) for y in range(1,10,1) if y >= x]

    digits = random.sample(all_digits, n_items)

    solution_acc = [random.choice([0,1]) for i in range(n_items)]
    order = [random.sample([0,1], 2) for i in range(n_items)]

    digits = [[digits[i][order[i][0]], digits[i][order[i][1]]] for i in range(n_items)]

    solutions = [sum(digits[i]) for i in range(n_items)]

    answers = [solutions[i] + random.choice([-1, 1]) if solution_acc[i] == 0 else solutions[i] for i in range(n_items)]

    resp_time = float(duration)/n_items
    draw_time = resp_time - isi

    win.flip()
    core.wait(start_delay)

    event.clearEvents()

    resps = []
    acc = []
    rts = []
    for i in range(n_items):

        trial_str = str(digits[i][0]) + " + " + str(digits[i][1]) + ' = ' + str(answers[i])

        instr.text = trial_str
        done = False
        RT.reset()

        while RT.getTime() <= resp_time:
            if RT.getTime() <= draw_time:
                instr.draw()
            win.flip()

            for key in event.getKeys(): # check for response on each frame
                if key in keys and not done and RT.getTime() <= resp_time:
                    resps.append(key)
                    acc.append(int(keys.index(key) == key_map.index(solution_acc[i])))
                    rts.append(RT.getTime())
                    done = True

        if len(resps) < i+1: # if no response was given in time
            resps.append('NA')
            acc.append(0)
            rts.append("NA")

    return(digits, answers, solution_acc, resps, acc, rts)
'''

# function for blocks of learning ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

def learn_blocks(learn_list, feedback = True, group_into = 10, n_blocks = 6):

    l_list = deepcopy(learn_list) # dont modify original list

    if len(l_list) != group_into*n_blocks:
        raise(Warning("in learn_block - learn_list not the right length"))

    random.shuffle(l_list)

    for b in range(n_blocks):
        press_key("Press SPACE to start.")
        win.flip()
        core.wait(.5)
        # study
        for l in range(group_into):
            study_pair(image = l_list[b*group_into + l]["file"], word = l_list[b*group_into + l]["word"])
            l_list[b*group_into + l]["block"] = b
            l_list[b*group_into + l]["study_order"] = l

        # recall in random order
        recall_order = range(group_into)
        random.shuffle(recall_order)

        instr.text = "RECALL"
        instr.draw()
        win.flip()
        core.wait(1)
        for l in range(group_into):
            recalled, acc, rt = recall_pair(cue_image = l_list[b*group_into + recall_order[l]]["file"], correct_word = l_list[b*group_into + recall_order[l]]["word"])
            l_list[b*group_into + recall_order[l]]["recall_order"] = l
            l_list[b*group_into + recall_order[l]]["recalled"] = recalled
            l_list[b*group_into + recall_order[l]]["recall_acc"] = acc
            l_list[b*group_into + recall_order[l]]["recall_rt"] = rt

        press_key("End of block.\n\nPress SPACE to continue.")

    return(l_list)


# function for test of learning ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

def learn_test(learn_list):

    l_list = deepcopy(learn_list) # dont modify original list

    random.shuffle(l_list)

    for i in range(len(l_list)):
        recalled, acc, rt = recall_pair(cue_image = l_list[i]["file"], correct_word = l_list[i]["word"])
        l_list[i]["recall_order"] = i
        l_list[i]["recalled"] = recalled
        l_list[i]["recall_acc"] = acc
        l_list[i]["recall_rt"] = rt

    return(l_list)


# WM task ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

def wm_block(trial_list, study_time=2, isi=.5):

    t_list = deepcopy(trial_list) # dont modify original list

    #sec_task_dat = []
    for i in range(len(t_list)):

        ll = len(t_list[i])

        press_key("Press SPACE to start trial.")
        win.flip()
        core.wait(.5)
        for j in range(ll):
            study_pair(image = t_list[i][j]["file"], word = t_list[i][j]["word"], study_time = study_time, isi = isi)
            t_list[i][j]["study_order"] = j

        #st_digits, st_answers, st_solution_acc, st_resps, st_acc, st_rts = secondary_task(n_items = 5)
        win.flip(); core.wait(2)

        recall_order = range(ll)
        random.shuffle(recall_order)

        for k in range(ll):
            recalled, acc, rt = recall_pair(cue_image = t_list[i][recall_order[k]]["file"], correct_word = t_list[i][recall_order[k]]["word"], feedback=False)
            t_list[i][recall_order[k]]["trial_no"] = i
            t_list[i][recall_order[k]]["recall_order"] = k
            t_list[i][recall_order[k]]["recalled"] = recalled
            t_list[i][recall_order[k]]["recall_acc"] = acc
            t_list[i][recall_order[k]]["recall_rt"] = rt

        #for l in range(len(st_resps)):
        #    sec_task_dat.append({"trial_no": i, "item": l, "digit1": st_digits[l][0], "digit2": st_digits[l][1], "answer_given": st_answers[l], "answer_acc": st_solution_acc[l], "response_key": st_resps[l], "response_acc": st_acc[l], "rt": st_rts[l]})

        if (i + 1)/float(len(t_list)) == 0.5 :
            press_key("You're half way!\n\nPlease take a break if you need one.\n\nPress \
SPACE when you are ready to continue.")

    #return(t_list, sec_task_dat)
    return(t_list)

'''
def secondary_block(n_trials):
    sec_task_dat = []

    for tr in range(n_trials):
        press_key("Rest your fingers on the %s and %s keys and press either to start trial." % SYMBOLS, k_list=["0", "1"])
        st_digits, st_answers, st_solution_acc, st_resps, st_acc, st_rts = secondary_task(n_items = 5)

        for l in range(len(st_resps)):
            sec_task_dat.append({"trial_no": tr, "item": l, "digit1": st_digits[l][0], "digit2": st_digits[l][1], "answer_given": st_answers[l], "answer_acc": st_solution_acc[l], "response": st_resps[l], "response_acc": st_acc[l], "rt": st_rts[l]})

    return(sec_task_dat)
'''

# LTM test ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

def ltm_test(test_list):

    t_list = deepcopy(test_list)

    press_key("Rest your fingers on the %s and %s keys and press either to start." % (u"\u25C4", u"\u25BA"), k_list=["left", "right"])
    win.flip()
    core.wait(.5)
    for i in range(len(t_list)):
        tafc_acc, tafc_rt, target_right, resp_right = tafc(cue_image = t_list[i]["file"], target = t_list[i]["target"], lure = t_list[i]["lure"])
        t_list[i]["acc"] = tafc_acc
        t_list[i]["rt"] = tafc_rt
        t_list[i]["target_right"] = target_right
        t_list[i]["resp_right"] = resp_right

        win.flip()
        core.wait(.5)

    return(t_list)


## MAIN EXPERIMENT

def main():

    global win, t_stim, i_stim, rect, instr, RT
    win = visual.Window(WINSIZE, units = 'deg', allowGUI= False, fullScr=True, color=BACKGROUND, monitor=mon)

    t_stim = visual.TextStim(win, color=FOREGROUND, pos=[0, -IMWORD_SEP/2.0], height=WORDSIZE_DEG, wrapWidth=25)
    i_stim = visual.ImageStim(win, pos=[0, IMWORD_SEP/2.0], size=[IMSIZE_DEG]*2) # alt. SimpleImageStim
    rect = visual.Rect(win, pos=[0,IMWORD_SEP/2.0], width=IMSIZE_DEG, height=IMSIZE_DEG, lineColor=[1,1,1], fillColor=[1,1,1])
    instr = visual.TextStim(win, color=FOREGROUND, pos=[0, 0], height=1, wrapWidth=20)
    RT = core.Clock()

    global_time = core.Clock() # to time study

    # each participant gets their own folder
    save_path = data_path + "participant_" + str(pNo) + "_e2_" + date + "/"
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    file_name = save_path + "p" + str(pNo) + "_e2_" + date + "_" # + a file specific suffix

    # allow the session to be restarted at a particular part if a crash occurs
    global learn_pairs, wm_trials, ltm_list

    # print(ltm_list)
    if expInfo["Start from"] != '1':
        # if we're not starting from the beginning we need to read in old objects
        # look for pickled objects matching participant number
        possible_dirs = [d for d in os.listdir(data_path) if d.startswith("participant_" + str(pNo)) and data_path+d+"/" != save_path]
        if len(possible_dirs) > 0:
            dir_choice = [string.ascii_lowercase[i] for i in range(len(possible_dirs))]
            dir_string = "\n".join([dir_choice[i] + ": " + possible_dirs[i] for i in range(len(possible_dirs))])
            dir_selection = press_key("The following folders were found for this participant number - press a letter key to select the correct folder for this participant.\n\n" + dir_string, k_list = dir_choice)

            load_dir = possible_dirs[dir_choice.index(dir_selection)]
            load_file = load_dir.replace("participant_", 'p')

            # check if the right data for the previous run was written
            if expInfo["Start from"] in ['2', '3'] and not os.path.exists(data_path + load_dir + "/" + load_file + "_learning-test.csv"):
                raise(Warning("You selected to start from part %s but the data from part 1 does not exist" % expInfo["Start from"]))
            if expInfo["Start from"] == '3' and not os.path.exists(data_path + load_dir + "/" + load_file + "_wm-main.csv"):
                raise(Warning("You selected to start from part 3 but the data from part 2 does not exist"))

            print("Loading lists from: " + load_dir)
            # replaces the files created above with ones created in a previously creashed session
            learn_pairs = pickle.load(open(data_path + load_dir + "/" + load_file + "_learn-list.pkl", "rb"))
            wm_trials = pickle.load(open(data_path + load_dir + "/" + load_file + "_wm-trials.pkl", "rb"))
            ltm_list = pickle.load(open(data_path + load_dir + "/" + load_file + "_ltm-list.pkl", "rb"))

            # write note
            sf_note = open(file_name + "start-from-note.txt","w")
            sf_note.write("Block lists loaded from " + load_dir)
            sf_note.close()

        else:
            press_key("You selected to start from part %s but no previous run can be found with the participant number %d. Press space to exit" %(expInfo["Start from"], pNo))
            core.quit()
    # print(ltm_list)

    # pickle the lists for future reference
    with open(file_name + "learn-list.pkl", "wb") as f:
        pickle.dump(learn_pairs, f)
    with open(file_name + "wm-trials.pkl", "wb") as f:
        pickle.dump(wm_trials, f)
    with open(file_name + "ltm-list.pkl", "wb") as f:
        pickle.dump(ltm_list, f)

    if expInfo["Start from"] == '1':
        # intro
        instr.text = "Welcome"
        instr.draw()
        win.flip()
        core.wait(1)

        intro_instr = "This experiment is split into three parts.\n\nWe will let you know what you need to do at the \
beginning of each part.\n\nPress SPACE to start."
        press_key(intro_instr)

        # run learning blocks
        instr.text = "PART 1"
        instr.draw()
        win.flip()
        core.wait(2)

        learn_instr1 = "In this part of the experiment we will present you with pairs of images and \
words to learn. Your memory for these pairs will also be tested in part 3.\n\nPress SPACE to see an example pair."
        press_key(learn_instr1)

        study_pair(image = example_file, word = example_word) # example pair

        learn_instr_list = [
        # screen 1
        "The pairs will be presented in groups of %i for you to study - after the %i pairs have been \
presented you will be asked to recall the word associated with each picture.\n\nPress SPACE to continue." % (GROUP_INTO, GROUP_INTO),
        # screen 2
        "During recall you will see '...' below an image you previously saw. You will have up to 10 seconds to \
recall the word associated with the image by saying the word out loud. The researcher will type your response.\n\nPress SPACE to continue."
        # screen 3
        "You will get feedback on whether the word you recall is right or wrong.\n\nThe word will turn green if it is right and red if it \
wrong. If it is wrong you will also see the correct word with the picture again.\n\nPress SPACE to continue.",
        # screen 4
        "You will now have a chance to practice this task. During practice you will see %i pairs to remember and \
then recall.\n\nPress SPACE to start." % N_LEARN_PRAC]

        present_instructions(learn_instr_list)

        prac_learn_dat = learn_blocks(learn_list = prac_learn_pairs, group_into=N_LEARN_PRAC, n_blocks=1)
        press_key("End of practice.\n\nIf you have any questions, please ask the researcher now. Remember, in the main task the pairs will be presented in blocks of %i.\n\nPress \
SPACE when you are ready to start the main task." % GROUP_INTO)

        start_loop = global_time.getTime()
        print("Start of learn loops = %.4f" % start_loop)

        loop = 0
        learn_done = False
        while not learn_done:
            loop += 1
            learn_dat = learn_blocks(learn_list = learn_pairs, group_into=GROUP_INTO, n_blocks=N_LEARN_BLOCK)

            learn_dat_pd = pd.DataFrame(learn_dat)
            learn_dat_pd["pid"] = pNo
            learn_dat_pd["date"] = date
            learn_dat_pd["age"] = age
            learn_dat_pd["block_loop"] = loop
            learn_dat_pd.to_csv(file_name + "learning-loop" + str(loop) + ".csv")
            learn_dat_pd.to_pickle(file_name + "learning-loop" + str(loop) + ".pkl")

            print(learn_dat_pd["recall_acc"].mean())
            if loop >= N_MAX_LEARN_LOOPS or learn_dat_pd["recall_acc"].mean() > .8:
                learn_done = True
            else:
                press_key("We'll do another loop though the pairs.\n\nPlease take a break if you need one.\n\nPress \
SPACE when you are ready to continue.")

        end_loop = global_time.getTime()
        print("End of learn loops = %.4f" % end_loop)
        print("Duration = %.4f" % (end_loop - start_loop))
        print("\n\n")

        # test learning
        test_instr = "Now you will be tested on all of the %i pairs you have been learning.\n\nOn each trial, an image \
will be presented and your task is to recall the word associated with the image. If you have any questions, \
please ask the researcher now.\n\nPress SPACE to start." % len(learn_pairs)
        press_key(test_instr)

        start_test = global_time.getTime()
        print("Start of learn test = %.4f" % start_test)

        learn_test_dat = learn_test(learn_list = learn_pairs)

        learn_test_dat_pd = pd.DataFrame(learn_test_dat)
        learn_test_dat_pd["pid"] = pNo
        learn_test_dat_pd["date"] = date
        learn_test_dat_pd["age"] = age
        learn_test_dat_pd.to_csv(file_name + "learning-test.csv")
        learn_test_dat_pd.to_pickle(file_name + "learning-test.pkl")

        end_test = global_time.getTime()
        print("End of learn test = %.4f" % end_test)
        print("Duration = %.4f" % (end_test - start_test))
        print("\n\n")

        end_learn_instr = "That is the end of part 1.\n\nWe will test your memory for the pairs you have learned \
in the final part of this experiment, so try to remember them.\n\nPress SPACE to continue."
        press_key(end_learn_instr)

    if expInfo["Start from"] != '3':
        # run wm task
        instr.text = "PART 2"
        instr.draw()
        win.flip()
        core.wait(2)

        wm_instr_list =[
        # screen 1
        "The task in this part of the experiment also uses pairs of images and words but is different from the task \
you did in part 1.\n\nIn this task you will be presented with sequences of %i image-word pairs to hold in mind over \
a 2 second interval.\n\nPress SPACE to continue." %(WM_LIST_LEN),
        # screen 2
        "After the 2 second interval you will be asked to recall out loud the word associated with each image.\n\nNext we will give you %i \
trials to practice this task.\n\nPress SPACE to start." % N_WM_PRAC
        ]

        present_instructions(wm_instr_list)

        #prac_wm_dat, prac_st_dat = wm_block(prac_wm_trials)
        prac_wm_dat = wm_block(prac_wm_trials)
        press_key("End of practice. If you have any questions about this task, please ask the researcher now.\n\nPress SPACE to start the main task.")

        start_wm = global_time.getTime()
        print("Start of wm task = %.4f" % start_wm)

        #wm_dat, st_dat = wm_block(wm_trials)
        wm_dat = wm_block(wm_trials)

        wm_dat_l = [] # unpack things to convert to pandas
        for i in range(len(wm_dat)):
            for j in range(len(wm_dat[i])):
                wm_dat_l.append(wm_dat[i][j])

        wm_dat_pd = pd.DataFrame(wm_dat_l)
        wm_dat_pd["pid"] = pNo
        wm_dat_pd["date"] = date
        wm_dat_pd["age"] = age
        wm_dat_pd.to_csv(file_name + "wm-main.csv")
        wm_dat_pd.to_pickle(file_name + "wm-main.pkl")

        end_wm = global_time.getTime()
        print("End of wm task = %.4f" % end_wm)
        print("Duration = %.4f" % (end_wm - start_wm))
        print("\n\n")

        press_key("End of part 2.\n\nPress SPACE to continue.")

    # run ltm test
    instr.text = "PART 3"
    instr.draw()
    win.flip()
    core.wait(2)

    ltm_instr_list = [
    # screen 1
    "This is the final test of the pairs you learned in part 1 of the experiment.\n\nOn each trial you will see an \
image with two words below it - one word will have been paired with the image in part 1. The other word will have \
been studied in the first part but not with that image.\n\nPress SPACE to continue",
    # screen 2
    "It is your task to indicate which word was paired with the particular image in part 1 of \
the experiment.\n\nWhen each image appears, use the left (%s) or right (%s) arrow keys to choose the correct \
word.\n\nPlease respond as quickly and as accurately as possible. If you have any questions about this \
task, please ask the researcher now.\n\nPress SPACE to start." % (u"\u25C4", u"\u25BA")
    ]

    present_instructions(ltm_instr_list)

    start_ltm = global_time.getTime()
    print("Start of ltm task = %.4f" % start_ltm)

    ltm_dat = ltm_test(test_list = ltm_list)

    ltm_dat_pd = pd.DataFrame(ltm_dat)
    ltm_dat_pd["pid"] = pNo
    ltm_dat_pd["date"] = date
    ltm_dat_pd["age"] = age
    ltm_dat_pd.to_csv(file_name + "ltm-task.csv")
    ltm_dat_pd.to_pickle(file_name + "ltm-task.pkl")

    end_ltm = global_time.getTime()
    print("End of ltm task = %.4f" % end_ltm)
    print("Duration = %.4f" % (end_ltm - start_ltm))
    print("\n\n")

    dur_f = open(file_name + "run-duration.txt","w")
    dur_f.write("Total running time = %.4f seconds \n\n" % end_ltm)
    if expInfo["Start from"] == '1':
        dur_f.write("Learn blocks = %.4f \n\n" % (end_loop - start_loop))
        dur_f.write("Learn test = %.4f \n\n" % (end_test - start_test))
    if expInfo["Start from"] != '3':
        dur_f.write("WM task = %.4f \n\n" % (end_wm - start_wm))
    dur_f.write("TAFC task = %.4f" % (end_ltm - start_ltm))
    dur_f.close()

    press_key("End of Experiment. Great job!\n\nThank you for taking part!")

if __name__ == '__main__':
    main()

# end
