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

# ================ ================ Game Controller ================ ================

# Button callback function for "Game Start".
def button_game_start_callback(context):
    if model.game_start(context) == -1:
        context.log(["You can only start the game when the game is stopped."])
    else:
        # Log the game information.
        messages = []
        messages.append("Game Started.")
        messages.append("Initial Board Layout: " + model.global_game_configuration['all']['initial_board_layout'])
        messages.append("Black Player: " + model.global_game_configuration['black']['agent'])
        messages.append("White Player: " + model.global_game_configuration['white']['agent'])
        context.log(messages)

# Button callback function for "Game Pause".
def button_game_pause_callback(context):
    if model.game_pause(context) == -1:
        context.log(["Game can't be paused."])
    else:
        context.log(["Game paused."])

# Button callback function for "Game Resume".
def button_game_resume_callback(context):
    if model.game_resume(context) == -1:
        context.log(["Game can't be resumed."])
    else:
        context.log(["Game resumed."])

# Button callback function for "Game Stop".
def button_game_stop_callback(context):
    if model.game_stop(context) == -1:
        context.log(["Game can't be stopped."])
    else:
        context.log(["Game stopped."])

# Button callback function for "Game Reset".
def button_game_reset_callback(context):
    if model.game_reset(context) == -1:
        context.log(["Game can't be reset."])
    else:
        context.log(["Game reset."])


# ================ ================ Piece Controller ================ ================

# Button callback function for "Black Step Back".
def button_step_back_callback(context):
    return_number = model.step_back_callback(context)
    if return_number == -1:
        context.log(["The game must be paused first."])
    elif return_number == -2:
        context.log(["There is no game history to step backward."])
    else:
        context.log(["Step back is executed."])

# Button callback function for "White Step Back".
def button_step_forward_callback(context):
    return_number = model.step_forward_callback(context)
    if return_number == -1:
        context.log(["The game must be paused first."])
    elif return_number == -2:
        context.log(["There is no game history to step forward."])
    else:
        context.log(["Step forward is executed."])


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

# Button callback function for "Volume Up".
def button_volume_up_callback(context):
    context.bgm_instance.volume_up()

# Button callback function for "Volume Down".
def button_volume_down_callback(context):
    context.bgm_instance.volume_down()

# Button callback function for "Get Funk".
def button_get_funk_callback(context):
    context.bgm_instance.get_funk()

# Button callback function for "Secret".
def button_secret1_callback(context):
    context.bgm_instance.secret()

# Button callback function for "Secret".
def button_secret2_callback(context):
    context.bgm_instance.secret()

# Button callback function for "Secret".
def button_secret3_callback(context):
    context.bgm_instance.secret()

