'''
Copyright (C) BCIT AI/ML Option 2018 Team with Members Following - All Rights Reserved.
- Jake Jonghun Choi     jchoi179@my.bcit.ca
- Justin Carey          justinthomascarey@gmail.com
- Pashan Irani          pashanirani@gmail.com
- Tony Huang	        tonyhuang1996@hotmail.ca
- Chil Yuqing Qiu       yuqingqiu93@gmail.com
Unauthorized copying of this file, via any medium is strictly prohibited.
Written by Jake Jonghun Choi <jchoi179@my.bcit.ca>
'''

import model

# ================ ================ Piece Controller ================ ================

# Button callback function for "Black Step Back".
def button_step_back_black_callback(context):
    context.log(["Hello Jake", "Button button_step_back_BLACK is clicked!", "Processing..."])

# Button callback function for "White Step Back".
def button_step_back_white_callback(context):
    context.log(["Hello Jake", "Button button_step_back_WHITE is clicked!", "Processing..."])



# ================ ================ Music Controller ================ ================

# Button callback function for "Start Music".
def button_start_music_callback(context):
    context.bgm_instance.start_music()

# Button callback function for "Stop Music".
def button_stop_music_callback(context):
    context.bgm_instance.stop_music()

# Button callback function for "Next Music".
def button_next_music_callback(context):
    context.bgm_instance.next_music()

# Button callback function for "Get Funk".
def button_get_funk_callback(context):
    context.bgm_instance.get_funk()



# ================ ================ Game Controller ================ ================

# Button callback function for "Game Start".
def button_game_start_callback(context):
    context.log(["Game started."])

    # Setup the global game configuration to start the game.
    model.set_global_game_configuration_from_gui(context)
    model.game_start(context)

# Button callback function for "Game Pause".
def button_game_pause_callback(context):
    context.log(["Game paused."])
    model.game_pause(context)

# Button callback function for "Game Resume".
def button_game_resume_callback(context):
    context.log(["Game resumed."])
    model.game_resume(context)

# Button callback function for "Game Stop".
def button_game_stop_callback(context):
    context.log(["Game stopped."])
    model.game_stop(context)

# Button callback function for "Game Reset".
def button_game_reset_callback(context):
    context.log(["Game reset."])
    model.game_reset(context)


