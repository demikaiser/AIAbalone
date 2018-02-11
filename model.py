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

import time

# Global game configuration object (Map).
# This is a multi-layered object (like a JSON),
# which is easy to read and handle.
global_game_configuration = {
    'black': {
        'agent':'',    # human | computer
        'move_limitation':-1,
        'time_limitation':-1,
    },
    'white': {
        'agent': '',  # human | computer
        'move_limitation': -1,
        'time_limitation': -1,
    },
    'all': {
        'initial_board_layout':'', # standard | german_daisy | belgian_daisy
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
        'time_taken_total': 0
    },
    'white': {
        'score': 0,
        'moves_taken': 0,
        'time_taken_for_last_move': 0,
        'time_taken_total': 0
    },
    'all': {
        # started_B_Human | started_B_Computer | started_W_Human | started_W_Computer | paused | stopped
        'game_state':'stopped'
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

    # Get status from white
    if context.radio_human_white.get_value():
        global_game_configuration['white']['agent'] = 'human'
    elif context.radio_computer_white.get_value():
        global_game_configuration['white']['agent'] = 'computer'

    global_game_configuration['white']['move_limitation'] \
        = context.slider_for_move_limit_white.get_value()

    global_game_configuration['white']['time_limitation'] \
        = context.slider_for_time_limit_white.get_value()

    # Get status from all
    if context.radio_standard.get_value():
        global_game_configuration['all']['initial_board_layout'] = 'standard'
    elif context.radio_german_daisy.get_value():
        global_game_configuration['all']['initial_board_layout'] = 'german_daisy'
    elif context.radio_belgian_daisy.get_value():
        global_game_configuration['all']['initial_board_layout'] = 'belgian_daisy'

# Start the game.
def game_start(context):
    initial_configuration_for_black = global_game_configuration['black']['agent']
    initial_game_start_position = global_game_configuration['all']['initial_board_layout']

    #sets starting position
    if initial_game_start_position == "german_daisy":
        context.create_pieces_german_daisy()
    elif initial_game_start_position == "belgian_daisy":
        context.create_pieces_belgian_daisy()
    else:
        context.create_pieces_standard()

    context.populate_gui_coordinates()
    context.update_canvas()

    if initial_configuration_for_black == 'human':
        global_game_play_state['all']['game_state'] = 'started_B_Human'
        context.update_game_state('started_B_H')
    elif initial_configuration_for_black == 'computer':
        global_game_play_state['all']['game_state'] = 'started_B_Computer'
        context.update_game_state('started_B_C')
        # Move by the artificial intelligence machine.
        messages = []
        messages.append("Black Computer moved!")
        context.log(messages)
        update_turn_state(context)

# Pause the game.
def game_pause(context):
    global_game_play_state['all']['game_state'] = 'paused'
    context.update_game_state('paused')

# Resume the game.
def game_resume(context):
    pass

# Stop the game.
def game_stop(context):
    global_game_play_state['all']['game_state'] = 'stopped'
    context.update_game_state('stopped')

# Reset the game.
def game_reset(context):
    global_game_play_state['all']['game_state'] = 'stopped'
    context.update_game_state('stopped')

# Update the state.
# started_B_Human | started_B_Computer | started_W_Human | started_W_Computer | paused | stopped
def update_turn_state(context):
    if global_game_play_state['all']['game_state'] == 'started_B_Human':
        if global_game_configuration['white']['agent'] == 'human':
            global_game_play_state['all']['game_state'] = 'started_W_Human'
            context.update_game_state('started_W_H')

        elif global_game_configuration['white']['agent'] == 'computer':
            global_game_play_state['all']['game_state'] = 'started_W_Computer'
            context.update_game_state('started_W_C')
            # Move by the artificial intelligence machine.
            messages = []
            messages.append("White Computer moved!")
            context.log(messages)
            update_turn_state(context)

    elif global_game_play_state['all']['game_state'] == 'started_B_Computer':
        if global_game_configuration['white']['agent'] == 'human':
            global_game_play_state['all']['game_state'] = 'started_W_Human'
            context.update_game_state('started_W_H')

        elif global_game_configuration['white']['agent'] == 'computer':
            global_game_play_state['all']['game_state'] = 'started_W_Computer'
            context.update_game_state('started_W_C')
            # Move by the artificial intelligence machine.
            messages = []
            messages.append("White Computer moved!")
            context.log(messages)
            update_turn_state(context)

    elif global_game_play_state['all']['game_state'] == 'started_W_Human':
        if global_game_configuration['black']['agent'] == 'human':
            global_game_play_state['all']['game_state'] = 'started_B_Human'
            context.update_game_state('started_B_H')

        elif global_game_configuration['black']['agent'] == 'computer':
            global_game_play_state['all']['game_state'] = 'started_B_Computer'
            context.update_game_state('started_B_C')
            # Move by the artificial intelligence machine.
            messages = []
            messages.append("Black Computer moved!")
            context.log(messages)
            update_turn_state(context)

    elif global_game_play_state['all']['game_state'] == 'started_W_Computer':
        if global_game_configuration['black']['agent'] == 'human':
            global_game_play_state['all']['game_state'] = 'started_B_Human'
            context.update_game_state('started_B_H')

        elif global_game_configuration['black']['agent'] == 'computer':
            global_game_play_state['all']['game_state'] = 'started_B_Computer'
            context.update_game_state('started_B_C')
            # Move by the artificial intelligence machine.
            messages = []
            messages.append("Black Computer moved!")
            context.log(messages)
            update_turn_state(context)















