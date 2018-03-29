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

# NO IMPORT STATEMENTS: TOTALLY INDEPENDENT, WILL BE TRANSPILED TO C CODE.

# Global game boundary object (Set).
global_game_board_boundary_for_all = {
    (4, 0), (5, 0), (6, 0), (7, 0),
    (8, 0), (8, 1), (8, 2), (8, 3),
    (8, 4), (7, 5), (6, 6), (5, 7),
    (4, 8), (3, 8), (2, 8), (1, 8),
    (0, 8), (0, 7), (0, 6), (0, 5),
    (0, 4), (1, 3), (2, 2), (3, 1)
}

global_game_board_boundary_for_x = {
    (4, 0), (3, 1), (2, 2), (1, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8),
    (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (7, 5), (6, 6), (5, 7), (4, 8)
}

global_game_board_boundary_for_y = {
    (0, 4), (1, 3), (2, 2), (3, 1), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0),
    (0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 7), (6, 6), (7, 5), (8, 4)
}

global_game_board_boundary_for_z = {
    (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4),
    (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (1, 8), (2, 8), (3, 8), (4, 8)
}

# ================ ================ Rules Application for GUI ================ ================

# Apply rules for move one piece.
def apply_rules_for_move_one_piece(stored_piece1, clicked_info):

    if (clicked_info[0], clicked_info[1]) \
        in generate_all_possible_legal_moves_for_one_piece(stored_piece1[0], stored_piece1[1]):
        return True

    return False

# Apply rules for move two pieces.
def apply_rules_for_move_two_pieces(stored_piece1, stored_piece2, clicked_info):

    for position in generate_all_possible_legal_moves_for_two_pieces(stored_piece1[0], stored_piece1[1],
                                                                     stored_piece2[0], stored_piece2[1]):
        if position[0] == clicked_info[0] and position[1] == clicked_info[1]:
            return position
        if position[2] == clicked_info[0] and position[3] == clicked_info[1]:
            return position

    for position in generate_all_possible_legal_moves_for_two_pieces(stored_piece2[0], stored_piece2[1],
                                                                     stored_piece1[0], stored_piece1[1]):
        if position[0] == clicked_info[0] and position[1] == clicked_info[1]:
            return position
        if position[2] == clicked_info[0] and position[3] == clicked_info[1]:
            return position

    return (-9, -9, -9, -9)

# Apply rules for move three pieces.
def apply_rules_for_move_three_pieces(stored_piece1, stored_piece2, stored_piece3, clicked_info):

    for position in generate_all_possible_legal_moves_for_three_pieces(stored_piece1[0], stored_piece1[1],
                                                                     stored_piece2[0], stored_piece2[1],
                                                                     stored_piece3[0], stored_piece3[1]):
        if position[0] == clicked_info[0] and position[1] == clicked_info[1]:
            return position
        if position[2] == clicked_info[0] and position[3] == clicked_info[1]:
            return position
        if position[4] == clicked_info[0] and position[5] == clicked_info[1]:
            return position

    for position in generate_all_possible_legal_moves_for_three_pieces(stored_piece1[0], stored_piece1[1],
                                                                     stored_piece3[0], stored_piece3[1],
                                                                     stored_piece2[0], stored_piece2[1]):
        if position[0] == clicked_info[0] and position[1] == clicked_info[1]:
            return position
        if position[2] == clicked_info[0] and position[3] == clicked_info[1]:
            return position
        if position[4] == clicked_info[0] and position[5] == clicked_info[1]:
            return position

    for position in generate_all_possible_legal_moves_for_three_pieces(stored_piece2[0], stored_piece2[1],
                                                                     stored_piece1[0], stored_piece1[1],
                                                                     stored_piece3[0], stored_piece3[1]):
        if position[0] == clicked_info[0] and position[1] == clicked_info[1]:
            return position
        if position[2] == clicked_info[0] and position[3] == clicked_info[1]:
            return position
        if position[4] == clicked_info[0] and position[5] == clicked_info[1]:
            return position

    for position in generate_all_possible_legal_moves_for_three_pieces(stored_piece2[0], stored_piece2[1],
                                                                     stored_piece3[0], stored_piece3[1],
                                                                     stored_piece1[0], stored_piece1[1]):
        if position[0] == clicked_info[0] and position[1] == clicked_info[1]:
            return position
        if position[2] == clicked_info[0] and position[3] == clicked_info[1]:
            return position
        if position[4] == clicked_info[0] and position[5] == clicked_info[1]:
            return position

    for position in generate_all_possible_legal_moves_for_three_pieces(stored_piece3[0], stored_piece3[1],
                                                                     stored_piece1[0], stored_piece1[1],
                                                                     stored_piece2[0], stored_piece2[1]):
        if position[0] == clicked_info[0] and position[1] == clicked_info[1]:
            return position
        if position[2] == clicked_info[0] and position[3] == clicked_info[1]:
            return position
        if position[4] == clicked_info[0] and position[5] == clicked_info[1]:
            return position

    for position in generate_all_possible_legal_moves_for_three_pieces(stored_piece3[0], stored_piece3[1],
                                                                     stored_piece2[0], stored_piece2[1],
                                                                     stored_piece1[0], stored_piece1[1]):
        if position[0] == clicked_info[0] and position[1] == clicked_info[1]:
            return position
        if position[2] == clicked_info[0] and position[3] == clicked_info[1]:
            return position
        if position[4] == clicked_info[0] and position[5] == clicked_info[1]:
            return position

    return (-9, -9, -9, -9)


# Apply rules for move 2 to 1 sumito.
def apply_rules_for_move_2_to_1_sumito(stored_piece1, stored_piece2, clicked_info):
    for position in generate_all_2_to_1_legal_sumitos(stored_piece1[0], stored_piece1[1],
                                                      stored_piece2[0], stored_piece2[1]):
        if position[0] == clicked_info[0] and position[1] == clicked_info[1]:
            return position
        if position[2] == clicked_info[0] and position[3] == clicked_info[1]:
            return position

    for position in generate_all_2_to_1_legal_sumitos(stored_piece2[0], stored_piece2[1],
                                                      stored_piece1[0], stored_piece1[1]):
        if position[0] == clicked_info[0] and position[1] == clicked_info[1]:
            return position
        if position[2] == clicked_info[0] and position[3] == clicked_info[1]:
            return position

    return (-9, -9, -9, -9)

# Apply rules for move 3 to 1 or 3 to 2 sumito.
def apply_rules_for_move_3_to_1_or_3_to_2_sumito(stored_piece1, stored_piece2, stored_piece3, clicked_info):

    for position in generate_all_3_to_1_legal_sumitos(stored_piece1[0], stored_piece1[1],
                                                     stored_piece2[0], stored_piece2[1],
                                                     stored_piece3[0], stored_piece3[1]):
        if position[0] == clicked_info[0] and position[1] == clicked_info[1]:
            return position
        if position[2] == clicked_info[0] and position[3] == clicked_info[1]:
            return position
        if position[4] == clicked_info[0] and position[5] == clicked_info[1]:
            return position

    for position in generate_all_3_to_1_legal_sumitos(stored_piece1[0], stored_piece1[1],
                                                     stored_piece3[0], stored_piece3[1],
                                                     stored_piece2[0], stored_piece2[1]):
        if position[0] == clicked_info[0] and position[1] == clicked_info[1]:
            return position
        if position[2] == clicked_info[0] and position[3] == clicked_info[1]:
            return position
        if position[4] == clicked_info[0] and position[5] == clicked_info[1]:
            return position

    for position in generate_all_3_to_1_legal_sumitos(stored_piece2[0], stored_piece2[1],
                                                     stored_piece1[0], stored_piece1[1],
                                                     stored_piece3[0], stored_piece3[1]):
        if position[0] == clicked_info[0] and position[1] == clicked_info[1]:
            return position
        if position[2] == clicked_info[0] and position[3] == clicked_info[1]:
            return position
        if position[4] == clicked_info[0] and position[5] == clicked_info[1]:
            return position

    for position in generate_all_3_to_1_legal_sumitos(stored_piece2[0], stored_piece2[1],
                                                     stored_piece3[0], stored_piece3[1],
                                                     stored_piece1[0], stored_piece1[1]):
        if position[0] == clicked_info[0] and position[1] == clicked_info[1]:
            return position
        if position[2] == clicked_info[0] and position[3] == clicked_info[1]:
            return position
        if position[4] == clicked_info[0] and position[5] == clicked_info[1]:
            return position

    for position in generate_all_3_to_1_legal_sumitos(stored_piece3[0], stored_piece3[1],
                                                     stored_piece1[0], stored_piece1[1],
                                                     stored_piece2[0], stored_piece2[1]):
        if position[0] == clicked_info[0] and position[1] == clicked_info[1]:
            return position
        if position[2] == clicked_info[0] and position[3] == clicked_info[1]:
            return position
        if position[4] == clicked_info[0] and position[5] == clicked_info[1]:
            return position

    for position in generate_all_3_to_1_legal_sumitos(stored_piece3[0], stored_piece3[1],
                                                     stored_piece2[0], stored_piece2[1],
                                                     stored_piece1[0], stored_piece1[1]):
        if position[0] == clicked_info[0] and position[1] == clicked_info[1]:
            return position
        if position[2] == clicked_info[0] and position[3] == clicked_info[1]:
            return position
        if position[4] == clicked_info[0] and position[5] == clicked_info[1]:
            return position

    for position in generate_all_3_to_2_legal_sumitos(stored_piece1[0], stored_piece1[1],
                                                     stored_piece2[0], stored_piece2[1],
                                                     stored_piece3[0], stored_piece3[1]):
        if position[0] == clicked_info[0] and position[1] == clicked_info[1]:
            return position
        if position[2] == clicked_info[0] and position[3] == clicked_info[1]:
            return position
        if position[4] == clicked_info[0] and position[5] == clicked_info[1]:
            return position

    for position in generate_all_3_to_2_legal_sumitos(stored_piece1[0], stored_piece1[1],
                                                     stored_piece3[0], stored_piece3[1],
                                                     stored_piece2[0], stored_piece2[1]):
        if position[0] == clicked_info[0] and position[1] == clicked_info[1]:
            return position
        if position[2] == clicked_info[0] and position[3] == clicked_info[1]:
            return position
        if position[4] == clicked_info[0] and position[5] == clicked_info[1]:
            return position

    for position in generate_all_3_to_2_legal_sumitos(stored_piece2[0], stored_piece2[1],
                                                     stored_piece1[0], stored_piece1[1],
                                                     stored_piece3[0], stored_piece3[1]):
        if position[0] == clicked_info[0] and position[1] == clicked_info[1]:
            return position
        if position[2] == clicked_info[0] and position[3] == clicked_info[1]:
            return position
        if position[4] == clicked_info[0] and position[5] == clicked_info[1]:
            return position

    for position in generate_all_3_to_2_legal_sumitos(stored_piece2[0], stored_piece2[1],
                                                     stored_piece3[0], stored_piece3[1],
                                                     stored_piece1[0], stored_piece1[1]):
        if position[0] == clicked_info[0] and position[1] == clicked_info[1]:
            return position
        if position[2] == clicked_info[0] and position[3] == clicked_info[1]:
            return position
        if position[4] == clicked_info[0] and position[5] == clicked_info[1]:
            return position

    for position in generate_all_3_to_2_legal_sumitos(stored_piece3[0], stored_piece3[1],
                                                     stored_piece1[0], stored_piece1[1],
                                                     stored_piece2[0], stored_piece2[1]):
        if position[0] == clicked_info[0] and position[1] == clicked_info[1]:
            return position
        if position[2] == clicked_info[0] and position[3] == clicked_info[1]:
            return position
        if position[4] == clicked_info[0] and position[5] == clicked_info[1]:
            return position

    for position in generate_all_3_to_2_legal_sumitos(stored_piece3[0], stored_piece3[1],
                                                     stored_piece2[0], stored_piece2[1],
                                                     stored_piece1[0], stored_piece1[1]):
        if position[0] == clicked_info[0] and position[1] == clicked_info[1]:
            return position
        if position[2] == clicked_info[0] and position[3] == clicked_info[1]:
            return position
        if position[4] == clicked_info[0] and position[5] == clicked_info[1]:
            return position

    return (-9, -9, -9, -9)


# ================ ================ Legal Movement Generation ================ ================

def generate_all_possible_legal_moves_for_one_piece(state, x1, y1):
    possible_moves = set()

    # Upper-Right.
    if is_the_position_inside_of_the_board(state, [(x1 + 1, y1 - 1)]):
        if is_the_position_empty_or_going_to_be_empty(state, [(x1 + 1, y1 - 1)], []):
            possible_moves.add((x1 + 1, y1 - 1))
    # Right.
    if is_the_position_inside_of_the_board(state, [(x1 + 1, y1 + 0)]):
        if is_the_position_empty_or_going_to_be_empty(state, [(x1 + 1, y1 + 0)], []):
            possible_moves.add((x1 + 1, y1 + 0))
    # Lower-Right.
    if is_the_position_inside_of_the_board(state, [(x1 + 0, y1 + 1)]):
        if is_the_position_empty_or_going_to_be_empty(state, [(x1 + 0, y1 + 1)], []):
            possible_moves.add((x1 + 0, y1 + 1))
    # Lower_Left.
    if is_the_position_inside_of_the_board(state, [(x1 - 1, y1 + 1)]):
        if is_the_position_empty_or_going_to_be_empty(state, [(x1 - 1, y1 + 1)], []):
            possible_moves.add((x1 - 1, y1 + 1))
    # Left.
    if is_the_position_inside_of_the_board(state, [(x1 - 1, y1 + 0)]):
        if is_the_position_empty_or_going_to_be_empty(state, [(x1 - 1, y1 + 0)], []):
            possible_moves.add((x1 - 1, y1 + 0))
    # Upper-Left.
    if is_the_position_inside_of_the_board(state, [(x1 + 0, y1 - 1)]):
        if is_the_position_empty_or_going_to_be_empty(state, [(x1 + 0, y1 - 1)], []):
            possible_moves.add((x1 + 0, y1 - 1))

    return possible_moves

def generate_all_possible_legal_moves_for_two_pieces(state, x1, y1, x2, y2):
    possible_moves = set()
    if is_two_pieces_inline(x1, y1, x2, y2):
        # Upper-Right.
        if is_the_position_inside_of_the_board(state, [(x1 + 1, y1 - 1), (x2 + 1, y2 - 1)]):
            if is_the_position_empty_or_going_to_be_empty(state, [(x1 + 1, y1 - 1), (x2 + 1, y2 - 1)], [(x1, y1), (x2, y2)]):
                possible_moves.add((x1 + 1, y1 - 1, x2 + 1, y2 - 1))
        # Right.
        if is_the_position_inside_of_the_board(state, [(x1 + 1, y1 + 0), (x2 + 1, y2 + 0)]):
            if is_the_position_empty_or_going_to_be_empty(state, [(x1 + 1, y1 + 0), (x2 + 1, y2 + 0)], [(x1, y1), (x2, y2)]):
                possible_moves.add((x1 + 1, y1 + 0, x2 + 1, y2 + 0))
        # Lower-Right.
        if is_the_position_inside_of_the_board(state, [(x1 + 0, y1 + 1), (x2 + 0, y2 + 1)]):
            if is_the_position_empty_or_going_to_be_empty(state, [(x1 + 0, y1 + 1), (x2 + 0, y2 + 1)], [(x1, y1), (x2, y2)]):
                possible_moves.add((x1 + 0, y1 + 1, x2 + 0, y2 + 1))
        # Lower_Left.
        if is_the_position_inside_of_the_board(state, [(x1 - 1, y1 + 1), (x2 - 1, y2 + 1)]):
            if is_the_position_empty_or_going_to_be_empty(state, [(x1 - 1, y1 + 1), (x2 - 1, y2 + 1)], [(x1, y1), (x2, y2)]):
                possible_moves.add((x1 - 1, y1 + 1, x2 - 1, y2 + 1))
        # Left.
        if is_the_position_inside_of_the_board(state, [(x1 - 1, y1 + 0), (x2 - 1, y2 + 0)]):
            if is_the_position_empty_or_going_to_be_empty(state, [(x1 - 1, y1 + 0), (x2 - 1, y2 + 0)], [(x1, y1), (x2, y2)]):
                possible_moves.add((x1 - 1, y1 + 0, x2 - 1, y2 + 0))
        # Upper-Left.
        if is_the_position_inside_of_the_board(state, [(x1 + 0, y1 - 1), (x2 + 0, y2 - 1)]):
            if is_the_position_empty_or_going_to_be_empty(state, [(x1 + 0, y1 - 1), (x2 + 0, y2 - 1)], [(x1, y1), (x2, y2)]):
                possible_moves.add((x1 + 0, y1 - 1, x2 + 0, y2 - 1))

    return possible_moves

def generate_all_possible_legal_moves_for_three_pieces(state, x1, y1, x2, y2, x3, y3):
    possible_moves = set()
    if is_three_pieces_inline(x1, y1, x2, y2, x3, y3):
        # Upper-Right.
        if is_the_position_inside_of_the_board(state, [(x1 + 1, y1 - 1), (x2 + 1, y2 - 1), (x3 + 1, y3 - 1)]):
            if is_the_position_empty_or_going_to_be_empty(state, [(x1 + 1, y1 - 1), (x2 + 1, y2 - 1), (x3 + 1, y3 - 1)], [(x1, y1), (x2, y2), (x3, y3)]):
                possible_moves.add((x1 + 1, y1 - 1, x2 + 1, y2 - 1, x3 + 1, y3 - 1))
        # Right.
        if is_the_position_inside_of_the_board(state, [(x1 + 1, y1 + 0), (x2 + 1, y2 + 0), (x3 + 1, y3 + 0)]):
            if is_the_position_empty_or_going_to_be_empty(state, [(x1 + 1, y1 + 0), (x2 + 1, y2 + 0), (x3 + 1, y3 + 0)], [(x1, y1), (x2, y2), (x3, y3)]):
                possible_moves.add((x1 + 1, y1 + 0, x2 + 1, y2 + 0, x3 + 1, y3 + 0))
        # Lower-Right.
        if is_the_position_inside_of_the_board(state, [(x1 + 0, y1 + 1), (x2 + 0, y2 + 1), (x3 + 0, y3 + 1)]):
            if is_the_position_empty_or_going_to_be_empty(state, [(x1 + 0, y1 + 1), (x2 + 0, y2 + 1), (x3 + 0, y3 + 1)], [(x1, y1), (x2, y2), (x3, y3)]):
                possible_moves.add((x1 + 0, y1 + 1, x2 + 0, y2 + 1, x3 + 0, y3 + 1))
        # Lower_Left.
        if is_the_position_inside_of_the_board(state, [(x1 - 1, y1 + 1), (x2 - 1, y2 + 1), (x3 - 1, y3 + 1)]):
            if is_the_position_empty_or_going_to_be_empty(state, [(x1 - 1, y1 + 1), (x2 - 1, y2 + 1), (x3 - 1, y3 + 1)], [(x1, y1), (x2, y2), (x3, y3)]):
                possible_moves.add((x1 - 1, y1 + 1, x2 - 1, y2 + 1, x3 - 1, y3 + 1))
        # Left.
        if is_the_position_inside_of_the_board(state, [(x1 - 1, y1 + 0), (x2 - 1, y2 + 0), (x3 - 1, y3 + 0)]):
            if is_the_position_empty_or_going_to_be_empty(state, [(x1 - 1, y1 + 0), (x2 - 1, y2 + 0), (x3 - 1, y3 + 0)], [(x1, y1), (x2, y2), (x3, y3)]):
                possible_moves.add((x1 - 1, y1 + 0, x2 - 1, y2 + 0, x3 - 1, y3 + 0))
        # Upper-Left.
        if is_the_position_inside_of_the_board(state, [(x1 + 0, y1 - 1), (x2 + 0, y2 - 1), (x3 + 0, y3 - 1)]):
            if is_the_position_empty_or_going_to_be_empty(state, [(x1 + 0, y1 - 1), (x2 + 0, y2 - 1), (x3 + 0, y3 - 1)], [(x1, y1), (x2, y2), (x3, y3)]):
                possible_moves.add((x1 + 0, y1 - 1, x2 + 0, y2 - 1, x3 + 0, y3 - 1))

    return possible_moves

def generate_all_2_to_1_legal_sumitos(state, x1, y1, x2, y2):
    possible_moves = set()
    if is_two_pieces_inline(x1, y1, x2, y2):
        possible_moves = get_2_to_1_sumito_coordinates_for_two_pieces_on_the_x_axis(state, x1, y1, x2, y2)
        if possible_moves == set():
            possible_moves = get_2_to_1_sumito_coordinates_for_two_pieces_on_the_y_axis(state, x1, y1, x2, y2)
            if possible_moves == set():
                possible_moves = get_2_to_1_sumito_coordinates_for_two_pieces_on_the_z_axis(state, x1, y1, x2, y2)

    return possible_moves

def generate_all_3_to_1_legal_sumitos(state, x1, y1, x2, y2, x3, y3):
    possible_moves = set()
    if is_three_pieces_inline(x1, y1, x2, y2, x3, y3):
        possible_moves = get_3_to_1_sumito_coordinates_for_three_pieces_on_the_x_axis(state, x1, y1, x2, y2, x3, y3)
        if possible_moves == set():
            possible_moves = get_3_to_1_sumito_coordinates_for_three_pieces_on_the_y_axis(state, x1, y1, x2, y2, x3, y3)
            if possible_moves == set():
                possible_moves = get_3_to_1_sumito_coordinates_for_three_pieces_on_the_z_axis(state, x1, y1, x2, y2, x3, y3)

    return possible_moves

def generate_all_3_to_2_legal_sumitos(state, x1, y1, x2, y2, x3, y3):
    possible_moves = set()
    if is_three_pieces_inline(x1, y1, x2, y2, x3, y3):
        possible_moves = get_3_to_2_sumito_coordinates_for_three_pieces_on_the_x_axis(state, x1, y1, x2, y2, x3, y3)
        if possible_moves == set():
            possible_moves = get_3_to_2_sumito_coordinates_for_three_pieces_on_the_y_axis(state, x1, y1, x2, y2, x3, y3)
            if possible_moves == set():
                possible_moves = get_3_to_2_sumito_coordinates_for_three_pieces_on_the_z_axis(state, x1, y1, x2, y2, x3, y3)

    return possible_moves


# ================ ================ Sumito Coordinates Calculation ================ ================

# Calculate 2 to 1 sumito coordinates on the direction x (y coordinates are same).
def get_2_to_1_sumito_coordinates_for_two_pieces_on_the_x_axis(state, x1, y1, x2, y2):

    # Get the color of the player.
    if state[x1][y1] == 1:
        ally = 1
        opponent = 2
    elif state[x1][y1] == 2:
        ally = 2
        opponent = 1
    else:
        return set()

    sumito_coordinates = set()

    if y1 == y2:
        y_common = y1

        x_adv_max_0 = max_from_two_elements(x1, x2) + 0
        x_adv_max_1 = max_from_two_elements(x1, x2) + 1
        x_adv_max_2 = max_from_two_elements(x1, x2) + 2

        x_adv_min_0 = min_from_two_elements(x1, x2) - 0
        x_adv_min_1 = min_from_two_elements(x1, x2) - 1
        x_adv_min_2 = min_from_two_elements(x1, x2) - 2

        # a. Plus direction, and the enemy is on the boundary.
        if is_the_position_inside_of_the_board(state, [(x_adv_max_1, y_common)]):
            if state[x_adv_max_1][y_common] == opponent:
                if is_the_location_boundary(x_adv_max_1, y_common, 'x'):
                    sumito_coordinates.add((x_adv_max_0, y_common, x_adv_max_1, y_common))

        # b. Plus direction, and the enemy will be pushed further.
        if is_the_position_inside_of_the_board(state, [(x_adv_max_2, y_common)]):
            if state[x_adv_max_1][y_common] == opponent:
                if is_the_location_empty(state, x_adv_max_2, y_common):
                    sumito_coordinates.add((x_adv_max_0, y_common, x_adv_max_1, y_common))

        # c. Minus direction, and the enemy is on the boundary.
        if is_the_position_inside_of_the_board(state, [(x_adv_min_1, y_common)]):
            if state[x_adv_min_1][y_common] == opponent:
                if is_the_location_boundary(x_adv_min_1, y_common, 'x'):
                    sumito_coordinates.add((x_adv_min_0, y_common, x_adv_min_1, y_common))

        # d. Minus direction, and the enemy will be pushed further.
        if is_the_position_inside_of_the_board(state, [(x_adv_min_2, y_common)]):
            if state[x_adv_min_1][y_common] == opponent:
                if is_the_location_empty(state, x_adv_min_2, y_common):
                    sumito_coordinates.add((x_adv_min_0, y_common, x_adv_min_1, y_common))

    return sumito_coordinates


# Calculate 3 to 1 sumito coordinates on the direction x (y coordinates are same).
def get_3_to_1_sumito_coordinates_for_three_pieces_on_the_x_axis(state, x1, y1, x2, y2, x3, y3):

    # Get the color of the player.
    if state[x1][y1] == 1:
        ally = 1
        opponent = 2
    elif state[x1][y1] == 2:
        ally = 2
        opponent = 1
    else:
        return set()

    sumito_coordinates = set()

    if y1 == y2 and y2 == y3:
        y_common = y1

        x_adv_max_0 = max_from_three_elements(x1, x2, x3) + 0
        x_adv_max_1 = max_from_three_elements(x1, x2, x3) + 1
        x_adv_max_2 = max_from_three_elements(x1, x2, x3) + 2

        x_adv_mid_0 = mid_from_three_elements(x1, x2, x3)

        x_adv_min_0 = min_from_three_elements(x1, x2, x3) - 0
        x_adv_min_1 = min_from_three_elements(x1, x2, x3) - 1
        x_adv_min_2 = min_from_three_elements(x1, x2, x3) - 2

        # a. Plus direction, and the enemy is on the boundary.
        if is_the_position_inside_of_the_board(state, [(x_adv_max_1, y_common)]):
            if state[x_adv_max_1][y_common] == opponent:
                if is_the_location_boundary(x_adv_max_1, y_common, 'x'):
                    sumito_coordinates.add((x_adv_max_0, y_common, x_adv_max_1, y_common, x_adv_mid_0, y_common))

        # b. Plus direction, and the enemy will be pushed further.
        if is_the_position_inside_of_the_board(state, [(x_adv_max_2, y_common)]):
            if state[x_adv_max_1][y_common] == opponent:
                if state[x_adv_max_2][y_common] == 0:
                    if is_the_location_empty(state, x_adv_max_2, y_common):
                        sumito_coordinates.add((x_adv_max_0, y_common, x_adv_max_1, y_common, x_adv_mid_0, y_common))

        # c. Minus direction, and the enemy is on the boundary.
        if is_the_position_inside_of_the_board(state, [(x_adv_min_1, y_common)]):
            if state[x_adv_min_1][y_common] == opponent:
                if is_the_location_boundary(x_adv_min_1, y_common, 'x'):
                    sumito_coordinates.add((x_adv_min_0, y_common, x_adv_min_1, y_common, x_adv_mid_0, y_common))

        # d. Minus direction, and the enemy will be pushed further.
        if is_the_position_inside_of_the_board(state, [(x_adv_min_2, y_common)]):
            if state[x_adv_min_1][y_common] == opponent:
                if state[x_adv_min_2][y_common] == 0:
                    if is_the_location_empty(state, x_adv_min_2, y_common):
                        sumito_coordinates.add((x_adv_min_0, y_common, x_adv_min_1, y_common, x_adv_mid_0, y_common))

    return sumito_coordinates

# Calculate 3 to 2 sumito coordinates on the direction x (y coordinates are same).
def get_3_to_2_sumito_coordinates_for_three_pieces_on_the_x_axis(state, x1, y1, x2, y2, x3, y3):

    # Get the color of the player.
    if state[x1][y1] == 1:
        ally = 1
        opponent = 2
    elif state[x1][y1] == 2:
        ally = 2
        opponent = 1
    else:
        return set()

    sumito_coordinates = set()

    if y1 == y2 and y2 == y3:
        y_common = y1

        x_adv_max_0 = max_from_three_elements(x1, x2, x3) + 0
        x_adv_max_1 = max_from_three_elements(x1, x2, x3) + 1
        x_adv_max_2 = max_from_three_elements(x1, x2, x3) + 2
        x_adv_max_3 = max_from_three_elements(x1, x2, x3) + 3

        x_adv_mid_0 = mid_from_three_elements(x1, x2, x3)

        x_adv_min_0 = min_from_three_elements(x1, x2, x3) - 0
        x_adv_min_1 = min_from_three_elements(x1, x2, x3) - 1
        x_adv_min_2 = min_from_three_elements(x1, x2, x3) - 2
        x_adv_min_3 = min_from_three_elements(x1, x2, x3) - 3

        # a. Plus direction, and the enemy is on the boundary.
        if is_the_position_inside_of_the_board(state, [(x_adv_max_2, y_common)]):
            if state[x_adv_max_1][y_common] == opponent:
                if state[x_adv_max_2][y_common] == opponent:
                    if is_the_location_boundary(x_adv_max_2, y_common, 'x'):
                        sumito_coordinates.add((x_adv_max_0, y_common, x_adv_max_1, y_common, x_adv_mid_0, y_common))

        # b. Plus direction, and the enemy will be pushed further.
        if is_the_position_inside_of_the_board(state, [(x_adv_max_3, y_common)]):
            if state[x_adv_max_1][y_common] == opponent:
                if state[x_adv_max_2][y_common] == opponent:
                    if state[x_adv_max_3][y_common] == 0:
                        if is_the_location_empty(state, x_adv_max_3, y_common):
                            sumito_coordinates.add((x_adv_max_0, y_common, x_adv_max_1, y_common, x_adv_mid_0, y_common))

        # c. Minus direction, and the enemy is on the boundary.
        if is_the_position_inside_of_the_board(state, [(x_adv_min_2, y_common)]):
            if state[x_adv_min_1][y_common] == opponent:
                if state[x_adv_min_2][y_common] == opponent:
                    if is_the_location_boundary(x_adv_min_2, y_common, 'x'):
                        sumito_coordinates.add((x_adv_min_0, y_common, x_adv_min_1, y_common, x_adv_mid_0, y_common))

        # d. Minus direction, and the enemy will be pushed further.
        if is_the_position_inside_of_the_board(state, [(x_adv_min_3, y_common)]):
            if state[x_adv_min_1][y_common] == opponent:
                if state[x_adv_min_2][y_common] == opponent:
                    if state[x_adv_min_3][y_common] == 0:
                        if is_the_location_empty(state, x_adv_min_3, y_common):
                            sumito_coordinates.add((x_adv_min_0, y_common, x_adv_min_1, y_common, x_adv_mid_0, y_common))

    return sumito_coordinates

# Calculate 2 to 1 sumito coordinates on the direction y (x coordinates are same).
def get_2_to_1_sumito_coordinates_for_two_pieces_on_the_y_axis(state, x1, y1, x2, y2):

    # Get the color of the player.
    if state[x1][y1] == 1:
        ally = 1
        opponent = 2
    elif state[x1][y1] == 2:
        ally = 2
        opponent = 1
    else:
        return set()

    sumito_coordinates = set()

    if x1 == x2:
        x_common = x1

        y_adv_max_0 = max_from_two_elements(y1, y2) + 0
        y_adv_max_1 = max_from_two_elements(y1, y2) + 1
        y_adv_max_2 = max_from_two_elements(y1, y2) + 2

        y_adv_min_0 = min_from_two_elements(y1, y2) - 0
        y_adv_min_1 = min_from_two_elements(y1, y2) - 1
        y_adv_min_2 = min_from_two_elements(y1, y2) - 2

        # a. Plus direction, and the enemy is on the boundary.
        if is_the_position_inside_of_the_board(state, [(x_common, y_adv_max_1)]):
            if state[x_common][y_adv_max_1] == opponent:
                if is_the_location_boundary(x_common, y_adv_max_1, 'y'):
                    sumito_coordinates.add((x_common, y_adv_max_0, x_common, y_adv_max_1))

        # b. Plus direction, and the enemy will be pushed further.
        if is_the_position_inside_of_the_board(state, [(x_common, y_adv_max_2)]):
            if state[x_common][y_adv_max_1] == opponent:
                if is_the_location_empty(state, x_common, y_adv_max_2):
                    sumito_coordinates.add((x_common, y_adv_max_0, x_common, y_adv_max_1))

        # c. Minus direction, and the enemy is on the boundary.
        if is_the_position_inside_of_the_board(state, [(x_common, y_adv_min_1)]):
            if state[x_common][y_adv_min_1] == opponent:
                if is_the_location_boundary(x_common, y_adv_min_1, 'y'):
                    sumito_coordinates.add((x_common, y_adv_min_0, x_common, y_adv_min_1))

        # d. Minus direction, and the enemy will be pushed further.
        if is_the_position_inside_of_the_board(state, [(x_common, y_adv_min_2)]):
            if state[x_common][y_adv_min_1] == opponent:
                if is_the_location_empty(state, x_common, y_adv_min_2):
                    sumito_coordinates.add((x_common, y_adv_min_0, x_common, y_adv_min_1))

    return sumito_coordinates

# Calculate 3 to 1 sumito coordinates on the direction y (x coordinates are same).
def get_3_to_1_sumito_coordinates_for_three_pieces_on_the_y_axis(state, x1, y1, x2, y2, x3, y3):

    # Get the color of the player.
    if state[x1][y1] == 1:
        ally = 1
        opponent = 2
    elif state[x1][y1] == 2:
        ally = 2
        opponent = 1
    else:
        return set()

    sumito_coordinates = set()

    if x1 == x2 and x2 == x3:
        x_common = x1

        y_adv_max_0 = max_from_three_elements(y1, y2, y3) + 0
        y_adv_max_1 = max_from_three_elements(y1, y2, y3) + 1
        y_adv_max_2 = max_from_three_elements(y1, y2, y3) + 2

        y_adv_mid_0 = mid_from_three_elements(y1, y2, y3)

        y_adv_min_0 = min_from_three_elements(y1, y2, y3) - 0
        y_adv_min_1 = min_from_three_elements(y1, y2, y3) - 1
        y_adv_min_2 = min_from_three_elements(y1, y2, y3) - 2

        # a. Plus direction, and the enemy is on the boundary.
        if is_the_position_inside_of_the_board(state, [(x_common, y_adv_max_1)]):
            if state[x_common][y_adv_max_1] == opponent:
                if is_the_location_boundary(x_common, y_adv_max_1, 'y'):
                    sumito_coordinates.add((x_common, y_adv_max_0, x_common, y_adv_max_1, x_common, y_adv_mid_0))

        # b. Plus direction, and the enemy will be pushed further.
        if is_the_position_inside_of_the_board(state, [(x_common, y_adv_max_2)]):
            if state[x_common][y_adv_max_1] == opponent:
                if state[x_common][y_adv_max_2] == 0:
                    if is_the_location_empty(state, x_common, y_adv_max_2):
                        sumito_coordinates.add((x_common, y_adv_max_0, x_common, y_adv_max_1, x_common, y_adv_mid_0))

        # c. Minus direction, and the enemy is on the boundary.
        if is_the_position_inside_of_the_board(state, [(x_common, y_adv_min_1)]):
            if state[x_common][y_adv_min_1] == opponent:
                if is_the_location_boundary(x_common, y_adv_min_1, 'y'):
                    sumito_coordinates.add((x_common, y_adv_min_0, x_common, y_adv_min_1, x_common, y_adv_mid_0))

        # d. Minus direction, and the enemy will be pushed further.
        if is_the_position_inside_of_the_board(state, [(x_common, y_adv_min_2)]):
            if state[x_common][y_adv_min_1] == opponent:
                if state[x_common][y_adv_min_2] == 0:
                    if is_the_location_empty(state, x_common, y_adv_min_2):
                        sumito_coordinates.add((x_common, y_adv_min_0, x_common, y_adv_min_1, x_common, y_adv_mid_0))

    return sumito_coordinates

# Calculate 3 to 2 sumito coordinates on the direction y (x coordinates are same).
def get_3_to_2_sumito_coordinates_for_three_pieces_on_the_y_axis(state, x1, y1, x2, y2, x3, y3):

    # Get the color of the player.
    if state[x1][y1] == 1:
        ally = 1
        opponent = 2
    elif state[x1][y1] == 2:
        ally = 2
        opponent = 1
    else:
        return set()

    sumito_coordinates = set()

    if x1 == x2 and x2 == x3:
        x_common = x1

        y_adv_max_0 = max_from_three_elements(y1, y2, y3) + 0
        y_adv_max_1 = max_from_three_elements(y1, y2, y3) + 1
        y_adv_max_2 = max_from_three_elements(y1, y2, y3) + 2
        y_adv_max_3 = max_from_three_elements(y1, y2, y3) + 3

        y_adv_mid_0 = mid_from_three_elements(y1, y2, y3)

        y_adv_min_0 = min_from_three_elements(y1, y2, y3) - 0
        y_adv_min_1 = min_from_three_elements(y1, y2, y3) - 1
        y_adv_min_2 = min_from_three_elements(y1, y2, y3) - 2
        y_adv_min_3 = min_from_three_elements(y1, y2, y3) - 3

        # a. Plus direction, and the enemy is on the boundary.
        if is_the_position_inside_of_the_board(state, [(x_common, y_adv_max_2)]):
            if state[x_common][y_adv_max_1] == opponent:
                if state[x_common][y_adv_max_2] == opponent:
                    if is_the_location_boundary(x_common, y_adv_max_2, 'y'):
                        sumito_coordinates.add((x_common, y_adv_max_0, x_common, y_adv_max_1, x_common, y_adv_mid_0))

        # b. Plus direction, and the enemy will be pushed further.
        if is_the_position_inside_of_the_board(state, [(x_common, y_adv_max_3)]):
            if state[x_common][y_adv_max_1] == opponent:
                if state[x_common][y_adv_max_2] == opponent:
                    if state[x_common][y_adv_max_3] == 0:
                        if is_the_location_empty(state, x_common, y_adv_max_3):
                            sumito_coordinates.add((x_common, y_adv_max_0, x_common, y_adv_max_1, x_common, y_adv_mid_0))

        # c. Minus direction, and the enemy is on the boundary.
        if is_the_position_inside_of_the_board(state, [(x_common, y_adv_min_2)]):
            if state[x_common][y_adv_min_1] == opponent:
                if state[x_common][y_adv_min_2] == opponent:
                    if is_the_location_boundary(x_common, y_adv_min_2, 'y'):
                        sumito_coordinates.add((x_common, y_adv_min_0, x_common, y_adv_min_1, x_common, y_adv_mid_0))

        # d. Minus direction, and the enemy will be pushed further.
        if is_the_position_inside_of_the_board(state, [(x_common, y_adv_min_3)]):
            if state[x_common][y_adv_min_1] == opponent:
                if state[x_common][y_adv_min_2] == opponent:
                    if state[x_common][y_adv_min_3] == 0:
                        if is_the_location_empty(state, x_common, y_adv_min_3):
                            sumito_coordinates.add((x_common, y_adv_min_0, x_common, y_adv_min_1, x_common, y_adv_mid_0))

    return sumito_coordinates

# Calculate 2 to 1 sumito coordinates on the direction z (multi-factored with x and y).
def get_2_to_1_sumito_coordinates_for_two_pieces_on_the_z_axis(state, x1, y1, x2, y2):

    # Get the color of the player.
    if state[x1][y1] == 1:
        ally = 1
        opponent = 2
    elif state[x1][y1] == 2:
        ally = 2
        opponent = 1
    else:
        return set()

    sumito_coordinates = set()

    if (x1 + 1 == x2 and y1 - 1 == y2) or (x2 + 1 == x1 and y2 - 1 == y1):

        x_adv_max_0 = max_from_two_elements(x1, x2) + 0
        x_adv_max_1 = max_from_two_elements(x1, x2) + 1
        x_adv_max_2 = max_from_two_elements(x1, x2) + 2

        x_adv_min_0 = min_from_two_elements(x1, x2) - 0
        x_adv_min_1 = min_from_two_elements(x1, x2) - 1
        x_adv_min_2 = min_from_two_elements(x1, x2) - 2

        y_adv_max_0 = min_from_two_elements(y1, y2) - 0
        y_adv_max_1 = min_from_two_elements(y1, y2) - 1
        y_adv_max_2 = min_from_two_elements(y1, y2) - 2

        y_adv_min_0 = max_from_two_elements(y1, y2) + 0
        y_adv_min_1 = max_from_two_elements(y1, y2) + 1
        y_adv_min_2 = max_from_two_elements(y1, y2) + 2

        # a. Plus direction, and the enemy is on the boundary.
        if is_the_position_inside_of_the_board(state, [(x_adv_max_1, y_adv_max_1)]):
            if state[x_adv_max_1][y_adv_max_1] == opponent:
                if is_the_location_boundary(x_adv_max_1, y_adv_max_1, 'z'):
                    sumito_coordinates.add((x_adv_max_0, y_adv_max_0, x_adv_max_1, y_adv_max_1))

        # b. Plus direction, and the enemy will be pushed further.
        if is_the_position_inside_of_the_board(state, [(x_adv_max_2, y_adv_max_2)]):
            if state[x_adv_max_1][y_adv_max_1] == opponent:
                if is_the_location_empty(state, x_adv_max_2, y_adv_max_2):
                    sumito_coordinates.add((x_adv_max_0, y_adv_max_0, x_adv_max_1, y_adv_max_1))

        # c. Minus direction, and the enemy is on the boundary.
        if is_the_position_inside_of_the_board(state, [(x_adv_min_1, y_adv_min_1)]):
            if state[x_adv_min_1][y_adv_min_1] == opponent:
                if is_the_location_boundary(x_adv_min_1, y_adv_min_1, 'z'):
                    sumito_coordinates.add((x_adv_min_0, y_adv_min_0, x_adv_min_1, y_adv_min_1))

        # d. Minus direction, and the enemy will be pushed further.
        if is_the_position_inside_of_the_board(state, [(x_adv_min_2, y_adv_min_2)]):
            if state[x_adv_min_1][y_adv_min_1] == opponent:
                if is_the_location_empty(state, x_adv_min_2, y_adv_min_2):
                    sumito_coordinates.add((x_adv_min_0, y_adv_min_0, x_adv_min_1, y_adv_min_1))

    return sumito_coordinates

# Calculate 3 to 1 sumito coordinates on the direction z (multi-factored with x and y).
def get_3_to_1_sumito_coordinates_for_three_pieces_on_the_z_axis(state, x1, y1, x2, y2, x3, y3):

    # Get the color of the player.
    if state[x1][y1] == 1:
        ally = 1
        opponent = 2
    elif state[x1][y1] == 2:
        ally = 2
        opponent = 1
    else:
        return set()

    sumito_coordinates = set()

    if get_3_to_1_sumito_coordinates_for_three_pieces_on_the_x_axis(state, x1, y1, x2, y2, x3, y3) == set() and \
            get_3_to_1_sumito_coordinates_for_three_pieces_on_the_y_axis(state, x1, y1, x2, y2, x3, y3) == set():

        # Check if this is on z-axis.
        if (x1 == x2 and x2 == x3) or (y1 == y2 and y2 == y3):
            return sumito_coordinates

        x_adv_max_0 = max_from_three_elements(x1, x2, x3) + 0
        x_adv_max_1 = max_from_three_elements(x1, x2, x3) + 1
        x_adv_max_2 = max_from_three_elements(x1, x2, x3) + 2

        x_adv_mid_0 = mid_from_three_elements(x1, x2, x3)

        x_adv_min_0 = min_from_three_elements(x1, x2, x3) - 0
        x_adv_min_1 = min_from_three_elements(x1, x2, x3) - 1
        x_adv_min_2 = min_from_three_elements(x1, x2, x3) - 2

        y_adv_max_0 = min_from_three_elements(y1, y2, y3) - 0
        y_adv_max_1 = min_from_three_elements(y1, y2, y3) - 1
        y_adv_max_2 = min_from_three_elements(y1, y2, y3) - 2

        y_adv_mid_0 = mid_from_three_elements(y1, y2, y3)

        y_adv_min_0 = max_from_three_elements(y1, y2, y3) + 0
        y_adv_min_1 = max_from_three_elements(y1, y2, y3) + 1
        y_adv_min_2 = max_from_three_elements(y1, y2, y3) + 2

        # a. Plus direction, and the enemy is on the boundary.
        if is_the_position_inside_of_the_board(state, [(x_adv_max_1, y_adv_max_1)]):
            if state[x_adv_max_1][y_adv_max_1] == opponent:
                if is_the_location_boundary(x_adv_max_1, y_adv_max_1, 'z'):
                    sumito_coordinates.add((x_adv_max_0, y_adv_max_0, x_adv_max_1, y_adv_max_1, x_adv_mid_0, y_adv_mid_0))

        # b. Plus direction, and the enemy will be pushed further.
        if is_the_position_inside_of_the_board(state, [(x_adv_max_2, y_adv_max_2)]):
            if state[x_adv_max_1][y_adv_max_1] == opponent:
                if state[x_adv_max_2][y_adv_max_2] == 0:
                    if is_the_location_empty(state, x_adv_max_2, y_adv_max_2):
                        sumito_coordinates.add((x_adv_max_0, y_adv_max_0, x_adv_max_1, y_adv_max_1, x_adv_mid_0, y_adv_mid_0))

        # c. Minus direction, and the enemy is on the boundary.
        if is_the_position_inside_of_the_board(state, [(x_adv_min_1, y_adv_min_1)]):
            if state[x_adv_min_1][y_adv_min_1] == opponent:
                if is_the_location_boundary(x_adv_min_1, y_adv_min_1, 'z'):
                    sumito_coordinates.add((x_adv_min_0, y_adv_min_0, x_adv_min_1, y_adv_min_1, x_adv_mid_0, y_adv_mid_0))

        # d. Minus direction, and the enemy will be pushed further.
        if is_the_position_inside_of_the_board(state, [(x_adv_min_2, y_adv_min_2)]):
            if state[x_adv_min_1][y_adv_min_1] == opponent:
                if state[x_adv_min_2][y_adv_min_2] == 0:
                    if is_the_location_empty(state, x_adv_min_2, y_adv_min_2):
                        sumito_coordinates.add((x_adv_min_0, y_adv_min_0, x_adv_min_1, y_adv_min_1, x_adv_mid_0, y_adv_mid_0))

    return sumito_coordinates


# Calculate 3 to 2 sumito coordinates on the direction z (multi-factored with x and y).
def get_3_to_2_sumito_coordinates_for_three_pieces_on_the_z_axis(state, x1, y1, x2, y2, x3, y3):

    # Get the color of the player.
    if state[x1][y1] == 1:
        ally = 1
        opponent = 2
    elif state[x1][y1] == 2:
        ally = 2
        opponent = 1
    else:
        return set()

    sumito_coordinates = set()

    if get_3_to_2_sumito_coordinates_for_three_pieces_on_the_x_axis(state, x1, y1, x2, y2, x3, y3) == set() and \
            get_3_to_2_sumito_coordinates_for_three_pieces_on_the_y_axis(state, x1, y1, x2, y2, x3, y3) == set():

        # Check if this is on z-axis.
        if (x1 == x2 and x2 == x3) or (y1 == y2 and y2 == y3):
            return sumito_coordinates

        x_adv_max_0 = max_from_three_elements(x1, x2, x3) + 0
        x_adv_max_1 = max_from_three_elements(x1, x2, x3) + 1
        x_adv_max_2 = max_from_three_elements(x1, x2, x3) + 2
        x_adv_max_3 = max_from_three_elements(x1, x2, x3) + 3

        x_adv_mid_0 = mid_from_three_elements(x1, x2, x3)

        x_adv_min_0 = min_from_three_elements(x1, x2, x3) - 0
        x_adv_min_1 = min_from_three_elements(x1, x2, x3) - 1
        x_adv_min_2 = min_from_three_elements(x1, x2, x3) - 2
        x_adv_min_3 = min_from_three_elements(x1, x2, x3) - 3

        y_adv_max_0 = min_from_three_elements(y1, y2, y3) - 0
        y_adv_max_1 = min_from_three_elements(y1, y2, y3) - 1
        y_adv_max_2 = min_from_three_elements(y1, y2, y3) - 2
        y_adv_max_3 = min_from_three_elements(y1, y2, y3) - 3

        y_adv_mid_0 = mid_from_three_elements(y1, y2, y3)

        y_adv_min_0 = max_from_three_elements(y1, y2, y3) + 0
        y_adv_min_1 = max_from_three_elements(y1, y2, y3) + 1
        y_adv_min_2 = max_from_three_elements(y1, y2, y3) + 2
        y_adv_min_3 = max_from_three_elements(y1, y2, y3) + 3

        # a. Plus direction, and the enemy is on the boundary.
        if is_the_position_inside_of_the_board(state, [(x_adv_max_2, y_adv_max_2)]):
            if state[x_adv_max_1][y_adv_max_1] == opponent:
                if state[x_adv_max_2][y_adv_max_2] == opponent:
                    if is_the_location_boundary(x_adv_max_2, y_adv_max_2, 'z'):
                        sumito_coordinates.add((x_adv_max_0, y_adv_max_0, x_adv_max_1, y_adv_max_1, x_adv_mid_0, y_adv_mid_0))

        # b. Plus direction, and the enemy will be pushed further.
        if is_the_position_inside_of_the_board(state, [(x_adv_max_3, y_adv_max_3)]):
            if state[x_adv_max_1][y_adv_max_1] == opponent:
                if state[x_adv_max_2][y_adv_max_2] == opponent:
                    if state[x_adv_max_3][y_adv_max_3] == 0:
                        if is_the_location_empty(state, x_adv_max_3, y_adv_max_3):
                            sumito_coordinates.add((x_adv_max_0, y_adv_max_0, x_adv_max_1, y_adv_max_1, x_adv_mid_0, y_adv_mid_0))

        # c. Minus direction, and the enemy is on the boundary.
        if is_the_position_inside_of_the_board(state, [(x_adv_min_2, y_adv_min_2)]):
            if state[x_adv_min_1][y_adv_min_1] == opponent:
                if state[x_adv_min_2][y_adv_min_2] == opponent:
                    if is_the_location_boundary(x_adv_min_2, y_adv_min_2, 'z'):
                        sumito_coordinates.add((x_adv_min_0, y_adv_min_0, x_adv_min_1, y_adv_min_1, x_adv_mid_0, y_adv_mid_0))

        # d. Minus direction, and the enemy will be pushed further.
        if is_the_position_inside_of_the_board(state, [(x_adv_min_3, y_adv_min_3)]):
            if state[x_adv_min_1][y_adv_min_1] == opponent:
                if state[x_adv_min_2][y_adv_min_2] == opponent:
                    if state[x_adv_min_3][y_adv_min_3] == 0:
                        if is_the_location_empty(state, x_adv_min_3, y_adv_min_3):
                            sumito_coordinates.add((x_adv_min_0, y_adv_min_0, x_adv_min_1, y_adv_min_1, x_adv_mid_0, y_adv_mid_0))

    return sumito_coordinates



# ================ ================ Utility Functions ================ ================


# Determine whether the location is currently empty.
def is_the_location_empty(state, x, y):
    if state[x][y] == 0:
        return True
    return False

# Determine whether the location is on the boundary.
def is_the_location_boundary(x, y, direction):

    global global_game_board_boundary_for_all
    global global_game_board_boundary_for_x
    global global_game_board_boundary_for_y
    global global_game_board_boundary_for_z

    if 'all' == direction:
        if (x, y) in global_game_board_boundary_for_all:
            return True
    elif 'x' == direction:
        if (x, y) in global_game_board_boundary_for_x:
            return True
    elif 'y' == direction:
        if (x, y) in global_game_board_boundary_for_y:
            return True
    elif 'z' == direction:
        if (x, y) in global_game_board_boundary_for_z:
            return True

    return False

# Find the maximum value from two elements.
def max_from_two_elements(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    if a == b:
        return a

# Find the maximum value from three elements.
def max_from_three_elements(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    if a == b and b == c:
        return a

# Find the minimum value from two elements.
def min_from_two_elements(a, b):
    if a < b:
        return a
    elif b < a:
        return b
    if a == b:
        return a

# Find the minimum value from three elements.
def min_from_three_elements(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    elif c < a and c < b:
        return c
    if a == b and b == c:
        return a

# Find the middle value from three elements.
def mid_from_three_elements(a, b, c):
    if (a < b and a > c) or (a > b and a < c):
        return a
    elif (b < a and b > c) or (b > a and b < c):
        return b
    elif (c < a and c > b) or (c > a and c < b):
        return c


# Determine whether two pieces inline.
def is_two_pieces_inline(x1, y1, x2, y2):

    # Find out if it's inline.
    if x1 + 1 == x2 and y1 - 1 == y2:
        return True
    elif x1 + 1 == x2 and y1 + 0 == y2:
        return True
    elif x1 + 0 == x2 and y1 + 1 == y2:
        return True
    elif x2 + 1 == x1 and y2 - 1 == y1:
        return True
    elif x2 + 1 == x1 and y2 + 0 == y1:
        return True
    elif x2 + 0 == x1 and y2 + 1 == y1:
        return True

    return False

# Determine whether three pieces inline.
def is_three_pieces_inline(x1, y1, x2, y2, x3, y3):

    # If all the pieces are not all inlines, then return false.
    how_many_are_inline = 0
    if is_two_pieces_inline(x1, y1, x2, y2):
        how_many_are_inline += 1

    if is_two_pieces_inline(x1, y1, x3, y3):
        how_many_are_inline += 1

    if is_two_pieces_inline(x2, y2, x3, y3):
        how_many_are_inline += 1

    if how_many_are_inline != 2:
        return False

    # Find out if it's inline.
    if x1 == (x2 + x3) / 2 and y1 == (y2 + y3) / 2:
        return True

    if x2 == (x1 + x3) / 2 and y2 == (y1 + y3) / 2:
        return True

    if x3 == (x1 + x2) / 2 and y3 == (y1 + y2) / 2:
        return True

    return False

# Determine whether the position is currently empty or going to be empty in move.
# positions is a list of tuples: [(x1, y1), (x2, y2), (x3, y3),...]
# exceptions is a list of tuples: [(x1, y1), (x2, y2), (x3, y3),...]
def is_the_position_empty_or_going_to_be_empty(state, positions, exceptions):
    for position in positions:
        if search_in_coordinates_tuples_list((position[0], position[1]), exceptions) == False:
            if state[position[0]][position[1]] != 0:
                return False
    return True

# Search if the coordinates is in the list.
def search_in_coordinates_tuples_list(key, list):
    for item in list:
        if key == item:
            return True
    return False

# Determine whether the position is out of board.
# positions is a list of tuples: [(x1, y1), (x2, y2), (x3, y3),...]
def is_the_position_inside_of_the_board(state, positions):
    for position in positions:
        if position[0] < 0 or position[0] > 8 or position[1] < 0 or position[1] > 8:
            return False
        if state[position[0]][position[1]] == -9:
            return False
    return True




