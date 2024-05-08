/******************* 
 * Proactive2 Test *
 *******************/

import { PsychoJS } from './lib/core-2020.1.js';
import * as core from './lib/core-2020.1.js';
import { TrialHandler } from './lib/data-2020.1.js';
import { Scheduler } from './lib/util-2020.1.js';
import * as util from './lib/util-2020.1.js';
import * as visual from './lib/visual-2020.1.js';
import * as sound from './lib/sound-2020.1.js';

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'norm',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'proactive2';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'please enter your date of birth (dd/mm/yyyy)': ''};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(consentRoutineBegin());
flowScheduler.add(consentRoutineEachFrame());
flowScheduler.add(consentRoutineEnd());
flowScheduler.add(welcomeRoutineBegin());
flowScheduler.add(welcomeRoutineEachFrame());
flowScheduler.add(welcomeRoutineEnd());
flowScheduler.add(learn_instr1RoutineBegin());
flowScheduler.add(learn_instr1RoutineEachFrame());
flowScheduler.add(learn_instr1RoutineEnd());
flowScheduler.add(learn_instr2RoutineBegin());
flowScheduler.add(learn_instr2RoutineEachFrame());
flowScheduler.add(learn_instr2RoutineEnd());
flowScheduler.add(learn_instr3RoutineBegin());
flowScheduler.add(learn_instr3RoutineEachFrame());
flowScheduler.add(learn_instr3RoutineEnd());
flowScheduler.add(learn_instr4RoutineBegin());
flowScheduler.add(learn_instr4RoutineEachFrame());
flowScheduler.add(learn_instr4RoutineEnd());
const example_recallLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(example_recallLoopBegin, example_recallLoopScheduler);
flowScheduler.add(example_recallLoopScheduler);
flowScheduler.add(example_recallLoopEnd);
flowScheduler.add(learn_instr5RoutineBegin());
flowScheduler.add(learn_instr5RoutineEachFrame());
flowScheduler.add(learn_instr5RoutineEnd());
const prac_learn_study_loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(prac_learn_study_loopLoopBegin, prac_learn_study_loopLoopScheduler);
flowScheduler.add(prac_learn_study_loopLoopScheduler);
flowScheduler.add(prac_learn_study_loopLoopEnd);
flowScheduler.add(learn_test_instrRoutineBegin());
flowScheduler.add(learn_test_instrRoutineEachFrame());
flowScheduler.add(learn_test_instrRoutineEnd());
const prac_learn_test_loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(prac_learn_test_loopLoopBegin, prac_learn_test_loopLoopScheduler);
flowScheduler.add(prac_learn_test_loopLoopScheduler);
flowScheduler.add(prac_learn_test_loopLoopEnd);
flowScheduler.add(learn_end_pracRoutineBegin());
flowScheduler.add(learn_end_pracRoutineEachFrame());
flowScheduler.add(learn_end_pracRoutineEnd());
const learn_blocks_loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(learn_blocks_loopLoopBegin, learn_blocks_loopLoopScheduler);
flowScheduler.add(learn_blocks_loopLoopScheduler);
flowScheduler.add(learn_blocks_loopLoopEnd);
flowScheduler.add(learn_final_instrRoutineBegin());
flowScheduler.add(learn_final_instrRoutineEachFrame());
flowScheduler.add(learn_final_instrRoutineEnd());
const final_learn_testLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(final_learn_testLoopBegin, final_learn_testLoopScheduler);
flowScheduler.add(final_learn_testLoopScheduler);
flowScheduler.add(final_learn_testLoopEnd);
flowScheduler.add(end_learnRoutineBegin());
flowScheduler.add(end_learnRoutineEachFrame());
flowScheduler.add(end_learnRoutineEnd());
flowScheduler.add(wm_instrRoutineBegin());
flowScheduler.add(wm_instrRoutineEachFrame());
flowScheduler.add(wm_instrRoutineEnd());
flowScheduler.add(wm_instr2RoutineBegin());
flowScheduler.add(wm_instr2RoutineEachFrame());
flowScheduler.add(wm_instr2RoutineEnd());
flowScheduler.add(search_instrRoutineBegin());
flowScheduler.add(search_instrRoutineEachFrame());
flowScheduler.add(search_instrRoutineEnd());
flowScheduler.add(search_instr2RoutineBegin());
flowScheduler.add(search_instr2RoutineEachFrame());
flowScheduler.add(search_instr2RoutineEnd());
flowScheduler.add(search_instr3RoutineBegin());
flowScheduler.add(search_instr3RoutineEachFrame());
flowScheduler.add(search_instr3RoutineEnd());
const search_loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(search_loopLoopBegin, search_loopLoopScheduler);
flowScheduler.add(search_loopLoopScheduler);
flowScheduler.add(search_loopLoopEnd);
flowScheduler.add(wm_instr3RoutineBegin());
flowScheduler.add(wm_instr3RoutineEachFrame());
flowScheduler.add(wm_instr3RoutineEnd());
const prac_wm_trial_loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(prac_wm_trial_loopLoopBegin, prac_wm_trial_loopLoopScheduler);
flowScheduler.add(prac_wm_trial_loopLoopScheduler);
flowScheduler.add(prac_wm_trial_loopLoopEnd);
flowScheduler.add(end_wm_pracRoutineBegin());
flowScheduler.add(end_wm_pracRoutineEachFrame());
flowScheduler.add(end_wm_pracRoutineEnd());
const wm_trial_loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(wm_trial_loopLoopBegin, wm_trial_loopLoopScheduler);
flowScheduler.add(wm_trial_loopLoopScheduler);
flowScheduler.add(wm_trial_loopLoopEnd);
flowScheduler.add(end_expRoutineBegin());
flowScheduler.add(end_expRoutineEachFrame());
flowScheduler.add(end_expRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.1.2';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  psychoJS.setRedirectUrls('https://app.prolific.co/submissions/complete?cc=5B5DB3C7', '');

  return Scheduler.Event.NEXT;
}


