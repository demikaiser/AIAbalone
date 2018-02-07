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

# Global game configuration object (Map).
# This is a multi-layered object (like a JSON),
# which is easy to read and handle.
global_game_configuration = {
    'black': {
        'agent':'',    # human | computer
        'move_limitation':-1,
        'time_limitation':-1,
        'AI_strategy':''    # defualt | etc...
    },
    'white': {
        'agent': '',  # human | computer
        'move_limitation': -1,
        'time_limitation': -1,
        'AI_strategy': ''  # defualt | etc...
    },
    'all': {
        'initial_board_layout':'', # standard | german_daisy | belgian_daisy
        'recent_game_state':'',    # started | paused | stopped | reset
    }
}

# Global game play state object (Map).
# This is a multi-layered object (like a JSON),
# which is easy to read and handle.
global_game_play_state = {
    'black': {
        'score': 0,
        'moves_taken': 0,
        'time_taken_for_last_move': 0,
    },
    'white': {
        'score': 0,
        'moves_taken': 0,
        'time_taken_for_last_move': 0,
    },
    'all': {
        'turn':''    # black | white
    }
}

# Global game state representation (Standard Setup).
# 1 is black, 2 is white, -9 is the non-use position.
# WARNING: This convention should be strictly followed.
global_game_board_state = [
    [-9, -9, -9, -9,  0,  0,  0,  1,  1],
    [-9, -9, -9,  0,  0,  0,  0,  1,  1],
    [-9, -9,  0,  0,  0,  0,  1,  1,  1],
    [-9,  2,  0,  0,  0,  0,  1,  1,  1],
    [ 2,  2,  2,  0,  0,  0,  1,  1,  1],
    [ 2,  2,  2,  0,  0,  0,  0,  1, -9],
    [ 2,  2,  2,  0,  0,  0,  0, -9, -9],
    [ 2,  2,  0,  0,  0,  0, -9, -9, -9],
    [ 2,  2,  0,  0,  0, -9, -9, -9, -9]
]

def set_global_game_configuration_from_gui(context):
    # Get status from black
    if context.radio_human_black.get_value():
        global_game_configuration['black']['agent'] = 'human'
    elif context.radio_computer_black.get_value():
        global_game_configuration['black']['agent'] = 'computer'

    global_game_configuration['black']['move_limitation'] \
        = context.slider_for_move_limit_black.get_value()

    global_game_configuration['black']['time_limitation'] \
        = context.slider_for_time_limit_black.get_value()

    if context.radio_default_strategy_black.get_value():
        global_game_configuration['black']['AI_strategy'] = 'default'

    # Get status from white
    if context.radio_human_white.get_value():
        global_game_configuration['white']['agent'] = 'human'
    elif context.radio_computer_white.get_value():
        global_game_configuration['white']['agent'] = 'computer'

    global_game_configuration['white']['move_limitation'] \
        = context.slider_for_move_limit_white.get_value()

    global_game_configuration['white']['time_limitation'] \
        = context.slider_for_time_limit_white.get_value()

    if context.radio_default_strategy_white.get_value():
        global_game_configuration['white']['AI_strategy'] = 'default'

    # Get status from all
    if context.radio_standard.get_value():
        global_game_configuration['all']['initial_board_layout'] = 'standard'
    elif context.radio_german_daisy.get_value():
        global_game_configuration['all']['initial_board_layout'] = 'german_daisy'
    elif context.radio_belgian_daisy.get_value():
        global_game_configuration['all']['initial_board_layout'] = 'belgian_daisy'








