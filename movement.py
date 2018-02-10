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

# Move one piece.
def move_one_piece(old_x, old_y, new_x, new_y):

    # Memorize the old piece.
    piece = model.global_game_board_state[old_x][old_y]

    # Remove the old piece.
    model.global_game_board_state[old_x][old_y] = 0

    # Place the piece to new location.
    model.global_game_board_state[new_x][new_y] = piece

# Move two pieces.
def move_two_pieces(old_x1, old_y1, new_x1, new_y1, old_x2, old_y2, new_x2, new_y2):

    # Memorize the old pieces.
    piece1 = model.global_game_board_state[old_x1][old_y1]
    piece2 = model.global_game_board_state[old_x2][old_y2]

    # Remove the old pieces.
    model.global_game_board_state[old_x1][old_y1] = 0
    model.global_game_board_state[old_x2][old_y2] = 0

    # Place the pieces to new location.
    model.global_game_board_state[new_x1][new_y1] = piece1
    model.global_game_board_state[new_x2][new_y2] = piece2

# Move three pieces.
def move_three_pieces(old_x1, old_y1, new_x1, new_y1, old_x2, old_y2, new_x2, new_y2, old_x3, old_y3, new_x3, new_y3):

    # Memorize the old pieces.
    piece1 = model.global_game_board_state[old_x1][old_y1]
    piece2 = model.global_game_board_state[old_x2][old_y2]
    piece3 = model.global_game_board_state[old_x3][old_y3]

    # Remove the old pieces.
    model.global_game_board_state[old_x1][old_y1] = 0
    model.global_game_board_state[old_x2][old_y2] = 0
    model.global_game_board_state[old_x3][old_y3] = 0

    # Place the pieces to new location.
    model.global_game_board_state[new_x1][new_y1] = piece1
    model.global_game_board_state[new_x2][new_y2] = piece2
    model.global_game_board_state[new_x3][new_y3] = piece3