var consentClock;
var consent_text;
var consent_key;
var welcomeClock;
var welcome_text;
var welcome_adv;
var list;
var skip_learn;
var continue_learning;
var im_size;
var xpos;
var ypos;
var xdisp;
var ydisp;
var learn_instr1Clock;
var part1;
var learn_intsr_text;
var learn_instr_adv;
var ex_word;
var ex_im;
var learn_instr2Clock;
var text;
var key_resp;
var learn_instr3Clock;
var text_2;
var key_resp_2;
var learn_instr4Clock;
var text_3;
var key_resp_3;
var learn_testClock;
var timer;
var test_image;
var recall_text;
var learn_feedbackClock;
var feedback_text;
var feed_image;
var post_fb_int;
var restudy_text;
var learn_instr5Clock;
var text_4;
var key_resp_4;
var learn_studyClock;
var study_text;
var study_image;
var learn_test_instrClock;
var learn_test_instr_text;
var learn_end_pracClock;
var text_5;
var key_resp_6;
var set_counterClock;
var begin_blockClock;
var text_10;
var key_resp_12;
var next_instrClock;
var next_instr_text;
var key_resp_13;
var break_learnClock;
var learn_final_instrClock;
var learn_final_text;
var key_resp_7;
var end_learnClock;
var text_8;
var key_resp_10;
var wm_instrClock;
var part2;
var wm_text;
var key_resp_5;
var wm_instr2Clock;
var text_6;
var key_resp_8;
var search_instrClock;
var top_text;
var mid_text;
var bottom_text;
var t_im;
var b_im;
var l_im;
var r_im;
var key_resp_11;
var search_instr2Clock;
var sim1_ex;
var sim2_ex;
var sim3_ex;
var sim4_ex;
var sim5_ex;
var sim6_ex;
var sim7_ex;
var sim8_ex;
var text_12;
var key_resp_14;
var text_15;
var search_instr3Clock;
var text_13;
var key_resp_15;
var searchClock;
var tars;
var nontars;
var im_dir;
var sim1;
var sim2;
var sim3;
var sim4;
var sim5;
var sim6;
var sim7;
var sim8;
var search_resp;
var search_fix;
var search_isiClock;
var text_9;
var wm_instr3Clock;
var text_14;
var key_resp_16;
var STClock;
var st_text;
var st_key;
var wm_studyClock;
var wm_study_im1;
var wm_study_tx1;
var wm_study_im2;
var wm_study_tx2;
var wm_study_im3;
var wm_study_tx3;
var wm_study_im4;
var wm_study_tx4;
var wm_testClock;
var timer_wm;
var wm_recall_text;
var wm_test_im;
var wm_recall_isiClock;
var wm_isi_blank;
var writeClock;
var text_11;
var search_reminderClock;
var text_16;
var end_wm_pracClock;
var text_7;
var key_resp_9;
var end_expClock;
var end_exp_text;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "consent"
  consentClock = new util.Clock();
  consent_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'consent_text',
    text: 'Thank you for volunteering to take part in this study conducted by researchers at the Department of Psychology at the University of Toronto. In this study we are looking at memory for random pairs of images and words. The images are drawings of everyday objects and the words are nouns with 4-6 letters. The study is split into two parts: The first part assesses learning of image-word pairs and the second part looks at short-term memory. In both parts your memory will be tested by presenting an image and asking you to recall the associated word by typing on the keyboard.\n\nThe data we collect for this study concerns the accuracy and speed of memory recall. These data will be stored in an anonymised format (using the ID assigned to you by prolific) and may be shared with other researchers via public data repositories (such as the open science framework; www.osf.io). You may exit the study at any time without penalty by pressing the escape key.\n\nIf you consent to take part in this study, please press ‘Y’\n\nIf you do not consent to take part, please press the escape key and close this window',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.07,  wrapWidth: 1.8, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  consent_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "welcome"
  welcomeClock = new util.Clock();
  welcome_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'welcome_text',
    text: 'This experiment is split into two sections.\n\nWe will let you know what you need to do at the beginning of each section.\n\nPress SPACE to start.\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: 1.6, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  welcome_adv = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  //var continue_learning, list, skip_learn;
  list = (Math.floor((Math.random() * ((6 - 1) + 1))) + 1);
  expInfo["list"] = list;
  skip_learn = 0;
  continue_learning = true;
  
  im_size = [100/1920, 100/1080];
  
  xpos = 400/1920;
  ypos=400/1080;
  
  xdisp = .03;
  ydisp = im_size[1];
  // Initialize components for Routine "learn_instr1"
  learn_instr1Clock = new util.Clock();
  part1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'part1',
    text: 'SECTION 1',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  learn_intsr_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'learn_intsr_text',
    text: 'In this section of the experiment we will present you with pairs of images and words to learn. An example pair is shown above. Press SPACE to continue.\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.7)], height: 0.1,  wrapWidth: 1.6, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  learn_instr_adv = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  ex_word = new visual.TextStim({
    win: psychoJS.window,
    name: 'ex_word',
    text: 'TOUGH',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.204)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  ex_im = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ex_im', units : undefined, 
    image : 'stimuli/images/PICTURE_747.png', mask : undefined,
    ori : 0, pos : [0, 0.204], size : [(600 / 1920), (600 / 1080)],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  // Initialize components for Routine "learn_instr2"
  learn_instr2Clock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'There are 30 pairs to learn and we will present them in groups of 10.\n\nThe 10 pairs will be presented in sequences and after they have been presented you will be asked to recall the word associated with each image.\n\nPress SPACE to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: 1.6, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "learn_instr3"
  learn_instr3Clock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: "During recall you will see an image you previously saw. You will have up to 15 seconds to recall the word associated with the image by typing it on the keyboard. Once the 15 seconds are up the task will move on automatically.\n\nWhen you have finished typing press the enter (or return) key to submit. If you can't remember the word you can press enter to pass. You can also delete mistakes using the backspace key.\n\nPress SPACE to continue.",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: 1.6, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "learn_instr4"
  learn_instr4Clock = new util.Clock();
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: 'You will get feedback on whether the word you recall is right or wrong. The word will turn green if it is right. If it is wrong the word you typed will turn red then you will see the correct word with the image again.\n\nOn the next screen you will see the image you saw before. Please type in the word that you saw with it and press enter (or return) to submit.\n\nPress SPACE to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: 1.6, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "learn_test"
  learn_testClock = new util.Clock();
  timer = new util.Clock()
  test_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'test_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0.204], size : [(600 / 1920), (600 / 1080)],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  recall_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'recall_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.204)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "learn_feedback"
  learn_feedbackClock = new util.Clock();
  feedback_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.204)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  feed_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'feed_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0.204], size : [(600 / 1920), (600 / 1080)],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  post_fb_int = new visual.TextStim({
    win: psychoJS.window,
    name: 'post_fb_int',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  restudy_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'restudy_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.204)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "learn_instr5"
  learn_instr5Clock = new util.Clock();
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: 'Great! You will now have a chance to practice this task. During practice you will see 5 pairs to remember and then recall.\n\nPress SPACE to start.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: 1.6, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "learn_study"
  learn_studyClock = new util.Clock();
  study_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'study_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.204)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  study_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'study_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0.204], size : [(600 / 1920), (600 / 1080)],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "learn_test_instr"
  learn_test_instrClock = new util.Clock();
  learn_test_instr_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'learn_test_instr_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "learn_test"
  learn_testClock = new util.Clock();
  timer = new util.Clock()
  test_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'test_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0.204], size : [(600 / 1920), (600 / 1080)],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  recall_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'recall_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.204)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "learn_feedback"
  learn_feedbackClock = new util.Clock();
  feedback_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.204)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  feed_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'feed_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0.204], size : [(600 / 1920), (600 / 1080)],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  post_fb_int = new visual.TextStim({
    win: psychoJS.window,
    name: 'post_fb_int',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  restudy_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'restudy_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.204)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "learn_end_prac"
  learn_end_pracClock = new util.Clock();
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: "End of practice.\n\nWe will now go though all of the pairs in groups of 10. We'll keep going until you get 80% correct or until you have seen all of the pairs three times.\n\nPress SPACE when you are ready to start the main task.",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: 1.6, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_6 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "set_counter"
  set_counterClock = new util.Clock();
  // Initialize components for Routine "begin_block"
  begin_blockClock = new util.Clock();
  text_10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_10',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: 1.6, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp_12 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "learn_study"
  learn_studyClock = new util.Clock();
  study_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'study_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.204)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  study_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'study_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0.204], size : [(600 / 1920), (600 / 1080)],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "learn_test_instr"
  learn_test_instrClock = new util.Clock();
  learn_test_instr_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'learn_test_instr_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "learn_test"
  learn_testClock = new util.Clock();
  timer = new util.Clock()
  test_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'test_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0.204], size : [(600 / 1920), (600 / 1080)],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  recall_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'recall_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.204)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "learn_feedback"
  learn_feedbackClock = new util.Clock();
  feedback_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.204)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  feed_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'feed_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0.204], size : [(600 / 1920), (600 / 1080)],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  post_fb_int = new visual.TextStim({
    win: psychoJS.window,
    name: 'post_fb_int',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  restudy_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'restudy_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.204)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "next_instr"
  next_instrClock = new util.Clock();
  next_instr_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'next_instr_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: 1.6, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp_13 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "break_learn"
  break_learnClock = new util.Clock();
  // Initialize components for Routine "learn_final_instr"
  learn_final_instrClock = new util.Clock();
  learn_final_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'learn_final_text',
    text: 'Now we will ask you about all of the 30 pairs you have been learning.\n\nEach image will be presented and your task is to recall the word associated with the image. Remember, you have 10 seconds to type your answer and press enter (or return) to submit.\n\nPress SPACE to start.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: 1.6, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_7 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "learn_test"
  learn_testClock = new util.Clock();
  timer = new util.Clock()
  test_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'test_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0.204], size : [(600 / 1920), (600 / 1080)],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  recall_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'recall_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.204)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "learn_feedback"
  learn_feedbackClock = new util.Clock();
  feedback_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.204)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  feed_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'feed_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0.204], size : [(600 / 1920), (600 / 1080)],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  post_fb_int = new visual.TextStim({
    win: psychoJS.window,
    name: 'post_fb_int',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  restudy_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'restudy_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.204)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "end_learn"
  end_learnClock = new util.Clock();
  text_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_8',
    text: 'That is the end of the first section.\n\nPress SPACE to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: 1.6, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_10 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "wm_instr"
  wm_instrClock = new util.Clock();
  part2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'part2',
    text: 'SECTION 2',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  wm_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'wm_text',
    text: 'The task in this section also uses pairs of images and words but is different from the task you did in section 1. In this section we are looking at short-term memory for pairs.\n\nIn this task you will be presented with sequences of 4 image-word pairs to hold in mind over a 2 second interval. During this 2 second interval you will be asked to perform another task (more on this soon).\n\nPress SPACE to continue.\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: 1.6, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "wm_instr2"
  wm_instr2Clock = new util.Clock();
  text_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_6',
    text: "After the 2 second interval you will be asked to recall the word associated with each image by typing it on the keyboard then pressing enter (or return) to submit. There won't be any feedback in this section.\n\nNext we will tell you more about the task your are asked to do during the 2 second interval.\n\nPress SPACE to start.",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: 1.6, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_8 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "search_instr"
  search_instrClock = new util.Clock();
  top_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'top_text',
    text: 'During the 2 second interval between seeing the pairs you need to remember and recalling them there is a search task. In this task you will see square symbols with open sides. All but one of these symbols will have an open side at the top or bottom.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.6], height: 0.08,  wrapWidth: 1.6, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  mid_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'mid_text',
    text: "The task is to find the one symbol that is open at the left or right. When you have found it press '1' if the target square is open on the left or '0' for right.",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: 1.6, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  bottom_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'bottom_text',
    text: "The next screen shows an example of a search screen where the correct answer is 'right' (the '0' key). \n\nPress SPACE to continue",
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.5)], height: 0.08,  wrapWidth: 1.6, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  t_im = new visual.ImageStim({
    win : psychoJS.window,
    name : 't_im', units : undefined, 
    image : 'stimuli/search/t.png', mask : undefined,
    ori : 0, pos : [(- 0.2), 0.25], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  b_im = new visual.ImageStim({
    win : psychoJS.window,
    name : 'b_im', units : undefined, 
    image : 'stimuli/search/b.png', mask : undefined,
    ori : 0, pos : [0.2, 0.25], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  l_im = new visual.ImageStim({
    win : psychoJS.window,
    name : 'l_im', units : undefined, 
    image : 'stimuli/search/l.png', mask : undefined,
    ori : 0, pos : [(- 0.2), (- 0.25)], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  r_im = new visual.ImageStim({
    win : psychoJS.window,
    name : 'r_im', units : undefined, 
    image : 'stimuli/search/r.png', mask : undefined,
    ori : 0, pos : [0.2, (- 0.25)], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -6.0 
  });
  key_resp_11 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "search_instr2"
  search_instr2Clock = new util.Clock();
  sim1_ex = new visual.ImageStim({
    win : psychoJS.window,
    name : 'sim1_ex', units : undefined, 
    image : 'stimuli/search/t.png', mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  sim2_ex = new visual.ImageStim({
    win : psychoJS.window,
    name : 'sim2_ex', units : undefined, 
    image : 'stimuli/search/b.png', mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  sim3_ex = new visual.ImageStim({
    win : psychoJS.window,
    name : 'sim3_ex', units : undefined, 
    image : 'stimuli/search/b.png', mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  sim4_ex = new visual.ImageStim({
    win : psychoJS.window,
    name : 'sim4_ex', units : undefined, 
    image : 'stimuli/search/t.png', mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  sim5_ex = new visual.ImageStim({
    win : psychoJS.window,
    name : 'sim5_ex', units : undefined, 
    image : 'stimuli/search/t.png', mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  sim6_ex = new visual.ImageStim({
    win : psychoJS.window,
    name : 'sim6_ex', units : undefined, 
    image : 'stimuli/search/b.png', mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -6.0 
  });
  sim7_ex = new visual.ImageStim({
    win : psychoJS.window,
    name : 'sim7_ex', units : undefined, 
    image : 'stimuli/search/t.png', mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -7.0 
  });
  sim8_ex = new visual.ImageStim({
    win : psychoJS.window,
    name : 'sim8_ex', units : undefined, 
    image : 'stimuli/search/r.png', mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -8.0 
  });
  text_12 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_12',
    text: "In this case the target is in the bottom left of the screen and is open on the right (so the correct response is '0'). In the main task the symbols will only be presented for 2 seconds. Press SPACE to continue\n",
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.75)], height: 0.08,  wrapWidth: 1.6, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -9.0 
  });
  
  key_resp_14 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_15 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_15',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -11.0 
  });
  
  // Initialize components for Routine "search_instr3"
  search_instr3Clock = new util.Clock();
  text_13 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_13',
    text: "Now we will practice this task by itself. Each screen will only appear for 2 seconds so try to search for the target (square open at the left or right) and respond as quickly and accurately as possible.\n\nRemember, press '1' if the target square is open on the left or '0' for right.\n\nRest your fingers over these keys and press either to begin",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: 1.6, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_15 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "search"
  searchClock = new util.Clock();
  tars = ["l", "r"];
  nontars = ["b", "t"];
  im_dir = "stimuli/search/";
  
  sim1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'sim1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  sim2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'sim2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  sim3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'sim3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  sim4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'sim4', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  sim5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'sim5', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  sim6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'sim6', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -6.0 
  });
  sim7 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'sim7', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -7.0 
  });
  sim8 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'sim8', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -8.0 
  });
  search_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  search_fix = new visual.TextStim({
    win: psychoJS.window,
    name: 'search_fix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -10.0 
  });
  
  // Initialize components for Routine "search_isi"
  search_isiClock = new util.Clock();
  text_9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_9',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "wm_instr3"
  wm_instr3Clock = new util.Clock();
  text_14 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_14',
    text: 'Well done!\n\nNow we will practice both tasks together. Remember, you will see 4 image-word pairs to remember. Then during the 2 second interval you will have to search for the target square and indicate if it is open on the left or right. After that you will be asked to type the word associated with each image you studied.\n\nThere will be 3 example sequences to practice the tasks together.\n\nPress SPACE to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: 1.6, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_16 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ST"
  STClock = new util.Clock();
  st_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'st_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: 1.6, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  st_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "wm_study"
  wm_studyClock = new util.Clock();
  wm_study_im1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'wm_study_im1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0.204], size : [(600 / 1920), (600 / 1080)],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  wm_study_tx1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'wm_study_tx1',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.204)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  wm_study_im2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'wm_study_im2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0.204], size : [(600 / 1920), (600 / 1080)],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  wm_study_tx2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'wm_study_tx2',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.204)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  wm_study_im3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'wm_study_im3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0.204], size : [(600 / 1920), (600 / 1080)],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  wm_study_tx3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'wm_study_tx3',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.204)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -6.0 
  });
  
  wm_study_im4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'wm_study_im4', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0.204], size : [(600 / 1920), (600 / 1080)],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -7.0 
  });
  wm_study_tx4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'wm_study_tx4',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.204)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -8.0 
  });
  
  // Initialize components for Routine "search"
  searchClock = new util.Clock();
  tars = ["l", "r"];
  nontars = ["b", "t"];
  im_dir = "stimuli/search/";
  
  sim1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'sim1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  sim2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'sim2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  sim3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'sim3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  sim4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'sim4', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  sim5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'sim5', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  sim6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'sim6', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -6.0 
  });
  sim7 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'sim7', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -7.0 
  });
  sim8 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'sim8', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -8.0 
  });
  search_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  search_fix = new visual.TextStim({
    win: psychoJS.window,
    name: 'search_fix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -10.0 
  });
  
  // Initialize components for Routine "wm_test"
  wm_testClock = new util.Clock();
  var testImage;
  timer_wm = new util.Clock()
  wm_recall_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'wm_recall_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.204)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  wm_test_im = new visual.ImageStim({
    win : psychoJS.window,
    name : 'wm_test_im', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0.204], size : [(600 / 1920), (600 / 1080)],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "wm_recall_isi"
  wm_recall_isiClock = new util.Clock();
  wm_isi_blank = new visual.TextStim({
    win: psychoJS.window,
    name: 'wm_isi_blank',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "write"
  writeClock = new util.Clock();
  text_11 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_11',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "search_reminder"
  search_reminderClock = new util.Clock();
  text_16 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_16',
    text: "Remember to respond to the search task! \n\nPress '1' if the target square is open on the left or '0' for right",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: 1.6, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "end_wm_prac"
  end_wm_pracClock = new util.Clock();
  text_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_7',
    text: 'End of practice.\n\nPress SPACE to start the main task.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: 1.6, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_9 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ST"
  STClock = new util.Clock();
  st_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'st_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: 1.6, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  st_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "wm_study"
  wm_studyClock = new util.Clock();
  wm_study_im1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'wm_study_im1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0.204], size : [(600 / 1920), (600 / 1080)],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  wm_study_tx1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'wm_study_tx1',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.204)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  wm_study_im2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'wm_study_im2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0.204], size : [(600 / 1920), (600 / 1080)],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  wm_study_tx2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'wm_study_tx2',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.204)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  wm_study_im3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'wm_study_im3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0.204], size : [(600 / 1920), (600 / 1080)],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  wm_study_tx3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'wm_study_tx3',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.204)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -6.0 
  });
  
  wm_study_im4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'wm_study_im4', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0.204], size : [(600 / 1920), (600 / 1080)],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -7.0 
  });
  wm_study_tx4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'wm_study_tx4',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.204)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -8.0 
  });
  
  // Initialize components for Routine "search"
  searchClock = new util.Clock();
  tars = ["l", "r"];
  nontars = ["b", "t"];
  im_dir = "stimuli/search/";
  
  sim1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'sim1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  sim2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'sim2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  sim3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'sim3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  sim4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'sim4', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  sim5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'sim5', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  sim6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'sim6', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -6.0 
  });
  sim7 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'sim7', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -7.0 
  });
  sim8 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'sim8', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -8.0 
  });
  search_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  search_fix = new visual.TextStim({
    win: psychoJS.window,
    name: 'search_fix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -10.0 
  });
  
  // Initialize components for Routine "wm_test"
  wm_testClock = new util.Clock();
  var testImage;
  timer_wm = new util.Clock()
  wm_recall_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'wm_recall_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.204)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  wm_test_im = new visual.ImageStim({
    win : psychoJS.window,
    name : 'wm_test_im', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0.204], size : [(600 / 1920), (600 / 1080)],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "wm_recall_isi"
  wm_recall_isiClock = new util.Clock();
  wm_isi_blank = new visual.TextStim({
    win: psychoJS.window,
    name: 'wm_isi_blank',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "write"
  writeClock = new util.Clock();
  text_11 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_11',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "search_reminder"
  search_reminderClock = new util.Clock();
  text_16 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_16',
    text: "Remember to respond to the search task! \n\nPress '1' if the target square is open on the left or '0' for right",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: 1.6, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "end_exp"
  end_expClock = new util.Clock();
  end_exp_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'end_exp_text',
    text: "That's the end of the experiment!\n\nThank you for taking part.\n\nPlease wait a moment for the data to be saved...",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var _consent_key_allKeys;
var consentComponents;
function consentRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'consent'-------
    t = 0;
    consentClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    consent_key.keys = undefined;
    consent_key.rt = undefined;
    _consent_key_allKeys = [];
    // keep track of which components have finished
    consentComponents = [];
    consentComponents.push(consent_text);
    consentComponents.push(consent_key);
    
    for (const thisComponent of consentComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var continueRoutine;
function consentRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'consent'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = consentClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *consent_text* updates
    if (t >= 0.0 && consent_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      consent_text.tStart = t;  // (not accounting for frame time here)
      consent_text.frameNStart = frameN;  // exact frame index
      
      consent_text.setAutoDraw(true);
    }

    
    // *consent_key* updates
    if (t >= 0.0 && consent_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      consent_key.tStart = t;  // (not accounting for frame time here)
      consent_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { consent_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { consent_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { consent_key.clearEvents(); });
    }

    if (consent_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = consent_key.getKeys({keyList: ['y'], waitRelease: false});
      _consent_key_allKeys = _consent_key_allKeys.concat(theseKeys);
      if (_consent_key_allKeys.length > 0) {
        consent_key.keys = _consent_key_allKeys[_consent_key_allKeys.length - 1].name;  // just the last key pressed
        consent_key.rt = _consent_key_allKeys[_consent_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of consentComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function consentRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'consent'-------
    for (const thisComponent of consentComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('consent_key.keys', consent_key.keys);
    if (typeof consent_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('consent_key.rt', consent_key.rt);
        routineTimer.reset();
        }
    
    consent_key.stop();
    // the Routine "consent" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _welcome_adv_allKeys;
var welcomeComponents;
function welcomeRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'welcome'-------
    t = 0;
    welcomeClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    welcome_adv.keys = undefined;
    welcome_adv.rt = undefined;
    _welcome_adv_allKeys = [];
    // keep track of which components have finished
    welcomeComponents = [];
    welcomeComponents.push(welcome_text);
    welcomeComponents.push(welcome_adv);
    
    for (const thisComponent of welcomeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function welcomeRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'welcome'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = welcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *welcome_text* updates
    if (t >= 0.0 && welcome_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcome_text.tStart = t;  // (not accounting for frame time here)
      welcome_text.frameNStart = frameN;  // exact frame index
      
      welcome_text.setAutoDraw(true);
    }

    
    // *welcome_adv* updates
    if (t >= 0.0 && welcome_adv.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcome_adv.tStart = t;  // (not accounting for frame time here)
      welcome_adv.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { welcome_adv.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { welcome_adv.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { welcome_adv.clearEvents(); });
    }

    if (welcome_adv.status === PsychoJS.Status.STARTED) {
      let theseKeys = welcome_adv.getKeys({keyList: ['space'], waitRelease: false});
      _welcome_adv_allKeys = _welcome_adv_allKeys.concat(theseKeys);
      if (_welcome_adv_allKeys.length > 0) {
        welcome_adv.keys = _welcome_adv_allKeys[_welcome_adv_allKeys.length - 1].name;  // just the last key pressed
        welcome_adv.rt = _welcome_adv_allKeys[_welcome_adv_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of welcomeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function welcomeRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'welcome'-------
    for (const thisComponent of welcomeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _learn_instr_adv_allKeys;
var learn_instr1Components;
function learn_instr1RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'learn_instr1'-------
    t = 0;
    learn_instr1Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    learn_instr_adv.keys = undefined;
    learn_instr_adv.rt = undefined;
    _learn_instr_adv_allKeys = [];
    // keep track of which components have finished
    learn_instr1Components = [];
    learn_instr1Components.push(part1);
    learn_instr1Components.push(learn_intsr_text);
    learn_instr1Components.push(learn_instr_adv);
    learn_instr1Components.push(ex_word);
    learn_instr1Components.push(ex_im);
    
    for (const thisComponent of learn_instr1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var frameRemains;
function learn_instr1RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'learn_instr1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = learn_instr1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *part1* updates
    if (t >= 0.0 && part1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      part1.tStart = t;  // (not accounting for frame time here)
      part1.frameNStart = frameN;  // exact frame index
      
      part1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (part1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      part1.setAutoDraw(false);
    }
    
    // *learn_intsr_text* updates
    if (t >= 2 && learn_intsr_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      learn_intsr_text.tStart = t;  // (not accounting for frame time here)
      learn_intsr_text.frameNStart = frameN;  // exact frame index
      
      learn_intsr_text.setAutoDraw(true);
    }

    
    // *learn_instr_adv* updates
    if (t >= 2 && learn_instr_adv.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      learn_instr_adv.tStart = t;  // (not accounting for frame time here)
      learn_instr_adv.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { learn_instr_adv.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { learn_instr_adv.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { learn_instr_adv.clearEvents(); });
    }

    if (learn_instr_adv.status === PsychoJS.Status.STARTED) {
      let theseKeys = learn_instr_adv.getKeys({keyList: ['space'], waitRelease: false});
      _learn_instr_adv_allKeys = _learn_instr_adv_allKeys.concat(theseKeys);
      if (_learn_instr_adv_allKeys.length > 0) {
        learn_instr_adv.keys = _learn_instr_adv_allKeys[_learn_instr_adv_allKeys.length - 1].name;  // just the last key pressed
        learn_instr_adv.rt = _learn_instr_adv_allKeys[_learn_instr_adv_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *ex_word* updates
    if (t >= 2 && ex_word.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ex_word.tStart = t;  // (not accounting for frame time here)
      ex_word.frameNStart = frameN;  // exact frame index
      
      ex_word.setAutoDraw(true);
    }

    
    // *ex_im* updates
    if (t >= 2 && ex_im.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ex_im.tStart = t;  // (not accounting for frame time here)
      ex_im.frameNStart = frameN;  // exact frame index
      
      ex_im.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of learn_instr1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function learn_instr1RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'learn_instr1'-------
    for (const thisComponent of learn_instr1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "learn_instr1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_allKeys;
var learn_instr2Components;
function learn_instr2RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'learn_instr2'-------
    t = 0;
    learn_instr2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    learn_instr2Components = [];
    learn_instr2Components.push(text);
    learn_instr2Components.push(key_resp);
    
    for (const thisComponent of learn_instr2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function learn_instr2RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'learn_instr2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = learn_instr2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of learn_instr2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function learn_instr2RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'learn_instr2'-------
    for (const thisComponent of learn_instr2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "learn_instr2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_2_allKeys;
var learn_instr3Components;
function learn_instr3RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'learn_instr3'-------
    t = 0;
    learn_instr3Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    learn_instr3Components = [];
    learn_instr3Components.push(text_2);
    learn_instr3Components.push(key_resp_2);
    
    for (const thisComponent of learn_instr3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function learn_instr3RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'learn_instr3'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = learn_instr3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }

    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of learn_instr3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function learn_instr3RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'learn_instr3'-------
    for (const thisComponent of learn_instr3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "learn_instr3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_3_allKeys;
var prac;
var learn_instr4Components;
function learn_instr4RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'learn_instr4'-------
    t = 0;
    learn_instr4Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    prac = 1;
    
    // keep track of which components have finished
    learn_instr4Components = [];
    learn_instr4Components.push(text_3);
    learn_instr4Components.push(key_resp_3);
    
    for (const thisComponent of learn_instr4Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function learn_instr4RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'learn_instr4'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = learn_instr4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_3* updates
    if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }

    
    // *key_resp_3* updates
    if (t >= 0.0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }

    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of learn_instr4Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function learn_instr4RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'learn_instr4'-------
    for (const thisComponent of learn_instr4Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "learn_instr4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var example_recall;
var currentLoop;
function example_recallLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  example_recall = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'stimuli/example.csv',
    seed: undefined, name: 'example_recall'
  });
  psychoJS.experiment.addLoop(example_recall); // add the loop to the experiment
  currentLoop = example_recall;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisExample_recall of example_recall) {
    const snapshot = example_recall.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(learn_testRoutineBegin(snapshot));
    thisScheduler.add(learn_testRoutineEachFrame(snapshot));
    thisScheduler.add(learn_testRoutineEnd(snapshot));
    thisScheduler.add(learn_feedbackRoutineBegin(snapshot));
    thisScheduler.add(learn_feedbackRoutineEachFrame(snapshot));
    thisScheduler.add(learn_feedbackRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function example_recallLoopEnd() {
  psychoJS.experiment.removeLoop(example_recall);

  return Scheduler.Event.NEXT;
}


var prac_learn_study_loop;
function prac_learn_study_loopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  prac_learn_study_loop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'stimuli/prac-learn-lists.csv',
    seed: undefined, name: 'prac_learn_study_loop'
  });
  psychoJS.experiment.addLoop(prac_learn_study_loop); // add the loop to the experiment
  currentLoop = prac_learn_study_loop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisPrac_learn_study_loop of prac_learn_study_loop) {
    const snapshot = prac_learn_study_loop.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(learn_studyRoutineBegin(snapshot));
    thisScheduler.add(learn_studyRoutineEachFrame(snapshot));
    thisScheduler.add(learn_studyRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function prac_learn_study_loopLoopEnd() {
  psychoJS.experiment.removeLoop(prac_learn_study_loop);

  return Scheduler.Event.NEXT;
}


var prac_learn_test_loop;
function prac_learn_test_loopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  prac_learn_test_loop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'stimuli/prac-learn-lists.csv',
    seed: undefined, name: 'prac_learn_test_loop'
  });
  psychoJS.experiment.addLoop(prac_learn_test_loop); // add the loop to the experiment
  currentLoop = prac_learn_test_loop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisPrac_learn_test_loop of prac_learn_test_loop) {
    const snapshot = prac_learn_test_loop.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(learn_testRoutineBegin(snapshot));
    thisScheduler.add(learn_testRoutineEachFrame(snapshot));
    thisScheduler.add(learn_testRoutineEnd(snapshot));
    thisScheduler.add(learn_feedbackRoutineBegin(snapshot));
    thisScheduler.add(learn_feedbackRoutineEachFrame(snapshot));
    thisScheduler.add(learn_feedbackRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function prac_learn_test_loopLoopEnd() {
  psychoJS.experiment.removeLoop(prac_learn_test_loop);

  return Scheduler.Event.NEXT;
}


var learn_blocks_loop;
function learn_blocks_loopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  learn_blocks_loop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 3, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'learn_blocks_loop'
  });
  psychoJS.experiment.addLoop(learn_blocks_loop); // add the loop to the experiment
  currentLoop = learn_blocks_loop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisLearn_blocks_loop of learn_blocks_loop) {
    const snapshot = learn_blocks_loop.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(set_counterRoutineBegin(snapshot));
    thisScheduler.add(set_counterRoutineEachFrame(snapshot));
    thisScheduler.add(set_counterRoutineEnd(snapshot));
    const learn_blocksLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(learn_blocksLoopBegin, learn_blocksLoopScheduler);
    thisScheduler.add(learn_blocksLoopScheduler);
    thisScheduler.add(learn_blocksLoopEnd);
    thisScheduler.add(next_instrRoutineBegin(snapshot));
    thisScheduler.add(next_instrRoutineEachFrame(snapshot));
    thisScheduler.add(next_instrRoutineEnd(snapshot));
    thisScheduler.add(break_learnRoutineBegin(snapshot));
    thisScheduler.add(break_learnRoutineEachFrame(snapshot));
    thisScheduler.add(break_learnRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


var learn_blocks;
function learn_blocksLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  learn_blocks = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'stimuli/learn-loop.csv',
    seed: undefined, name: 'learn_blocks'
  });
  psychoJS.experiment.addLoop(learn_blocks); // add the loop to the experiment
  currentLoop = learn_blocks;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisLearn_block of learn_blocks) {
    const snapshot = learn_blocks.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(begin_blockRoutineBegin(snapshot));
    thisScheduler.add(begin_blockRoutineEachFrame(snapshot));
    thisScheduler.add(begin_blockRoutineEnd(snapshot));
    const learn_study_loopLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(learn_study_loopLoopBegin, learn_study_loopLoopScheduler);
    thisScheduler.add(learn_study_loopLoopScheduler);
    thisScheduler.add(learn_study_loopLoopEnd);
    thisScheduler.add(learn_test_instrRoutineBegin(snapshot));
    thisScheduler.add(learn_test_instrRoutineEachFrame(snapshot));
    thisScheduler.add(learn_test_instrRoutineEnd(snapshot));
    const learn_test_loopLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(learn_test_loopLoopBegin, learn_test_loopLoopScheduler);
    thisScheduler.add(learn_test_loopLoopScheduler);
    thisScheduler.add(learn_test_loopLoopEnd);
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


var learn_study_loop;
function learn_study_loopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  learn_study_loop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: block_csv,
    seed: undefined, name: 'learn_study_loop'
  });
  psychoJS.experiment.addLoop(learn_study_loop); // add the loop to the experiment
  currentLoop = learn_study_loop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisLearn_study_loop of learn_study_loop) {
    const snapshot = learn_study_loop.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(learn_studyRoutineBegin(snapshot));
    thisScheduler.add(learn_studyRoutineEachFrame(snapshot));
    thisScheduler.add(learn_studyRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function learn_study_loopLoopEnd() {
  psychoJS.experiment.removeLoop(learn_study_loop);

  return Scheduler.Event.NEXT;
}


var learn_test_loop;
function learn_test_loopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  learn_test_loop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: block_csv,
    seed: undefined, name: 'learn_test_loop'
  });
  psychoJS.experiment.addLoop(learn_test_loop); // add the loop to the experiment
  currentLoop = learn_test_loop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisLearn_test_loop of learn_test_loop) {
    const snapshot = learn_test_loop.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(learn_testRoutineBegin(snapshot));
    thisScheduler.add(learn_testRoutineEachFrame(snapshot));
    thisScheduler.add(learn_testRoutineEnd(snapshot));
    thisScheduler.add(learn_feedbackRoutineBegin(snapshot));
    thisScheduler.add(learn_feedbackRoutineEachFrame(snapshot));
    thisScheduler.add(learn_feedbackRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function learn_test_loopLoopEnd() {
  psychoJS.experiment.removeLoop(learn_test_loop);

  return Scheduler.Event.NEXT;
}


function learn_blocksLoopEnd() {
  psychoJS.experiment.removeLoop(learn_blocks);

  return Scheduler.Event.NEXT;
}


function learn_blocks_loopLoopEnd() {
  psychoJS.experiment.removeLoop(learn_blocks_loop);

  return Scheduler.Event.NEXT;
}


var final_learn_test;
function final_learn_testLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  final_learn_test = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'stimuli/learn-lists.csv',
    seed: undefined, name: 'final_learn_test'
  });
  psychoJS.experiment.addLoop(final_learn_test); // add the loop to the experiment
  currentLoop = final_learn_test;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisFinal_learn_test of final_learn_test) {
    const snapshot = final_learn_test.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(learn_testRoutineBegin(snapshot));
    thisScheduler.add(learn_testRoutineEachFrame(snapshot));
    thisScheduler.add(learn_testRoutineEnd(snapshot));
    thisScheduler.add(learn_feedbackRoutineBegin(snapshot));
    thisScheduler.add(learn_feedbackRoutineEachFrame(snapshot));
    thisScheduler.add(learn_feedbackRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function final_learn_testLoopEnd() {
  psychoJS.experiment.removeLoop(final_learn_test);

  return Scheduler.Event.NEXT;
}


var search_loop;
function search_loopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  search_loop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 20, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'search_loop'
  });
  psychoJS.experiment.addLoop(search_loop); // add the loop to the experiment
  currentLoop = search_loop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisSearch_loop of search_loop) {
    const snapshot = search_loop.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(searchRoutineBegin(snapshot));
    thisScheduler.add(searchRoutineEachFrame(snapshot));
    thisScheduler.add(searchRoutineEnd(snapshot));
    thisScheduler.add(search_isiRoutineBegin(snapshot));
    thisScheduler.add(search_isiRoutineEachFrame(snapshot));
    thisScheduler.add(search_isiRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function search_loopLoopEnd() {
  psychoJS.experiment.removeLoop(search_loop);

  return Scheduler.Event.NEXT;
}


var prac_wm_trial_loop;
function prac_wm_trial_loopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  prac_wm_trial_loop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'stimuli/prac-wm-lists.csv',
    seed: undefined, name: 'prac_wm_trial_loop'
  });
  psychoJS.experiment.addLoop(prac_wm_trial_loop); // add the loop to the experiment
  currentLoop = prac_wm_trial_loop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisPrac_wm_trial_loop of prac_wm_trial_loop) {
    const snapshot = prac_wm_trial_loop.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(STRoutineBegin(snapshot));
    thisScheduler.add(STRoutineEachFrame(snapshot));
    thisScheduler.add(STRoutineEnd(snapshot));
    thisScheduler.add(wm_studyRoutineBegin(snapshot));
    thisScheduler.add(wm_studyRoutineEachFrame(snapshot));
    thisScheduler.add(wm_studyRoutineEnd(snapshot));
    thisScheduler.add(searchRoutineBegin(snapshot));
    thisScheduler.add(searchRoutineEachFrame(snapshot));
    thisScheduler.add(searchRoutineEnd(snapshot));
    const prac_wm_test_loopLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(prac_wm_test_loopLoopBegin, prac_wm_test_loopLoopScheduler);
    thisScheduler.add(prac_wm_test_loopLoopScheduler);
    thisScheduler.add(prac_wm_test_loopLoopEnd);
    thisScheduler.add(writeRoutineBegin(snapshot));
    thisScheduler.add(writeRoutineEachFrame(snapshot));
    thisScheduler.add(writeRoutineEnd(snapshot));
    thisScheduler.add(search_reminderRoutineBegin(snapshot));
    thisScheduler.add(search_reminderRoutineEachFrame(snapshot));
    thisScheduler.add(search_reminderRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


var prac_wm_test_loop;
function prac_wm_test_loopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  prac_wm_test_loop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 4, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'prac_wm_test_loop'
  });
  psychoJS.experiment.addLoop(prac_wm_test_loop); // add the loop to the experiment
  currentLoop = prac_wm_test_loop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisPrac_wm_test_loop of prac_wm_test_loop) {
    const snapshot = prac_wm_test_loop.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(wm_testRoutineBegin(snapshot));
    thisScheduler.add(wm_testRoutineEachFrame(snapshot));
    thisScheduler.add(wm_testRoutineEnd(snapshot));
    thisScheduler.add(wm_recall_isiRoutineBegin(snapshot));
    thisScheduler.add(wm_recall_isiRoutineEachFrame(snapshot));
    thisScheduler.add(wm_recall_isiRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function prac_wm_test_loopLoopEnd() {
  psychoJS.experiment.removeLoop(prac_wm_test_loop);

  return Scheduler.Event.NEXT;
}


function prac_wm_trial_loopLoopEnd() {
  psychoJS.experiment.removeLoop(prac_wm_trial_loop);

  return Scheduler.Event.NEXT;
}


var wm_trial_loop;
function wm_trial_loopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  wm_trial_loop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'stimuli/wm-lists.csv',
    seed: undefined, name: 'wm_trial_loop'
  });
  psychoJS.experiment.addLoop(wm_trial_loop); // add the loop to the experiment
  currentLoop = wm_trial_loop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisWm_trial_loop of wm_trial_loop) {
    const snapshot = wm_trial_loop.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(STRoutineBegin(snapshot));
    thisScheduler.add(STRoutineEachFrame(snapshot));
    thisScheduler.add(STRoutineEnd(snapshot));
    thisScheduler.add(wm_studyRoutineBegin(snapshot));
    thisScheduler.add(wm_studyRoutineEachFrame(snapshot));
    thisScheduler.add(wm_studyRoutineEnd(snapshot));
    thisScheduler.add(searchRoutineBegin(snapshot));
    thisScheduler.add(searchRoutineEachFrame(snapshot));
    thisScheduler.add(searchRoutineEnd(snapshot));
    const wm_test_loopLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(wm_test_loopLoopBegin, wm_test_loopLoopScheduler);
    thisScheduler.add(wm_test_loopLoopScheduler);
    thisScheduler.add(wm_test_loopLoopEnd);
    thisScheduler.add(writeRoutineBegin(snapshot));
    thisScheduler.add(writeRoutineEachFrame(snapshot));
    thisScheduler.add(writeRoutineEnd(snapshot));
    thisScheduler.add(search_reminderRoutineBegin(snapshot));
    thisScheduler.add(search_reminderRoutineEachFrame(snapshot));
    thisScheduler.add(search_reminderRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


var wm_test_loop;
function wm_test_loopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  wm_test_loop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 4, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'wm_test_loop'
  });
  psychoJS.experiment.addLoop(wm_test_loop); // add the loop to the experiment
  currentLoop = wm_test_loop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisWm_test_loop of wm_test_loop) {
    const snapshot = wm_test_loop.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(wm_testRoutineBegin(snapshot));
    thisScheduler.add(wm_testRoutineEachFrame(snapshot));
    thisScheduler.add(wm_testRoutineEnd(snapshot));
    thisScheduler.add(wm_recall_isiRoutineBegin(snapshot));
    thisScheduler.add(wm_recall_isiRoutineEachFrame(snapshot));
    thisScheduler.add(wm_recall_isiRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function wm_test_loopLoopEnd() {
  psychoJS.experiment.removeLoop(wm_test_loop);

  return Scheduler.Event.NEXT;
}


function wm_trial_loopLoopEnd() {
  psychoJS.experiment.removeLoop(wm_trial_loop);

  return Scheduler.Event.NEXT;
}


var validkeys;
var recall_started;
var learn_testComponents;
function learn_testRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'learn_test'-------
    t = 0;
    learn_testClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    validkeys = 'abcdefghijklmnopqrstuvwxyz'.split('');
    psychoJS.eventManager.clearKeys();
    recall_text.text = '';
    recall_started = false;
    
    timer.reset()
    test_image.setImage(file);
    recall_text.setText('');
    // keep track of which components have finished
    learn_testComponents = [];
    learn_testComponents.push(test_image);
    learn_testComponents.push(recall_text);
    
    for (const thisComponent of learn_testComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var textAdd;
function learn_testRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'learn_test'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = learn_testClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    if ((prac !== 1)) {
        if (((list_no !== expInfo["list"]) || (! continue_learning))) {
            continueRoutine = false;
        }
    }
    if ((skip_learn === 1)) {
        continueRoutine = false;
    }
    
    if (!recall_started){
        recall_text.text = '?'
    }
    
    
    let theseKeys = psychoJS.eventManager.getKeys();
    if (theseKeys.length > 0) {  // at least one key was pressed
      textAdd = theseKeys[theseKeys.length-1]; 
      }
    
    if (textAdd === 'return') {
        textAdd = '';  // Add nothing
        continueRoutine = false;  // End routine (if that is what you want)
    } else if (textAdd === 'backspace') {
        recall_text.text = recall_text.text.slice(0, -1);
        textAdd = undefined;
    } else if (validkeys.includes(textAdd)) {
        recall_started = true;
        if (recall_text.text === '?'){
            recall_text.text = ''
        }
        recall_text.text = recall_text.text + textAdd.toUpperCase();
        textAdd = undefined;
    }
    
    if ( timer.getTime() > 15 ){
        continueRoutine = false;
    }
    
    // *test_image* updates
    if (t >= 0.0 && test_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test_image.tStart = t;  // (not accounting for frame time here)
      test_image.frameNStart = frameN;  // exact frame index
      
      test_image.setAutoDraw(true);
    }

    
    // *recall_text* updates
    if (t >= 0.0 && recall_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      recall_text.tStart = t;  // (not accounting for frame time here)
      recall_text.frameNStart = frameN;  // exact frame index
      
      recall_text.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of learn_testComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function learn_testRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'learn_test'-------
    for (const thisComponent of learn_testComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData("recalled", recall_text.text)
    psychoJS.experiment.addData("recalled_rt", timer.getTime())
    
    // the Routine "learn_test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var accuracy;
var feedback_col;
var feedback_dur;
var learn_feedbackComponents;
function learn_feedbackRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'learn_feedback'-------
    t = 0;
    learn_feedbackClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    if ((recall_text.text === word)) {
        accuracy = 1;
        feedback_col = "lightgreen";
        feedback_dur = 0;
    } else {
        accuracy = 0;
        feedback_col = "red";
        feedback_dur = 4;
    }
    
    feedback_text.setColor(new util.Color(feedback_col));
    feedback_text.setText(recall_text.text);
    feed_image.setImage(file);
    restudy_text.setText(word);
    // keep track of which components have finished
    learn_feedbackComponents = [];
    learn_feedbackComponents.push(feedback_text);
    learn_feedbackComponents.push(feed_image);
    learn_feedbackComponents.push(post_fb_int);
    learn_feedbackComponents.push(restudy_text);
    
    for (const thisComponent of learn_feedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function learn_feedbackRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'learn_feedback'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = learn_feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    if ((prac !== 1)) {
        if (((list_no !== expInfo["list"]) || (! continue_learning))) {
            continueRoutine = false;
        }
    }
    if ((skip_learn === 1)) {
        continueRoutine = false;
    }
    
    
    // *feedback_text* updates
    if (t >= 0 && feedback_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_text.tStart = t;  // (not accounting for frame time here)
      feedback_text.frameNStart = frameN;  // exact frame index
      
      feedback_text.setAutoDraw(true);
    }

    frameRemains = 0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (feedback_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback_text.setAutoDraw(false);
    }
    
    // *feed_image* updates
    if (t >= 0 && feed_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feed_image.tStart = t;  // (not accounting for frame time here)
      feed_image.frameNStart = frameN;  // exact frame index
      
      feed_image.setAutoDraw(true);
    }

    frameRemains = 0 + (feedback_dur + 1) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (feed_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feed_image.setAutoDraw(false);
    }
    
    // *post_fb_int* updates
    if (t >= (feedback_dur + 1) && post_fb_int.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      post_fb_int.tStart = t;  // (not accounting for frame time here)
      post_fb_int.frameNStart = frameN;  // exact frame index
      
      post_fb_int.setAutoDraw(true);
    }

    frameRemains = (feedback_dur + 1) + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (post_fb_int.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      post_fb_int.setAutoDraw(false);
    }
    
    // *restudy_text* updates
    if (t >= 1 && restudy_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      restudy_text.tStart = t;  // (not accounting for frame time here)
      restudy_text.frameNStart = frameN;  // exact frame index
      
      restudy_text.setAutoDraw(true);
    }

    frameRemains = 1 + feedback_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (restudy_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      restudy_text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of learn_feedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function learn_feedbackRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'learn_feedback'-------
    for (const thisComponent of learn_feedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData("recall_acc", accuracy);
    
    if ((prac === 0)) {
        learn_n_correct += accuracy;
        if ((list_no === expInfo["list"])) {
            learn_n_done += 1;
        }
    }
    
    // the Routine "learn_feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_4_allKeys;
var learn_instr5Components;
function learn_instr5RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'learn_instr5'-------
    t = 0;
    learn_instr5Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_4.keys = undefined;
    key_resp_4.rt = undefined;
    _key_resp_4_allKeys = [];
    prac = 1;
    
    // keep track of which components have finished
    learn_instr5Components = [];
    learn_instr5Components.push(text_4);
    learn_instr5Components.push(key_resp_4);
    
    for (const thisComponent of learn_instr5Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function learn_instr5RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'learn_instr5'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = learn_instr5Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_4* updates
    if (t >= 0.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }

    
    // *key_resp_4* updates
    if (t >= 0.0 && key_resp_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_4.tStart = t;  // (not accounting for frame time here)
      key_resp_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.clearEvents(); });
    }

    if (key_resp_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_4.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_4_allKeys = _key_resp_4_allKeys.concat(theseKeys);
      if (_key_resp_4_allKeys.length > 0) {
        key_resp_4.keys = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].name;  // just the last key pressed
        key_resp_4.rt = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of learn_instr5Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function learn_instr5RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'learn_instr5'-------
    for (const thisComponent of learn_instr5Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "learn_instr5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var learn_studyComponents;
function learn_studyRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'learn_study'-------
    t = 0;
    learn_studyClock.reset(); // clock
    frameN = -1;
    routineTimer.add(4.500000);
    // update component parameters for each repeat
    study_text.setText(word);
    study_image.setImage(file);
    // keep track of which components have finished
    learn_studyComponents = [];
    learn_studyComponents.push(study_text);
    learn_studyComponents.push(study_image);
    
    for (const thisComponent of learn_studyComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function learn_studyRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'learn_study'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = learn_studyClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    if ((prac !== 1)) {
        if (((list_no !== expInfo["list"]) || (! continue_learning))) {
            continueRoutine = false;
        }
    }
    if ((skip_learn === 1)) {
        continueRoutine = false;
    }
    
    
    // *study_text* updates
    if (t >= 0.5 && study_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      study_text.tStart = t;  // (not accounting for frame time here)
      study_text.frameNStart = frameN;  // exact frame index
      
      study_text.setAutoDraw(true);
    }

    frameRemains = 0.5 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (study_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      study_text.setAutoDraw(false);
    }
    
    // *study_image* updates
    if (t >= 0.5 && study_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      study_image.tStart = t;  // (not accounting for frame time here)
      study_image.frameNStart = frameN;  // exact frame index
      
      study_image.setAutoDraw(true);
    }

    frameRemains = 0.5 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (study_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      study_image.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of learn_studyComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function learn_studyRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'learn_study'-------
    for (const thisComponent of learn_studyComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var learn_test_instrComponents;
function learn_test_instrRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'learn_test_instr'-------
    t = 0;
    learn_test_instrClock.reset(); // clock
    frameN = -1;
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    learn_test_instr_text.setText("We'll now test your memory...");
    // keep track of which components have finished
    learn_test_instrComponents = [];
    learn_test_instrComponents.push(learn_test_instr_text);
    
    for (const thisComponent of learn_test_instrComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function learn_test_instrRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'learn_test_instr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = learn_test_instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    if ((skip_learn === 1) || (continue_learning===false)) {
        continueRoutine = false;
    }
    
    
    // *learn_test_instr_text* updates
    if (t >= 0.0 && learn_test_instr_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      learn_test_instr_text.tStart = t;  // (not accounting for frame time here)
      learn_test_instr_text.frameNStart = frameN;  // exact frame index
      
      learn_test_instr_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (learn_test_instr_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      learn_test_instr_text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of learn_test_instrComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function learn_test_instrRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'learn_test_instr'-------
    for (const thisComponent of learn_test_instrComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_6_allKeys;
var learn_blocks_done;
var learn_end_pracComponents;
function learn_end_pracRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'learn_end_prac'-------
    t = 0;
    learn_end_pracClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_6.keys = undefined;
    key_resp_6.rt = undefined;
    _key_resp_6_allKeys = [];
    prac = 0;
    continue_learning = true;
    learn_blocks_done = 0;
    
    // keep track of which components have finished
    learn_end_pracComponents = [];
    learn_end_pracComponents.push(text_5);
    learn_end_pracComponents.push(key_resp_6);
    
    for (const thisComponent of learn_end_pracComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function learn_end_pracRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'learn_end_prac'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = learn_end_pracClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_5* updates
    if (t >= 0.0 && text_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_5.tStart = t;  // (not accounting for frame time here)
      text_5.frameNStart = frameN;  // exact frame index
      
      text_5.setAutoDraw(true);
    }

    
    // *key_resp_6* updates
    if (t >= 0.0 && key_resp_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_6.tStart = t;  // (not accounting for frame time here)
      key_resp_6.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_6.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.clearEvents(); });
    }

    if (key_resp_6.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_6.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_6_allKeys = _key_resp_6_allKeys.concat(theseKeys);
      if (_key_resp_6_allKeys.length > 0) {
        key_resp_6.keys = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].name;  // just the last key pressed
        key_resp_6.rt = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of learn_end_pracComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function learn_end_pracRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'learn_end_prac'-------
    for (const thisComponent of learn_end_pracComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "learn_end_prac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var learn_n_correct;
var learn_n_done;
var set_counterComponents;
function set_counterRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'set_counter'-------
    t = 0;
    set_counterClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    learn_n_correct = 0;
    learn_n_done = 0;
    learn_blocks_done += 1;
    
    // keep track of which components have finished
    set_counterComponents = [];
    
    for (const thisComponent of set_counterComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function set_counterRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'set_counter'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = set_counterClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    if (((skip_learn === 1) || (! continue_learning))) {
        continueRoutine = false;
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of set_counterComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function set_counterRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'set_counter'-------
    for (const thisComponent of set_counterComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "set_counter" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_12_allKeys;
var begin_blockComponents;
function begin_blockRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'begin_block'-------
    t = 0;
    begin_blockClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    text_10.setText('Press SPACE to see the next set of 10 pairs');
    key_resp_12.keys = undefined;
    key_resp_12.rt = undefined;
    _key_resp_12_allKeys = [];
    // keep track of which components have finished
    begin_blockComponents = [];
    begin_blockComponents.push(text_10);
    begin_blockComponents.push(key_resp_12);
    
    for (const thisComponent of begin_blockComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function begin_blockRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'begin_block'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = begin_blockClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    if ((skip_learn === 1) || (! continue_learning)) {
        continueRoutine = false;
    }
    
    
    // *text_10* updates
    if (t >= 0.0 && text_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_10.tStart = t;  // (not accounting for frame time here)
      text_10.frameNStart = frameN;  // exact frame index
      
      text_10.setAutoDraw(true);
    }

    
    // *key_resp_12* updates
    if (t >= 0.0 && key_resp_12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_12.tStart = t;  // (not accounting for frame time here)
      key_resp_12.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_12.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_12.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_12.clearEvents(); });
    }

    if (key_resp_12.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_12.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_12_allKeys = _key_resp_12_allKeys.concat(theseKeys);
      if (_key_resp_12_allKeys.length > 0) {
        key_resp_12.keys = _key_resp_12_allKeys[_key_resp_12_allKeys.length - 1].name;  // just the last key pressed
        key_resp_12.rt = _key_resp_12_allKeys[_key_resp_12_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of begin_blockComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function begin_blockRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'begin_block'-------
    for (const thisComponent of begin_blockComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "begin_block" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var perccor;
var next_instr;
var _key_resp_13_allKeys;
var next_instrComponents;
function next_instrRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'next_instr'-------
    t = 0;
    next_instrClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    perccor = Number.parseInt(((learn_n_correct / learn_n_done) * 100));
    if ((((learn_n_correct / learn_n_done) >= 0.8) || (learn_blocks_done === 3))) {
        next_instr = "Well done! You got " + perccor + "% of the pairs correct. We will now move on to the next part of the experiment.\n\nPress SPACE to continue.";
    } else {
        next_instr = "Well done! You got " + perccor + "% of the pairs correct. We will loop through all of the pairs again in groups of 10.\n\nPress SPACE to continue.";
    }
    
    next_instr_text.setText(next_instr);
    key_resp_13.keys = undefined;
    key_resp_13.rt = undefined;
    _key_resp_13_allKeys = [];
    // keep track of which components have finished
    next_instrComponents = [];
    next_instrComponents.push(next_instr_text);
    next_instrComponents.push(key_resp_13);
    
    for (const thisComponent of next_instrComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function next_instrRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'next_instr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = next_instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *next_instr_text* updates
    if (t >= 0.0 && next_instr_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      next_instr_text.tStart = t;  // (not accounting for frame time here)
      next_instr_text.frameNStart = frameN;  // exact frame index
      
      next_instr_text.setAutoDraw(true);
    }

    
    // *key_resp_13* updates
    if (t >= 0.0 && key_resp_13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_13.tStart = t;  // (not accounting for frame time here)
      key_resp_13.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_13.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_13.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_13.clearEvents(); });
    }

    if (key_resp_13.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_13.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_13_allKeys = _key_resp_13_allKeys.concat(theseKeys);
      if (_key_resp_13_allKeys.length > 0) {
        key_resp_13.keys = _key_resp_13_allKeys[_key_resp_13_allKeys.length - 1].name;  // just the last key pressed
        key_resp_13.rt = _key_resp_13_allKeys[_key_resp_13_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of next_instrComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function next_instrRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'next_instr'-------
    for (const thisComponent of next_instrComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp_13.keys', key_resp_13.keys);
    if (typeof key_resp_13.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_13.rt', key_resp_13.rt);
        routineTimer.reset();
        }
    
    key_resp_13.stop();
    // the Routine "next_instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var break_learnComponents;
function break_learnRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'break_learn'-------
    t = 0;
    break_learnClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // keep track of which components have finished
    break_learnComponents = [];
    
    for (const thisComponent of break_learnComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function break_learnRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'break_learn'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = break_learnClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    console.log(learn_n_correct);
    console.log(learn_n_done);
    console.log((learn_n_correct / learn_n_done));
    if ((learn_n_correct / learn_n_done) >= 0.8) {
        console.log("I should have stopped")
        trials.finished = true;
        learn_blocks.finished = true;
        learn_blocks_loop.finished = true;
        learn_study_loop.finished = true;
        learn_test_loop.finished = true;
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of break_learnComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function break_learnRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'break_learn'-------
    for (const thisComponent of break_learnComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "break_learn" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_7_allKeys;
var learn_final_instrComponents;
function learn_final_instrRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'learn_final_instr'-------
    t = 0;
    learn_final_instrClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_7.keys = undefined;
    key_resp_7.rt = undefined;
    _key_resp_7_allKeys = [];
    continue_learning = true;
    
    // keep track of which components have finished
    learn_final_instrComponents = [];
    learn_final_instrComponents.push(learn_final_text);
    learn_final_instrComponents.push(key_resp_7);
    
    for (const thisComponent of learn_final_instrComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function learn_final_instrRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'learn_final_instr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = learn_final_instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *learn_final_text* updates
    if (t >= 0.0 && learn_final_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      learn_final_text.tStart = t;  // (not accounting for frame time here)
      learn_final_text.frameNStart = frameN;  // exact frame index
      
      learn_final_text.setAutoDraw(true);
    }

    
    // *key_resp_7* updates
    if (t >= 0.0 && key_resp_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_7.tStart = t;  // (not accounting for frame time here)
      key_resp_7.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_7.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_7.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_7.clearEvents(); });
    }

    if (key_resp_7.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_7.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_7_allKeys = _key_resp_7_allKeys.concat(theseKeys);
      if (_key_resp_7_allKeys.length > 0) {
        key_resp_7.keys = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].name;  // just the last key pressed
        key_resp_7.rt = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of learn_final_instrComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function learn_final_instrRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'learn_final_instr'-------
    for (const thisComponent of learn_final_instrComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "learn_final_instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_10_allKeys;
var end_learnComponents;
function end_learnRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'end_learn'-------
    t = 0;
    end_learnClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_10.keys = undefined;
    key_resp_10.rt = undefined;
    _key_resp_10_allKeys = [];
    // keep track of which components have finished
    end_learnComponents = [];
    end_learnComponents.push(text_8);
    end_learnComponents.push(key_resp_10);
    
    for (const thisComponent of end_learnComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function end_learnRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'end_learn'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = end_learnClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_8* updates
    if (t >= 0.0 && text_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_8.tStart = t;  // (not accounting for frame time here)
      text_8.frameNStart = frameN;  // exact frame index
      
      text_8.setAutoDraw(true);
    }

    
    // *key_resp_10* updates
    if (t >= 0.0 && key_resp_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_10.tStart = t;  // (not accounting for frame time here)
      key_resp_10.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_10.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_10.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_10.clearEvents(); });
    }

    if (key_resp_10.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_10.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_10_allKeys = _key_resp_10_allKeys.concat(theseKeys);
      if (_key_resp_10_allKeys.length > 0) {
        key_resp_10.keys = _key_resp_10_allKeys[_key_resp_10_allKeys.length - 1].name;  // just the last key pressed
        key_resp_10.rt = _key_resp_10_allKeys[_key_resp_10_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of end_learnComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function end_learnRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'end_learn'-------
    for (const thisComponent of end_learnComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "end_learn" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_5_allKeys;
var wm_instrComponents;
function wm_instrRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'wm_instr'-------
    t = 0;
    wm_instrClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_5.keys = undefined;
    key_resp_5.rt = undefined;
    _key_resp_5_allKeys = [];
    // keep track of which components have finished
    wm_instrComponents = [];
    wm_instrComponents.push(part2);
    wm_instrComponents.push(wm_text);
    wm_instrComponents.push(key_resp_5);
    
    for (const thisComponent of wm_instrComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function wm_instrRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'wm_instr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = wm_instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *part2* updates
    if (t >= 0.0 && part2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      part2.tStart = t;  // (not accounting for frame time here)
      part2.frameNStart = frameN;  // exact frame index
      
      part2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (part2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      part2.setAutoDraw(false);
    }
    
    // *wm_text* updates
    if (t >= 2 && wm_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      wm_text.tStart = t;  // (not accounting for frame time here)
      wm_text.frameNStart = frameN;  // exact frame index
      
      wm_text.setAutoDraw(true);
    }

    
    // *key_resp_5* updates
    if (t >= 2 && key_resp_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_5.tStart = t;  // (not accounting for frame time here)
      key_resp_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.clearEvents(); });
    }

    if (key_resp_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_5.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_5_allKeys = _key_resp_5_allKeys.concat(theseKeys);
      if (_key_resp_5_allKeys.length > 0) {
        key_resp_5.keys = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].name;  // just the last key pressed
        key_resp_5.rt = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of wm_instrComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function wm_instrRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'wm_instr'-------
    for (const thisComponent of wm_instrComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "wm_instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_8_allKeys;
var wm_instr2Components;
function wm_instr2RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'wm_instr2'-------
    t = 0;
    wm_instr2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_8.keys = undefined;
    key_resp_8.rt = undefined;
    _key_resp_8_allKeys = [];
    // keep track of which components have finished
    wm_instr2Components = [];
    wm_instr2Components.push(text_6);
    wm_instr2Components.push(key_resp_8);
    
    for (const thisComponent of wm_instr2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function wm_instr2RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'wm_instr2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = wm_instr2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_6* updates
    if (t >= 0.0 && text_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_6.tStart = t;  // (not accounting for frame time here)
      text_6.frameNStart = frameN;  // exact frame index
      
      text_6.setAutoDraw(true);
    }

    
    // *key_resp_8* updates
    if (t >= 0.0 && key_resp_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_8.tStart = t;  // (not accounting for frame time here)
      key_resp_8.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_8.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_8.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_8.clearEvents(); });
    }

    if (key_resp_8.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_8.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_8_allKeys = _key_resp_8_allKeys.concat(theseKeys);
      if (_key_resp_8_allKeys.length > 0) {
        key_resp_8.keys = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].name;  // just the last key pressed
        key_resp_8.rt = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of wm_instr2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function wm_instr2RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'wm_instr2'-------
    for (const thisComponent of wm_instr2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "wm_instr2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_11_allKeys;
var search_instrComponents;
function search_instrRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'search_instr'-------
    t = 0;
    search_instrClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    t_im.setSize(im_size);
    b_im.setSize(im_size);
    l_im.setSize(im_size);
    r_im.setSize(im_size);
    key_resp_11.keys = undefined;
    key_resp_11.rt = undefined;
    _key_resp_11_allKeys = [];
    // keep track of which components have finished
    search_instrComponents = [];
    search_instrComponents.push(top_text);
    search_instrComponents.push(mid_text);
    search_instrComponents.push(bottom_text);
    search_instrComponents.push(t_im);
    search_instrComponents.push(b_im);
    search_instrComponents.push(l_im);
    search_instrComponents.push(r_im);
    search_instrComponents.push(key_resp_11);
    
    for (const thisComponent of search_instrComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function search_instrRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'search_instr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = search_instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *top_text* updates
    if (t >= 0.0 && top_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      top_text.tStart = t;  // (not accounting for frame time here)
      top_text.frameNStart = frameN;  // exact frame index
      
      top_text.setAutoDraw(true);
    }

    
    // *mid_text* updates
    if (t >= 0.0 && mid_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mid_text.tStart = t;  // (not accounting for frame time here)
      mid_text.frameNStart = frameN;  // exact frame index
      
      mid_text.setAutoDraw(true);
    }

    
    // *bottom_text* updates
    if (t >= 0.0 && bottom_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      bottom_text.tStart = t;  // (not accounting for frame time here)
      bottom_text.frameNStart = frameN;  // exact frame index
      
      bottom_text.setAutoDraw(true);
    }

    
    // *t_im* updates
    if (t >= 0.0 && t_im.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      t_im.tStart = t;  // (not accounting for frame time here)
      t_im.frameNStart = frameN;  // exact frame index
      
      t_im.setAutoDraw(true);
    }

    
    // *b_im* updates
    if (t >= 0.0 && b_im.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      b_im.tStart = t;  // (not accounting for frame time here)
      b_im.frameNStart = frameN;  // exact frame index
      
      b_im.setAutoDraw(true);
    }

    
    // *l_im* updates
    if (t >= 0.0 && l_im.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      l_im.tStart = t;  // (not accounting for frame time here)
      l_im.frameNStart = frameN;  // exact frame index
      
      l_im.setAutoDraw(true);
    }

    
    // *r_im* updates
    if (t >= 0.0 && r_im.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      r_im.tStart = t;  // (not accounting for frame time here)
      r_im.frameNStart = frameN;  // exact frame index
      
      r_im.setAutoDraw(true);
    }

    
    // *key_resp_11* updates
    if (t >= 0.0 && key_resp_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_11.tStart = t;  // (not accounting for frame time here)
      key_resp_11.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_11.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_11.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_11.clearEvents(); });
    }

    if (key_resp_11.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_11.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_11_allKeys = _key_resp_11_allKeys.concat(theseKeys);
      if (_key_resp_11_allKeys.length > 0) {
        key_resp_11.keys = _key_resp_11_allKeys[_key_resp_11_allKeys.length - 1].name;  // just the last key pressed
        key_resp_11.rt = _key_resp_11_allKeys[_key_resp_11_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of search_instrComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function search_instrRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'search_instr'-------
    for (const thisComponent of search_instrComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "search_instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var s1posex;
var s2posex;
var s3posex;
var s4posex;
var s5posex;
var s6posex;
var s7posex;
var s8posex;
var _key_resp_14_allKeys;
var search_instr2Components;
function search_instr2RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'search_instr2'-------
    t = 0;
    search_instr2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    var s1posex, s2posex, s3posex, s4posex, s5posex, s6posex, s7posex, s8posex;
    s1posex = [((- xpos) - xdisp), (ypos + ((Math.random() - 0.5) * ydisp))];
    s2posex = [((- xpos) + xdisp), (ypos + ((Math.random() - 0.5) * ydisp))];
    s3posex = [(xpos - xdisp), (ypos + ((Math.random() - 0.5) * ydisp))];
    s4posex = [(xpos + xdisp), (ypos + ((Math.random() - 0.5) * ydisp))];
    s5posex = [(xpos - xdisp), ((- ypos) + ((Math.random() - 0.5) * ydisp))];
    s6posex = [(xpos + xdisp), ((- ypos) + ((Math.random() - 0.5) * ydisp))];
    s7posex = [((- xpos) - xdisp), ((- ypos) + ((Math.random() - 0.5) * ydisp))];
    s8posex = [((- xpos) + xdisp), ((- ypos) + ((Math.random() - 0.5) * ydisp))];
    
    sim1_ex.setPos(s1posex);
    sim1_ex.setSize(im_size);
    sim2_ex.setPos(s2posex);
    sim2_ex.setSize(im_size);
    sim3_ex.setPos(s3posex);
    sim3_ex.setSize(im_size);
    sim4_ex.setPos(s4posex);
    sim4_ex.setSize(im_size);
    sim5_ex.setPos(s5posex);
    sim5_ex.setSize(im_size);
    sim6_ex.setPos(s6posex);
    sim6_ex.setSize(im_size);
    sim7_ex.setPos(s7posex);
    sim7_ex.setSize(im_size);
    sim8_ex.setPos(s8posex);
    sim8_ex.setSize(im_size);
    key_resp_14.keys = undefined;
    key_resp_14.rt = undefined;
    _key_resp_14_allKeys = [];
    // keep track of which components have finished
    search_instr2Components = [];
    search_instr2Components.push(sim1_ex);
    search_instr2Components.push(sim2_ex);
    search_instr2Components.push(sim3_ex);
    search_instr2Components.push(sim4_ex);
    search_instr2Components.push(sim5_ex);
    search_instr2Components.push(sim6_ex);
    search_instr2Components.push(sim7_ex);
    search_instr2Components.push(sim8_ex);
    search_instr2Components.push(text_12);
    search_instr2Components.push(key_resp_14);
    search_instr2Components.push(text_15);
    
    for (const thisComponent of search_instr2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function search_instr2RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'search_instr2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = search_instr2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *sim1_ex* updates
    if (t >= 0.0 && sim1_ex.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sim1_ex.tStart = t;  // (not accounting for frame time here)
      sim1_ex.frameNStart = frameN;  // exact frame index
      
      sim1_ex.setAutoDraw(true);
    }

    
    // *sim2_ex* updates
    if (t >= 0.0 && sim2_ex.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sim2_ex.tStart = t;  // (not accounting for frame time here)
      sim2_ex.frameNStart = frameN;  // exact frame index
      
      sim2_ex.setAutoDraw(true);
    }

    
    // *sim3_ex* updates
    if (t >= 0.0 && sim3_ex.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sim3_ex.tStart = t;  // (not accounting for frame time here)
      sim3_ex.frameNStart = frameN;  // exact frame index
      
      sim3_ex.setAutoDraw(true);
    }

    
    // *sim4_ex* updates
    if (t >= 0.0 && sim4_ex.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sim4_ex.tStart = t;  // (not accounting for frame time here)
      sim4_ex.frameNStart = frameN;  // exact frame index
      
      sim4_ex.setAutoDraw(true);
    }

    
    // *sim5_ex* updates
    if (t >= 0.0 && sim5_ex.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sim5_ex.tStart = t;  // (not accounting for frame time here)
      sim5_ex.frameNStart = frameN;  // exact frame index
      
      sim5_ex.setAutoDraw(true);
    }

    
    // *sim6_ex* updates
    if (t >= 0.0 && sim6_ex.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sim6_ex.tStart = t;  // (not accounting for frame time here)
      sim6_ex.frameNStart = frameN;  // exact frame index
      
      sim6_ex.setAutoDraw(true);
    }

    
    // *sim7_ex* updates
    if (t >= 0.0 && sim7_ex.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sim7_ex.tStart = t;  // (not accounting for frame time here)
      sim7_ex.frameNStart = frameN;  // exact frame index
      
      sim7_ex.setAutoDraw(true);
    }

    
    // *sim8_ex* updates
    if (t >= 0.0 && sim8_ex.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sim8_ex.tStart = t;  // (not accounting for frame time here)
      sim8_ex.frameNStart = frameN;  // exact frame index
      
      sim8_ex.setAutoDraw(true);
    }

    
    // *text_12* updates
    if (t >= 3 && text_12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_12.tStart = t;  // (not accounting for frame time here)
      text_12.frameNStart = frameN;  // exact frame index
      
      text_12.setAutoDraw(true);
    }

    
    // *key_resp_14* updates
    if (t >= 3 && key_resp_14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_14.tStart = t;  // (not accounting for frame time here)
      key_resp_14.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_14.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_14.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_14.clearEvents(); });
    }

    if (key_resp_14.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_14.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_14_allKeys = _key_resp_14_allKeys.concat(theseKeys);
      if (_key_resp_14_allKeys.length > 0) {
        key_resp_14.keys = _key_resp_14_allKeys[_key_resp_14_allKeys.length - 1].name;  // just the last key pressed
        key_resp_14.rt = _key_resp_14_allKeys[_key_resp_14_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_15* updates
    if (t >= 0.0 && text_15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_15.tStart = t;  // (not accounting for frame time here)
      text_15.frameNStart = frameN;  // exact frame index
      
      text_15.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of search_instr2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function search_instr2RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'search_instr2'-------
    for (const thisComponent of search_instr2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "search_instr2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_15_allKeys;
var search_instr3Components;
function search_instr3RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'search_instr3'-------
    t = 0;
    search_instr3Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_15.keys = undefined;
    key_resp_15.rt = undefined;
    _key_resp_15_allKeys = [];
    prac = 1;
    
    // keep track of which components have finished
    search_instr3Components = [];
    search_instr3Components.push(text_13);
    search_instr3Components.push(key_resp_15);
    
    for (const thisComponent of search_instr3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function search_instr3RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'search_instr3'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = search_instr3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_13* updates
    if (t >= 0.0 && text_13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_13.tStart = t;  // (not accounting for frame time here)
      text_13.frameNStart = frameN;  // exact frame index
      
      text_13.setAutoDraw(true);
    }

    
    // *key_resp_15* updates
    if (t >= 0.0 && key_resp_15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_15.tStart = t;  // (not accounting for frame time here)
      key_resp_15.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_15.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_15.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_15.clearEvents(); });
    }

    if (key_resp_15.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_15.getKeys({keyList: ['1', '0'], waitRelease: false});
      _key_resp_15_allKeys = _key_resp_15_allKeys.concat(theseKeys);
      if (_key_resp_15_allKeys.length > 0) {
        key_resp_15.keys = _key_resp_15_allKeys[_key_resp_15_allKeys.length - 1].name;  // just the last key pressed
        key_resp_15.rt = _key_resp_15_allKeys[_key_resp_15_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of search_instr3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function search_instr3RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'search_instr3'-------
    for (const thisComponent of search_instr3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "search_instr3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var s1pos;
var s2pos;
var s3pos;
var s4pos;
var s5pos;
var s6pos;
var s7pos;
var s8pos;
var tari;
var tarright;
var ims;
var s1;
var s2;
var s3;
var s4;
var s5;
var s6;
var s7;
var s8;
var _search_resp_allKeys;
var searchComponents;
function searchRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'search'-------
    t = 0;
    searchClock.reset(); // clock
    frameN = -1;
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    var ims, opts, s1, s1pos, s2, s2pos, s3, s3pos, s4, s4pos, s5, s5pos, s6, s6pos, s7, s7pos, s8, s8pos, tari, tarright;
    s1pos = [((- xpos) - xdisp), (ypos + ((Math.random() - 0.5) * ydisp))];
    s2pos = [((- xpos) + xdisp), (ypos + ((Math.random() - 0.5) * ydisp))];
    s3pos = [(xpos - xdisp), (ypos + ((Math.random() - 0.5) * ydisp))];
    s4pos = [(xpos + xdisp), (ypos + ((Math.random() - 0.5) * ydisp))];
    s5pos = [(xpos - xdisp), ((- ypos) + ((Math.random() - 0.5) * ydisp))];
    s6pos = [(xpos + xdisp), ((- ypos) + ((Math.random() - 0.5) * ydisp))];
    s7pos = [((- xpos) - xdisp), ((- ypos) + ((Math.random() - 0.5) * ydisp))];
    s8pos = [((- xpos) + xdisp), ((- ypos) + ((Math.random() - 0.5) * ydisp))];
    tari = (Math.floor((Math.random() * ((3 - 0) + 1))) + 0);
    tarright = Math.random() > 0.5 === true ? 1 : 0;
    ims = [];
    for (var i, _pj_c = 0, _pj_a = [0, 1, 2, 3], _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        i = _pj_a[_pj_c];
        if (i === tari) {
            console.log(tarright)
            opts = [tars[tarright], nontars[Math.random() > 0.5 === true ? 1 : 0]];
        } else {
            opts = nontars;
        }
        if (Math.random() > 0.5) {
            ims = ims.concat(opts);
        } else {
            ims = ims.concat([opts[1], opts[0]]);
        }
    }
    s1 = ((im_dir + ims[0]) + ".png");
    s2 = ((im_dir + ims[1]) + ".png");
    s3 = ((im_dir + ims[2]) + ".png");
    s4 = ((im_dir + ims[3]) + ".png");
    s5 = ((im_dir + ims[4]) + ".png");
    s6 = ((im_dir + ims[5]) + ".png");
    s7 = ((im_dir + ims[6]) + ".png");
    s8 = ((im_dir + ims[7]) + ".png");
    
    psychoJS.experiment.addData("s_im1", s1);
    psychoJS.experiment.addData("s_im2", s2);
    psychoJS.experiment.addData("s_im3", s3);
    psychoJS.experiment.addData("s_im4", s4);
    psychoJS.experiment.addData("s_im5", s5);
    psychoJS.experiment.addData("s_im6", s6);
    psychoJS.experiment.addData("s_im7", s7);
    psychoJS.experiment.addData("s_im8", s8);
    psychoJS.experiment.addData("s_im1pos", s1pos);
    psychoJS.experiment.addData("s_im2pos", s2pos);
    psychoJS.experiment.addData("s_im3pos", s3pos);
    psychoJS.experiment.addData("s_im4pos", s4pos);
    psychoJS.experiment.addData("s_im5pos", s5pos);
    psychoJS.experiment.addData("s_im6pos", s6pos);
    psychoJS.experiment.addData("s_im7pos", s7pos);
    psychoJS.experiment.addData("s_im8pos", s8pos);
    psychoJS.experiment.addData("s_tarright", tarright);
    
    sim1.setPos(s1pos);
    sim1.setSize(im_size);
    sim1.setImage(s1);
    sim2.setPos(s2pos);
    sim2.setSize(im_size);
    sim2.setImage(s2);
    sim3.setPos(s3pos);
    sim3.setSize(im_size);
    sim3.setImage(s3);
    sim4.setPos(s4pos);
    sim4.setSize(im_size);
    sim4.setImage(s4);
    sim5.setPos(s5pos);
    sim5.setSize(im_size);
    sim5.setImage(s5);
    sim6.setPos(s6pos);
    sim6.setSize(im_size);
    sim6.setImage(s6);
    sim7.setPos(s7pos);
    sim7.setSize(im_size);
    sim7.setImage(s7);
    sim8.setPos(s8pos);
    sim8.setSize(im_size);
    sim8.setImage(s8);
    search_resp.keys = undefined;
    search_resp.rt = undefined;
    _search_resp_allKeys = [];
    // keep track of which components have finished
    searchComponents = [];
    searchComponents.push(sim1);
    searchComponents.push(sim2);
    searchComponents.push(sim3);
    searchComponents.push(sim4);
    searchComponents.push(sim5);
    searchComponents.push(sim6);
    searchComponents.push(sim7);
    searchComponents.push(sim8);
    searchComponents.push(search_resp);
    searchComponents.push(search_fix);
    
    for (const thisComponent of searchComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function searchRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'search'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = searchClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    if ((prac !== 1)) {
        if ((list_no !== expInfo["list"])) {
            continueRoutine = false;
        }
    }
    
    
    // *sim1* updates
    if (t >= 0.0 && sim1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sim1.tStart = t;  // (not accounting for frame time here)
      sim1.frameNStart = frameN;  // exact frame index
      
      sim1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (sim1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      sim1.setAutoDraw(false);
    }
    
    // *sim2* updates
    if (t >= 0.0 && sim2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sim2.tStart = t;  // (not accounting for frame time here)
      sim2.frameNStart = frameN;  // exact frame index
      
      sim2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (sim2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      sim2.setAutoDraw(false);
    }
    
    // *sim3* updates
    if (t >= 0.0 && sim3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sim3.tStart = t;  // (not accounting for frame time here)
      sim3.frameNStart = frameN;  // exact frame index
      
      sim3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (sim3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      sim3.setAutoDraw(false);
    }
    
    // *sim4* updates
    if (t >= 0.0 && sim4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sim4.tStart = t;  // (not accounting for frame time here)
      sim4.frameNStart = frameN;  // exact frame index
      
      sim4.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (sim4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      sim4.setAutoDraw(false);
    }
    
    // *sim5* updates
    if (t >= 0.0 && sim5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sim5.tStart = t;  // (not accounting for frame time here)
      sim5.frameNStart = frameN;  // exact frame index
      
      sim5.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (sim5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      sim5.setAutoDraw(false);
    }
    
    // *sim6* updates
    if (t >= 0.0 && sim6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sim6.tStart = t;  // (not accounting for frame time here)
      sim6.frameNStart = frameN;  // exact frame index
      
      sim6.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (sim6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      sim6.setAutoDraw(false);
    }
    
    // *sim7* updates
    if (t >= 0.0 && sim7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sim7.tStart = t;  // (not accounting for frame time here)
      sim7.frameNStart = frameN;  // exact frame index
      
      sim7.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (sim7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      sim7.setAutoDraw(false);
    }
    
    // *sim8* updates
    if (t >= 0.0 && sim8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sim8.tStart = t;  // (not accounting for frame time here)
      sim8.frameNStart = frameN;  // exact frame index
      
      sim8.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (sim8.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      sim8.setAutoDraw(false);
    }
    
    // *search_resp* updates
    if (t >= 0.0 && search_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      search_resp.tStart = t;  // (not accounting for frame time here)
      search_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { search_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { search_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { search_resp.clearEvents(); });
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (search_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      search_resp.status = PsychoJS.Status.FINISHED;
  }

    if (search_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = search_resp.getKeys({keyList: ['1', '0'], waitRelease: false});
      _search_resp_allKeys = _search_resp_allKeys.concat(theseKeys);
      if (_search_resp_allKeys.length > 0) {
        search_resp.keys = _search_resp_allKeys[_search_resp_allKeys.length - 1].name;  // just the last key pressed
        search_resp.rt = _search_resp_allKeys[_search_resp_allKeys.length - 1].rt;
      }
    }
    
    
    // *search_fix* updates
    if (t >= 0.0 && search_fix.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      search_fix.tStart = t;  // (not accounting for frame time here)
      search_fix.frameNStart = frameN;  // exact frame index
      
      search_fix.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (search_fix.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      search_fix.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of searchComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function searchRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'search'-------
    for (const thisComponent of searchComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('search_resp.keys', search_resp.keys);
    if (typeof search_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('search_resp.rt', search_resp.rt);
        }
    
    search_resp.stop();
    return Scheduler.Event.NEXT;
  };
}


var search_isiComponents;
function search_isiRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'search_isi'-------
    t = 0;
    search_isiClock.reset(); // clock
    frameN = -1;
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    search_isiComponents = [];
    search_isiComponents.push(text_9);
    
    for (const thisComponent of search_isiComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function search_isiRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'search_isi'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = search_isiClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_9* updates
    if (t >= 0.0 && text_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_9.tStart = t;  // (not accounting for frame time here)
      text_9.frameNStart = frameN;  // exact frame index
      
      text_9.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_9.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_9.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of search_isiComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function search_isiRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'search_isi'-------
    for (const thisComponent of search_isiComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_16_allKeys;
var wm_instr3Components;
function wm_instr3RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'wm_instr3'-------
    t = 0;
    wm_instr3Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_16.keys = undefined;
    key_resp_16.rt = undefined;
    _key_resp_16_allKeys = [];
    prac = 1;
    
    // keep track of which components have finished
    wm_instr3Components = [];
    wm_instr3Components.push(text_14);
    wm_instr3Components.push(key_resp_16);
    
    for (const thisComponent of wm_instr3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function wm_instr3RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'wm_instr3'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = wm_instr3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_14* updates
    if (t >= 0.0 && text_14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_14.tStart = t;  // (not accounting for frame time here)
      text_14.frameNStart = frameN;  // exact frame index
      
      text_14.setAutoDraw(true);
    }

    
    // *key_resp_16* updates
    if (t >= 0.0 && key_resp_16.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_16.tStart = t;  // (not accounting for frame time here)
      key_resp_16.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_16.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_16.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_16.clearEvents(); });
    }

    if (key_resp_16.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_16.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_16_allKeys = _key_resp_16_allKeys.concat(theseKeys);
      if (_key_resp_16_allKeys.length > 0) {
        key_resp_16.keys = _key_resp_16_allKeys[_key_resp_16_allKeys.length - 1].name;  // just the last key pressed
        key_resp_16.rt = _key_resp_16_allKeys[_key_resp_16_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of wm_instr3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function wm_instr3RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'wm_instr3'-------
    for (const thisComponent of wm_instr3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "wm_instr3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _st_key_allKeys;
var STComponents;
function STRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'ST'-------
    t = 0;
    STClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    st_text.setText("Press '1' or '0' to start the next sequence...");
    st_key.keys = undefined;
    st_key.rt = undefined;
    _st_key_allKeys = [];
    // keep track of which components have finished
    STComponents = [];
    STComponents.push(st_text);
    STComponents.push(st_key);
    
    for (const thisComponent of STComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function STRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'ST'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = STClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    if ((prac !== 1)) {
        if ((list_no !== expInfo["list"])) {
            continueRoutine = false;
        }
    }
    
    
    // *st_text* updates
    if (t >= 0.0 && st_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      st_text.tStart = t;  // (not accounting for frame time here)
      st_text.frameNStart = frameN;  // exact frame index
      
      st_text.setAutoDraw(true);
    }

    
    // *st_key* updates
    if (t >= 0.0 && st_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      st_key.tStart = t;  // (not accounting for frame time here)
      st_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { st_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { st_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { st_key.clearEvents(); });
    }

    if (st_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = st_key.getKeys({keyList: ['1', '0'], waitRelease: false});
      _st_key_allKeys = _st_key_allKeys.concat(theseKeys);
      if (_st_key_allKeys.length > 0) {
        st_key.keys = _st_key_allKeys[_st_key_allKeys.length - 1].name;  // just the last key pressed
        st_key.rt = _st_key_allKeys[_st_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of STComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function STRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'ST'-------
    for (const thisComponent of STComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "ST" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var wm_studyComponents;
function wm_studyRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'wm_study'-------
    t = 0;
    wm_studyClock.reset(); // clock
    frameN = -1;
    routineTimer.add(7.800000);
    // update component parameters for each repeat
    wm_study_im1.setImage(file1);
    wm_study_tx1.setText(word1);
    wm_study_im2.setImage(file2);
    wm_study_tx2.setText(word2);
    wm_study_im3.setImage(file3);
    wm_study_tx3.setText(word3);
    wm_study_im4.setImage(file4);
    wm_study_tx4.setText(word4);
    // keep track of which components have finished
    wm_studyComponents = [];
    wm_studyComponents.push(wm_study_im1);
    wm_studyComponents.push(wm_study_tx1);
    wm_studyComponents.push(wm_study_im2);
    wm_studyComponents.push(wm_study_tx2);
    wm_studyComponents.push(wm_study_im3);
    wm_studyComponents.push(wm_study_tx3);
    wm_studyComponents.push(wm_study_im4);
    wm_studyComponents.push(wm_study_tx4);
    
    for (const thisComponent of wm_studyComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function wm_studyRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'wm_study'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = wm_studyClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    if ((prac !== 1)) {
        if ((list_no !== expInfo["list"])) {
            continueRoutine = false;
        }
    }
    
    
    // *wm_study_im1* updates
    if (t >= 0.0 && wm_study_im1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      wm_study_im1.tStart = t;  // (not accounting for frame time here)
      wm_study_im1.frameNStart = frameN;  // exact frame index
      
      wm_study_im1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (wm_study_im1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      wm_study_im1.setAutoDraw(false);
    }
    
    // *wm_study_tx1* updates
    if (t >= 0.0 && wm_study_tx1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      wm_study_tx1.tStart = t;  // (not accounting for frame time here)
      wm_study_tx1.frameNStart = frameN;  // exact frame index
      
      wm_study_tx1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (wm_study_tx1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      wm_study_tx1.setAutoDraw(false);
    }
    
    // *wm_study_im2* updates
    if (t >= 2 && wm_study_im2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      wm_study_im2.tStart = t;  // (not accounting for frame time here)
      wm_study_im2.frameNStart = frameN;  // exact frame index
      
      wm_study_im2.setAutoDraw(true);
    }

    frameRemains = 2 + 1.8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (wm_study_im2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      wm_study_im2.setAutoDraw(false);
    }
    
    // *wm_study_tx2* updates
    if (t >= 2 && wm_study_tx2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      wm_study_tx2.tStart = t;  // (not accounting for frame time here)
      wm_study_tx2.frameNStart = frameN;  // exact frame index
      
      wm_study_tx2.setAutoDraw(true);
    }

    frameRemains = 2 + 1.8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (wm_study_tx2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      wm_study_tx2.setAutoDraw(false);
    }
    
    // *wm_study_im3* updates
    if (t >= 4 && wm_study_im3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      wm_study_im3.tStart = t;  // (not accounting for frame time here)
      wm_study_im3.frameNStart = frameN;  // exact frame index
      
      wm_study_im3.setAutoDraw(true);
    }

    frameRemains = 4 + 1.8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (wm_study_im3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      wm_study_im3.setAutoDraw(false);
    }
    
    // *wm_study_tx3* updates
    if (t >= 4 && wm_study_tx3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      wm_study_tx3.tStart = t;  // (not accounting for frame time here)
      wm_study_tx3.frameNStart = frameN;  // exact frame index
      
      wm_study_tx3.setAutoDraw(true);
    }

    frameRemains = 4 + 1.8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (wm_study_tx3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      wm_study_tx3.setAutoDraw(false);
    }
    
    // *wm_study_im4* updates
    if (t >= 6 && wm_study_im4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      wm_study_im4.tStart = t;  // (not accounting for frame time here)
      wm_study_im4.frameNStart = frameN;  // exact frame index
      
      wm_study_im4.setAutoDraw(true);
    }

    frameRemains = 6 + 1.8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (wm_study_im4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      wm_study_im4.setAutoDraw(false);
    }
    
    // *wm_study_tx4* updates
    if (t >= 6 && wm_study_tx4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      wm_study_tx4.tStart = t;  // (not accounting for frame time here)
      wm_study_tx4.frameNStart = frameN;  // exact frame index
      
      wm_study_tx4.setAutoDraw(true);
    }

    frameRemains = 6 + 1.8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (wm_study_tx4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      wm_study_tx4.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of wm_studyComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var testOrder;
var testImages;
var testWords;
var recallCounter;
var all_recalled;
var all_recall_rt;
function wm_studyRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'wm_study'-------
    for (const thisComponent of wm_studyComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // SET THE ORDER OF TEST
    
    function shuffle(array) {
    
        var currentIndex = array.length;
        var temporaryValue, randomIndex;
    
        // While there remain elements to shuffle...
        while (0 !== currentIndex) {
            // Pick a remaining element...
            randomIndex = Math.floor(Math.random() * currentIndex);
            currentIndex -= 1;
    
            // And swap it with the current element.
            temporaryValue = array[currentIndex];
            array[currentIndex] = array[randomIndex];
            array[randomIndex] = temporaryValue;
        }
    
        return array;
    
    };
    
    testOrder = [0, 1, 2, 3];
    testImages = [file1, file2, file3, file4];
    testWords = [word1, word2, word3, word4];
    
    testOrder = shuffle(testOrder);
    recallCounter = 0;
    
    all_recalled = [];
    all_recall_rt = [];
    
    
    return Scheduler.Event.NEXT;
  };
}


var testImage;
var wm_testComponents;
function wm_testRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'wm_test'-------
    t = 0;
    wm_testClock.reset(); // clock
    frameN = -1;
    routineTimer.add(10.000000);
    // update component parameters for each repeat
    // SET TEST IMAGE + TEXT
    
    validkeys = 'abcdefghijklmnopqrstuvwxyz'.split('');
    wm_recall_text.text = '';
    psychoJS.eventManager.clearKeys();
    
    recall_started = false;
    timer_wm.reset()
    
    testImage = testImages[testOrder[recallCounter]];
    
    recallCounter += 1;
    
    wm_recall_text.setText('');
    wm_test_im.setImage(testImage);
    // keep track of which components have finished
    wm_testComponents = [];
    wm_testComponents.push(wm_recall_text);
    wm_testComponents.push(wm_test_im);
    
    for (const thisComponent of wm_testComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function wm_testRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'wm_test'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = wm_testClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    if ((prac !== 1)) {
        if ((list_no !== expInfo["list"])) {
            continueRoutine = false;
        }
    }
    
    if (!recall_started){
        wm_recall_text.text = '?'
    }
    
    
    let theseKeys = psychoJS.eventManager.getKeys();
    if (theseKeys.length > 0) {  // at least one key was pressed
      textAdd = theseKeys[theseKeys.length-1]; 
      }
    
    if (textAdd === 'return') {
        textAdd = '';  // Add nothing
        continueRoutine = false;  // End routine (if that is what you want)
    } else if (textAdd === 'backspace') {
        wm_recall_text.text = wm_recall_text.text.slice(0, -1);
        textAdd = undefined;
    } else if (validkeys.includes(textAdd)) {
        recall_started = true;
        if (wm_recall_text.text === '?'){
            wm_recall_text.text = ''
        }
        wm_recall_text.text = wm_recall_text.text + textAdd.toUpperCase();
        textAdd = undefined;
    }
    
    if ( timer_wm.getTime() > 15 ){
        continueRoutine = false;
    }
    
    
    
    
    // *wm_recall_text* updates
    if (t >= 0.0 && wm_recall_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      wm_recall_text.tStart = t;  // (not accounting for frame time here)
      wm_recall_text.frameNStart = frameN;  // exact frame index
      
      wm_recall_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (wm_recall_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      wm_recall_text.setAutoDraw(false);
    }
    
    // *wm_test_im* updates
    if (t >= 0 && wm_test_im.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      wm_test_im.tStart = t;  // (not accounting for frame time here)
      wm_test_im.frameNStart = frameN;  // exact frame index
      
      wm_test_im.setAutoDraw(true);
    }

    frameRemains = 0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (wm_test_im.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      wm_test_im.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of wm_testComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function wm_testRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'wm_test'-------
    for (const thisComponent of wm_testComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    all_recalled.push(wm_recall_text.text);
    all_recall_rt.push(timer_wm.getTime());
    
    return Scheduler.Event.NEXT;
  };
}


var wm_recall_isiComponents;
function wm_recall_isiRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'wm_recall_isi'-------
    t = 0;
    wm_recall_isiClock.reset(); // clock
    frameN = -1;
    routineTimer.add(0.200000);
    // update component parameters for each repeat
    // keep track of which components have finished
    wm_recall_isiComponents = [];
    wm_recall_isiComponents.push(wm_isi_blank);
    
    for (const thisComponent of wm_recall_isiComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function wm_recall_isiRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'wm_recall_isi'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = wm_recall_isiClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    if ((prac !== 1)) {
        if ((list_no !== expInfo["list"])) {
            continueRoutine = false;
        }
    }
    
    
    // *wm_isi_blank* updates
    if (t >= 0.0 && wm_isi_blank.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      wm_isi_blank.tStart = t;  // (not accounting for frame time here)
      wm_isi_blank.frameNStart = frameN;  // exact frame index
      
      wm_isi_blank.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (wm_isi_blank.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      wm_isi_blank.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of wm_recall_isiComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function wm_recall_isiRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'wm_recall_isi'-------
    for (const thisComponent of wm_recall_isiComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var writeComponents;
function writeRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'write'-------
    t = 0;
    writeClock.reset(); // clock
    frameN = -1;
    routineTimer.add(0.300000);
    // update component parameters for each repeat
    for (var i = 0, _pj_a = 4; (i < _pj_a); i += 1) {
        psychoJS.experiment.addData(("wm_recalled" + (i + 1).toString()), all_recalled[i]);
        psychoJS.experiment.addData(("wm_recall_rt" + (i + 1).toString()), all_recall_rt[i]);
        psychoJS.experiment.addData(("wm_probed" + (i + 1).toString()), testOrder[i]);
        psychoJS.experiment.addData(("wm_recall_acc"+(i + 1).toString()), testWords[testOrder[i]] === all_recalled[i]);
    }
    
    // keep track of which components have finished
    writeComponents = [];
    writeComponents.push(text_11);
    
    for (const thisComponent of writeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function writeRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'write'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = writeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    if ((prac !== 1)) {
        if ((list_no !== expInfo["list"])) {
            continueRoutine = false;
        }
    }
    
    
    // *text_11* updates
    if (t >= 0.0 && text_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_11.tStart = t;  // (not accounting for frame time here)
      text_11.frameNStart = frameN;  // exact frame index
      
      text_11.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_11.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_11.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of writeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function writeRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'write'-------
    for (const thisComponent of writeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var search_reminderComponents;
function search_reminderRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'search_reminder'-------
    t = 0;
    search_reminderClock.reset(); // clock
    frameN = -1;
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    search_reminderComponents = [];
    search_reminderComponents.push(text_16);
    
    for (const thisComponent of search_reminderComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function search_reminderRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'search_reminder'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = search_reminderClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    if ((prac !== 1)) {
        if ((list_no !== expInfo["list"])) {
            continueRoutine = false;
        }
    }
    if (((search_resp.keys === "0") || (search_resp.keys === "1"))) {
        continueRoutine = false;
    }
    
    
    // *text_16* updates
    if (t >= 0.0 && text_16.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_16.tStart = t;  // (not accounting for frame time here)
      text_16.frameNStart = frameN;  // exact frame index
      
      text_16.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_16.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_16.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of search_reminderComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function search_reminderRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'search_reminder'-------
    for (const thisComponent of search_reminderComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_9_allKeys;
var end_wm_pracComponents;
function end_wm_pracRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'end_wm_prac'-------
    t = 0;
    end_wm_pracClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_9.keys = undefined;
    key_resp_9.rt = undefined;
    _key_resp_9_allKeys = [];
    prac = 0;
    
    // keep track of which components have finished
    end_wm_pracComponents = [];
    end_wm_pracComponents.push(text_7);
    end_wm_pracComponents.push(key_resp_9);
    
    for (const thisComponent of end_wm_pracComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function end_wm_pracRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'end_wm_prac'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = end_wm_pracClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_7* updates
    if (t >= 0.0 && text_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_7.tStart = t;  // (not accounting for frame time here)
      text_7.frameNStart = frameN;  // exact frame index
      
      text_7.setAutoDraw(true);
    }

    
    // *key_resp_9* updates
    if (t >= 0.0 && key_resp_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_9.tStart = t;  // (not accounting for frame time here)
      key_resp_9.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_9.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_9.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_9.clearEvents(); });
    }

    if (key_resp_9.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_9.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_9_allKeys = _key_resp_9_allKeys.concat(theseKeys);
      if (_key_resp_9_allKeys.length > 0) {
        key_resp_9.keys = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].name;  // just the last key pressed
        key_resp_9.rt = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of end_wm_pracComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function end_wm_pracRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'end_wm_prac'-------
    for (const thisComponent of end_wm_pracComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "end_wm_prac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var end_expComponents;
function end_expRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'end_exp'-------
    t = 0;
    end_expClock.reset(); // clock
    frameN = -1;
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    end_expComponents = [];
    end_expComponents.push(end_exp_text);
    
    for (const thisComponent of end_expComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function end_expRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'end_exp'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = end_expClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *end_exp_text* updates
    if (t >= 0.0 && end_exp_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_exp_text.tStart = t;  // (not accounting for frame time here)
      end_exp_text.frameNStart = frameN;  // exact frame index
      
      end_exp_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (end_exp_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      end_exp_text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of end_expComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function end_expRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'end_exp'-------
    for (const thisComponent of end_expComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(thisScheduler, loop) {
  // ------Prepare for next entry------
  return function () {
    if (typeof loop !== 'undefined') {
      // ------Check if user ended loop early------
      if (loop.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(loop);
        }
      thisScheduler.stop();
      } else {
        const thisTrial = loop.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(loop);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(trials) {
  return function () {
    psychoJS.importAttributes(trials.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
