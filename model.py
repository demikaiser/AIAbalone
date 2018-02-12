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

import time, gameboard, aimachine

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

global_temporary_game_state_for_pause_and_resume = ''

# Global game state representation (Standard Setup).
# 1 is black, 2 is white, -9 is the non-use position.
# WARNING: This convention should be strictly followed.
global_game_board_state = [
    [-9, -9, -9, -9,  0,  0,  0,  0,  0],
    [-9, -9, -9,  0,  0,  0,  0,  0,  0],
    [-9, -9,  0,  0,  0,  0,  0,  0,  0],
    [-9,  0,  0,  0,  0,  0,  0,  0,  0],
    [ 0,  0,  0,  0,  0,  0,  0,  0,  0],
    [ 0,  0,  0,  0,  0,  0,  0,  0, -9],
    [ 0,  0,  0,  0,  0,  0,  0, -9, -9],
    [ 0,  0,  0,  0,  0,  0, -9, -9, -9],
    [ 0,  0,  0,  0,  0, -9, -9, -9, -9]
]

# Inital game board settings.
initial_game_board_state_standard = [
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

initial_game_board_state_german_daisy = [
    [-9, -9, -9, -9,  0,  0,  1,  1,  0],
    [-9, -9, -9,  0,  0,  1,  1,  1,  0],
    [-9, -9,  2,  2,  0,  1,  1,  0,  0],
    [-9,  2,  2,  2,  0,  0,  0,  0,  0],
    [ 0,  2,  2,  0,  0,  0,  2,  2,  0],
    [ 0,  0,  0,  0,  0,  2,  2,  2, -9],
    [ 0,  0,  1,  1,  0,  2,  2, -9, -9],
    [ 0,  1,  1,  1,  0,  0, -9, -9, -9],
    [ 0,  1,  1,  0,  0, -9, -9, -9, -9]
]

initial_game_board_state_belgian_daisy = [
    [-9, -9, -9, -9,  0,  0,  0,  1,  1],
    [-9, -9, -9,  0,  0,  0,  1,  1,  1],
    [-9, -9,  0,  0,  0,  0,  1,  1,  0],
    [-9,  2,  2,  0,  0,  0,  0,  2,  2],
    [ 2,  2,  2,  0,  0,  0,  2,  2,  2],
    [ 2,  2,  0,  0,  0,  0,  2,  2, -9],
    [ 0,  1,  1,  0,  0,  0,  0, -9, -9],
    [ 1,  1,  1,  0,  0,  0, -9, -9, -9],
    [ 1,  1,  0,  0,  0, -9, -9, -9, -9]
]

initial_game_board_state_empty_for_reset = [
    [-9, -9, -9, -9,  0,  0,  0,  0,  0],
    [-9, -9, -9,  0,  0,  0,  0,  0,  0],
    [-9, -9,  0,  0,  0,  0,  0,  0,  0],
    [-9,  0,  0,  0,  0,  0,  0,  0,  0],
    [ 0,  0,  0,  0,  0,  0,  0,  0,  0],
    [ 0,  0,  0,  0,  0,  0,  0,  0, -9],
    [ 0,  0,  0,  0,  0,  0,  0, -9, -9],
    [ 0,  0,  0,  0,  0,  0, -9, -9, -9],
    [ 0,  0,  0,  0,  0, -9, -9, -9, -9]
]

# Set global game configuration from gui.
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

    # Game play configuration setup.
    global_game_play_state['black']['score'] = 0
    global_game_play_state['white']['score'] = 0

    global_game_play_state['black']['moves_taken'] = 0
    global_game_play_state['white']['moves_taken'] = 0

    global_game_play_state['black']['time_taken_for_last_move'] = 0
    global_game_play_state['white']['time_taken_for_last_move'] = 0

    global_game_play_state['black']['time_taken_total'] = 0
    global_game_play_state['white']['time_taken_total'] = 0

# Start the game.
def game_start(context):

    # Setup the global game configuration to start the game.
    set_global_game_configuration_from_gui(context)

    initial_configuration_for_black = global_game_configuration['black']['agent']
    initial_game_start_position = global_game_configuration['all']['initial_board_layout']

    global global_game_board_state
    global initial_game_board_state_standard
    global initial_game_board_state_german_daisy
    global initial_game_board_state_belgian_daisy

    # Set the starting position.
    if initial_game_start_position == "german_daisy":
        copy_all_state_coordinates(global_game_board_state, initial_game_board_state_german_daisy)
    elif initial_game_start_position == "belgian_daisy":
        copy_all_state_coordinates(global_game_board_state, initial_game_board_state_belgian_daisy)
    else:
        copy_all_state_coordinates(global_game_board_state, initial_game_board_state_standard)

    context.populate_gui_coordinates()
    context.update_canvas()
    gameboard.update_gui_game_panel(context)

    # Kick off the first move.
    if initial_configuration_for_black == 'human':
        global_game_play_state['all']['game_state'] = 'started_B_Human'
        context.update_game_state('started_B_H')
    elif initial_configuration_for_black == 'computer':
        global_game_play_state['all']['game_state'] = 'started_B_Computer'
        context.update_game_state('started_B_C')

        # Start moving by the artificial intelligence machine.
        aimachine.make_movement(context, 'black')

# Pause the game.
def game_pause(context):
    global global_temporary_game_state_for_pause_and_resume
    global_temporary_game_state_for_pause_and_resume = global_game_play_state['all']['game_state']
    global_game_play_state['all']['game_state'] = 'paused'
    context.update_game_state('paused')

# Resume the game.
def game_resume(context):
    global global_temporary_game_state_for_pause_and_resume
    global_game_play_state['all']['game_state'] = global_temporary_game_state_for_pause_and_resume

    if global_game_play_state['all']['game_state'] == 'started_B_Human':
        context.update_game_state('started_B_H')
    if global_game_play_state['all']['game_state'] == 'started_B_Computer':
        context.update_game_state('started_B_C')
    if global_game_play_state['all']['game_state'] == 'started_W_Human':
        context.update_game_state('started_W_H')
    if global_game_play_state['all']['game_state'] == 'started_W_Computer':
        context.update_game_state('started_W_C')

    global_temporary_game_state_for_pause_and_resume = ''

# Stop the game.
def game_stop(context):
    global_game_play_state['all']['game_state'] = 'stopped'
    context.update_game_state('stopped')

# Reset the game.
def game_reset(context):
    global_game_play_state['all']['game_state'] = 'stopped'
    context.update_game_state('stopped')

    # Reset the board.
    global global_game_board_state
    global initial_game_board_state_empty_for_reset
    copy_all_state_coordinates(global_game_board_state, initial_game_board_state_empty_for_reset)

    # Reset the game play state.
    global_game_play_state['black']['score'] = 0
    global_game_play_state['black']['moves_taken'] = 0
    global_game_play_state['black']['time_taken_for_last_move'] = 0
    global_game_play_state['black']['time_taken_total'] = 0
    global_game_play_state['white']['score'] = 0
    global_game_play_state['white']['moves_taken'] = 0
    global_game_play_state['white']['time_taken_for_last_move'] = 0
    global_game_play_state['white']['time_taken_total'] = 0

    # Update gui.
    context.update_canvas()
    context.show_game_board()

# Update the state.
# started_B_Human | started_B_Computer | started_W_Human | started_W_Computer | paused | stopped
def update_turn_state(context):
    if global_game_play_state['all']['game_state'] == 'started_B_Human':
        if global_game_configuration['white']['agent'] == 'human':
            global_game_play_state['all']['game_state'] = 'started_W_Human'
            context.update_game_state('started_W_H')

            # Update gameboard after movement.
            gameboard.update_gui_game_panel(context)

        elif global_game_configuration['white']['agent'] == 'computer':
            global_game_play_state['all']['game_state'] = 'started_W_Computer'
            context.update_game_state('started_W_C')

            # Move by the artificial intelligence machine.
            aimachine.make_movement(context, 'white')

    elif global_game_play_state['all']['game_state'] == 'started_B_Computer':
        if global_game_configuration['white']['agent'] == 'human':
            global_game_play_state['all']['game_state'] = 'started_W_Human'
            context.update_game_state('started_W_H')

            # Update gameboard after movement.
            gameboard.update_gui_game_panel(context)

        elif global_game_configuration['white']['agent'] == 'computer':
            global_game_play_state['all']['game_state'] = 'started_W_Computer'
            context.update_game_state('started_W_C')

            # Move by the artificial intelligence machine.
            aimachine.make_movement(context, 'white')

    elif global_game_play_state['all']['game_state'] == 'started_W_Human':
        if global_game_configuration['black']['agent'] == 'human':
            global_game_play_state['all']['game_state'] = 'started_B_Human'
            context.update_game_state('started_B_H')

            # Update gameboard after movement.
            gameboard.update_gui_game_panel(context)


        elif global_game_configuration['black']['agent'] == 'computer':
            global_game_play_state['all']['game_state'] = 'started_B_Computer'
            context.update_game_state('started_B_C')

            # Move by the artificial intelligence machine.
            aimachine.make_movement(context, 'black')

    elif global_game_play_state['all']['game_state'] == 'started_W_Computer':
        if global_game_configuration['black']['agent'] == 'human':
            global_game_play_state['all']['game_state'] = 'started_B_Human'
            context.update_game_state('started_B_H')

            # Update gameboard after movement.
            gameboard.update_gui_game_panel(context)

        elif global_game_configuration['black']['agent'] == 'computer':
            global_game_play_state['all']['game_state'] = 'started_B_Computer'
            context.update_game_state('started_B_C')

            # Move by the artificial intelligence machine.
            aimachine.make_movement(context, 'black')

# Goal test
def goal_test(context):
    if global_game_play_state['black']['score'] == 6:
        # Update the global game state.
        global_game_play_state['all']['game_state'] = 'stopped'

        # Update the gui game state.
        context.update_game_state('Stopped')

        # Send win log message for white.
        messages = []
        messages.append("Black won!")
        messages.append("Game stopped.")
        context.log(messages)

    elif global_game_play_state['white']['score'] == 6:
        # Update the global game state.
        global_game_play_state['all']['game_state'] = 'stopped'

        # Update the gui game state.
        context.update_game_state('Stopped')

        # Send win log message for white.
        messages = []
        messages.append("White won!")
        messages.append("Game stopped.")
        context.log(messages)


# ================ ================ Utility Functions ================ ================

# Copy all state coordinates to state representation A from state representation B.
def copy_all_state_coordinates(state_representation_a, state_representation_b):
    for i in range(9):
        for j in range(9):
            state_representation_a[i][j] = state_representation_b[i][j]















