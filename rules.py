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
def apply_rules_for_move_2_to_1_sumito():
    #TODO
    return True

# Apply rules for move 3 to 1 or 3 to 2 sumito.
def apply_rules_for_move_3_to_1_or_3_to_2_sumito():
    #TODO
    return True


# ================ ================ Legal Movement Generation ================ ================

def generate_all_possible_legal_moves_for_one_piece(x1, y1):
    possible_moves = set()

    # Upper-Right.
    if is_the_position_inside_of_the_board([(x1 + 1, y1 - 1)]):
        if is_the_position_empty_or_going_to_be_empty([(x1 + 1, y1 - 1)], []):
            possible_moves.add((x1 + 1, y1 - 1))
    # Right.
    if is_the_position_inside_of_the_board([(x1 + 1, y1 + 0)]):
        if is_the_position_empty_or_going_to_be_empty([(x1 + 1, y1 + 0)], []):
            possible_moves.add((x1 + 1, y1 + 0))
    # Lower-Right.
    if is_the_position_inside_of_the_board([(x1 + 0, y1 + 1)]):
        if is_the_position_empty_or_going_to_be_empty([(x1 + 0, y1 + 1)], []):
            possible_moves.add((x1 + 0, y1 + 1))
    # Lower_Left.
    if is_the_position_inside_of_the_board([(x1 - 1, y1 + 1)]):
        if is_the_position_empty_or_going_to_be_empty([(x1 - 1, y1 + 1)], []):
            possible_moves.add((x1 - 1, y1 + 1))
    # Left.
    if is_the_position_inside_of_the_board([(x1 - 1, y1 + 0)]):
        if is_the_position_empty_or_going_to_be_empty([(x1 - 1, y1 + 0)], []):
            possible_moves.add((x1 - 1, y1 + 0))
    # Upper-Left.
    if is_the_position_inside_of_the_board([(x1 + 0, y1 - 1)]):
        if is_the_position_empty_or_going_to_be_empty([(x1 + 0, y1 - 1)], []):
            possible_moves.add((x1 + 0, y1 - 1))

    return possible_moves



def generate_all_possible_legal_moves_for_two_pieces(x1, y1, x2, y2):
    possible_moves = set()
    if is_two_pieces_inline(x1, y1, x2, y2):
        # Upper-Right.
        if is_the_position_inside_of_the_board([(x1 + 1, y1 - 1), (x2 + 1, y2 - 1)]):
            if is_the_position_empty_or_going_to_be_empty([(x1 + 1, y1 - 1), (x2 + 1, y2 - 1)], [(x1, y1), (x2, y2)]):
                possible_moves.add((x1 + 1, y1 - 1, x2 + 1, y2 - 1))
        # Right.
        if is_the_position_inside_of_the_board([(x1 + 1, y1 + 0), (x2 + 1, y2 + 0)]):
            if is_the_position_empty_or_going_to_be_empty([(x1 + 1, y1 + 0), (x2 + 1, y2 + 0)], [(x1, y1), (x2, y2)]):
                possible_moves.add((x1 + 1, y1 + 0, x2 + 1, y2 + 0))
        # Lower-Right.
        if is_the_position_inside_of_the_board([(x1 + 0, y1 + 1), (x2 + 0, y2 + 1)]):
            if is_the_position_empty_or_going_to_be_empty([(x1 + 0, y1 + 1), (x2 + 0, y2 + 1)], [(x1, y1), (x2, y2)]):
                possible_moves.add((x1 + 0, y1 + 1, x2 + 0, y2 + 1))
        # Lower_Left.
        if is_the_position_inside_of_the_board([(x1 - 1, y1 + 1), (x2 - 1, y2 + 1)]):
            if is_the_position_empty_or_going_to_be_empty([(x1 - 1, y1 + 1), (x2 - 1, y2 + 1)], [(x1, y1), (x2, y2)]):
                possible_moves.add((x1 - 1, y1 + 1, x2 - 1, y2 + 1))
        # Left.
        if is_the_position_inside_of_the_board([(x1 - 1, y1 + 0), (x2 - 1, y2 + 0)]):
            if is_the_position_empty_or_going_to_be_empty([(x1 - 1, y1 + 0), (x2 - 1, y2 + 0)], [(x1, y1), (x2, y2)]):
                possible_moves.add((x1 - 1, y1 + 0, x2 - 1, y2 + 0))
        # Upper-Left.
        if is_the_position_inside_of_the_board([(x1 + 0, y1 - 1), (x2 + 0, y2 - 1)]):
            if is_the_position_empty_or_going_to_be_empty([(x1 + 0, y1 - 1), (x2 + 0, y2 - 1)], [(x1, y1), (x2, y2)]):
                possible_moves.add((x1 + 0, y1 - 1, x2 + 0, y2 - 1))

    return possible_moves


