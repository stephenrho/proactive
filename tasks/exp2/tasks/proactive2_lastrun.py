#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on Thu Aug 13 06:17:16 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.2'
expName = 'proactive'  # from the Builder filename that created this script
expInfo = {'participant': '', 'please enter your date of birth (dd/mm/yyyy)': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/stephenrhodes/Dropbox/Current Projects/Baycrest/proactive/online/exp2/task/proactive2_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 800], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='norm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "consent"
consentClock = core.Clock()
consent_text = visual.TextStim(win=win, name='consent_text',
    text='Thank you for volunteering to take part in this study conducted by researchers at the Department of Psychology at the University of Toronto. In this study we are looking at memory for random pairs of images and words. The images are drawings of everyday objects and the words are nouns with 4-6 letters. The study is split into two parts: The first part assesses learning of image-word pairs and the second part looks at short-term memory. In both parts your memory will be tested by presenting an image and asking you to recall the associated word by typing on the keyboard.\n\nThe data we collect for this study concerns the accuracy and speed of memory recall. These data will be stored in an anonymised format (using the ID assigned to you by prolific) and may be shared with other researchers via public data repositories (such as the open science framework; www.osf.io). You may exit the study at any time without penalty by pressing the escape key.\n\nIf you consent to take part in this study, please press ‘Y’\n\nIf you do not consent to take part, please press the escape key and close this window',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=1.8, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
consent_key = keyboard.Keyboard()

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
welcome_text = visual.TextStim(win=win, name='welcome_text',
    text='This experiment is split into two sections.\n\nWe will let you know what you need to do at the beginning of each section.\n\nPress SPACE to start.\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.6, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
welcome_adv = keyboard.Keyboard()
from random import randint

list = randint(1, 6)
expInfo["list"] = list

skip_learn=1
continue_learning=True

im_size = [100/1920, 100/1080]

xpos = 400/1920
ypos=400/1080

xdisp = .03
ydisp = im_size[1]

# Initialize components for Routine "learn_instr1"
learn_instr1Clock = core.Clock()
part1 = visual.TextStim(win=win, name='part1',
    text='SECTION 1',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
learn_intsr_text = visual.TextStim(win=win, name='learn_intsr_text',
    text='In this section of the experiment we will present you with pairs of images and words to learn. An example pair is shown above. Press SPACE to continue.\n',
    font='Arial',
    pos=(0, -.7), height=0.1, wrapWidth=1.6, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
learn_instr_adv = keyboard.Keyboard()
ex_word = visual.TextStim(win=win, name='ex_word',
    text='TOUGH',
    font='Arial',
    pos=(0, -.204), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
ex_im = visual.ImageStim(
    win=win,
    name='ex_im', 
    image='stimuli/images/PICTURE_747.png', mask=None,
    ori=0, pos=(0, .204), size=(600/1920, 600/1080),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "learn_instr2"
learn_instr2Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='There are 30 pairs to learn and we will present them in groups of 10.\n\nThe 10 pairs will be presented in sequences and after they have been presented you will be asked to recall the word associated with each image.\n\nPress SPACE to continue.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.6, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "learn_instr3"
learn_instr3Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text="During recall you will see an image you previously saw. You will have up to 15 seconds to recall the word associated with the image by typing it on the keyboard. Once the 15 seconds are up the task will move on automatically.\n\nWhen you have finished typing press the enter (or return) key to submit. If you can't remember the word you can press enter to pass. You can also delete mistakes using the backspace key.\n\nPress SPACE to continue.",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.6, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "learn_instr4"
learn_instr4Clock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='You will get feedback on whether the word you recall is right or wrong. The word will turn green if it is right. If it is wrong the word you typed will turn red then you will see the correct word with the image again.\n\nOn the next screen you will see the image you saw before. Please type in the word that you saw with it and press enter (or return) to submit.\n\nPress SPACE to continue.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.6, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "learn_test"
learn_testClock = core.Clock()
timer = core.Clock()
test_image = visual.ImageStim(
    win=win,
    name='test_image', 
    image='sin', mask=None,
    ori=0, pos=(0, .204), size=(600/1920, 600/1080),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
recall_text = visual.TextStim(win=win, name='recall_text',
    text=None,
    font='Arial',
    pos=(0, -.204), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "learn_feedback"
learn_feedbackClock = core.Clock()
feedback_text = visual.TextStim(win=win, name='feedback_text',
    text='default text',
    font='Arial',
    pos=(0, -.204), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
feed_image = visual.ImageStim(
    win=win,
    name='feed_image', 
    image='sin', mask=None,
    ori=0, pos=(0, .204), size=(600/1920, 600/1080),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
post_fb_int = visual.TextStim(win=win, name='post_fb_int',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
restudy_text = visual.TextStim(win=win, name='restudy_text',
    text='default text',
    font='Arial',
    pos=(0, -.204), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "learn_instr5"
learn_instr5Clock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='Great! You will now have a chance to practice this task. During practice you will see 5 pairs to remember and then recall.\n\nPress SPACE to start.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.6, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "learn_study"
learn_studyClock = core.Clock()
study_text = visual.TextStim(win=win, name='study_text',
    text='default text',
    font='Arial',
    pos=(0, -.204), height=.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
study_image = visual.ImageStim(
    win=win,
    name='study_image', 
    image='sin', mask=None,
    ori=0, pos=(0, .204), size=(600/1920, 600/1080),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "learn_test_instr"
learn_test_instrClock = core.Clock()
learn_test_instr_text = visual.TextStim(win=win, name='learn_test_instr_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "learn_test"
learn_testClock = core.Clock()
timer = core.Clock()
test_image = visual.ImageStim(
    win=win,
    name='test_image', 
    image='sin', mask=None,
    ori=0, pos=(0, .204), size=(600/1920, 600/1080),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
recall_text = visual.TextStim(win=win, name='recall_text',
    text=None,
    font='Arial',
    pos=(0, -.204), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "learn_feedback"
learn_feedbackClock = core.Clock()
feedback_text = visual.TextStim(win=win, name='feedback_text',
    text='default text',
    font='Arial',
    pos=(0, -.204), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
feed_image = visual.ImageStim(
    win=win,
    name='feed_image', 
    image='sin', mask=None,
    ori=0, pos=(0, .204), size=(600/1920, 600/1080),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
post_fb_int = visual.TextStim(win=win, name='post_fb_int',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
restudy_text = visual.TextStim(win=win, name='restudy_text',
    text='default text',
    font='Arial',
    pos=(0, -.204), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "learn_end_prac"
learn_end_pracClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text="End of practice.\n\nWe will now go though all of the pairs in groups of 10. We'll keep going until you get 80% correct or until you have seen all of the pairs three times.\n\nPress SPACE when you are ready to start the main task.",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.6, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "set_counter"
set_counterClock = core.Clock()

# Initialize components for Routine "begin_block"
begin_blockClock = core.Clock()
text_10 = visual.TextStim(win=win, name='text_10',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.6, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_12 = keyboard.Keyboard()

# Initialize components for Routine "learn_study"
learn_studyClock = core.Clock()
study_text = visual.TextStim(win=win, name='study_text',
    text='default text',
    font='Arial',
    pos=(0, -.204), height=.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
study_image = visual.ImageStim(
    win=win,
    name='study_image', 
    image='sin', mask=None,
    ori=0, pos=(0, .204), size=(600/1920, 600/1080),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "learn_test_instr"
learn_test_instrClock = core.Clock()
learn_test_instr_text = visual.TextStim(win=win, name='learn_test_instr_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "learn_test"
learn_testClock = core.Clock()
timer = core.Clock()
test_image = visual.ImageStim(
    win=win,
    name='test_image', 
    image='sin', mask=None,
    ori=0, pos=(0, .204), size=(600/1920, 600/1080),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
recall_text = visual.TextStim(win=win, name='recall_text',
    text=None,
    font='Arial',
    pos=(0, -.204), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "learn_feedback"
learn_feedbackClock = core.Clock()
feedback_text = visual.TextStim(win=win, name='feedback_text',
    text='default text',
    font='Arial',
    pos=(0, -.204), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
feed_image = visual.ImageStim(
    win=win,
    name='feed_image', 
    image='sin', mask=None,
    ori=0, pos=(0, .204), size=(600/1920, 600/1080),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
post_fb_int = visual.TextStim(win=win, name='post_fb_int',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
restudy_text = visual.TextStim(win=win, name='restudy_text',
    text='default text',
    font='Arial',
    pos=(0, -.204), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "next_instr"
next_instrClock = core.Clock()
next_instr_text = visual.TextStim(win=win, name='next_instr_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.6, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_13 = keyboard.Keyboard()

# Initialize components for Routine "break_learn"
break_learnClock = core.Clock()

# Initialize components for Routine "learn_final_instr"
learn_final_instrClock = core.Clock()
learn_final_text = visual.TextStim(win=win, name='learn_final_text',
    text='Now we will ask you about all of the 30 pairs you have been learning.\n\nEach image will be presented and your task is to recall the word associated with the image. Remember, you have 10 seconds to type your answer and press enter (or return) to submit.\n\nPress SPACE to start.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.6, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "learn_test"
learn_testClock = core.Clock()
timer = core.Clock()
test_image = visual.ImageStim(
    win=win,
    name='test_image', 
    image='sin', mask=None,
    ori=0, pos=(0, .204), size=(600/1920, 600/1080),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
recall_text = visual.TextStim(win=win, name='recall_text',
    text=None,
    font='Arial',
    pos=(0, -.204), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "learn_feedback"
learn_feedbackClock = core.Clock()
feedback_text = visual.TextStim(win=win, name='feedback_text',
    text='default text',
    font='Arial',
    pos=(0, -.204), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
feed_image = visual.ImageStim(
    win=win,
    name='feed_image', 
    image='sin', mask=None,
    ori=0, pos=(0, .204), size=(600/1920, 600/1080),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
post_fb_int = visual.TextStim(win=win, name='post_fb_int',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
restudy_text = visual.TextStim(win=win, name='restudy_text',
    text='default text',
    font='Arial',
    pos=(0, -.204), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "end_learn"
end_learnClock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text='That is the end of the first section.\n\nPress SPACE to continue.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.6, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_10 = keyboard.Keyboard()

# Initialize components for Routine "wm_instr"
wm_instrClock = core.Clock()
part2 = visual.TextStim(win=win, name='part2',
    text='SECTION 2',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
wm_text = visual.TextStim(win=win, name='wm_text',
    text='The task in this section also uses pairs of images and words but is different from the task you did in section 1. In this section we are looking at short-term memory for pairs.\n\nIn this task you will be presented with sequences of 4 image-word pairs to hold in mind over a 2 second interval. During this 2 second interval you will be asked to perform another task (more on this soon).\n\nPress SPACE to continue.\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.6, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "wm_instr2"
wm_instr2Clock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text="After the 2 second interval you will be asked to recall the word associated with each image by typing it on the keyboard then pressing enter (or return) to submit. There won't be any feedback in this section.\n\nNext we will tell you more about the task your are asked to do during the 2 second interval.\n\nPress SPACE to start.",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.6, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_8 = keyboard.Keyboard()

# Initialize components for Routine "search_instr"
search_instrClock = core.Clock()
top_text = visual.TextStim(win=win, name='top_text',
    text='During the 2 second interval between seeing the pairs you need to remember and recalling them there is a search task. In this task you will see square symbols with open sides. All but one of these symbols will have an open side at the top or bottom.',
    font='Arial',
    pos=(0, .6), height=0.08, wrapWidth=1.6, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
mid_text = visual.TextStim(win=win, name='mid_text',
    text="The task is to find the one symbol that is open at the left or right. When you have found it press '1' if the square is open on the left or '0' for right.",
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=1.6, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
bottom_text = visual.TextStim(win=win, name='bottom_text',
    text="The next screen shows an example of a search screen where the correct answer is 'right' (the '0' key). \n\nPress SPACE to continue",
    font='Arial',
    pos=(0, -.5), height=0.08, wrapWidth=1.6, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
t_im = visual.ImageStim(
    win=win,
    name='t_im', 
    image='stimuli/search/t.png', mask=None,
    ori=0, pos=(-.2, .25), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
b_im = visual.ImageStim(
    win=win,
    name='b_im', 
    image='stimuli/search/b.png', mask=None,
    ori=0, pos=(.2, .25), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
l_im = visual.ImageStim(
    win=win,
    name='l_im', 
    image='stimuli/search/l.png', mask=None,
    ori=0, pos=(-.2, -.25), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
r_im = visual.ImageStim(
    win=win,
    name='r_im', 
    image='stimuli/search/r.png', mask=None,
    ori=0, pos=(.2, -.25), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
key_resp_11 = keyboard.Keyboard()

# Initialize components for Routine "search_instr2"
search_instr2Clock = core.Clock()
sim1_ex = visual.ImageStim(
    win=win,
    name='sim1_ex', 
    image='stimuli/search/t.png', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
sim2_ex = visual.ImageStim(
    win=win,
    name='sim2_ex', 
    image='stimuli/search/b.png', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
sim3_ex = visual.ImageStim(
    win=win,
    name='sim3_ex', 
    image='stimuli/search/b.png', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
sim4_ex = visual.ImageStim(
    win=win,
    name='sim4_ex', 
    image='stimuli/search/t.png', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
sim5_ex = visual.ImageStim(
    win=win,
    name='sim5_ex', 
    image='stimuli/search/t.png', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
sim6_ex = visual.ImageStim(
    win=win,
    name='sim6_ex', 
    image='stimuli/search/b.png', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
sim7_ex = visual.ImageStim(
    win=win,
    name='sim7_ex', 
    image='stimuli/search/t.png', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
sim8_ex = visual.ImageStim(
    win=win,
    name='sim8_ex', 
    image='stimuli/search/r.png', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
text_12 = visual.TextStim(win=win, name='text_12',
    text="In this case the target is in the bottom left of the screen and is open on the right (so the correct response is '0'). In the main task the symbols will only be presented for 2 seconds. Press SPACE to continue\n",
    font='Arial',
    pos=(0, -.75), height=0.08, wrapWidth=1.6, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
key_resp_14 = keyboard.Keyboard()
text_15 = visual.TextStim(win=win, name='text_15',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);

# Initialize components for Routine "search_instr3"
search_instr3Clock = core.Clock()
text_13 = visual.TextStim(win=win, name='text_13',
    text="Now we will practice this task by itself. Each screen will only appear for 2 seconds so try to search for the target (square open at the left or right) and respond as quickly and accurately as possible.\n\nRemember, press '1' for left or '0' for right.\n\nRest your fingers over these keys and press either to begin",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.6, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_15 = keyboard.Keyboard()

# Initialize components for Routine "search"
searchClock = core.Clock()
tars = ['l', 'r']
nontars = ['b', 't']

im_dir = "stimuli/search/"
sim1 = visual.ImageStim(
    win=win,
    name='sim1', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
sim2 = visual.ImageStim(
    win=win,
    name='sim2', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
sim3 = visual.ImageStim(
    win=win,
    name='sim3', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
sim4 = visual.ImageStim(
    win=win,
    name='sim4', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
sim5 = visual.ImageStim(
    win=win,
    name='sim5', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
sim6 = visual.ImageStim(
    win=win,
    name='sim6', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
sim7 = visual.ImageStim(
    win=win,
    name='sim7', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
sim8 = visual.ImageStim(
    win=win,
    name='sim8', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
search_resp = keyboard.Keyboard()
search_fix = visual.TextStim(win=win, name='search_fix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);

# Initialize components for Routine "search_isi"
search_isiClock = core.Clock()
text_9 = visual.TextStim(win=win, name='text_9',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "wm_instr3"
wm_instr3Clock = core.Clock()
text_14 = visual.TextStim(win=win, name='text_14',
    text='Well done!\n\nNow we will practice both tasks together. Remember, you will see 4 image-word pairs to remember. Then during the 2 second interval you will have to search for the target square and indicate if it is open on the left or right. After that you will be asked to type the word associated with each image you studied.\n\nThere will be 3 example sequences to practice the tasks together.\n\nPress SPACE to continue.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.6, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_16 = keyboard.Keyboard()

# Initialize components for Routine "ST"
STClock = core.Clock()
st_text = visual.TextStim(win=win, name='st_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.6, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
st_key = keyboard.Keyboard()

# Initialize components for Routine "wm_study"
wm_studyClock = core.Clock()
wm_study_im1 = visual.ImageStim(
    win=win,
    name='wm_study_im1', 
    image='sin', mask=None,
    ori=0, pos=(0, .204), size=(600/1920, 600/1080),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
wm_study_tx1 = visual.TextStim(win=win, name='wm_study_tx1',
    text='default text',
    font='Arial',
    pos=(0, -.204), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
wm_study_im2 = visual.ImageStim(
    win=win,
    name='wm_study_im2', 
    image='sin', mask=None,
    ori=0, pos=(0, .204), size=(600/1920, 600/1080),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
wm_study_tx2 = visual.TextStim(win=win, name='wm_study_tx2',
    text='default text',
    font='Arial',
    pos=(0, -.204), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
wm_study_im3 = visual.ImageStim(
    win=win,
    name='wm_study_im3', 
    image='sin', mask=None,
    ori=0, pos=(0, .204), size=(600/1920, 600/1080),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
wm_study_tx3 = visual.TextStim(win=win, name='wm_study_tx3',
    text='default text',
    font='Arial',
    pos=(0, -.204), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
wm_study_im4 = visual.ImageStim(
    win=win,
    name='wm_study_im4', 
    image='sin', mask=None,
    ori=0, pos=(0, .204), size=(600/1920, 600/1080),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
wm_study_tx4 = visual.TextStim(win=win, name='wm_study_tx4',
    text='default text',
    font='Arial',
    pos=(0, -.204), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);

# Initialize components for Routine "search"
searchClock = core.Clock()
tars = ['l', 'r']
nontars = ['b', 't']

im_dir = "stimuli/search/"
sim1 = visual.ImageStim(
    win=win,
    name='sim1', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
sim2 = visual.ImageStim(
    win=win,
    name='sim2', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
sim3 = visual.ImageStim(
    win=win,
    name='sim3', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
sim4 = visual.ImageStim(
    win=win,
    name='sim4', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
sim5 = visual.ImageStim(
    win=win,
    name='sim5', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
sim6 = visual.ImageStim(
    win=win,
    name='sim6', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
sim7 = visual.ImageStim(
    win=win,
    name='sim7', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
sim8 = visual.ImageStim(
    win=win,
    name='sim8', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
search_resp = keyboard.Keyboard()
search_fix = visual.TextStim(win=win, name='search_fix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);

# Initialize components for Routine "wm_test"
wm_testClock = core.Clock()
testImage = None
timer_wm = core.Clock()
wm_recall_text = visual.TextStim(win=win, name='wm_recall_text',
    text=None,
    font='Arial',
    pos=(0, -.204), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
wm_test_im = visual.ImageStim(
    win=win,
    name='wm_test_im', 
    image='sin', mask=None,
    ori=0, pos=(0, .204), size=(600/1920, 600/1080),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "wm_recall_isi"
wm_recall_isiClock = core.Clock()
wm_isi_blank = visual.TextStim(win=win, name='wm_isi_blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "write"
writeClock = core.Clock()
text_11 = visual.TextStim(win=win, name='text_11',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "search_reminder"
search_reminderClock = core.Clock()
text_16 = visual.TextStim(win=win, name='text_16',
    text="Remember to respond to the search task! \n\nPress '1' for left or '0' for right",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.6, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "end_wm_prac"
end_wm_pracClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='End of practice.\n\nPress SPACE to start the main task.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.6, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "ST"
STClock = core.Clock()
st_text = visual.TextStim(win=win, name='st_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.6, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
st_key = keyboard.Keyboard()

# Initialize components for Routine "wm_study"
wm_studyClock = core.Clock()
wm_study_im1 = visual.ImageStim(
    win=win,
    name='wm_study_im1', 
    image='sin', mask=None,
    ori=0, pos=(0, .204), size=(600/1920, 600/1080),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
wm_study_tx1 = visual.TextStim(win=win, name='wm_study_tx1',
    text='default text',
    font='Arial',
    pos=(0, -.204), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
wm_study_im2 = visual.ImageStim(
    win=win,
    name='wm_study_im2', 
    image='sin', mask=None,
    ori=0, pos=(0, .204), size=(600/1920, 600/1080),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
wm_study_tx2 = visual.TextStim(win=win, name='wm_study_tx2',
    text='default text',
    font='Arial',
    pos=(0, -.204), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
wm_study_im3 = visual.ImageStim(
    win=win,
    name='wm_study_im3', 
    image='sin', mask=None,
    ori=0, pos=(0, .204), size=(600/1920, 600/1080),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
wm_study_tx3 = visual.TextStim(win=win, name='wm_study_tx3',
    text='default text',
    font='Arial',
    pos=(0, -.204), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
wm_study_im4 = visual.ImageStim(
    win=win,
    name='wm_study_im4', 
    image='sin', mask=None,
    ori=0, pos=(0, .204), size=(600/1920, 600/1080),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
wm_study_tx4 = visual.TextStim(win=win, name='wm_study_tx4',
    text='default text',
    font='Arial',
    pos=(0, -.204), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);

# Initialize components for Routine "search"
searchClock = core.Clock()
tars = ['l', 'r']
nontars = ['b', 't']

im_dir = "stimuli/search/"
sim1 = visual.ImageStim(
    win=win,
    name='sim1', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
sim2 = visual.ImageStim(
    win=win,
    name='sim2', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
sim3 = visual.ImageStim(
    win=win,
    name='sim3', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
sim4 = visual.ImageStim(
    win=win,
    name='sim4', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
sim5 = visual.ImageStim(
    win=win,
    name='sim5', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
sim6 = visual.ImageStim(
    win=win,
    name='sim6', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
sim7 = visual.ImageStim(
    win=win,
    name='sim7', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
sim8 = visual.ImageStim(
    win=win,
    name='sim8', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
search_resp = keyboard.Keyboard()
search_fix = visual.TextStim(win=win, name='search_fix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);

# Initialize components for Routine "wm_test"
wm_testClock = core.Clock()
testImage = None
timer_wm = core.Clock()
wm_recall_text = visual.TextStim(win=win, name='wm_recall_text',
    text=None,
    font='Arial',
    pos=(0, -.204), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
wm_test_im = visual.ImageStim(
    win=win,
    name='wm_test_im', 
    image='sin', mask=None,
    ori=0, pos=(0, .204), size=(600/1920, 600/1080),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "wm_recall_isi"
wm_recall_isiClock = core.Clock()
wm_isi_blank = visual.TextStim(win=win, name='wm_isi_blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "write"
writeClock = core.Clock()
text_11 = visual.TextStim(win=win, name='text_11',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "search_reminder"
search_reminderClock = core.Clock()
text_16 = visual.TextStim(win=win, name='text_16',
    text="Remember to respond to the search task! \n\nPress '1' for left or '0' for right",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.6, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "end_exp"
end_expClock = core.Clock()
end_exp_text = visual.TextStim(win=win, name='end_exp_text',
    text="That's the end of the experiment!\n\nThank you for taking part.\n\nPlease wait a moment for the data to be saved...",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "consent"-------
continueRoutine = True
# update component parameters for each repeat
consent_key.keys = []
consent_key.rt = []
_consent_key_allKeys = []
# keep track of which components have finished
consentComponents = [consent_text, consent_key]
for thisComponent in consentComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
consentClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "consent"-------
while continueRoutine:
    # get current time
    t = consentClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=consentClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *consent_text* updates
    if consent_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        consent_text.frameNStart = frameN  # exact frame index
        consent_text.tStart = t  # local t and not account for scr refresh
        consent_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(consent_text, 'tStartRefresh')  # time at next scr refresh
        consent_text.setAutoDraw(True)
    
    # *consent_key* updates
    waitOnFlip = False
    if consent_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        consent_key.frameNStart = frameN  # exact frame index
        consent_key.tStart = t  # local t and not account for scr refresh
        consent_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(consent_key, 'tStartRefresh')  # time at next scr refresh
        consent_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(consent_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(consent_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if consent_key.status == STARTED and not waitOnFlip:
        theseKeys = consent_key.getKeys(keyList=['y'], waitRelease=False)
        _consent_key_allKeys.extend(theseKeys)
        if len(_consent_key_allKeys):
            consent_key.keys = _consent_key_allKeys[-1].name  # just the last key pressed
            consent_key.rt = _consent_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in consentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "consent"-------
for thisComponent in consentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('consent_text.started', consent_text.tStartRefresh)
thisExp.addData('consent_text.stopped', consent_text.tStopRefresh)
# check responses
if consent_key.keys in ['', [], None]:  # No response was made
    consent_key.keys = None
thisExp.addData('consent_key.keys',consent_key.keys)
if consent_key.keys != None:  # we had a response
    thisExp.addData('consent_key.rt', consent_key.rt)
thisExp.addData('consent_key.started', consent_key.tStartRefresh)
thisExp.addData('consent_key.stopped', consent_key.tStopRefresh)
thisExp.nextEntry()
# the Routine "consent" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "welcome"-------
continueRoutine = True
# update component parameters for each repeat
welcome_adv.keys = []
welcome_adv.rt = []
_welcome_adv_allKeys = []
# keep track of which components have finished
welcomeComponents = [welcome_text, welcome_adv]
for thisComponent in welcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcome"-------
while continueRoutine:
    # get current time
    t = welcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome_text* updates
    if welcome_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_text.frameNStart = frameN  # exact frame index
        welcome_text.tStart = t  # local t and not account for scr refresh
        welcome_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_text, 'tStartRefresh')  # time at next scr refresh
        welcome_text.setAutoDraw(True)
    
    # *welcome_adv* updates
    waitOnFlip = False
    if welcome_adv.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_adv.frameNStart = frameN  # exact frame index
        welcome_adv.tStart = t  # local t and not account for scr refresh
        welcome_adv.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_adv, 'tStartRefresh')  # time at next scr refresh
        welcome_adv.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(welcome_adv.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(welcome_adv.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if welcome_adv.status == STARTED and not waitOnFlip:
        theseKeys = welcome_adv.getKeys(keyList=['space'], waitRelease=False)
        _welcome_adv_allKeys.extend(theseKeys)
        if len(_welcome_adv_allKeys):
            welcome_adv.keys = _welcome_adv_allKeys[-1].name  # just the last key pressed
            welcome_adv.rt = _welcome_adv_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome"-------
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('welcome_text.started', welcome_text.tStartRefresh)
thisExp.addData('welcome_text.stopped', welcome_text.tStopRefresh)
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learn_instr1"-------
continueRoutine = True
# update component parameters for each repeat
learn_instr_adv.keys = []
learn_instr_adv.rt = []
_learn_instr_adv_allKeys = []
# keep track of which components have finished
learn_instr1Components = [part1, learn_intsr_text, learn_instr_adv, ex_word, ex_im]
for thisComponent in learn_instr1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learn_instr1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learn_instr1"-------
while continueRoutine:
    # get current time
    t = learn_instr1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learn_instr1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *part1* updates
    if part1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        part1.frameNStart = frameN  # exact frame index
        part1.tStart = t  # local t and not account for scr refresh
        part1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(part1, 'tStartRefresh')  # time at next scr refresh
        part1.setAutoDraw(True)
    if part1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > part1.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            part1.tStop = t  # not accounting for scr refresh
            part1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(part1, 'tStopRefresh')  # time at next scr refresh
            part1.setAutoDraw(False)
    
    # *learn_intsr_text* updates
    if learn_intsr_text.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        learn_intsr_text.frameNStart = frameN  # exact frame index
        learn_intsr_text.tStart = t  # local t and not account for scr refresh
        learn_intsr_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(learn_intsr_text, 'tStartRefresh')  # time at next scr refresh
        learn_intsr_text.setAutoDraw(True)
    
    # *learn_instr_adv* updates
    waitOnFlip = False
    if learn_instr_adv.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        learn_instr_adv.frameNStart = frameN  # exact frame index
        learn_instr_adv.tStart = t  # local t and not account for scr refresh
        learn_instr_adv.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(learn_instr_adv, 'tStartRefresh')  # time at next scr refresh
        learn_instr_adv.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(learn_instr_adv.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(learn_instr_adv.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if learn_instr_adv.status == STARTED and not waitOnFlip:
        theseKeys = learn_instr_adv.getKeys(keyList=['space'], waitRelease=False)
        _learn_instr_adv_allKeys.extend(theseKeys)
        if len(_learn_instr_adv_allKeys):
            learn_instr_adv.keys = _learn_instr_adv_allKeys[-1].name  # just the last key pressed
            learn_instr_adv.rt = _learn_instr_adv_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *ex_word* updates
    if ex_word.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        ex_word.frameNStart = frameN  # exact frame index
        ex_word.tStart = t  # local t and not account for scr refresh
        ex_word.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ex_word, 'tStartRefresh')  # time at next scr refresh
        ex_word.setAutoDraw(True)
    
    # *ex_im* updates
    if ex_im.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        ex_im.frameNStart = frameN  # exact frame index
        ex_im.tStart = t  # local t and not account for scr refresh
        ex_im.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ex_im, 'tStartRefresh')  # time at next scr refresh
        ex_im.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learn_instr1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learn_instr1"-------
for thisComponent in learn_instr1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('part1.started', part1.tStartRefresh)
thisExp.addData('part1.stopped', part1.tStopRefresh)
thisExp.addData('learn_intsr_text.started', learn_intsr_text.tStartRefresh)
thisExp.addData('learn_intsr_text.stopped', learn_intsr_text.tStopRefresh)
thisExp.addData('ex_word.started', ex_word.tStartRefresh)
thisExp.addData('ex_word.stopped', ex_word.tStopRefresh)
thisExp.addData('ex_im.started', ex_im.tStartRefresh)
thisExp.addData('ex_im.stopped', ex_im.tStopRefresh)
# the Routine "learn_instr1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learn_instr2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
learn_instr2Components = [text, key_resp]
for thisComponent in learn_instr2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learn_instr2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learn_instr2"-------
while continueRoutine:
    # get current time
    t = learn_instr2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learn_instr2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learn_instr2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learn_instr2"-------
for thisComponent in learn_instr2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# the Routine "learn_instr2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learn_instr3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
learn_instr3Components = [text_2, key_resp_2]
for thisComponent in learn_instr3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learn_instr3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learn_instr3"-------
while continueRoutine:
    # get current time
    t = learn_instr3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learn_instr3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learn_instr3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learn_instr3"-------
for thisComponent in learn_instr3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# the Routine "learn_instr3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learn_instr4"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
prac=1
# keep track of which components have finished
learn_instr4Components = [text_3, key_resp_3]
for thisComponent in learn_instr4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learn_instr4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learn_instr4"-------
while continueRoutine:
    # get current time
    t = learn_instr4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learn_instr4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learn_instr4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learn_instr4"-------
for thisComponent in learn_instr4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
# the Routine "learn_instr4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
example_recall = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuli/example.csv'),
    seed=None, name='example_recall')
thisExp.addLoop(example_recall)  # add the loop to the experiment
thisExample_recall = example_recall.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisExample_recall.rgb)
if thisExample_recall != None:
    for paramName in thisExample_recall:
        exec('{} = thisExample_recall[paramName]'.format(paramName))

for thisExample_recall in example_recall:
    currentLoop = example_recall
    # abbreviate parameter names if possible (e.g. rgb = thisExample_recall.rgb)
    if thisExample_recall != None:
        for paramName in thisExample_recall:
            exec('{} = thisExample_recall[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "learn_test"-------
    continueRoutine = True
    # update component parameters for each repeat
    validkeys = [char for char in 'abcdefghijklmnopqrstuvwxyz']
    event.clearEvents('keyboard')
    recall_text.text = ''
    recall_started = False
    
    timer.reset()
    test_image.setImage(file)
    recall_text.setText('')
    # keep track of which components have finished
    learn_testComponents = [test_image, recall_text]
    for thisComponent in learn_testComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    learn_testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "learn_test"-------
    while continueRoutine:
        # get current time
        t = learn_testClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=learn_testClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if prac != 1:
            if list_no != expInfo["list"] or not continue_learning:
                continueRoutine = False
        
        if skip_learn==1:
            continueRoutine = False
        if not recall_started:
            recall_text.text = '?'
        
        keys = event.getKeys()
        if len(keys):
            key = keys[0]
            if key in validkeys:
                recall_started = True
                if recall_text.text == '?':
                    recall_text.text = ''
                recall_text.text = recall_text.text + key.upper()
            elif key == 'return':
                continueRoutine = False
            elif key == 'backspace':
                recall_text.text = recall_text.text[:-1]
        
        if timer.getTime() > 15:
            continueRoutine = False
        
        # *test_image* updates
        if test_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test_image.frameNStart = frameN  # exact frame index
            test_image.tStart = t  # local t and not account for scr refresh
            test_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test_image, 'tStartRefresh')  # time at next scr refresh
            test_image.setAutoDraw(True)
        
        # *recall_text* updates
        if recall_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            recall_text.frameNStart = frameN  # exact frame index
            recall_text.tStart = t  # local t and not account for scr refresh
            recall_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recall_text, 'tStartRefresh')  # time at next scr refresh
            recall_text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learn_testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "learn_test"-------
    for thisComponent in learn_testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData("recalled", recall_text.text)
    thisExp.addData("recalled_rt", timer.getTime())
    example_recall.addData('test_image.started', test_image.tStartRefresh)
    example_recall.addData('test_image.stopped', test_image.tStopRefresh)
    example_recall.addData('recall_text.started', recall_text.tStartRefresh)
    example_recall.addData('recall_text.stopped', recall_text.tStopRefresh)
    # the Routine "learn_test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "learn_feedback"-------
    continueRoutine = True
    # update component parameters for each repeat
    
    if recall_text.text == word:
        accuracy = 1
        feedback_col = "lightgreen"
        feedback_dur = 0
    else:
        accuracy = 0
        feedback_col = "red"
        feedback_dur = 4
    feedback_text.setColor(feedback_col, colorSpace='rgb')
    feedback_text.setText(recall_text.text)
    feed_image.setImage(file)
    restudy_text.setText(word)
    # keep track of which components have finished
    learn_feedbackComponents = [feedback_text, feed_image, post_fb_int, restudy_text]
    for thisComponent in learn_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    learn_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "learn_feedback"-------
    while continueRoutine:
        # get current time
        t = learn_feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=learn_feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if prac != 1:
            if list_no != expInfo["list"] or not continue_learning:
                continueRoutine = False
        
        if skip_learn==1:
            continueRoutine = False
        
        # *feedback_text* updates
        if feedback_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            feedback_text.frameNStart = frameN  # exact frame index
            feedback_text.tStart = t  # local t and not account for scr refresh
            feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
            feedback_text.setAutoDraw(True)
        if feedback_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_text.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                feedback_text.tStop = t  # not accounting for scr refresh
                feedback_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback_text, 'tStopRefresh')  # time at next scr refresh
                feedback_text.setAutoDraw(False)
        
        # *feed_image* updates
        if feed_image.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            feed_image.frameNStart = frameN  # exact frame index
            feed_image.tStart = t  # local t and not account for scr refresh
            feed_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feed_image, 'tStartRefresh')  # time at next scr refresh
            feed_image.setAutoDraw(True)
        if feed_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feed_image.tStartRefresh + feedback_dur + 1-frameTolerance:
                # keep track of stop time/frame for later
                feed_image.tStop = t  # not accounting for scr refresh
                feed_image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feed_image, 'tStopRefresh')  # time at next scr refresh
                feed_image.setAutoDraw(False)
        
        # *post_fb_int* updates
        if post_fb_int.status == NOT_STARTED and tThisFlip >= feedback_dur + 1-frameTolerance:
            # keep track of start time/frame for later
            post_fb_int.frameNStart = frameN  # exact frame index
            post_fb_int.tStart = t  # local t and not account for scr refresh
            post_fb_int.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(post_fb_int, 'tStartRefresh')  # time at next scr refresh
            post_fb_int.setAutoDraw(True)
        if post_fb_int.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > post_fb_int.tStartRefresh + .2-frameTolerance:
                # keep track of stop time/frame for later
                post_fb_int.tStop = t  # not accounting for scr refresh
                post_fb_int.frameNStop = frameN  # exact frame index
                win.timeOnFlip(post_fb_int, 'tStopRefresh')  # time at next scr refresh
                post_fb_int.setAutoDraw(False)
        
        # *restudy_text* updates
        if restudy_text.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            restudy_text.frameNStart = frameN  # exact frame index
            restudy_text.tStart = t  # local t and not account for scr refresh
            restudy_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(restudy_text, 'tStartRefresh')  # time at next scr refresh
            restudy_text.setAutoDraw(True)
        if restudy_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > restudy_text.tStartRefresh + feedback_dur-frameTolerance:
                # keep track of stop time/frame for later
                restudy_text.tStop = t  # not accounting for scr refresh
                restudy_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(restudy_text, 'tStopRefresh')  # time at next scr refresh
                restudy_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learn_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "learn_feedback"-------
    for thisComponent in learn_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData("recall_acc", accuracy)
    
    if prac == 0:
        learn_n_correct += accuracy
    
        if list_no == expInfo["list"]:
            learn_n_done += 1
    example_recall.addData('feedback_text.started', feedback_text.tStartRefresh)
    example_recall.addData('feedback_text.stopped', feedback_text.tStopRefresh)
    example_recall.addData('feed_image.started', feed_image.tStartRefresh)
    example_recall.addData('feed_image.stopped', feed_image.tStopRefresh)
    example_recall.addData('post_fb_int.started', post_fb_int.tStartRefresh)
    example_recall.addData('post_fb_int.stopped', post_fb_int.tStopRefresh)
    example_recall.addData('restudy_text.started', restudy_text.tStartRefresh)
    example_recall.addData('restudy_text.stopped', restudy_text.tStopRefresh)
    # the Routine "learn_feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'example_recall'


# ------Prepare to start Routine "learn_instr5"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
prac=1
# keep track of which components have finished
learn_instr5Components = [text_4, key_resp_4]
for thisComponent in learn_instr5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learn_instr5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learn_instr5"-------
while continueRoutine:
    # get current time
    t = learn_instr5Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learn_instr5Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learn_instr5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learn_instr5"-------
for thisComponent in learn_instr5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)
# the Routine "learn_instr5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
prac_learn_study_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuli/prac-learn-lists.csv'),
    seed=None, name='prac_learn_study_loop')
thisExp.addLoop(prac_learn_study_loop)  # add the loop to the experiment
thisPrac_learn_study_loop = prac_learn_study_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPrac_learn_study_loop.rgb)
if thisPrac_learn_study_loop != None:
    for paramName in thisPrac_learn_study_loop:
        exec('{} = thisPrac_learn_study_loop[paramName]'.format(paramName))

for thisPrac_learn_study_loop in prac_learn_study_loop:
    currentLoop = prac_learn_study_loop
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_learn_study_loop.rgb)
    if thisPrac_learn_study_loop != None:
        for paramName in thisPrac_learn_study_loop:
            exec('{} = thisPrac_learn_study_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "learn_study"-------
    continueRoutine = True
    routineTimer.add(4.500000)
    # update component parameters for each repeat
    study_text.setText(word)
    study_image.setImage(file)
    # keep track of which components have finished
    learn_studyComponents = [study_text, study_image]
    for thisComponent in learn_studyComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    learn_studyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "learn_study"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = learn_studyClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=learn_studyClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if prac != 1:
            if list_no != expInfo["list"] or not continue_learning:
                continueRoutine = False
        
        if skip_learn==1:
            continueRoutine = False
        
        # *study_text* updates
        if study_text.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            study_text.frameNStart = frameN  # exact frame index
            study_text.tStart = t  # local t and not account for scr refresh
            study_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(study_text, 'tStartRefresh')  # time at next scr refresh
            study_text.setAutoDraw(True)
        if study_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > study_text.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                study_text.tStop = t  # not accounting for scr refresh
                study_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(study_text, 'tStopRefresh')  # time at next scr refresh
                study_text.setAutoDraw(False)
        
        # *study_image* updates
        if study_image.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            study_image.frameNStart = frameN  # exact frame index
            study_image.tStart = t  # local t and not account for scr refresh
            study_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(study_image, 'tStartRefresh')  # time at next scr refresh
            study_image.setAutoDraw(True)
        if study_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > study_image.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                study_image.tStop = t  # not accounting for scr refresh
                study_image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(study_image, 'tStopRefresh')  # time at next scr refresh
                study_image.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learn_studyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "learn_study"-------
    for thisComponent in learn_studyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    prac_learn_study_loop.addData('study_text.started', study_text.tStartRefresh)
    prac_learn_study_loop.addData('study_text.stopped', study_text.tStopRefresh)
    prac_learn_study_loop.addData('study_image.started', study_image.tStartRefresh)
    prac_learn_study_loop.addData('study_image.stopped', study_image.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'prac_learn_study_loop'


# ------Prepare to start Routine "learn_test_instr"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
learn_test_instr_text.setText("We'll now test your memory...")
# keep track of which components have finished
learn_test_instrComponents = [learn_test_instr_text]
for thisComponent in learn_test_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learn_test_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learn_test_instr"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = learn_test_instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learn_test_instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    if skip_learn==1 or not continue_learning:
        continueRoutine = False
    
    
    
    # *learn_test_instr_text* updates
    if learn_test_instr_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        learn_test_instr_text.frameNStart = frameN  # exact frame index
        learn_test_instr_text.tStart = t  # local t and not account for scr refresh
        learn_test_instr_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(learn_test_instr_text, 'tStartRefresh')  # time at next scr refresh
        learn_test_instr_text.setAutoDraw(True)
    if learn_test_instr_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > learn_test_instr_text.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            learn_test_instr_text.tStop = t  # not accounting for scr refresh
            learn_test_instr_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(learn_test_instr_text, 'tStopRefresh')  # time at next scr refresh
            learn_test_instr_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learn_test_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learn_test_instr"-------
for thisComponent in learn_test_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('learn_test_instr_text.started', learn_test_instr_text.tStartRefresh)
thisExp.addData('learn_test_instr_text.stopped', learn_test_instr_text.tStopRefresh)

# set up handler to look after randomisation of conditions etc
prac_learn_test_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuli/prac-learn-lists.csv'),
    seed=None, name='prac_learn_test_loop')
thisExp.addLoop(prac_learn_test_loop)  # add the loop to the experiment
thisPrac_learn_test_loop = prac_learn_test_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPrac_learn_test_loop.rgb)
if thisPrac_learn_test_loop != None:
    for paramName in thisPrac_learn_test_loop:
        exec('{} = thisPrac_learn_test_loop[paramName]'.format(paramName))

for thisPrac_learn_test_loop in prac_learn_test_loop:
    currentLoop = prac_learn_test_loop
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_learn_test_loop.rgb)
    if thisPrac_learn_test_loop != None:
        for paramName in thisPrac_learn_test_loop:
            exec('{} = thisPrac_learn_test_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "learn_test"-------
    continueRoutine = True
    # update component parameters for each repeat
    validkeys = [char for char in 'abcdefghijklmnopqrstuvwxyz']
    event.clearEvents('keyboard')
    recall_text.text = ''
    recall_started = False
    
    timer.reset()
    test_image.setImage(file)
    recall_text.setText('')
    # keep track of which components have finished
    learn_testComponents = [test_image, recall_text]
    for thisComponent in learn_testComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    learn_testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "learn_test"-------
    while continueRoutine:
        # get current time
        t = learn_testClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=learn_testClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if prac != 1:
            if list_no != expInfo["list"] or not continue_learning:
                continueRoutine = False
        
        if skip_learn==1:
            continueRoutine = False
        if not recall_started:
            recall_text.text = '?'
        
        keys = event.getKeys()
        if len(keys):
            key = keys[0]
            if key in validkeys:
                recall_started = True
                if recall_text.text == '?':
                    recall_text.text = ''
                recall_text.text = recall_text.text + key.upper()
            elif key == 'return':
                continueRoutine = False
            elif key == 'backspace':
                recall_text.text = recall_text.text[:-1]
        
        if timer.getTime() > 15:
            continueRoutine = False
        
        # *test_image* updates
        if test_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test_image.frameNStart = frameN  # exact frame index
            test_image.tStart = t  # local t and not account for scr refresh
            test_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test_image, 'tStartRefresh')  # time at next scr refresh
            test_image.setAutoDraw(True)
        
        # *recall_text* updates
        if recall_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            recall_text.frameNStart = frameN  # exact frame index
            recall_text.tStart = t  # local t and not account for scr refresh
            recall_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recall_text, 'tStartRefresh')  # time at next scr refresh
            recall_text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learn_testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "learn_test"-------
    for thisComponent in learn_testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData("recalled", recall_text.text)
    thisExp.addData("recalled_rt", timer.getTime())
    prac_learn_test_loop.addData('test_image.started', test_image.tStartRefresh)
    prac_learn_test_loop.addData('test_image.stopped', test_image.tStopRefresh)
    prac_learn_test_loop.addData('recall_text.started', recall_text.tStartRefresh)
    prac_learn_test_loop.addData('recall_text.stopped', recall_text.tStopRefresh)
    # the Routine "learn_test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "learn_feedback"-------
    continueRoutine = True
    # update component parameters for each repeat
    
    if recall_text.text == word:
        accuracy = 1
        feedback_col = "lightgreen"
        feedback_dur = 0
    else:
        accuracy = 0
        feedback_col = "red"
        feedback_dur = 4
    feedback_text.setColor(feedback_col, colorSpace='rgb')
    feedback_text.setText(recall_text.text)
    feed_image.setImage(file)
    restudy_text.setText(word)
    # keep track of which components have finished
    learn_feedbackComponents = [feedback_text, feed_image, post_fb_int, restudy_text]
    for thisComponent in learn_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    learn_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "learn_feedback"-------
    while continueRoutine:
        # get current time
        t = learn_feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=learn_feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if prac != 1:
            if list_no != expInfo["list"] or not continue_learning:
                continueRoutine = False
        
        if skip_learn==1:
            continueRoutine = False
        
        # *feedback_text* updates
        if feedback_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            feedback_text.frameNStart = frameN  # exact frame index
            feedback_text.tStart = t  # local t and not account for scr refresh
            feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
            feedback_text.setAutoDraw(True)
        if feedback_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_text.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                feedback_text.tStop = t  # not accounting for scr refresh
                feedback_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback_text, 'tStopRefresh')  # time at next scr refresh
                feedback_text.setAutoDraw(False)
        
        # *feed_image* updates
        if feed_image.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            feed_image.frameNStart = frameN  # exact frame index
            feed_image.tStart = t  # local t and not account for scr refresh
            feed_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feed_image, 'tStartRefresh')  # time at next scr refresh
            feed_image.setAutoDraw(True)
        if feed_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feed_image.tStartRefresh + feedback_dur + 1-frameTolerance:
                # keep track of stop time/frame for later
                feed_image.tStop = t  # not accounting for scr refresh
                feed_image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feed_image, 'tStopRefresh')  # time at next scr refresh
                feed_image.setAutoDraw(False)
        
        # *post_fb_int* updates
        if post_fb_int.status == NOT_STARTED and tThisFlip >= feedback_dur + 1-frameTolerance:
            # keep track of start time/frame for later
            post_fb_int.frameNStart = frameN  # exact frame index
            post_fb_int.tStart = t  # local t and not account for scr refresh
            post_fb_int.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(post_fb_int, 'tStartRefresh')  # time at next scr refresh
            post_fb_int.setAutoDraw(True)
        if post_fb_int.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > post_fb_int.tStartRefresh + .2-frameTolerance:
                # keep track of stop time/frame for later
                post_fb_int.tStop = t  # not accounting for scr refresh
                post_fb_int.frameNStop = frameN  # exact frame index
                win.timeOnFlip(post_fb_int, 'tStopRefresh')  # time at next scr refresh
                post_fb_int.setAutoDraw(False)
        
        # *restudy_text* updates
        if restudy_text.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            restudy_text.frameNStart = frameN  # exact frame index
            restudy_text.tStart = t  # local t and not account for scr refresh
            restudy_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(restudy_text, 'tStartRefresh')  # time at next scr refresh
            restudy_text.setAutoDraw(True)
        if restudy_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > restudy_text.tStartRefresh + feedback_dur-frameTolerance:
                # keep track of stop time/frame for later
                restudy_text.tStop = t  # not accounting for scr refresh
                restudy_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(restudy_text, 'tStopRefresh')  # time at next scr refresh
                restudy_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learn_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "learn_feedback"-------
    for thisComponent in learn_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData("recall_acc", accuracy)
    
    if prac == 0:
        learn_n_correct += accuracy
    
        if list_no == expInfo["list"]:
            learn_n_done += 1
    prac_learn_test_loop.addData('feedback_text.started', feedback_text.tStartRefresh)
    prac_learn_test_loop.addData('feedback_text.stopped', feedback_text.tStopRefresh)
    prac_learn_test_loop.addData('feed_image.started', feed_image.tStartRefresh)
    prac_learn_test_loop.addData('feed_image.stopped', feed_image.tStopRefresh)
    prac_learn_test_loop.addData('post_fb_int.started', post_fb_int.tStartRefresh)
    prac_learn_test_loop.addData('post_fb_int.stopped', post_fb_int.tStopRefresh)
    prac_learn_test_loop.addData('restudy_text.started', restudy_text.tStartRefresh)
    prac_learn_test_loop.addData('restudy_text.stopped', restudy_text.tStopRefresh)
    # the Routine "learn_feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'prac_learn_test_loop'


# ------Prepare to start Routine "learn_end_prac"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
prac=0
continue_learning=True
learn_blocks_done = 0
# keep track of which components have finished
learn_end_pracComponents = [text_5, key_resp_6]
for thisComponent in learn_end_pracComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learn_end_pracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learn_end_prac"-------
while continueRoutine:
    # get current time
    t = learn_end_pracClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learn_end_pracClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learn_end_pracComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learn_end_prac"-------
for thisComponent in learn_end_pracComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)
# the Routine "learn_end_prac" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
learn_blocks_loop = data.TrialHandler(nReps=3, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='learn_blocks_loop')
thisExp.addLoop(learn_blocks_loop)  # add the loop to the experiment
thisLearn_blocks_loop = learn_blocks_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLearn_blocks_loop.rgb)
if thisLearn_blocks_loop != None:
    for paramName in thisLearn_blocks_loop:
        exec('{} = thisLearn_blocks_loop[paramName]'.format(paramName))

for thisLearn_blocks_loop in learn_blocks_loop:
    currentLoop = learn_blocks_loop
    # abbreviate parameter names if possible (e.g. rgb = thisLearn_blocks_loop.rgb)
    if thisLearn_blocks_loop != None:
        for paramName in thisLearn_blocks_loop:
            exec('{} = thisLearn_blocks_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "set_counter"-------
    continueRoutine = True
    # update component parameters for each repeat
    
    learn_n_correct = 0
    learn_n_done = 0
    
    learn_blocks_done += 1
    # keep track of which components have finished
    set_counterComponents = []
    for thisComponent in set_counterComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    set_counterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "set_counter"-------
    while continueRoutine:
        # get current time
        t = set_counterClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=set_counterClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if skip_learn==1 or not continue_learning:
            continueRoutine = False
        
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in set_counterComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "set_counter"-------
    for thisComponent in set_counterComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "set_counter" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    learn_blocks = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('stimuli/learn-loop.csv'),
        seed=None, name='learn_blocks')
    thisExp.addLoop(learn_blocks)  # add the loop to the experiment
    thisLearn_block = learn_blocks.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLearn_block.rgb)
    if thisLearn_block != None:
        for paramName in thisLearn_block:
            exec('{} = thisLearn_block[paramName]'.format(paramName))
    
    for thisLearn_block in learn_blocks:
        currentLoop = learn_blocks
        # abbreviate parameter names if possible (e.g. rgb = thisLearn_block.rgb)
        if thisLearn_block != None:
            for paramName in thisLearn_block:
                exec('{} = thisLearn_block[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "begin_block"-------
        continueRoutine = True
        # update component parameters for each repeat
        text_10.setText('Press SPACE to see the next set of 10 pairs')
        key_resp_12.keys = []
        key_resp_12.rt = []
        _key_resp_12_allKeys = []
        # keep track of which components have finished
        begin_blockComponents = [text_10, key_resp_12]
        for thisComponent in begin_blockComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        begin_blockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "begin_block"-------
        while continueRoutine:
            # get current time
            t = begin_blockClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=begin_blockClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if skip_learn==1 or not continue_learning:
                continueRoutine = False
            
            
            
            # *text_10* updates
            if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_10.frameNStart = frameN  # exact frame index
                text_10.tStart = t  # local t and not account for scr refresh
                text_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
                text_10.setAutoDraw(True)
            
            # *key_resp_12* updates
            waitOnFlip = False
            if key_resp_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_12.frameNStart = frameN  # exact frame index
                key_resp_12.tStart = t  # local t and not account for scr refresh
                key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
                key_resp_12.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_12.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_12.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_12_allKeys.extend(theseKeys)
                if len(_key_resp_12_allKeys):
                    key_resp_12.keys = _key_resp_12_allKeys[-1].name  # just the last key pressed
                    key_resp_12.rt = _key_resp_12_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in begin_blockComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "begin_block"-------
        for thisComponent in begin_blockComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        learn_blocks.addData('text_10.started', text_10.tStartRefresh)
        learn_blocks.addData('text_10.stopped', text_10.tStopRefresh)
        # the Routine "begin_block" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        learn_study_loop = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(block_csv),
            seed=None, name='learn_study_loop')
        thisExp.addLoop(learn_study_loop)  # add the loop to the experiment
        thisLearn_study_loop = learn_study_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLearn_study_loop.rgb)
        if thisLearn_study_loop != None:
            for paramName in thisLearn_study_loop:
                exec('{} = thisLearn_study_loop[paramName]'.format(paramName))
        
        for thisLearn_study_loop in learn_study_loop:
            currentLoop = learn_study_loop
            # abbreviate parameter names if possible (e.g. rgb = thisLearn_study_loop.rgb)
            if thisLearn_study_loop != None:
                for paramName in thisLearn_study_loop:
                    exec('{} = thisLearn_study_loop[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "learn_study"-------
            continueRoutine = True
            routineTimer.add(4.500000)
            # update component parameters for each repeat
            study_text.setText(word)
            study_image.setImage(file)
            # keep track of which components have finished
            learn_studyComponents = [study_text, study_image]
            for thisComponent in learn_studyComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            learn_studyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "learn_study"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = learn_studyClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=learn_studyClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                if prac != 1:
                    if list_no != expInfo["list"] or not continue_learning:
                        continueRoutine = False
                
                if skip_learn==1:
                    continueRoutine = False
                
                # *study_text* updates
                if study_text.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    study_text.frameNStart = frameN  # exact frame index
                    study_text.tStart = t  # local t and not account for scr refresh
                    study_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(study_text, 'tStartRefresh')  # time at next scr refresh
                    study_text.setAutoDraw(True)
                if study_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > study_text.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        study_text.tStop = t  # not accounting for scr refresh
                        study_text.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(study_text, 'tStopRefresh')  # time at next scr refresh
                        study_text.setAutoDraw(False)
                
                # *study_image* updates
                if study_image.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    study_image.frameNStart = frameN  # exact frame index
                    study_image.tStart = t  # local t and not account for scr refresh
                    study_image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(study_image, 'tStartRefresh')  # time at next scr refresh
                    study_image.setAutoDraw(True)
                if study_image.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > study_image.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        study_image.tStop = t  # not accounting for scr refresh
                        study_image.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(study_image, 'tStopRefresh')  # time at next scr refresh
                        study_image.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in learn_studyComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "learn_study"-------
            for thisComponent in learn_studyComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            learn_study_loop.addData('study_text.started', study_text.tStartRefresh)
            learn_study_loop.addData('study_text.stopped', study_text.tStopRefresh)
            learn_study_loop.addData('study_image.started', study_image.tStartRefresh)
            learn_study_loop.addData('study_image.stopped', study_image.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 1 repeats of 'learn_study_loop'
        
        
        # ------Prepare to start Routine "learn_test_instr"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        learn_test_instr_text.setText("We'll now test your memory...")
        # keep track of which components have finished
        learn_test_instrComponents = [learn_test_instr_text]
        for thisComponent in learn_test_instrComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        learn_test_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "learn_test_instr"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = learn_test_instrClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=learn_test_instrClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if skip_learn==1 or not continue_learning:
                continueRoutine = False
            
            
            
            # *learn_test_instr_text* updates
            if learn_test_instr_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                learn_test_instr_text.frameNStart = frameN  # exact frame index
                learn_test_instr_text.tStart = t  # local t and not account for scr refresh
                learn_test_instr_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(learn_test_instr_text, 'tStartRefresh')  # time at next scr refresh
                learn_test_instr_text.setAutoDraw(True)
            if learn_test_instr_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > learn_test_instr_text.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    learn_test_instr_text.tStop = t  # not accounting for scr refresh
                    learn_test_instr_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(learn_test_instr_text, 'tStopRefresh')  # time at next scr refresh
                    learn_test_instr_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in learn_test_instrComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "learn_test_instr"-------
        for thisComponent in learn_test_instrComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        learn_blocks.addData('learn_test_instr_text.started', learn_test_instr_text.tStartRefresh)
        learn_blocks.addData('learn_test_instr_text.stopped', learn_test_instr_text.tStopRefresh)
        
        # set up handler to look after randomisation of conditions etc
        learn_test_loop = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(block_csv),
            seed=None, name='learn_test_loop')
        thisExp.addLoop(learn_test_loop)  # add the loop to the experiment
        thisLearn_test_loop = learn_test_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLearn_test_loop.rgb)
        if thisLearn_test_loop != None:
            for paramName in thisLearn_test_loop:
                exec('{} = thisLearn_test_loop[paramName]'.format(paramName))
        
        for thisLearn_test_loop in learn_test_loop:
            currentLoop = learn_test_loop
            # abbreviate parameter names if possible (e.g. rgb = thisLearn_test_loop.rgb)
            if thisLearn_test_loop != None:
                for paramName in thisLearn_test_loop:
                    exec('{} = thisLearn_test_loop[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "learn_test"-------
            continueRoutine = True
            # update component parameters for each repeat
            validkeys = [char for char in 'abcdefghijklmnopqrstuvwxyz']
            event.clearEvents('keyboard')
            recall_text.text = ''
            recall_started = False
            
            timer.reset()
            test_image.setImage(file)
            recall_text.setText('')
            # keep track of which components have finished
            learn_testComponents = [test_image, recall_text]
            for thisComponent in learn_testComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            learn_testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "learn_test"-------
            while continueRoutine:
                # get current time
                t = learn_testClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=learn_testClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                if prac != 1:
                    if list_no != expInfo["list"] or not continue_learning:
                        continueRoutine = False
                
                if skip_learn==1:
                    continueRoutine = False
                if not recall_started:
                    recall_text.text = '?'
                
                keys = event.getKeys()
                if len(keys):
                    key = keys[0]
                    if key in validkeys:
                        recall_started = True
                        if recall_text.text == '?':
                            recall_text.text = ''
                        recall_text.text = recall_text.text + key.upper()
                    elif key == 'return':
                        continueRoutine = False
                    elif key == 'backspace':
                        recall_text.text = recall_text.text[:-1]
                
                if timer.getTime() > 15:
                    continueRoutine = False
                
                # *test_image* updates
                if test_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    test_image.frameNStart = frameN  # exact frame index
                    test_image.tStart = t  # local t and not account for scr refresh
                    test_image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(test_image, 'tStartRefresh')  # time at next scr refresh
                    test_image.setAutoDraw(True)
                
                # *recall_text* updates
                if recall_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    recall_text.frameNStart = frameN  # exact frame index
                    recall_text.tStart = t  # local t and not account for scr refresh
                    recall_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(recall_text, 'tStartRefresh')  # time at next scr refresh
                    recall_text.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in learn_testComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "learn_test"-------
            for thisComponent in learn_testComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData("recalled", recall_text.text)
            thisExp.addData("recalled_rt", timer.getTime())
            learn_test_loop.addData('test_image.started', test_image.tStartRefresh)
            learn_test_loop.addData('test_image.stopped', test_image.tStopRefresh)
            learn_test_loop.addData('recall_text.started', recall_text.tStartRefresh)
            learn_test_loop.addData('recall_text.stopped', recall_text.tStopRefresh)
            # the Routine "learn_test" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "learn_feedback"-------
            continueRoutine = True
            # update component parameters for each repeat
            
            if recall_text.text == word:
                accuracy = 1
                feedback_col = "lightgreen"
                feedback_dur = 0
            else:
                accuracy = 0
                feedback_col = "red"
                feedback_dur = 4
            feedback_text.setColor(feedback_col, colorSpace='rgb')
            feedback_text.setText(recall_text.text)
            feed_image.setImage(file)
            restudy_text.setText(word)
            # keep track of which components have finished
            learn_feedbackComponents = [feedback_text, feed_image, post_fb_int, restudy_text]
            for thisComponent in learn_feedbackComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            learn_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "learn_feedback"-------
            while continueRoutine:
                # get current time
                t = learn_feedbackClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=learn_feedbackClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                if prac != 1:
                    if list_no != expInfo["list"] or not continue_learning:
                        continueRoutine = False
                
                if skip_learn==1:
                    continueRoutine = False
                
                # *feedback_text* updates
                if feedback_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    feedback_text.frameNStart = frameN  # exact frame index
                    feedback_text.tStart = t  # local t and not account for scr refresh
                    feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
                    feedback_text.setAutoDraw(True)
                if feedback_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > feedback_text.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        feedback_text.tStop = t  # not accounting for scr refresh
                        feedback_text.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(feedback_text, 'tStopRefresh')  # time at next scr refresh
                        feedback_text.setAutoDraw(False)
                
                # *feed_image* updates
                if feed_image.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    feed_image.frameNStart = frameN  # exact frame index
                    feed_image.tStart = t  # local t and not account for scr refresh
                    feed_image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(feed_image, 'tStartRefresh')  # time at next scr refresh
                    feed_image.setAutoDraw(True)
                if feed_image.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > feed_image.tStartRefresh + feedback_dur + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        feed_image.tStop = t  # not accounting for scr refresh
                        feed_image.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(feed_image, 'tStopRefresh')  # time at next scr refresh
                        feed_image.setAutoDraw(False)
                
                # *post_fb_int* updates
                if post_fb_int.status == NOT_STARTED and tThisFlip >= feedback_dur + 1-frameTolerance:
                    # keep track of start time/frame for later
                    post_fb_int.frameNStart = frameN  # exact frame index
                    post_fb_int.tStart = t  # local t and not account for scr refresh
                    post_fb_int.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(post_fb_int, 'tStartRefresh')  # time at next scr refresh
                    post_fb_int.setAutoDraw(True)
                if post_fb_int.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > post_fb_int.tStartRefresh + .2-frameTolerance:
                        # keep track of stop time/frame for later
                        post_fb_int.tStop = t  # not accounting for scr refresh
                        post_fb_int.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(post_fb_int, 'tStopRefresh')  # time at next scr refresh
                        post_fb_int.setAutoDraw(False)
                
                # *restudy_text* updates
                if restudy_text.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    restudy_text.frameNStart = frameN  # exact frame index
                    restudy_text.tStart = t  # local t and not account for scr refresh
                    restudy_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(restudy_text, 'tStartRefresh')  # time at next scr refresh
                    restudy_text.setAutoDraw(True)
                if restudy_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > restudy_text.tStartRefresh + feedback_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        restudy_text.tStop = t  # not accounting for scr refresh
                        restudy_text.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(restudy_text, 'tStopRefresh')  # time at next scr refresh
                        restudy_text.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in learn_feedbackComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "learn_feedback"-------
            for thisComponent in learn_feedbackComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData("recall_acc", accuracy)
            
            if prac == 0:
                learn_n_correct += accuracy
            
                if list_no == expInfo["list"]:
                    learn_n_done += 1
            learn_test_loop.addData('feedback_text.started', feedback_text.tStartRefresh)
            learn_test_loop.addData('feedback_text.stopped', feedback_text.tStopRefresh)
            learn_test_loop.addData('feed_image.started', feed_image.tStartRefresh)
            learn_test_loop.addData('feed_image.stopped', feed_image.tStopRefresh)
            learn_test_loop.addData('post_fb_int.started', post_fb_int.tStartRefresh)
            learn_test_loop.addData('post_fb_int.stopped', post_fb_int.tStopRefresh)
            learn_test_loop.addData('restudy_text.started', restudy_text.tStartRefresh)
            learn_test_loop.addData('restudy_text.stopped', restudy_text.tStopRefresh)
            # the Routine "learn_feedback" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'learn_test_loop'
        
        thisExp.nextEntry()
        
    # completed 1 repeats of 'learn_blocks'
    
    
    # ------Prepare to start Routine "next_instr"-------
    continueRoutine = True
    # update component parameters for each repeat
    
    perccor = int((learn_n_correct/learn_n_done)*100)
    
    if learn_n_correct/learn_n_done >= .8 or learn_blocks_done == 3:
        next_instr = "Well done! You got {}% of the pairs correct. We will now move on to the next part of the experiment.\n\nPress SPACE to continue.".format(perccor)
    else:
        next_instr = "Well done! You got {}% of the pairs correct. We will loop through all of the pairs again in groups of 10.\n\nPress SPACE to continue.".format(perccor)
    next_instr_text.setText(next_instr)
    key_resp_13.keys = []
    key_resp_13.rt = []
    _key_resp_13_allKeys = []
    # keep track of which components have finished
    next_instrComponents = [next_instr_text, key_resp_13]
    for thisComponent in next_instrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    next_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "next_instr"-------
    while continueRoutine:
        # get current time
        t = next_instrClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=next_instrClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *next_instr_text* updates
        if next_instr_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            next_instr_text.frameNStart = frameN  # exact frame index
            next_instr_text.tStart = t  # local t and not account for scr refresh
            next_instr_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(next_instr_text, 'tStartRefresh')  # time at next scr refresh
            next_instr_text.setAutoDraw(True)
        
        # *key_resp_13* updates
        waitOnFlip = False
        if key_resp_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_13.frameNStart = frameN  # exact frame index
            key_resp_13.tStart = t  # local t and not account for scr refresh
            key_resp_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_13, 'tStartRefresh')  # time at next scr refresh
            key_resp_13.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_13.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_13.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_13.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_13_allKeys.extend(theseKeys)
            if len(_key_resp_13_allKeys):
                key_resp_13.keys = _key_resp_13_allKeys[-1].name  # just the last key pressed
                key_resp_13.rt = _key_resp_13_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in next_instrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "next_instr"-------
    for thisComponent in next_instrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    learn_blocks_loop.addData('next_instr_text.started', next_instr_text.tStartRefresh)
    learn_blocks_loop.addData('next_instr_text.stopped', next_instr_text.tStopRefresh)
    # check responses
    if key_resp_13.keys in ['', [], None]:  # No response was made
        key_resp_13.keys = None
    learn_blocks_loop.addData('key_resp_13.keys',key_resp_13.keys)
    if key_resp_13.keys != None:  # we had a response
        learn_blocks_loop.addData('key_resp_13.rt', key_resp_13.rt)
    learn_blocks_loop.addData('key_resp_13.started', key_resp_13.tStartRefresh)
    learn_blocks_loop.addData('key_resp_13.stopped', key_resp_13.tStopRefresh)
    # the Routine "next_instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "break_learn"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    break_learnComponents = []
    for thisComponent in break_learnComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    break_learnClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "break_learn"-------
    while continueRoutine:
        # get current time
        t = break_learnClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=break_learnClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        print(learn_n_correct)
        print(learn_n_done)
        print(learn_n_correct/learn_n_done)
        
        if learn_n_correct/learn_n_done >= .8:
            learn_blocks_loop.finished = True
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in break_learnComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "break_learn"-------
    for thisComponent in break_learnComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "break_learn" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 3 repeats of 'learn_blocks_loop'


# ------Prepare to start Routine "learn_final_instr"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# reset this to run final test
continue_learning = True
# keep track of which components have finished
learn_final_instrComponents = [learn_final_text, key_resp_7]
for thisComponent in learn_final_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learn_final_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learn_final_instr"-------
while continueRoutine:
    # get current time
    t = learn_final_instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learn_final_instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *learn_final_text* updates
    if learn_final_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        learn_final_text.frameNStart = frameN  # exact frame index
        learn_final_text.tStart = t  # local t and not account for scr refresh
        learn_final_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(learn_final_text, 'tStartRefresh')  # time at next scr refresh
        learn_final_text.setAutoDraw(True)
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_7_allKeys.extend(theseKeys)
        if len(_key_resp_7_allKeys):
            key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
            key_resp_7.rt = _key_resp_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learn_final_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learn_final_instr"-------
for thisComponent in learn_final_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('learn_final_text.started', learn_final_text.tStartRefresh)
thisExp.addData('learn_final_text.stopped', learn_final_text.tStopRefresh)
# the Routine "learn_final_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
final_learn_test = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuli/learn-lists.csv'),
    seed=None, name='final_learn_test')
thisExp.addLoop(final_learn_test)  # add the loop to the experiment
thisFinal_learn_test = final_learn_test.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFinal_learn_test.rgb)
if thisFinal_learn_test != None:
    for paramName in thisFinal_learn_test:
        exec('{} = thisFinal_learn_test[paramName]'.format(paramName))

for thisFinal_learn_test in final_learn_test:
    currentLoop = final_learn_test
    # abbreviate parameter names if possible (e.g. rgb = thisFinal_learn_test.rgb)
    if thisFinal_learn_test != None:
        for paramName in thisFinal_learn_test:
            exec('{} = thisFinal_learn_test[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "learn_test"-------
    continueRoutine = True
    # update component parameters for each repeat
    validkeys = [char for char in 'abcdefghijklmnopqrstuvwxyz']
    event.clearEvents('keyboard')
    recall_text.text = ''
    recall_started = False
    
    timer.reset()
    test_image.setImage(file)
    recall_text.setText('')
    # keep track of which components have finished
    learn_testComponents = [test_image, recall_text]
    for thisComponent in learn_testComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    learn_testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "learn_test"-------
    while continueRoutine:
        # get current time
        t = learn_testClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=learn_testClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if prac != 1:
            if list_no != expInfo["list"] or not continue_learning:
                continueRoutine = False
        
        if skip_learn==1:
            continueRoutine = False
        if not recall_started:
            recall_text.text = '?'
        
        keys = event.getKeys()
        if len(keys):
            key = keys[0]
            if key in validkeys:
                recall_started = True
                if recall_text.text == '?':
                    recall_text.text = ''
                recall_text.text = recall_text.text + key.upper()
            elif key == 'return':
                continueRoutine = False
            elif key == 'backspace':
                recall_text.text = recall_text.text[:-1]
        
        if timer.getTime() > 15:
            continueRoutine = False
        
        # *test_image* updates
        if test_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test_image.frameNStart = frameN  # exact frame index
            test_image.tStart = t  # local t and not account for scr refresh
            test_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test_image, 'tStartRefresh')  # time at next scr refresh
            test_image.setAutoDraw(True)
        
        # *recall_text* updates
        if recall_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            recall_text.frameNStart = frameN  # exact frame index
            recall_text.tStart = t  # local t and not account for scr refresh
            recall_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recall_text, 'tStartRefresh')  # time at next scr refresh
            recall_text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learn_testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "learn_test"-------
    for thisComponent in learn_testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData("recalled", recall_text.text)
    thisExp.addData("recalled_rt", timer.getTime())
    final_learn_test.addData('test_image.started', test_image.tStartRefresh)
    final_learn_test.addData('test_image.stopped', test_image.tStopRefresh)
    final_learn_test.addData('recall_text.started', recall_text.tStartRefresh)
    final_learn_test.addData('recall_text.stopped', recall_text.tStopRefresh)
    # the Routine "learn_test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "learn_feedback"-------
    continueRoutine = True
    # update component parameters for each repeat
    
    if recall_text.text == word:
        accuracy = 1
        feedback_col = "lightgreen"
        feedback_dur = 0
    else:
        accuracy = 0
        feedback_col = "red"
        feedback_dur = 4
    feedback_text.setColor(feedback_col, colorSpace='rgb')
    feedback_text.setText(recall_text.text)
    feed_image.setImage(file)
    restudy_text.setText(word)
    # keep track of which components have finished
    learn_feedbackComponents = [feedback_text, feed_image, post_fb_int, restudy_text]
    for thisComponent in learn_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    learn_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "learn_feedback"-------
    while continueRoutine:
        # get current time
        t = learn_feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=learn_feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if prac != 1:
            if list_no != expInfo["list"] or not continue_learning:
                continueRoutine = False
        
        if skip_learn==1:
            continueRoutine = False
        
        # *feedback_text* updates
        if feedback_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            feedback_text.frameNStart = frameN  # exact frame index
            feedback_text.tStart = t  # local t and not account for scr refresh
            feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
            feedback_text.setAutoDraw(True)
        if feedback_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_text.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                feedback_text.tStop = t  # not accounting for scr refresh
                feedback_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback_text, 'tStopRefresh')  # time at next scr refresh
                feedback_text.setAutoDraw(False)
        
        # *feed_image* updates
        if feed_image.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            feed_image.frameNStart = frameN  # exact frame index
            feed_image.tStart = t  # local t and not account for scr refresh
            feed_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feed_image, 'tStartRefresh')  # time at next scr refresh
            feed_image.setAutoDraw(True)
        if feed_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feed_image.tStartRefresh + feedback_dur + 1-frameTolerance:
                # keep track of stop time/frame for later
                feed_image.tStop = t  # not accounting for scr refresh
                feed_image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feed_image, 'tStopRefresh')  # time at next scr refresh
                feed_image.setAutoDraw(False)
        
        # *post_fb_int* updates
        if post_fb_int.status == NOT_STARTED and tThisFlip >= feedback_dur + 1-frameTolerance:
            # keep track of start time/frame for later
            post_fb_int.frameNStart = frameN  # exact frame index
            post_fb_int.tStart = t  # local t and not account for scr refresh
            post_fb_int.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(post_fb_int, 'tStartRefresh')  # time at next scr refresh
            post_fb_int.setAutoDraw(True)
        if post_fb_int.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > post_fb_int.tStartRefresh + .2-frameTolerance:
                # keep track of stop time/frame for later
                post_fb_int.tStop = t  # not accounting for scr refresh
                post_fb_int.frameNStop = frameN  # exact frame index
                win.timeOnFlip(post_fb_int, 'tStopRefresh')  # time at next scr refresh
                post_fb_int.setAutoDraw(False)
        
        # *restudy_text* updates
        if restudy_text.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            restudy_text.frameNStart = frameN  # exact frame index
            restudy_text.tStart = t  # local t and not account for scr refresh
            restudy_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(restudy_text, 'tStartRefresh')  # time at next scr refresh
            restudy_text.setAutoDraw(True)
        if restudy_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > restudy_text.tStartRefresh + feedback_dur-frameTolerance:
                # keep track of stop time/frame for later
                restudy_text.tStop = t  # not accounting for scr refresh
                restudy_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(restudy_text, 'tStopRefresh')  # time at next scr refresh
                restudy_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learn_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "learn_feedback"-------
    for thisComponent in learn_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData("recall_acc", accuracy)
    
    if prac == 0:
        learn_n_correct += accuracy
    
        if list_no == expInfo["list"]:
            learn_n_done += 1
    final_learn_test.addData('feedback_text.started', feedback_text.tStartRefresh)
    final_learn_test.addData('feedback_text.stopped', feedback_text.tStopRefresh)
    final_learn_test.addData('feed_image.started', feed_image.tStartRefresh)
    final_learn_test.addData('feed_image.stopped', feed_image.tStopRefresh)
    final_learn_test.addData('post_fb_int.started', post_fb_int.tStartRefresh)
    final_learn_test.addData('post_fb_int.stopped', post_fb_int.tStopRefresh)
    final_learn_test.addData('restudy_text.started', restudy_text.tStartRefresh)
    final_learn_test.addData('restudy_text.stopped', restudy_text.tStopRefresh)
    # the Routine "learn_feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'final_learn_test'


# ------Prepare to start Routine "end_learn"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_10.keys = []
key_resp_10.rt = []
_key_resp_10_allKeys = []
# keep track of which components have finished
end_learnComponents = [text_8, key_resp_10]
for thisComponent in end_learnComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
end_learnClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end_learn"-------
while continueRoutine:
    # get current time
    t = end_learnClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=end_learnClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_8* updates
    if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_8.frameNStart = frameN  # exact frame index
        text_8.tStart = t  # local t and not account for scr refresh
        text_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        text_8.setAutoDraw(True)
    
    # *key_resp_10* updates
    waitOnFlip = False
    if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.tStart = t  # local t and not account for scr refresh
        key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_10.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_10.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_10_allKeys.extend(theseKeys)
        if len(_key_resp_10_allKeys):
            key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
            key_resp_10.rt = _key_resp_10_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_learnComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end_learn"-------
for thisComponent in end_learnComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_8.started', text_8.tStartRefresh)
thisExp.addData('text_8.stopped', text_8.tStopRefresh)
# the Routine "end_learn" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "wm_instr"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
wm_instrComponents = [part2, wm_text, key_resp_5]
for thisComponent in wm_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
wm_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "wm_instr"-------
while continueRoutine:
    # get current time
    t = wm_instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=wm_instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *part2* updates
    if part2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        part2.frameNStart = frameN  # exact frame index
        part2.tStart = t  # local t and not account for scr refresh
        part2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(part2, 'tStartRefresh')  # time at next scr refresh
        part2.setAutoDraw(True)
    if part2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > part2.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            part2.tStop = t  # not accounting for scr refresh
            part2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(part2, 'tStopRefresh')  # time at next scr refresh
            part2.setAutoDraw(False)
    
    # *wm_text* updates
    if wm_text.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        wm_text.frameNStart = frameN  # exact frame index
        wm_text.tStart = t  # local t and not account for scr refresh
        wm_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wm_text, 'tStartRefresh')  # time at next scr refresh
        wm_text.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wm_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "wm_instr"-------
for thisComponent in wm_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('part2.started', part2.tStartRefresh)
thisExp.addData('part2.stopped', part2.tStopRefresh)
thisExp.addData('wm_text.started', wm_text.tStartRefresh)
thisExp.addData('wm_text.stopped', wm_text.tStopRefresh)
# the Routine "wm_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "wm_instr2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
wm_instr2Components = [text_6, key_resp_8]
for thisComponent in wm_instr2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
wm_instr2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "wm_instr2"-------
while continueRoutine:
    # get current time
    t = wm_instr2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=wm_instr2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wm_instr2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "wm_instr2"-------
for thisComponent in wm_instr2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
# the Routine "wm_instr2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "search_instr"-------
continueRoutine = True
# update component parameters for each repeat
t_im.setSize(im_size)
b_im.setSize(im_size)
l_im.setSize(im_size)
r_im.setSize(im_size)
key_resp_11.keys = []
key_resp_11.rt = []
_key_resp_11_allKeys = []
# keep track of which components have finished
search_instrComponents = [top_text, mid_text, bottom_text, t_im, b_im, l_im, r_im, key_resp_11]
for thisComponent in search_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
search_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "search_instr"-------
while continueRoutine:
    # get current time
    t = search_instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=search_instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *top_text* updates
    if top_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        top_text.frameNStart = frameN  # exact frame index
        top_text.tStart = t  # local t and not account for scr refresh
        top_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(top_text, 'tStartRefresh')  # time at next scr refresh
        top_text.setAutoDraw(True)
    
    # *mid_text* updates
    if mid_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mid_text.frameNStart = frameN  # exact frame index
        mid_text.tStart = t  # local t and not account for scr refresh
        mid_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mid_text, 'tStartRefresh')  # time at next scr refresh
        mid_text.setAutoDraw(True)
    
    # *bottom_text* updates
    if bottom_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        bottom_text.frameNStart = frameN  # exact frame index
        bottom_text.tStart = t  # local t and not account for scr refresh
        bottom_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bottom_text, 'tStartRefresh')  # time at next scr refresh
        bottom_text.setAutoDraw(True)
    
    # *t_im* updates
    if t_im.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        t_im.frameNStart = frameN  # exact frame index
        t_im.tStart = t  # local t and not account for scr refresh
        t_im.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(t_im, 'tStartRefresh')  # time at next scr refresh
        t_im.setAutoDraw(True)
    
    # *b_im* updates
    if b_im.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        b_im.frameNStart = frameN  # exact frame index
        b_im.tStart = t  # local t and not account for scr refresh
        b_im.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(b_im, 'tStartRefresh')  # time at next scr refresh
        b_im.setAutoDraw(True)
    
    # *l_im* updates
    if l_im.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        l_im.frameNStart = frameN  # exact frame index
        l_im.tStart = t  # local t and not account for scr refresh
        l_im.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(l_im, 'tStartRefresh')  # time at next scr refresh
        l_im.setAutoDraw(True)
    
    # *r_im* updates
    if r_im.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        r_im.frameNStart = frameN  # exact frame index
        r_im.tStart = t  # local t and not account for scr refresh
        r_im.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(r_im, 'tStartRefresh')  # time at next scr refresh
        r_im.setAutoDraw(True)
    
    # *key_resp_11* updates
    waitOnFlip = False
    if key_resp_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_11.frameNStart = frameN  # exact frame index
        key_resp_11.tStart = t  # local t and not account for scr refresh
        key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
        key_resp_11.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_11.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_11.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_11_allKeys.extend(theseKeys)
        if len(_key_resp_11_allKeys):
            key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
            key_resp_11.rt = _key_resp_11_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in search_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "search_instr"-------
for thisComponent in search_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('top_text.started', top_text.tStartRefresh)
thisExp.addData('top_text.stopped', top_text.tStopRefresh)
thisExp.addData('mid_text.started', mid_text.tStartRefresh)
thisExp.addData('mid_text.stopped', mid_text.tStopRefresh)
thisExp.addData('bottom_text.started', bottom_text.tStartRefresh)
thisExp.addData('bottom_text.stopped', bottom_text.tStopRefresh)
thisExp.addData('t_im.started', t_im.tStartRefresh)
thisExp.addData('t_im.stopped', t_im.tStopRefresh)
thisExp.addData('b_im.started', b_im.tStartRefresh)
thisExp.addData('b_im.stopped', b_im.tStopRefresh)
thisExp.addData('l_im.started', l_im.tStartRefresh)
thisExp.addData('l_im.stopped', l_im.tStopRefresh)
thisExp.addData('r_im.started', r_im.tStartRefresh)
thisExp.addData('r_im.stopped', r_im.tStopRefresh)
# the Routine "search_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "search_instr2"-------
continueRoutine = True
# update component parameters for each repeat
from random import random

s1posex = [-xpos-xdisp, ypos + ((random() - .5)*ydisp)]
s2posex = [-xpos+xdisp, ypos + ((random() - .5)*ydisp)]

s3posex = [xpos-xdisp, ypos + ((random() - .5)*ydisp)]
s4posex = [xpos+xdisp, ypos + ((random() - .5)*ydisp)]

s5posex = [xpos-xdisp, -ypos + ((random() - .5)*ydisp)]
s6posex = [xpos+xdisp, -ypos + ((random() - .5)*ydisp)]

s7posex = [-xpos-xdisp, -ypos + ((random() - .5)*ydisp)]
s8posex = [-xpos+xdisp, -ypos + ((random() - .5)*ydisp)]
sim1_ex.setPos(s1posex)
sim1_ex.setSize(im_size)
sim2_ex.setPos(s2posex)
sim2_ex.setSize(im_size)
sim3_ex.setPos(s3posex)
sim3_ex.setSize(im_size)
sim4_ex.setPos(s4posex)
sim4_ex.setSize(im_size)
sim5_ex.setPos(s5posex)
sim5_ex.setSize(im_size)
sim6_ex.setPos(s6posex)
sim6_ex.setSize(im_size)
sim7_ex.setPos(s7posex)
sim7_ex.setSize(im_size)
sim8_ex.setPos(s8posex)
sim8_ex.setSize(im_size)
key_resp_14.keys = []
key_resp_14.rt = []
_key_resp_14_allKeys = []
# keep track of which components have finished
search_instr2Components = [sim1_ex, sim2_ex, sim3_ex, sim4_ex, sim5_ex, sim6_ex, sim7_ex, sim8_ex, text_12, key_resp_14, text_15]
for thisComponent in search_instr2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
search_instr2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "search_instr2"-------
while continueRoutine:
    # get current time
    t = search_instr2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=search_instr2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *sim1_ex* updates
    if sim1_ex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sim1_ex.frameNStart = frameN  # exact frame index
        sim1_ex.tStart = t  # local t and not account for scr refresh
        sim1_ex.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sim1_ex, 'tStartRefresh')  # time at next scr refresh
        sim1_ex.setAutoDraw(True)
    
    # *sim2_ex* updates
    if sim2_ex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sim2_ex.frameNStart = frameN  # exact frame index
        sim2_ex.tStart = t  # local t and not account for scr refresh
        sim2_ex.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sim2_ex, 'tStartRefresh')  # time at next scr refresh
        sim2_ex.setAutoDraw(True)
    
    # *sim3_ex* updates
    if sim3_ex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sim3_ex.frameNStart = frameN  # exact frame index
        sim3_ex.tStart = t  # local t and not account for scr refresh
        sim3_ex.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sim3_ex, 'tStartRefresh')  # time at next scr refresh
        sim3_ex.setAutoDraw(True)
    
    # *sim4_ex* updates
    if sim4_ex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sim4_ex.frameNStart = frameN  # exact frame index
        sim4_ex.tStart = t  # local t and not account for scr refresh
        sim4_ex.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sim4_ex, 'tStartRefresh')  # time at next scr refresh
        sim4_ex.setAutoDraw(True)
    
    # *sim5_ex* updates
    if sim5_ex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sim5_ex.frameNStart = frameN  # exact frame index
        sim5_ex.tStart = t  # local t and not account for scr refresh
        sim5_ex.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sim5_ex, 'tStartRefresh')  # time at next scr refresh
        sim5_ex.setAutoDraw(True)
    
    # *sim6_ex* updates
    if sim6_ex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sim6_ex.frameNStart = frameN  # exact frame index
        sim6_ex.tStart = t  # local t and not account for scr refresh
        sim6_ex.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sim6_ex, 'tStartRefresh')  # time at next scr refresh
        sim6_ex.setAutoDraw(True)
    
    # *sim7_ex* updates
    if sim7_ex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sim7_ex.frameNStart = frameN  # exact frame index
        sim7_ex.tStart = t  # local t and not account for scr refresh
        sim7_ex.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sim7_ex, 'tStartRefresh')  # time at next scr refresh
        sim7_ex.setAutoDraw(True)
    
    # *sim8_ex* updates
    if sim8_ex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sim8_ex.frameNStart = frameN  # exact frame index
        sim8_ex.tStart = t  # local t and not account for scr refresh
        sim8_ex.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sim8_ex, 'tStartRefresh')  # time at next scr refresh
        sim8_ex.setAutoDraw(True)
    
    # *text_12* updates
    if text_12.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
        # keep track of start time/frame for later
        text_12.frameNStart = frameN  # exact frame index
        text_12.tStart = t  # local t and not account for scr refresh
        text_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
        text_12.setAutoDraw(True)
    
    # *key_resp_14* updates
    waitOnFlip = False
    if key_resp_14.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
        # keep track of start time/frame for later
        key_resp_14.frameNStart = frameN  # exact frame index
        key_resp_14.tStart = t  # local t and not account for scr refresh
        key_resp_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_14, 'tStartRefresh')  # time at next scr refresh
        key_resp_14.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_14.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_14.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_14.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_14_allKeys.extend(theseKeys)
        if len(_key_resp_14_allKeys):
            key_resp_14.keys = _key_resp_14_allKeys[-1].name  # just the last key pressed
            key_resp_14.rt = _key_resp_14_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_15* updates
    if text_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_15.frameNStart = frameN  # exact frame index
        text_15.tStart = t  # local t and not account for scr refresh
        text_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_15, 'tStartRefresh')  # time at next scr refresh
        text_15.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in search_instr2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "search_instr2"-------
for thisComponent in search_instr2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('sim1_ex.started', sim1_ex.tStartRefresh)
thisExp.addData('sim1_ex.stopped', sim1_ex.tStopRefresh)
thisExp.addData('sim2_ex.started', sim2_ex.tStartRefresh)
thisExp.addData('sim2_ex.stopped', sim2_ex.tStopRefresh)
thisExp.addData('sim3_ex.started', sim3_ex.tStartRefresh)
thisExp.addData('sim3_ex.stopped', sim3_ex.tStopRefresh)
thisExp.addData('sim4_ex.started', sim4_ex.tStartRefresh)
thisExp.addData('sim4_ex.stopped', sim4_ex.tStopRefresh)
thisExp.addData('sim5_ex.started', sim5_ex.tStartRefresh)
thisExp.addData('sim5_ex.stopped', sim5_ex.tStopRefresh)
thisExp.addData('sim6_ex.started', sim6_ex.tStartRefresh)
thisExp.addData('sim6_ex.stopped', sim6_ex.tStopRefresh)
thisExp.addData('sim7_ex.started', sim7_ex.tStartRefresh)
thisExp.addData('sim7_ex.stopped', sim7_ex.tStopRefresh)
thisExp.addData('sim8_ex.started', sim8_ex.tStartRefresh)
thisExp.addData('sim8_ex.stopped', sim8_ex.tStopRefresh)
thisExp.addData('text_12.started', text_12.tStartRefresh)
thisExp.addData('text_12.stopped', text_12.tStopRefresh)
thisExp.addData('text_15.started', text_15.tStartRefresh)
thisExp.addData('text_15.stopped', text_15.tStopRefresh)
# the Routine "search_instr2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "search_instr3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_15.keys = []
key_resp_15.rt = []
_key_resp_15_allKeys = []
prac=1

# keep track of which components have finished
search_instr3Components = [text_13, key_resp_15]
for thisComponent in search_instr3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
search_instr3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "search_instr3"-------
while continueRoutine:
    # get current time
    t = search_instr3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=search_instr3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_13* updates
    if text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_13.frameNStart = frameN  # exact frame index
        text_13.tStart = t  # local t and not account for scr refresh
        text_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
        text_13.setAutoDraw(True)
    
    # *key_resp_15* updates
    waitOnFlip = False
    if key_resp_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_15.frameNStart = frameN  # exact frame index
        key_resp_15.tStart = t  # local t and not account for scr refresh
        key_resp_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_15, 'tStartRefresh')  # time at next scr refresh
        key_resp_15.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_15.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_15.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_15.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_15.getKeys(keyList=['1', '0'], waitRelease=False)
        _key_resp_15_allKeys.extend(theseKeys)
        if len(_key_resp_15_allKeys):
            key_resp_15.keys = _key_resp_15_allKeys[-1].name  # just the last key pressed
            key_resp_15.rt = _key_resp_15_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in search_instr3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "search_instr3"-------
for thisComponent in search_instr3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_13.started', text_13.tStartRefresh)
thisExp.addData('text_13.stopped', text_13.tStopRefresh)
# the Routine "search_instr3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
search_loop = data.TrialHandler(nReps=20, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='search_loop')
thisExp.addLoop(search_loop)  # add the loop to the experiment
thisSearch_loop = search_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSearch_loop.rgb)
if thisSearch_loop != None:
    for paramName in thisSearch_loop:
        exec('{} = thisSearch_loop[paramName]'.format(paramName))

for thisSearch_loop in search_loop:
    currentLoop = search_loop
    # abbreviate parameter names if possible (e.g. rgb = thisSearch_loop.rgb)
    if thisSearch_loop != None:
        for paramName in thisSearch_loop:
            exec('{} = thisSearch_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "search"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    
    from random import random, randint
    
    s1pos = [-xpos-xdisp, ypos + ((random() - .5)*ydisp)]
    s2pos = [-xpos+xdisp, ypos + ((random() - .5)*ydisp)]
    
    s3pos = [xpos-xdisp, ypos + ((random() - .5)*ydisp)]
    s4pos = [xpos+xdisp, ypos + ((random() - .5)*ydisp)]
    
    s5pos = [xpos-xdisp, -ypos + ((random() - .5)*ydisp)]
    s6pos = [xpos+xdisp, -ypos + ((random() - .5)*ydisp)]
    
    s7pos = [-xpos-xdisp, -ypos + ((random() - .5)*ydisp)]
    s8pos = [-xpos+xdisp, -ypos + ((random() - .5)*ydisp)]
    
    tari = randint(0, 3)
    tarright = random() > .5
    
    ims = []
    for i in [0,1,2,3]:
        if i == tari:
            opts = [tars[tarright], nontars[random() > .5]]
        else:
            opts = nontars[:]
        if random() > .5:
            ims.extend(opts)
        else:
            ims.extend([opts[1], opts[0]])
    
    s1 = im_dir + ims[0] + ".png"
    s2 = im_dir + ims[1] + ".png"
    
    s3 = im_dir + ims[2] + ".png"
    s4 = im_dir + ims[3] + ".png"
    
    s5 = im_dir + ims[4] + ".png"
    s6 = im_dir + ims[5] + ".png"
    
    s7 = im_dir + ims[6] + ".png"
    s8 = im_dir + ims[7] + ".png"
    
    thisExp.addData("s_im1", s1)
    thisExp.addData("s_im2", s2)
    thisExp.addData("s_im3", s3)
    thisExp.addData("s_im4", s4)
    thisExp.addData("s_im5", s5)
    thisExp.addData("s_im6", s6)
    thisExp.addData("s_im7", s7)
    thisExp.addData("s_im8", s8)
    
    thisExp.addData("s_im1pos", s1pos)
    thisExp.addData("s_im2pos", s2pos)
    thisExp.addData("s_im3pos", s3pos)
    thisExp.addData("s_im4pos", s4pos)
    thisExp.addData("s_im5pos", s5pos)
    thisExp.addData("s_im6pos", s6pos)
    thisExp.addData("s_im7pos", s7pos)
    thisExp.addData("s_im8pos", s8pos)
    
    thisExp.addData("s_tarright", tarright)
    sim1.setPos(s1pos)
    sim1.setSize(im_size)
    sim1.setImage(s1)
    sim2.setPos(s2pos)
    sim2.setSize(im_size)
    sim2.setImage(s2)
    sim3.setPos(s3pos)
    sim3.setSize(im_size)
    sim3.setImage(s3)
    sim4.setPos(s4pos)
    sim4.setSize(im_size)
    sim4.setImage(s4)
    sim5.setPos(s5pos)
    sim5.setSize(im_size)
    sim5.setImage(s5)
    sim6.setPos(s6pos)
    sim6.setSize(im_size)
    sim6.setImage(s6)
    sim7.setPos(s7pos)
    sim7.setSize(im_size)
    sim7.setImage(s7)
    sim8.setPos(s8pos)
    sim8.setSize(im_size)
    sim8.setImage(s8)
    search_resp.keys = []
    search_resp.rt = []
    _search_resp_allKeys = []
    # keep track of which components have finished
    searchComponents = [sim1, sim2, sim3, sim4, sim5, sim6, sim7, sim8, search_resp, search_fix]
    for thisComponent in searchComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    searchClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "search"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = searchClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=searchClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if prac != 1:
            if list_no != expInfo["list"]:
                continueRoutine = False
        
        # *sim1* updates
        if sim1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sim1.frameNStart = frameN  # exact frame index
            sim1.tStart = t  # local t and not account for scr refresh
            sim1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sim1, 'tStartRefresh')  # time at next scr refresh
            sim1.setAutoDraw(True)
        if sim1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sim1.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                sim1.tStop = t  # not accounting for scr refresh
                sim1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sim1, 'tStopRefresh')  # time at next scr refresh
                sim1.setAutoDraw(False)
        
        # *sim2* updates
        if sim2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sim2.frameNStart = frameN  # exact frame index
            sim2.tStart = t  # local t and not account for scr refresh
            sim2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sim2, 'tStartRefresh')  # time at next scr refresh
            sim2.setAutoDraw(True)
        if sim2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sim2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                sim2.tStop = t  # not accounting for scr refresh
                sim2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sim2, 'tStopRefresh')  # time at next scr refresh
                sim2.setAutoDraw(False)
        
        # *sim3* updates
        if sim3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sim3.frameNStart = frameN  # exact frame index
            sim3.tStart = t  # local t and not account for scr refresh
            sim3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sim3, 'tStartRefresh')  # time at next scr refresh
            sim3.setAutoDraw(True)
        if sim3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sim3.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                sim3.tStop = t  # not accounting for scr refresh
                sim3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sim3, 'tStopRefresh')  # time at next scr refresh
                sim3.setAutoDraw(False)
        
        # *sim4* updates
        if sim4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sim4.frameNStart = frameN  # exact frame index
            sim4.tStart = t  # local t and not account for scr refresh
            sim4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sim4, 'tStartRefresh')  # time at next scr refresh
            sim4.setAutoDraw(True)
        if sim4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sim4.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                sim4.tStop = t  # not accounting for scr refresh
                sim4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sim4, 'tStopRefresh')  # time at next scr refresh
                sim4.setAutoDraw(False)
        
        # *sim5* updates
        if sim5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sim5.frameNStart = frameN  # exact frame index
            sim5.tStart = t  # local t and not account for scr refresh
            sim5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sim5, 'tStartRefresh')  # time at next scr refresh
            sim5.setAutoDraw(True)
        if sim5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sim5.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                sim5.tStop = t  # not accounting for scr refresh
                sim5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sim5, 'tStopRefresh')  # time at next scr refresh
                sim5.setAutoDraw(False)
        
        # *sim6* updates
        if sim6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sim6.frameNStart = frameN  # exact frame index
            sim6.tStart = t  # local t and not account for scr refresh
            sim6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sim6, 'tStartRefresh')  # time at next scr refresh
            sim6.setAutoDraw(True)
        if sim6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sim6.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                sim6.tStop = t  # not accounting for scr refresh
                sim6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sim6, 'tStopRefresh')  # time at next scr refresh
                sim6.setAutoDraw(False)
        
        # *sim7* updates
        if sim7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sim7.frameNStart = frameN  # exact frame index
            sim7.tStart = t  # local t and not account for scr refresh
            sim7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sim7, 'tStartRefresh')  # time at next scr refresh
            sim7.setAutoDraw(True)
        if sim7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sim7.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                sim7.tStop = t  # not accounting for scr refresh
                sim7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sim7, 'tStopRefresh')  # time at next scr refresh
                sim7.setAutoDraw(False)
        
        # *sim8* updates
        if sim8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sim8.frameNStart = frameN  # exact frame index
            sim8.tStart = t  # local t and not account for scr refresh
            sim8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sim8, 'tStartRefresh')  # time at next scr refresh
            sim8.setAutoDraw(True)
        if sim8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sim8.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                sim8.tStop = t  # not accounting for scr refresh
                sim8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sim8, 'tStopRefresh')  # time at next scr refresh
                sim8.setAutoDraw(False)
        
        # *search_resp* updates
        waitOnFlip = False
        if search_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            search_resp.frameNStart = frameN  # exact frame index
            search_resp.tStart = t  # local t and not account for scr refresh
            search_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(search_resp, 'tStartRefresh')  # time at next scr refresh
            search_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(search_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(search_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if search_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > search_resp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                search_resp.tStop = t  # not accounting for scr refresh
                search_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(search_resp, 'tStopRefresh')  # time at next scr refresh
                search_resp.status = FINISHED
        if search_resp.status == STARTED and not waitOnFlip:
            theseKeys = search_resp.getKeys(keyList=['1', '0'], waitRelease=False)
            _search_resp_allKeys.extend(theseKeys)
            if len(_search_resp_allKeys):
                search_resp.keys = _search_resp_allKeys[-1].name  # just the last key pressed
                search_resp.rt = _search_resp_allKeys[-1].rt
        
        # *search_fix* updates
        if search_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            search_fix.frameNStart = frameN  # exact frame index
            search_fix.tStart = t  # local t and not account for scr refresh
            search_fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(search_fix, 'tStartRefresh')  # time at next scr refresh
            search_fix.setAutoDraw(True)
        if search_fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > search_fix.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                search_fix.tStop = t  # not accounting for scr refresh
                search_fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(search_fix, 'tStopRefresh')  # time at next scr refresh
                search_fix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in searchComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "search"-------
    for thisComponent in searchComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    search_loop.addData('sim1.started', sim1.tStartRefresh)
    search_loop.addData('sim1.stopped', sim1.tStopRefresh)
    search_loop.addData('sim2.started', sim2.tStartRefresh)
    search_loop.addData('sim2.stopped', sim2.tStopRefresh)
    search_loop.addData('sim3.started', sim3.tStartRefresh)
    search_loop.addData('sim3.stopped', sim3.tStopRefresh)
    search_loop.addData('sim4.started', sim4.tStartRefresh)
    search_loop.addData('sim4.stopped', sim4.tStopRefresh)
    search_loop.addData('sim5.started', sim5.tStartRefresh)
    search_loop.addData('sim5.stopped', sim5.tStopRefresh)
    search_loop.addData('sim6.started', sim6.tStartRefresh)
    search_loop.addData('sim6.stopped', sim6.tStopRefresh)
    search_loop.addData('sim7.started', sim7.tStartRefresh)
    search_loop.addData('sim7.stopped', sim7.tStopRefresh)
    search_loop.addData('sim8.started', sim8.tStartRefresh)
    search_loop.addData('sim8.stopped', sim8.tStopRefresh)
    # check responses
    if search_resp.keys in ['', [], None]:  # No response was made
        search_resp.keys = None
    search_loop.addData('search_resp.keys',search_resp.keys)
    if search_resp.keys != None:  # we had a response
        search_loop.addData('search_resp.rt', search_resp.rt)
    search_loop.addData('search_resp.started', search_resp.tStartRefresh)
    search_loop.addData('search_resp.stopped', search_resp.tStopRefresh)
    search_loop.addData('search_fix.started', search_fix.tStartRefresh)
    search_loop.addData('search_fix.stopped', search_fix.tStopRefresh)
    
    # ------Prepare to start Routine "search_isi"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    search_isiComponents = [text_9]
    for thisComponent in search_isiComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    search_isiClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "search_isi"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = search_isiClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=search_isiClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_9* updates
        if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_9.frameNStart = frameN  # exact frame index
            text_9.tStart = t  # local t and not account for scr refresh
            text_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
            text_9.setAutoDraw(True)
        if text_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_9.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_9.tStop = t  # not accounting for scr refresh
                text_9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_9, 'tStopRefresh')  # time at next scr refresh
                text_9.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in search_isiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "search_isi"-------
    for thisComponent in search_isiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    search_loop.addData('text_9.started', text_9.tStartRefresh)
    search_loop.addData('text_9.stopped', text_9.tStopRefresh)
    thisExp.nextEntry()
    
# completed 20 repeats of 'search_loop'


# ------Prepare to start Routine "wm_instr3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_16.keys = []
key_resp_16.rt = []
_key_resp_16_allKeys = []
prac=1
# keep track of which components have finished
wm_instr3Components = [text_14, key_resp_16]
for thisComponent in wm_instr3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
wm_instr3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "wm_instr3"-------
while continueRoutine:
    # get current time
    t = wm_instr3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=wm_instr3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_14* updates
    if text_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_14.frameNStart = frameN  # exact frame index
        text_14.tStart = t  # local t and not account for scr refresh
        text_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
        text_14.setAutoDraw(True)
    
    # *key_resp_16* updates
    waitOnFlip = False
    if key_resp_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_16.frameNStart = frameN  # exact frame index
        key_resp_16.tStart = t  # local t and not account for scr refresh
        key_resp_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_16, 'tStartRefresh')  # time at next scr refresh
        key_resp_16.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_16.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_16.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_16.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_16.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_16_allKeys.extend(theseKeys)
        if len(_key_resp_16_allKeys):
            key_resp_16.keys = _key_resp_16_allKeys[-1].name  # just the last key pressed
            key_resp_16.rt = _key_resp_16_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wm_instr3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "wm_instr3"-------
for thisComponent in wm_instr3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_14.started', text_14.tStartRefresh)
thisExp.addData('text_14.stopped', text_14.tStopRefresh)
# the Routine "wm_instr3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
prac_wm_trial_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuli/prac-wm-lists.csv'),
    seed=None, name='prac_wm_trial_loop')
thisExp.addLoop(prac_wm_trial_loop)  # add the loop to the experiment
thisPrac_wm_trial_loop = prac_wm_trial_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPrac_wm_trial_loop.rgb)
if thisPrac_wm_trial_loop != None:
    for paramName in thisPrac_wm_trial_loop:
        exec('{} = thisPrac_wm_trial_loop[paramName]'.format(paramName))

for thisPrac_wm_trial_loop in prac_wm_trial_loop:
    currentLoop = prac_wm_trial_loop
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_wm_trial_loop.rgb)
    if thisPrac_wm_trial_loop != None:
        for paramName in thisPrac_wm_trial_loop:
            exec('{} = thisPrac_wm_trial_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ST"-------
    continueRoutine = True
    # update component parameters for each repeat
    st_text.setText("Press '1' or '0' to start the next sequence...")
    st_key.keys = []
    st_key.rt = []
    _st_key_allKeys = []
    # keep track of which components have finished
    STComponents = [st_text, st_key]
    for thisComponent in STComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    STClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ST"-------
    while continueRoutine:
        # get current time
        t = STClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=STClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if prac != 1:
            if list_no != expInfo["list"]:
                continueRoutine = False
        
        # *st_text* updates
        if st_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            st_text.frameNStart = frameN  # exact frame index
            st_text.tStart = t  # local t and not account for scr refresh
            st_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(st_text, 'tStartRefresh')  # time at next scr refresh
            st_text.setAutoDraw(True)
        
        # *st_key* updates
        waitOnFlip = False
        if st_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            st_key.frameNStart = frameN  # exact frame index
            st_key.tStart = t  # local t and not account for scr refresh
            st_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(st_key, 'tStartRefresh')  # time at next scr refresh
            st_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(st_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(st_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if st_key.status == STARTED and not waitOnFlip:
            theseKeys = st_key.getKeys(keyList=['1', '0'], waitRelease=False)
            _st_key_allKeys.extend(theseKeys)
            if len(_st_key_allKeys):
                st_key.keys = _st_key_allKeys[-1].name  # just the last key pressed
                st_key.rt = _st_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in STComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ST"-------
    for thisComponent in STComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ST" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "wm_study"-------
    continueRoutine = True
    routineTimer.add(7.800000)
    # update component parameters for each repeat
    wm_study_im1.setImage(file1)
    wm_study_tx1.setText(word1)
    wm_study_im2.setImage(file2)
    wm_study_tx2.setText(word2)
    wm_study_im3.setImage(file3)
    wm_study_tx3.setText(word3)
    wm_study_im4.setImage(file4)
    wm_study_tx4.setText(word4)
    # keep track of which components have finished
    wm_studyComponents = [wm_study_im1, wm_study_tx1, wm_study_im2, wm_study_tx2, wm_study_im3, wm_study_tx3, wm_study_im4, wm_study_tx4]
    for thisComponent in wm_studyComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    wm_studyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "wm_study"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = wm_studyClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=wm_studyClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if prac != 1:
            if list_no != expInfo["list"]:
                continueRoutine = False
        
        # *wm_study_im1* updates
        if wm_study_im1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wm_study_im1.frameNStart = frameN  # exact frame index
            wm_study_im1.tStart = t  # local t and not account for scr refresh
            wm_study_im1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wm_study_im1, 'tStartRefresh')  # time at next scr refresh
            wm_study_im1.setAutoDraw(True)
        if wm_study_im1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wm_study_im1.tStartRefresh + 1.8-frameTolerance:
                # keep track of stop time/frame for later
                wm_study_im1.tStop = t  # not accounting for scr refresh
                wm_study_im1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(wm_study_im1, 'tStopRefresh')  # time at next scr refresh
                wm_study_im1.setAutoDraw(False)
        
        # *wm_study_tx1* updates
        if wm_study_tx1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wm_study_tx1.frameNStart = frameN  # exact frame index
            wm_study_tx1.tStart = t  # local t and not account for scr refresh
            wm_study_tx1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wm_study_tx1, 'tStartRefresh')  # time at next scr refresh
            wm_study_tx1.setAutoDraw(True)
        if wm_study_tx1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wm_study_tx1.tStartRefresh + 1.8-frameTolerance:
                # keep track of stop time/frame for later
                wm_study_tx1.tStop = t  # not accounting for scr refresh
                wm_study_tx1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(wm_study_tx1, 'tStopRefresh')  # time at next scr refresh
                wm_study_tx1.setAutoDraw(False)
        
        # *wm_study_im2* updates
        if wm_study_im2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            wm_study_im2.frameNStart = frameN  # exact frame index
            wm_study_im2.tStart = t  # local t and not account for scr refresh
            wm_study_im2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wm_study_im2, 'tStartRefresh')  # time at next scr refresh
            wm_study_im2.setAutoDraw(True)
        if wm_study_im2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wm_study_im2.tStartRefresh + 1.8-frameTolerance:
                # keep track of stop time/frame for later
                wm_study_im2.tStop = t  # not accounting for scr refresh
                wm_study_im2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(wm_study_im2, 'tStopRefresh')  # time at next scr refresh
                wm_study_im2.setAutoDraw(False)
        
        # *wm_study_tx2* updates
        if wm_study_tx2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            wm_study_tx2.frameNStart = frameN  # exact frame index
            wm_study_tx2.tStart = t  # local t and not account for scr refresh
            wm_study_tx2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wm_study_tx2, 'tStartRefresh')  # time at next scr refresh
            wm_study_tx2.setAutoDraw(True)
        if wm_study_tx2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wm_study_tx2.tStartRefresh + 1.8-frameTolerance:
                # keep track of stop time/frame for later
                wm_study_tx2.tStop = t  # not accounting for scr refresh
                wm_study_tx2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(wm_study_tx2, 'tStopRefresh')  # time at next scr refresh
                wm_study_tx2.setAutoDraw(False)
        
        # *wm_study_im3* updates
        if wm_study_im3.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            wm_study_im3.frameNStart = frameN  # exact frame index
            wm_study_im3.tStart = t  # local t and not account for scr refresh
            wm_study_im3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wm_study_im3, 'tStartRefresh')  # time at next scr refresh
            wm_study_im3.setAutoDraw(True)
        if wm_study_im3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wm_study_im3.tStartRefresh + 1.8-frameTolerance:
                # keep track of stop time/frame for later
                wm_study_im3.tStop = t  # not accounting for scr refresh
                wm_study_im3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(wm_study_im3, 'tStopRefresh')  # time at next scr refresh
                wm_study_im3.setAutoDraw(False)
        
        # *wm_study_tx3* updates
        if wm_study_tx3.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            wm_study_tx3.frameNStart = frameN  # exact frame index
            wm_study_tx3.tStart = t  # local t and not account for scr refresh
            wm_study_tx3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wm_study_tx3, 'tStartRefresh')  # time at next scr refresh
            wm_study_tx3.setAutoDraw(True)
        if wm_study_tx3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wm_study_tx3.tStartRefresh + 1.8-frameTolerance:
                # keep track of stop time/frame for later
                wm_study_tx3.tStop = t  # not accounting for scr refresh
                wm_study_tx3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(wm_study_tx3, 'tStopRefresh')  # time at next scr refresh
                wm_study_tx3.setAutoDraw(False)
        
        # *wm_study_im4* updates
        if wm_study_im4.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
            # keep track of start time/frame for later
            wm_study_im4.frameNStart = frameN  # exact frame index
            wm_study_im4.tStart = t  # local t and not account for scr refresh
            wm_study_im4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wm_study_im4, 'tStartRefresh')  # time at next scr refresh
            wm_study_im4.setAutoDraw(True)
        if wm_study_im4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wm_study_im4.tStartRefresh + 1.8-frameTolerance:
                # keep track of stop time/frame for later
                wm_study_im4.tStop = t  # not accounting for scr refresh
                wm_study_im4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(wm_study_im4, 'tStopRefresh')  # time at next scr refresh
                wm_study_im4.setAutoDraw(False)
        
        # *wm_study_tx4* updates
        if wm_study_tx4.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
            # keep track of start time/frame for later
            wm_study_tx4.frameNStart = frameN  # exact frame index
            wm_study_tx4.tStart = t  # local t and not account for scr refresh
            wm_study_tx4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wm_study_tx4, 'tStartRefresh')  # time at next scr refresh
            wm_study_tx4.setAutoDraw(True)
        if wm_study_tx4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wm_study_tx4.tStartRefresh + 1.8-frameTolerance:
                # keep track of stop time/frame for later
                wm_study_tx4.tStop = t  # not accounting for scr refresh
                wm_study_tx4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(wm_study_tx4, 'tStopRefresh')  # time at next scr refresh
                wm_study_tx4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wm_studyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "wm_study"-------
    for thisComponent in wm_studyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # SET THE ORDER OF TEST
    
    from random import shuffle
    
    testOrder = [0,1,2,3]
    
    testImages = [file1, file2, file3, file4]
    testWords = [word1, word2, word3, word4]
    
    shuffle(testOrder)
    recallCounter = 0
    
    all_recalled = []
    all_recall_rt = []
    prac_wm_trial_loop.addData('wm_study_im1.started', wm_study_im1.tStartRefresh)
    prac_wm_trial_loop.addData('wm_study_im1.stopped', wm_study_im1.tStopRefresh)
    prac_wm_trial_loop.addData('wm_study_tx1.started', wm_study_tx1.tStartRefresh)
    prac_wm_trial_loop.addData('wm_study_tx1.stopped', wm_study_tx1.tStopRefresh)
    prac_wm_trial_loop.addData('wm_study_im2.started', wm_study_im2.tStartRefresh)
    prac_wm_trial_loop.addData('wm_study_im2.stopped', wm_study_im2.tStopRefresh)
    prac_wm_trial_loop.addData('wm_study_tx2.started', wm_study_tx2.tStartRefresh)
    prac_wm_trial_loop.addData('wm_study_tx2.stopped', wm_study_tx2.tStopRefresh)
    prac_wm_trial_loop.addData('wm_study_im3.started', wm_study_im3.tStartRefresh)
    prac_wm_trial_loop.addData('wm_study_im3.stopped', wm_study_im3.tStopRefresh)
    prac_wm_trial_loop.addData('wm_study_tx3.started', wm_study_tx3.tStartRefresh)
    prac_wm_trial_loop.addData('wm_study_tx3.stopped', wm_study_tx3.tStopRefresh)
    prac_wm_trial_loop.addData('wm_study_im4.started', wm_study_im4.tStartRefresh)
    prac_wm_trial_loop.addData('wm_study_im4.stopped', wm_study_im4.tStopRefresh)
    prac_wm_trial_loop.addData('wm_study_tx4.started', wm_study_tx4.tStartRefresh)
    prac_wm_trial_loop.addData('wm_study_tx4.stopped', wm_study_tx4.tStopRefresh)
    
    # ------Prepare to start Routine "search"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    
    from random import random, randint
    
    s1pos = [-xpos-xdisp, ypos + ((random() - .5)*ydisp)]
    s2pos = [-xpos+xdisp, ypos + ((random() - .5)*ydisp)]
    
    s3pos = [xpos-xdisp, ypos + ((random() - .5)*ydisp)]
    s4pos = [xpos+xdisp, ypos + ((random() - .5)*ydisp)]
    
    s5pos = [xpos-xdisp, -ypos + ((random() - .5)*ydisp)]
    s6pos = [xpos+xdisp, -ypos + ((random() - .5)*ydisp)]
    
    s7pos = [-xpos-xdisp, -ypos + ((random() - .5)*ydisp)]
    s8pos = [-xpos+xdisp, -ypos + ((random() - .5)*ydisp)]
    
    tari = randint(0, 3)
    tarright = random() > .5
    
    ims = []
    for i in [0,1,2,3]:
        if i == tari:
            opts = [tars[tarright], nontars[random() > .5]]
        else:
            opts = nontars[:]
        if random() > .5:
            ims.extend(opts)
        else:
            ims.extend([opts[1], opts[0]])
    
    s1 = im_dir + ims[0] + ".png"
    s2 = im_dir + ims[1] + ".png"
    
    s3 = im_dir + ims[2] + ".png"
    s4 = im_dir + ims[3] + ".png"
    
    s5 = im_dir + ims[4] + ".png"
    s6 = im_dir + ims[5] + ".png"
    
    s7 = im_dir + ims[6] + ".png"
    s8 = im_dir + ims[7] + ".png"
    
    thisExp.addData("s_im1", s1)
    thisExp.addData("s_im2", s2)
    thisExp.addData("s_im3", s3)
    thisExp.addData("s_im4", s4)
    thisExp.addData("s_im5", s5)
    thisExp.addData("s_im6", s6)
    thisExp.addData("s_im7", s7)
    thisExp.addData("s_im8", s8)
    
    thisExp.addData("s_im1pos", s1pos)
    thisExp.addData("s_im2pos", s2pos)
    thisExp.addData("s_im3pos", s3pos)
    thisExp.addData("s_im4pos", s4pos)
    thisExp.addData("s_im5pos", s5pos)
    thisExp.addData("s_im6pos", s6pos)
    thisExp.addData("s_im7pos", s7pos)
    thisExp.addData("s_im8pos", s8pos)
    
    thisExp.addData("s_tarright", tarright)
    sim1.setPos(s1pos)
    sim1.setSize(im_size)
    sim1.setImage(s1)
    sim2.setPos(s2pos)
    sim2.setSize(im_size)
    sim2.setImage(s2)
    sim3.setPos(s3pos)
    sim3.setSize(im_size)
    sim3.setImage(s3)
    sim4.setPos(s4pos)
    sim4.setSize(im_size)
    sim4.setImage(s4)
    sim5.setPos(s5pos)
    sim5.setSize(im_size)
    sim5.setImage(s5)
    sim6.setPos(s6pos)
    sim6.setSize(im_size)
    sim6.setImage(s6)
    sim7.setPos(s7pos)
    sim7.setSize(im_size)
    sim7.setImage(s7)
    sim8.setPos(s8pos)
    sim8.setSize(im_size)
    sim8.setImage(s8)
    search_resp.keys = []
    search_resp.rt = []
    _search_resp_allKeys = []
    # keep track of which components have finished
    searchComponents = [sim1, sim2, sim3, sim4, sim5, sim6, sim7, sim8, search_resp, search_fix]
    for thisComponent in searchComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    searchClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "search"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = searchClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=searchClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if prac != 1:
            if list_no != expInfo["list"]:
                continueRoutine = False
        
        # *sim1* updates
        if sim1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sim1.frameNStart = frameN  # exact frame index
            sim1.tStart = t  # local t and not account for scr refresh
            sim1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sim1, 'tStartRefresh')  # time at next scr refresh
            sim1.setAutoDraw(True)
        if sim1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sim1.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                sim1.tStop = t  # not accounting for scr refresh
                sim1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sim1, 'tStopRefresh')  # time at next scr refresh
                sim1.setAutoDraw(False)
        
        # *sim2* updates
        if sim2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sim2.frameNStart = frameN  # exact frame index
            sim2.tStart = t  # local t and not account for scr refresh
            sim2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sim2, 'tStartRefresh')  # time at next scr refresh
            sim2.setAutoDraw(True)
        if sim2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sim2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                sim2.tStop = t  # not accounting for scr refresh
                sim2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sim2, 'tStopRefresh')  # time at next scr refresh
                sim2.setAutoDraw(False)
        
        # *sim3* updates
        if sim3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sim3.frameNStart = frameN  # exact frame index
            sim3.tStart = t  # local t and not account for scr refresh
            sim3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sim3, 'tStartRefresh')  # time at next scr refresh
            sim3.setAutoDraw(True)
        if sim3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sim3.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                sim3.tStop = t  # not accounting for scr refresh
                sim3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sim3, 'tStopRefresh')  # time at next scr refresh
                sim3.setAutoDraw(False)
        
        # *sim4* updates
        if sim4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sim4.frameNStart = frameN  # exact frame index
            sim4.tStart = t  # local t and not account for scr refresh
            sim4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sim4, 'tStartRefresh')  # time at next scr refresh
            sim4.setAutoDraw(True)
        if sim4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sim4.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                sim4.tStop = t  # not accounting for scr refresh
                sim4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sim4, 'tStopRefresh')  # time at next scr refresh
                sim4.setAutoDraw(False)
        
        # *sim5* updates
        if sim5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sim5.frameNStart = frameN  # exact frame index
            sim5.tStart = t  # local t and not account for scr refresh
            sim5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sim5, 'tStartRefresh')  # time at next scr refresh
            sim5.setAutoDraw(True)
        if sim5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sim5.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                sim5.tStop = t  # not accounting for scr refresh
                sim5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sim5, 'tStopRefresh')  # time at next scr refresh
                sim5.setAutoDraw(False)
        
        # *sim6* updates
        if sim6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sim6.frameNStart = frameN  # exact frame index
            sim6.tStart = t  # local t and not account for scr refresh
            sim6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sim6, 'tStartRefresh')  # time at next scr refresh
            sim6.setAutoDraw(True)
        if sim6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sim6.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                sim6.tStop = t  # not accounting for scr refresh
                sim6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sim6, 'tStopRefresh')  # time at next scr refresh
                sim6.setAutoDraw(False)
        
        # *sim7* updates
        if sim7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sim7.frameNStart = frameN  # exact frame index
            sim7.tStart = t  # local t and not account for scr refresh
            sim7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sim7, 'tStartRefresh')  # time at next scr refresh
            sim7.setAutoDraw(True)
        if sim7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sim7.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                sim7.tStop = t  # not accounting for scr refresh
                sim7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sim7, 'tStopRefresh')  # time at next scr refresh
                sim7.setAutoDraw(False)
        
        # *sim8* updates
        if sim8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sim8.frameNStart = frameN  # exact frame index
            sim8.tStart = t  # local t and not account for scr refresh
            sim8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sim8, 'tStartRefresh')  # time at next scr refresh
            sim8.setAutoDraw(True)
        if sim8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sim8.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                sim8.tStop = t  # not accounting for scr refresh
                sim8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sim8, 'tStopRefresh')  # time at next scr refresh
                sim8.setAutoDraw(False)
        
        # *search_resp* updates
        waitOnFlip = False
        if search_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            search_resp.frameNStart = frameN  # exact frame index
            search_resp.tStart = t  # local t and not account for scr refresh
            search_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(search_resp, 'tStartRefresh')  # time at next scr refresh
            search_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(search_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(search_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if search_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > search_resp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                search_resp.tStop = t  # not accounting for scr refresh
                search_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(search_resp, 'tStopRefresh')  # time at next scr refresh
                search_resp.status = FINISHED
        if search_resp.status == STARTED and not waitOnFlip:
            theseKeys = search_resp.getKeys(keyList=['1', '0'], waitRelease=False)
            _search_resp_allKeys.extend(theseKeys)
            if len(_search_resp_allKeys):
                search_resp.keys = _search_resp_allKeys[-1].name  # just the last key pressed
                search_resp.rt = _search_resp_allKeys[-1].rt
        
        # *search_fix* updates
        if search_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            search_fix.frameNStart = frameN  # exact frame index
            search_fix.tStart = t  # local t and not account for scr refresh
            search_fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(search_fix, 'tStartRefresh')  # time at next scr refresh
            search_fix.setAutoDraw(True)
        if search_fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > search_fix.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                search_fix.tStop = t  # not accounting for scr refresh
                search_fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(search_fix, 'tStopRefresh')  # time at next scr refresh
                search_fix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in searchComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "search"-------
    for thisComponent in searchComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    prac_wm_trial_loop.addData('sim1.started', sim1.tStartRefresh)
    prac_wm_trial_loop.addData('sim1.stopped', sim1.tStopRefresh)
    prac_wm_trial_loop.addData('sim2.started', sim2.tStartRefresh)
    prac_wm_trial_loop.addData('sim2.stopped', sim2.tStopRefresh)
    prac_wm_trial_loop.addData('sim3.started', sim3.tStartRefresh)
    prac_wm_trial_loop.addData('sim3.stopped', sim3.tStopRefresh)
    prac_wm_trial_loop.addData('sim4.started', sim4.tStartRefresh)
    prac_wm_trial_loop.addData('sim4.stopped', sim4.tStopRefresh)
    prac_wm_trial_loop.addData('sim5.started', sim5.tStartRefresh)
    prac_wm_trial_loop.addData('sim5.stopped', sim5.tStopRefresh)
    prac_wm_trial_loop.addData('sim6.started', sim6.tStartRefresh)
    prac_wm_trial_loop.addData('sim6.stopped', sim6.tStopRefresh)
    prac_wm_trial_loop.addData('sim7.started', sim7.tStartRefresh)
    prac_wm_trial_loop.addData('sim7.stopped', sim7.tStopRefresh)
    prac_wm_trial_loop.addData('sim8.started', sim8.tStartRefresh)
    prac_wm_trial_loop.addData('sim8.stopped', sim8.tStopRefresh)
    # check responses
    if search_resp.keys in ['', [], None]:  # No response was made
        search_resp.keys = None
    prac_wm_trial_loop.addData('search_resp.keys',search_resp.keys)
    if search_resp.keys != None:  # we had a response
        prac_wm_trial_loop.addData('search_resp.rt', search_resp.rt)
    prac_wm_trial_loop.addData('search_resp.started', search_resp.tStartRefresh)
    prac_wm_trial_loop.addData('search_resp.stopped', search_resp.tStopRefresh)
    prac_wm_trial_loop.addData('search_fix.started', search_fix.tStartRefresh)
    prac_wm_trial_loop.addData('search_fix.stopped', search_fix.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    prac_wm_test_loop = data.TrialHandler(nReps=4, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='prac_wm_test_loop')
    thisExp.addLoop(prac_wm_test_loop)  # add the loop to the experiment
    thisPrac_wm_test_loop = prac_wm_test_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_wm_test_loop.rgb)
    if thisPrac_wm_test_loop != None:
        for paramName in thisPrac_wm_test_loop:
            exec('{} = thisPrac_wm_test_loop[paramName]'.format(paramName))
    
    for thisPrac_wm_test_loop in prac_wm_test_loop:
        currentLoop = prac_wm_test_loop
        # abbreviate parameter names if possible (e.g. rgb = thisPrac_wm_test_loop.rgb)
        if thisPrac_wm_test_loop != None:
            for paramName in thisPrac_wm_test_loop:
                exec('{} = thisPrac_wm_test_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "wm_test"-------
        continueRoutine = True
        routineTimer.add(10.000000)
        # update component parameters for each repeat
        # SET TEST IMAGE + TEXT
        
        validkeys = [char for char in 'abcdefghijklmnopqrstuvwxyz']
        wm_recall_text.text = ''
        event.clearEvents('keyboard')
        
        recall_started = False
        timer_wm.reset()
        
        testImage = testImages[testOrder[recallCounter]]
        
        recallCounter += 1
        wm_recall_text.setText('')
        wm_test_im.setImage(testImage)
        # keep track of which components have finished
        wm_testComponents = [wm_recall_text, wm_test_im]
        for thisComponent in wm_testComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        wm_testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "wm_test"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = wm_testClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=wm_testClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if prac != 1:
                if list_no != expInfo["list"]:
                    continueRoutine = False
            
            if not recall_started:
                wm_recall_text.text = '?'
            
            keys = event.getKeys()
            if len(keys):
                key = keys[0]
                if key in validkeys:
                    recall_started = True
                    if wm_recall_text.text == '?':
                        wm_recall_text.text = ''
                    wm_recall_text.text = wm_recall_text.text + key.upper()
                elif key == 'return':
                    continueRoutine = False
                elif key == 'backspace':
                    wm_recall_text.text = wm_recall_text.text[:-1]
            
            if timer_wm.getTime() > 15:
                continueRoutine = False
            
            
            # *wm_recall_text* updates
            if wm_recall_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wm_recall_text.frameNStart = frameN  # exact frame index
                wm_recall_text.tStart = t  # local t and not account for scr refresh
                wm_recall_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_recall_text, 'tStartRefresh')  # time at next scr refresh
                wm_recall_text.setAutoDraw(True)
            if wm_recall_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > wm_recall_text.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    wm_recall_text.tStop = t  # not accounting for scr refresh
                    wm_recall_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(wm_recall_text, 'tStopRefresh')  # time at next scr refresh
                    wm_recall_text.setAutoDraw(False)
            
            # *wm_test_im* updates
            if wm_test_im.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                wm_test_im.frameNStart = frameN  # exact frame index
                wm_test_im.tStart = t  # local t and not account for scr refresh
                wm_test_im.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_test_im, 'tStartRefresh')  # time at next scr refresh
                wm_test_im.setAutoDraw(True)
            if wm_test_im.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > wm_test_im.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    wm_test_im.tStop = t  # not accounting for scr refresh
                    wm_test_im.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(wm_test_im, 'tStopRefresh')  # time at next scr refresh
                    wm_test_im.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in wm_testComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "wm_test"-------
        for thisComponent in wm_testComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        all_recalled.append(wm_recall_text.text)
        all_recall_rt.append(timer_wm.getTime())
        prac_wm_test_loop.addData('wm_recall_text.started', wm_recall_text.tStartRefresh)
        prac_wm_test_loop.addData('wm_recall_text.stopped', wm_recall_text.tStopRefresh)
        prac_wm_test_loop.addData('wm_test_im.started', wm_test_im.tStartRefresh)
        prac_wm_test_loop.addData('wm_test_im.stopped', wm_test_im.tStopRefresh)
        
        # ------Prepare to start Routine "wm_recall_isi"-------
        continueRoutine = True
        routineTimer.add(0.200000)
        # update component parameters for each repeat
        # keep track of which components have finished
        wm_recall_isiComponents = [wm_isi_blank]
        for thisComponent in wm_recall_isiComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        wm_recall_isiClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "wm_recall_isi"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = wm_recall_isiClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=wm_recall_isiClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if prac != 1:
                if list_no != expInfo["list"]:
                    continueRoutine = False
            
            # *wm_isi_blank* updates
            if wm_isi_blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wm_isi_blank.frameNStart = frameN  # exact frame index
                wm_isi_blank.tStart = t  # local t and not account for scr refresh
                wm_isi_blank.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_isi_blank, 'tStartRefresh')  # time at next scr refresh
                wm_isi_blank.setAutoDraw(True)
            if wm_isi_blank.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > wm_isi_blank.tStartRefresh + .2-frameTolerance:
                    # keep track of stop time/frame for later
                    wm_isi_blank.tStop = t  # not accounting for scr refresh
                    wm_isi_blank.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(wm_isi_blank, 'tStopRefresh')  # time at next scr refresh
                    wm_isi_blank.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in wm_recall_isiComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "wm_recall_isi"-------
        for thisComponent in wm_recall_isiComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        prac_wm_test_loop.addData('wm_isi_blank.started', wm_isi_blank.tStartRefresh)
        prac_wm_test_loop.addData('wm_isi_blank.stopped', wm_isi_blank.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 4 repeats of 'prac_wm_test_loop'
    
    
    # ------Prepare to start Routine "write"-------
    continueRoutine = True
    routineTimer.add(0.300000)
    # update component parameters for each repeat
    
    for i in range(4):
        thisExp.addData("wm_recalled"+str(i+1), all_recalled[i])
        thisExp.addData("wm_recall_rt"+str(i+1), all_recall_rt[i])
        thisExp.addData("wm_probed"+str(i+1), testOrder[i])
        thisExp.addData("wm_recall_acc"+str(i+1), testWords[testOrder[i]] == all_recalled[i])
    
    # keep track of which components have finished
    writeComponents = [text_11]
    for thisComponent in writeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    writeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "write"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = writeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=writeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if prac != 1:
            if list_no != expInfo["list"]:
                continueRoutine = False
        
        
        # *text_11* updates
        if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_11.frameNStart = frameN  # exact frame index
            text_11.tStart = t  # local t and not account for scr refresh
            text_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
            text_11.setAutoDraw(True)
        if text_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_11.tStartRefresh + .3-frameTolerance:
                # keep track of stop time/frame for later
                text_11.tStop = t  # not accounting for scr refresh
                text_11.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_11, 'tStopRefresh')  # time at next scr refresh
                text_11.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in writeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "write"-------
    for thisComponent in writeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    prac_wm_trial_loop.addData('text_11.started', text_11.tStartRefresh)
    prac_wm_trial_loop.addData('text_11.stopped', text_11.tStopRefresh)
    
    # ------Prepare to start Routine "search_reminder"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    search_reminderComponents = [text_16]
    for thisComponent in search_reminderComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    search_reminderClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "search_reminder"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = search_reminderClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=search_reminderClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if prac != 1:
            if list_no != expInfo["list"]:
                continueRoutine = False
        
        if search_resp.keys == '0' or search_resp.keys == '1':
            continueRoutine = False
        
        # *text_16* updates
        if text_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_16.frameNStart = frameN  # exact frame index
            text_16.tStart = t  # local t and not account for scr refresh
            text_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_16, 'tStartRefresh')  # time at next scr refresh
            text_16.setAutoDraw(True)
        if text_16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_16.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_16.tStop = t  # not accounting for scr refresh
                text_16.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_16, 'tStopRefresh')  # time at next scr refresh
                text_16.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in search_reminderComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "search_reminder"-------
    for thisComponent in search_reminderComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    prac_wm_trial_loop.addData('text_16.started', text_16.tStartRefresh)
    prac_wm_trial_loop.addData('text_16.stopped', text_16.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'prac_wm_trial_loop'


# ------Prepare to start Routine "end_wm_prac"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
prac=0
# keep track of which components have finished
end_wm_pracComponents = [text_7, key_resp_9]
for thisComponent in end_wm_pracComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
end_wm_pracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end_wm_prac"-------
while continueRoutine:
    # get current time
    t = end_wm_pracClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=end_wm_pracClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_wm_pracComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end_wm_prac"-------
for thisComponent in end_wm_pracComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)
# the Routine "end_wm_prac" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
wm_trial_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuli/wm-lists.csv'),
    seed=None, name='wm_trial_loop')
thisExp.addLoop(wm_trial_loop)  # add the loop to the experiment
thisWm_trial_loop = wm_trial_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisWm_trial_loop.rgb)
if thisWm_trial_loop != None:
    for paramName in thisWm_trial_loop:
        exec('{} = thisWm_trial_loop[paramName]'.format(paramName))

for thisWm_trial_loop in wm_trial_loop:
    currentLoop = wm_trial_loop
    # abbreviate parameter names if possible (e.g. rgb = thisWm_trial_loop.rgb)
    if thisWm_trial_loop != None:
        for paramName in thisWm_trial_loop:
            exec('{} = thisWm_trial_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ST"-------
    continueRoutine = True
    # update component parameters for each repeat
    st_text.setText("Press '1' or '0' to start the next sequence...")
    st_key.keys = []
    st_key.rt = []
    _st_key_allKeys = []
    # keep track of which components have finished
    STComponents = [st_text, st_key]
    for thisComponent in STComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    STClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ST"-------
    while continueRoutine:
        # get current time
        t = STClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=STClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if prac != 1:
            if list_no != expInfo["list"]:
                continueRoutine = False
        
        # *st_text* updates
        if st_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            st_text.frameNStart = frameN  # exact frame index
            st_text.tStart = t  # local t and not account for scr refresh
            st_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(st_text, 'tStartRefresh')  # time at next scr refresh
            st_text.setAutoDraw(True)
        
        # *st_key* updates
        waitOnFlip = False
        if st_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            st_key.frameNStart = frameN  # exact frame index
            st_key.tStart = t  # local t and not account for scr refresh
            st_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(st_key, 'tStartRefresh')  # time at next scr refresh
            st_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(st_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(st_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if st_key.status == STARTED and not waitOnFlip:
            theseKeys = st_key.getKeys(keyList=['1', '0'], waitRelease=False)
            _st_key_allKeys.extend(theseKeys)
            if len(_st_key_allKeys):
                st_key.keys = _st_key_allKeys[-1].name  # just the last key pressed
                st_key.rt = _st_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in STComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ST"-------
    for thisComponent in STComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ST" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "wm_study"-------
    continueRoutine = True
    routineTimer.add(7.800000)
    # update component parameters for each repeat
    wm_study_im1.setImage(file1)
    wm_study_tx1.setText(word1)
    wm_study_im2.setImage(file2)
    wm_study_tx2.setText(word2)
    wm_study_im3.setImage(file3)
    wm_study_tx3.setText(word3)
    wm_study_im4.setImage(file4)
    wm_study_tx4.setText(word4)
    # keep track of which components have finished
    wm_studyComponents = [wm_study_im1, wm_study_tx1, wm_study_im2, wm_study_tx2, wm_study_im3, wm_study_tx3, wm_study_im4, wm_study_tx4]
    for thisComponent in wm_studyComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    wm_studyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "wm_study"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = wm_studyClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=wm_studyClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if prac != 1:
            if list_no != expInfo["list"]:
                continueRoutine = False
        
        # *wm_study_im1* updates
        if wm_study_im1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wm_study_im1.frameNStart = frameN  # exact frame index
            wm_study_im1.tStart = t  # local t and not account for scr refresh
            wm_study_im1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wm_study_im1, 'tStartRefresh')  # time at next scr refresh
            wm_study_im1.setAutoDraw(True)
        if wm_study_im1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wm_study_im1.tStartRefresh + 1.8-frameTolerance:
                # keep track of stop time/frame for later
                wm_study_im1.tStop = t  # not accounting for scr refresh
                wm_study_im1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(wm_study_im1, 'tStopRefresh')  # time at next scr refresh
                wm_study_im1.setAutoDraw(False)
        
        # *wm_study_tx1* updates
        if wm_study_tx1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wm_study_tx1.frameNStart = frameN  # exact frame index
            wm_study_tx1.tStart = t  # local t and not account for scr refresh
            wm_study_tx1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wm_study_tx1, 'tStartRefresh')  # time at next scr refresh
            wm_study_tx1.setAutoDraw(True)
        if wm_study_tx1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wm_study_tx1.tStartRefresh + 1.8-frameTolerance:
                # keep track of stop time/frame for later
                wm_study_tx1.tStop = t  # not accounting for scr refresh
                wm_study_tx1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(wm_study_tx1, 'tStopRefresh')  # time at next scr refresh
                wm_study_tx1.setAutoDraw(False)
        
        # *wm_study_im2* updates
        if wm_study_im2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            wm_study_im2.frameNStart = frameN  # exact frame index
            wm_study_im2.tStart = t  # local t and not account for scr refresh
            wm_study_im2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wm_study_im2, 'tStartRefresh')  # time at next scr refresh
            wm_study_im2.setAutoDraw(True)
        if wm_study_im2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wm_study_im2.tStartRefresh + 1.8-frameTolerance:
                # keep track of stop time/frame for later
                wm_study_im2.tStop = t  # not accounting for scr refresh
                wm_study_im2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(wm_study_im2, 'tStopRefresh')  # time at next scr refresh
                wm_study_im2.setAutoDraw(False)
        
        # *wm_study_tx2* updates
        if wm_study_tx2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            wm_study_tx2.frameNStart = frameN  # exact frame index
            wm_study_tx2.tStart = t  # local t and not account for scr refresh
            wm_study_tx2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wm_study_tx2, 'tStartRefresh')  # time at next scr refresh
            wm_study_tx2.setAutoDraw(True)
        if wm_study_tx2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wm_study_tx2.tStartRefresh + 1.8-frameTolerance:
                # keep track of stop time/frame for later
                wm_study_tx2.tStop = t  # not accounting for scr refresh
                wm_study_tx2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(wm_study_tx2, 'tStopRefresh')  # time at next scr refresh
                wm_study_tx2.setAutoDraw(False)
        
        # *wm_study_im3* updates
        if wm_study_im3.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            wm_study_im3.frameNStart = frameN  # exact frame index
            wm_study_im3.tStart = t  # local t and not account for scr refresh
            wm_study_im3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wm_study_im3, 'tStartRefresh')  # time at next scr refresh
            wm_study_im3.setAutoDraw(True)
        if wm_study_im3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wm_study_im3.tStartRefresh + 1.8-frameTolerance:
                # keep track of stop time/frame for later
                wm_study_im3.tStop = t  # not accounting for scr refresh
                wm_study_im3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(wm_study_im3, 'tStopRefresh')  # time at next scr refresh
                wm_study_im3.setAutoDraw(False)
        
        # *wm_study_tx3* updates
        if wm_study_tx3.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            wm_study_tx3.frameNStart = frameN  # exact frame index
            wm_study_tx3.tStart = t  # local t and not account for scr refresh
            wm_study_tx3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wm_study_tx3, 'tStartRefresh')  # time at next scr refresh
            wm_study_tx3.setAutoDraw(True)
        if wm_study_tx3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wm_study_tx3.tStartRefresh + 1.8-frameTolerance:
                # keep track of stop time/frame for later
                wm_study_tx3.tStop = t  # not accounting for scr refresh
                wm_study_tx3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(wm_study_tx3, 'tStopRefresh')  # time at next scr refresh
                wm_study_tx3.setAutoDraw(False)
        
        # *wm_study_im4* updates
        if wm_study_im4.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
            # keep track of start time/frame for later
            wm_study_im4.frameNStart = frameN  # exact frame index
            wm_study_im4.tStart = t  # local t and not account for scr refresh
            wm_study_im4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wm_study_im4, 'tStartRefresh')  # time at next scr refresh
            wm_study_im4.setAutoDraw(True)
        if wm_study_im4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wm_study_im4.tStartRefresh + 1.8-frameTolerance:
                # keep track of stop time/frame for later
                wm_study_im4.tStop = t  # not accounting for scr refresh
                wm_study_im4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(wm_study_im4, 'tStopRefresh')  # time at next scr refresh
                wm_study_im4.setAutoDraw(False)
        
        # *wm_study_tx4* updates
        if wm_study_tx4.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
            # keep track of start time/frame for later
            wm_study_tx4.frameNStart = frameN  # exact frame index
            wm_study_tx4.tStart = t  # local t and not account for scr refresh
            wm_study_tx4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wm_study_tx4, 'tStartRefresh')  # time at next scr refresh
            wm_study_tx4.setAutoDraw(True)
        if wm_study_tx4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wm_study_tx4.tStartRefresh + 1.8-frameTolerance:
                # keep track of stop time/frame for later
                wm_study_tx4.tStop = t  # not accounting for scr refresh
                wm_study_tx4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(wm_study_tx4, 'tStopRefresh')  # time at next scr refresh
                wm_study_tx4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wm_studyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "wm_study"-------
    for thisComponent in wm_studyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # SET THE ORDER OF TEST
    
    from random import shuffle
    
    testOrder = [0,1,2,3]
    
    testImages = [file1, file2, file3, file4]
    testWords = [word1, word2, word3, word4]
    
    shuffle(testOrder)
    recallCounter = 0
    
    all_recalled = []
    all_recall_rt = []
    wm_trial_loop.addData('wm_study_im1.started', wm_study_im1.tStartRefresh)
    wm_trial_loop.addData('wm_study_im1.stopped', wm_study_im1.tStopRefresh)
    wm_trial_loop.addData('wm_study_tx1.started', wm_study_tx1.tStartRefresh)
    wm_trial_loop.addData('wm_study_tx1.stopped', wm_study_tx1.tStopRefresh)
    wm_trial_loop.addData('wm_study_im2.started', wm_study_im2.tStartRefresh)
    wm_trial_loop.addData('wm_study_im2.stopped', wm_study_im2.tStopRefresh)
    wm_trial_loop.addData('wm_study_tx2.started', wm_study_tx2.tStartRefresh)
    wm_trial_loop.addData('wm_study_tx2.stopped', wm_study_tx2.tStopRefresh)
    wm_trial_loop.addData('wm_study_im3.started', wm_study_im3.tStartRefresh)
    wm_trial_loop.addData('wm_study_im3.stopped', wm_study_im3.tStopRefresh)
    wm_trial_loop.addData('wm_study_tx3.started', wm_study_tx3.tStartRefresh)
    wm_trial_loop.addData('wm_study_tx3.stopped', wm_study_tx3.tStopRefresh)
    wm_trial_loop.addData('wm_study_im4.started', wm_study_im4.tStartRefresh)
    wm_trial_loop.addData('wm_study_im4.stopped', wm_study_im4.tStopRefresh)
    wm_trial_loop.addData('wm_study_tx4.started', wm_study_tx4.tStartRefresh)
    wm_trial_loop.addData('wm_study_tx4.stopped', wm_study_tx4.tStopRefresh)
    
    # ------Prepare to start Routine "search"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    
    from random import random, randint
    
    s1pos = [-xpos-xdisp, ypos + ((random() - .5)*ydisp)]
    s2pos = [-xpos+xdisp, ypos + ((random() - .5)*ydisp)]
    
    s3pos = [xpos-xdisp, ypos + ((random() - .5)*ydisp)]
    s4pos = [xpos+xdisp, ypos + ((random() - .5)*ydisp)]
    
    s5pos = [xpos-xdisp, -ypos + ((random() - .5)*ydisp)]
    s6pos = [xpos+xdisp, -ypos + ((random() - .5)*ydisp)]
    
    s7pos = [-xpos-xdisp, -ypos + ((random() - .5)*ydisp)]
    s8pos = [-xpos+xdisp, -ypos + ((random() - .5)*ydisp)]
    
    tari = randint(0, 3)
    tarright = random() > .5
    
    ims = []
    for i in [0,1,2,3]:
        if i == tari:
            opts = [tars[tarright], nontars[random() > .5]]
        else:
            opts = nontars[:]
        if random() > .5:
            ims.extend(opts)
        else:
            ims.extend([opts[1], opts[0]])
    
    s1 = im_dir + ims[0] + ".png"
    s2 = im_dir + ims[1] + ".png"
    
    s3 = im_dir + ims[2] + ".png"
    s4 = im_dir + ims[3] + ".png"
    
    s5 = im_dir + ims[4] + ".png"
    s6 = im_dir + ims[5] + ".png"
    
    s7 = im_dir + ims[6] + ".png"
    s8 = im_dir + ims[7] + ".png"
    
    thisExp.addData("s_im1", s1)
    thisExp.addData("s_im2", s2)
    thisExp.addData("s_im3", s3)
    thisExp.addData("s_im4", s4)
    thisExp.addData("s_im5", s5)
    thisExp.addData("s_im6", s6)
    thisExp.addData("s_im7", s7)
    thisExp.addData("s_im8", s8)
    
    thisExp.addData("s_im1pos", s1pos)
    thisExp.addData("s_im2pos", s2pos)
    thisExp.addData("s_im3pos", s3pos)
    thisExp.addData("s_im4pos", s4pos)
    thisExp.addData("s_im5pos", s5pos)
    thisExp.addData("s_im6pos", s6pos)
    thisExp.addData("s_im7pos", s7pos)
    thisExp.addData("s_im8pos", s8pos)
    
    thisExp.addData("s_tarright", tarright)
    sim1.setPos(s1pos)
    sim1.setSize(im_size)
    sim1.setImage(s1)
    sim2.setPos(s2pos)
    sim2.setSize(im_size)
    sim2.setImage(s2)
    sim3.setPos(s3pos)
    sim3.setSize(im_size)
    sim3.setImage(s3)
    sim4.setPos(s4pos)
    sim4.setSize(im_size)
    sim4.setImage(s4)
    sim5.setPos(s5pos)
    sim5.setSize(im_size)
    sim5.setImage(s5)
    sim6.setPos(s6pos)
    sim6.setSize(im_size)
    sim6.setImage(s6)
    sim7.setPos(s7pos)
    sim7.setSize(im_size)
    sim7.setImage(s7)
    sim8.setPos(s8pos)
    sim8.setSize(im_size)
    sim8.setImage(s8)
    search_resp.keys = []
    search_resp.rt = []
    _search_resp_allKeys = []
    # keep track of which components have finished
    searchComponents = [sim1, sim2, sim3, sim4, sim5, sim6, sim7, sim8, search_resp, search_fix]
    for thisComponent in searchComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    searchClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "search"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = searchClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=searchClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if prac != 1:
            if list_no != expInfo["list"]:
                continueRoutine = False
        
        # *sim1* updates
        if sim1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sim1.frameNStart = frameN  # exact frame index
            sim1.tStart = t  # local t and not account for scr refresh
            sim1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sim1, 'tStartRefresh')  # time at next scr refresh
            sim1.setAutoDraw(True)
        if sim1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sim1.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                sim1.tStop = t  # not accounting for scr refresh
                sim1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sim1, 'tStopRefresh')  # time at next scr refresh
                sim1.setAutoDraw(False)
        
        # *sim2* updates
        if sim2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sim2.frameNStart = frameN  # exact frame index
            sim2.tStart = t  # local t and not account for scr refresh
            sim2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sim2, 'tStartRefresh')  # time at next scr refresh
            sim2.setAutoDraw(True)
        if sim2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sim2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                sim2.tStop = t  # not accounting for scr refresh
                sim2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sim2, 'tStopRefresh')  # time at next scr refresh
                sim2.setAutoDraw(False)
        
        # *sim3* updates
        if sim3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sim3.frameNStart = frameN  # exact frame index
            sim3.tStart = t  # local t and not account for scr refresh
            sim3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sim3, 'tStartRefresh')  # time at next scr refresh
            sim3.setAutoDraw(True)
        if sim3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sim3.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                sim3.tStop = t  # not accounting for scr refresh
                sim3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sim3, 'tStopRefresh')  # time at next scr refresh
                sim3.setAutoDraw(False)
        
        # *sim4* updates
        if sim4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sim4.frameNStart = frameN  # exact frame index
            sim4.tStart = t  # local t and not account for scr refresh
            sim4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sim4, 'tStartRefresh')  # time at next scr refresh
            sim4.setAutoDraw(True)
        if sim4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sim4.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                sim4.tStop = t  # not accounting for scr refresh
                sim4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sim4, 'tStopRefresh')  # time at next scr refresh
                sim4.setAutoDraw(False)
        
        # *sim5* updates
        if sim5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sim5.frameNStart = frameN  # exact frame index
            sim5.tStart = t  # local t and not account for scr refresh
            sim5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sim5, 'tStartRefresh')  # time at next scr refresh
            sim5.setAutoDraw(True)
        if sim5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sim5.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                sim5.tStop = t  # not accounting for scr refresh
                sim5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sim5, 'tStopRefresh')  # time at next scr refresh
                sim5.setAutoDraw(False)
        
        # *sim6* updates
        if sim6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sim6.frameNStart = frameN  # exact frame index
            sim6.tStart = t  # local t and not account for scr refresh
            sim6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sim6, 'tStartRefresh')  # time at next scr refresh
            sim6.setAutoDraw(True)
        if sim6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sim6.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                sim6.tStop = t  # not accounting for scr refresh
                sim6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sim6, 'tStopRefresh')  # time at next scr refresh
                sim6.setAutoDraw(False)
        
        # *sim7* updates
        if sim7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sim7.frameNStart = frameN  # exact frame index
            sim7.tStart = t  # local t and not account for scr refresh
            sim7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sim7, 'tStartRefresh')  # time at next scr refresh
            sim7.setAutoDraw(True)
        if sim7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sim7.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                sim7.tStop = t  # not accounting for scr refresh
                sim7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sim7, 'tStopRefresh')  # time at next scr refresh
                sim7.setAutoDraw(False)
        
        # *sim8* updates
        if sim8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sim8.frameNStart = frameN  # exact frame index
            sim8.tStart = t  # local t and not account for scr refresh
            sim8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sim8, 'tStartRefresh')  # time at next scr refresh
            sim8.setAutoDraw(True)
        if sim8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sim8.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                sim8.tStop = t  # not accounting for scr refresh
                sim8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sim8, 'tStopRefresh')  # time at next scr refresh
                sim8.setAutoDraw(False)
        
        # *search_resp* updates
        waitOnFlip = False
        if search_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            search_resp.frameNStart = frameN  # exact frame index
            search_resp.tStart = t  # local t and not account for scr refresh
            search_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(search_resp, 'tStartRefresh')  # time at next scr refresh
            search_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(search_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(search_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if search_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > search_resp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                search_resp.tStop = t  # not accounting for scr refresh
                search_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(search_resp, 'tStopRefresh')  # time at next scr refresh
                search_resp.status = FINISHED
        if search_resp.status == STARTED and not waitOnFlip:
            theseKeys = search_resp.getKeys(keyList=['1', '0'], waitRelease=False)
            _search_resp_allKeys.extend(theseKeys)
            if len(_search_resp_allKeys):
                search_resp.keys = _search_resp_allKeys[-1].name  # just the last key pressed
                search_resp.rt = _search_resp_allKeys[-1].rt
        
        # *search_fix* updates
        if search_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            search_fix.frameNStart = frameN  # exact frame index
            search_fix.tStart = t  # local t and not account for scr refresh
            search_fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(search_fix, 'tStartRefresh')  # time at next scr refresh
            search_fix.setAutoDraw(True)
        if search_fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > search_fix.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                search_fix.tStop = t  # not accounting for scr refresh
                search_fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(search_fix, 'tStopRefresh')  # time at next scr refresh
                search_fix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in searchComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "search"-------
    for thisComponent in searchComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    wm_trial_loop.addData('sim1.started', sim1.tStartRefresh)
    wm_trial_loop.addData('sim1.stopped', sim1.tStopRefresh)
    wm_trial_loop.addData('sim2.started', sim2.tStartRefresh)
    wm_trial_loop.addData('sim2.stopped', sim2.tStopRefresh)
    wm_trial_loop.addData('sim3.started', sim3.tStartRefresh)
    wm_trial_loop.addData('sim3.stopped', sim3.tStopRefresh)
    wm_trial_loop.addData('sim4.started', sim4.tStartRefresh)
    wm_trial_loop.addData('sim4.stopped', sim4.tStopRefresh)
    wm_trial_loop.addData('sim5.started', sim5.tStartRefresh)
    wm_trial_loop.addData('sim5.stopped', sim5.tStopRefresh)
    wm_trial_loop.addData('sim6.started', sim6.tStartRefresh)
    wm_trial_loop.addData('sim6.stopped', sim6.tStopRefresh)
    wm_trial_loop.addData('sim7.started', sim7.tStartRefresh)
    wm_trial_loop.addData('sim7.stopped', sim7.tStopRefresh)
    wm_trial_loop.addData('sim8.started', sim8.tStartRefresh)
    wm_trial_loop.addData('sim8.stopped', sim8.tStopRefresh)
    # check responses
    if search_resp.keys in ['', [], None]:  # No response was made
        search_resp.keys = None
    wm_trial_loop.addData('search_resp.keys',search_resp.keys)
    if search_resp.keys != None:  # we had a response
        wm_trial_loop.addData('search_resp.rt', search_resp.rt)
    wm_trial_loop.addData('search_resp.started', search_resp.tStartRefresh)
    wm_trial_loop.addData('search_resp.stopped', search_resp.tStopRefresh)
    wm_trial_loop.addData('search_fix.started', search_fix.tStartRefresh)
    wm_trial_loop.addData('search_fix.stopped', search_fix.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    wm_test_loop = data.TrialHandler(nReps=4, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='wm_test_loop')
    thisExp.addLoop(wm_test_loop)  # add the loop to the experiment
    thisWm_test_loop = wm_test_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisWm_test_loop.rgb)
    if thisWm_test_loop != None:
        for paramName in thisWm_test_loop:
            exec('{} = thisWm_test_loop[paramName]'.format(paramName))
    
    for thisWm_test_loop in wm_test_loop:
        currentLoop = wm_test_loop
        # abbreviate parameter names if possible (e.g. rgb = thisWm_test_loop.rgb)
        if thisWm_test_loop != None:
            for paramName in thisWm_test_loop:
                exec('{} = thisWm_test_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "wm_test"-------
        continueRoutine = True
        routineTimer.add(10.000000)
        # update component parameters for each repeat
        # SET TEST IMAGE + TEXT
        
        validkeys = [char for char in 'abcdefghijklmnopqrstuvwxyz']
        wm_recall_text.text = ''
        event.clearEvents('keyboard')
        
        recall_started = False
        timer_wm.reset()
        
        testImage = testImages[testOrder[recallCounter]]
        
        recallCounter += 1
        wm_recall_text.setText('')
        wm_test_im.setImage(testImage)
        # keep track of which components have finished
        wm_testComponents = [wm_recall_text, wm_test_im]
        for thisComponent in wm_testComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        wm_testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "wm_test"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = wm_testClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=wm_testClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if prac != 1:
                if list_no != expInfo["list"]:
                    continueRoutine = False
            
            if not recall_started:
                wm_recall_text.text = '?'
            
            keys = event.getKeys()
            if len(keys):
                key = keys[0]
                if key in validkeys:
                    recall_started = True
                    if wm_recall_text.text == '?':
                        wm_recall_text.text = ''
                    wm_recall_text.text = wm_recall_text.text + key.upper()
                elif key == 'return':
                    continueRoutine = False
                elif key == 'backspace':
                    wm_recall_text.text = wm_recall_text.text[:-1]
            
            if timer_wm.getTime() > 15:
                continueRoutine = False
            
            
            # *wm_recall_text* updates
            if wm_recall_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wm_recall_text.frameNStart = frameN  # exact frame index
                wm_recall_text.tStart = t  # local t and not account for scr refresh
                wm_recall_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_recall_text, 'tStartRefresh')  # time at next scr refresh
                wm_recall_text.setAutoDraw(True)
            if wm_recall_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > wm_recall_text.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    wm_recall_text.tStop = t  # not accounting for scr refresh
                    wm_recall_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(wm_recall_text, 'tStopRefresh')  # time at next scr refresh
                    wm_recall_text.setAutoDraw(False)
            
            # *wm_test_im* updates
            if wm_test_im.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                wm_test_im.frameNStart = frameN  # exact frame index
                wm_test_im.tStart = t  # local t and not account for scr refresh
                wm_test_im.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_test_im, 'tStartRefresh')  # time at next scr refresh
                wm_test_im.setAutoDraw(True)
            if wm_test_im.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > wm_test_im.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    wm_test_im.tStop = t  # not accounting for scr refresh
                    wm_test_im.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(wm_test_im, 'tStopRefresh')  # time at next scr refresh
                    wm_test_im.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in wm_testComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "wm_test"-------
        for thisComponent in wm_testComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        all_recalled.append(wm_recall_text.text)
        all_recall_rt.append(timer_wm.getTime())
        wm_test_loop.addData('wm_recall_text.started', wm_recall_text.tStartRefresh)
        wm_test_loop.addData('wm_recall_text.stopped', wm_recall_text.tStopRefresh)
        wm_test_loop.addData('wm_test_im.started', wm_test_im.tStartRefresh)
        wm_test_loop.addData('wm_test_im.stopped', wm_test_im.tStopRefresh)
        
        # ------Prepare to start Routine "wm_recall_isi"-------
        continueRoutine = True
        routineTimer.add(0.200000)
        # update component parameters for each repeat
        # keep track of which components have finished
        wm_recall_isiComponents = [wm_isi_blank]
        for thisComponent in wm_recall_isiComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        wm_recall_isiClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "wm_recall_isi"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = wm_recall_isiClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=wm_recall_isiClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if prac != 1:
                if list_no != expInfo["list"]:
                    continueRoutine = False
            
            # *wm_isi_blank* updates
            if wm_isi_blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wm_isi_blank.frameNStart = frameN  # exact frame index
                wm_isi_blank.tStart = t  # local t and not account for scr refresh
                wm_isi_blank.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_isi_blank, 'tStartRefresh')  # time at next scr refresh
                wm_isi_blank.setAutoDraw(True)
            if wm_isi_blank.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > wm_isi_blank.tStartRefresh + .2-frameTolerance:
                    # keep track of stop time/frame for later
                    wm_isi_blank.tStop = t  # not accounting for scr refresh
                    wm_isi_blank.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(wm_isi_blank, 'tStopRefresh')  # time at next scr refresh
                    wm_isi_blank.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in wm_recall_isiComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "wm_recall_isi"-------
        for thisComponent in wm_recall_isiComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        wm_test_loop.addData('wm_isi_blank.started', wm_isi_blank.tStartRefresh)
        wm_test_loop.addData('wm_isi_blank.stopped', wm_isi_blank.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 4 repeats of 'wm_test_loop'
    
    
    # ------Prepare to start Routine "write"-------
    continueRoutine = True
    routineTimer.add(0.300000)
    # update component parameters for each repeat
    
    for i in range(4):
        thisExp.addData("wm_recalled"+str(i+1), all_recalled[i])
        thisExp.addData("wm_recall_rt"+str(i+1), all_recall_rt[i])
        thisExp.addData("wm_probed"+str(i+1), testOrder[i])
        thisExp.addData("wm_recall_acc"+str(i+1), testWords[testOrder[i]] == all_recalled[i])
    
    # keep track of which components have finished
    writeComponents = [text_11]
    for thisComponent in writeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    writeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "write"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = writeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=writeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if prac != 1:
            if list_no != expInfo["list"]:
                continueRoutine = False
        
        
        # *text_11* updates
        if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_11.frameNStart = frameN  # exact frame index
            text_11.tStart = t  # local t and not account for scr refresh
            text_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
            text_11.setAutoDraw(True)
        if text_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_11.tStartRefresh + .3-frameTolerance:
                # keep track of stop time/frame for later
                text_11.tStop = t  # not accounting for scr refresh
                text_11.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_11, 'tStopRefresh')  # time at next scr refresh
                text_11.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in writeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "write"-------
    for thisComponent in writeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    wm_trial_loop.addData('text_11.started', text_11.tStartRefresh)
    wm_trial_loop.addData('text_11.stopped', text_11.tStopRefresh)
    
    # ------Prepare to start Routine "search_reminder"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    search_reminderComponents = [text_16]
    for thisComponent in search_reminderComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    search_reminderClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "search_reminder"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = search_reminderClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=search_reminderClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if prac != 1:
            if list_no != expInfo["list"]:
                continueRoutine = False
        
        if search_resp.keys == '0' or search_resp.keys == '1':
            continueRoutine = False
        
        # *text_16* updates
        if text_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_16.frameNStart = frameN  # exact frame index
            text_16.tStart = t  # local t and not account for scr refresh
            text_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_16, 'tStartRefresh')  # time at next scr refresh
            text_16.setAutoDraw(True)
        if text_16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_16.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_16.tStop = t  # not accounting for scr refresh
                text_16.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_16, 'tStopRefresh')  # time at next scr refresh
                text_16.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in search_reminderComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "search_reminder"-------
    for thisComponent in search_reminderComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    wm_trial_loop.addData('text_16.started', text_16.tStartRefresh)
    wm_trial_loop.addData('text_16.stopped', text_16.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'wm_trial_loop'


# ------Prepare to start Routine "end_exp"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
end_expComponents = [end_exp_text]
for thisComponent in end_expComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
end_expClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end_exp"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = end_expClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=end_expClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_exp_text* updates
    if end_exp_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_exp_text.frameNStart = frameN  # exact frame index
        end_exp_text.tStart = t  # local t and not account for scr refresh
        end_exp_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_exp_text, 'tStartRefresh')  # time at next scr refresh
        end_exp_text.setAutoDraw(True)
    if end_exp_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_exp_text.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            end_exp_text.tStop = t  # not accounting for scr refresh
            end_exp_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_exp_text, 'tStopRefresh')  # time at next scr refresh
            end_exp_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_expComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end_exp"-------
for thisComponent in end_expComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('end_exp_text.started', end_exp_text.tStartRefresh)
thisExp.addData('end_exp_text.stopped', end_exp_text.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
