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

# Update the gameboard for GUI panels.
def update_gui_game_panel(context):

    # Update scores.
    context.update_score('black', model.global_game_play_state['black']['score'])
    context.update_score('white', model.global_game_play_state['white']['score'])

    # Update moves taken for each side.
    context.update_moves_taken('black', model.global_game_play_state['black']['moves_taken'])
    context.update_moves_taken('white', model.global_game_play_state['white']['moves_taken'])

# Update the movement for each side.
def update_moves_taken_for(color):

    if color == 'black':
        model.global_game_play_state['black']['moves_taken'] += 1
    elif color == 'white':
        model.global_game_play_state['white']['moves_taken'] += 1

# Update the game score.
def update_game_score():
    black_number = 0
    white_number = 0

    for j in range(9):
        for i in range(9):
            if model.global_game_board_state[i][j] == 1:
                black_number += 1
            elif model.global_game_board_state[i][j] == 2:
                white_number += 1

    black_score = 14 - white_number
    white_score = 14 - black_number

    model.global_game_play_state['black']['score'] = black_score
    model.global_game_play_state['white']['score'] = white_score

# Reset the current timer to 0.
def reset_current_timer():
    model.global_game_play_state['black']['time_taken_for_last_move'] = 0
    model.global_game_play_state['white']['time_taken_for_last_move'] = 0


