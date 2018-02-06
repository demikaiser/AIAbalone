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

# Button callback function for "Black Step Back".
def button_step_back_black_callback(context):
    context.log(["Hello Jake", "Button button_step_back_BLACK is clicked!", "Processing..."])

# Button callback function for "White Step Back".
def button_step_back_white_callback(context):
    context.log(["Hello Jake", "Button button_step_back_WHITE is clicked!", "Processing..."])

# Button callback function for "Game Start".
def button_game_start_callback(context):
    context.log(["Button START"])

    # Setup the global game configuration to start the game.
    model.set_global_game_configuration_from_gui(context)




# Button callback function for "Game Pause".
def button_game_pause_callback(context):
    context.log(["Button PAUSE"])

# Button callback function for "Game Stop".
def button_game_stop_callback(context):
    context.log(["Button STOP"])

# Button callback function for "Game Reset".
def button_game_reset_callback(context):
    context.log(["Button RESET"])