def generate_all_possible_legal_moves_for_three_pieces(x1, y1, x2, y2, x3, y3):
    possible_moves = set()
    if is_three_pieces_inline(x1, y1, x2, y2, x3, y3):
        # Upper-Right.
        if is_the_position_inside_of_the_board([(x1 + 1, y1 - 1), (x2 + 1, y2 - 1), (x3 + 1, y3 - 1)]):
            if is_the_position_empty_or_going_to_be_empty([(x1 + 1, y1 - 1), (x2 + 1, y2 - 1), (x3 + 1, y3 - 1)], [(x1, y1), (x2, y2), (x3, y3)]):
                possible_moves.add((x1 + 1, y1 - 1, x2 + 1, y2 - 1, x3 + 1, y3 - 1))
        # Right.
        if is_the_position_inside_of_the_board([(x1 + 1, y1 + 0), (x2 + 1, y2 + 0), (x3 + 1, y3 + 0)]):
            if is_the_position_empty_or_going_to_be_empty([(x1 + 1, y1 + 0), (x2 + 1, y2 + 0), (x3 + 1, y3 + 0)], [(x1, y1), (x2, y2), (x3, y3)]):
                possible_moves.add((x1 + 1, y1 + 0, x2 + 1, y2 + 0, x3 + 1, y3 + 0))
        # Lower-Right.
        if is_the_position_inside_of_the_board([(x1 + 0, y1 + 1), (x2 + 0, y2 + 1), (x3 + 0, y3 + 1)]):
            if is_the_position_empty_or_going_to_be_empty([(x1 + 0, y1 + 1), (x2 + 0, y2 + 1), (x3 + 0, y3 + 1)], [(x1, y1), (x2, y2), (x3, y3)]):
                possible_moves.add((x1 + 0, y1 + 1, x2 + 0, y2 + 1, x3 + 0, y3 + 1))
        # Lower_Left.
        if is_the_position_inside_of_the_board([(x1 - 1, y1 + 1), (x2 - 1, y2 + 1), (x3 - 1, y3 + 1)]):
            if is_the_position_empty_or_going_to_be_empty([(x1 - 1, y1 + 1), (x2 - 1, y2 + 1), (x3 - 1, y3 + 1)], [(x1, y1), (x2, y2), (x3, y3)]):
                possible_moves.add((x1 - 1, y1 + 1, x2 - 1, y2 + 1, x3 - 1, y3 + 1))
        # Left.
        if is_the_position_inside_of_the_board([(x1 - 1, y1 + 0), (x2 - 1, y2 + 0), (x3 - 1, y3 + 0)]):
            if is_the_position_empty_or_going_to_be_empty([(x1 - 1, y1 + 0), (x2 - 1, y2 + 0), (x3 - 1, y3 + 0)], [(x1, y1), (x2, y2), (x3, y3)]):
                possible_moves.add((x1 - 1, y1 + 0, x2 - 1, y2 + 0, x3 - 1, y3 + 0))
        # Upper-Left.
        if is_the_position_inside_of_the_board([(x1 + 0, y1 - 1), (x2 + 0, y2 - 1), (x3 + 0, y3 - 1)]):
            if is_the_position_empty_or_going_to_be_empty([(x1 + 0, y1 - 1), (x2 + 0, y2 - 1), (x3 + 0, y3 - 1)], [(x1, y1), (x2, y2), (x3, y3)]):
                possible_moves.add((x1 + 0, y1 - 1, x2 + 0, y2 - 1, x3 + 0, y3 - 1))

    return possible_moves




def generate_all_2_to_1_legal_sumitos(x1, y1, x2, y2):
    possible_moves = set()
    if is_two_pieces_inline(x1, y1, x2, y2):
        pass
        #TODO

    return possible_moves

def generate_all_3_to_1_legal_sumitos(x1, y1, x2, y2, x3, y3):
    possible_moves = set()
    if is_three_pieces_inline(x1, y1, x2, y2, x3, y3):
        pass
        #TODO

    return possible_moves

def generate_all_3_to_2_legal_sumitos(x1, y1, x2, y2, x3, y3):
    possible_moves = set()
    if is_three_pieces_inline(x1, y1, x2, y2, x3, y3):
        pass
        #TODO

    return possible_moves


# ================ ================ Utility Functions ================ ================

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
def is_the_position_empty_or_going_to_be_empty(positions, exceptions):
    for position in positions:
        if search_in_coordinates_tuples_list((position[0], position[1]), exceptions) == False:
            if model.global_game_board_state[position[0]][position[1]] != 0:
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
def is_the_position_inside_of_the_board(positions):
    for position in positions:
        if position[0] < 0 or position[0] > 8 or position[1] < 0 or position[1] > 8:
            return False
        if model.global_game_board_state[position[0]][position[1]] == -9:
            return False
    return True







