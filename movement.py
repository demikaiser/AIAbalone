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

import model, rules

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

# Move 2 to 1 sumito.
def move_2_to_1_sumito(old_x1, old_y1, new_x1, new_y1,
                       old_x2, old_y2, new_x2, new_y2):
    # Get the clicked position.
    clicked_position = get_the_differences_from_sets_for_sumitos({(new_x1, new_y1), (new_x2, new_y2)},
                                                                 {(old_x1, old_y1), (old_x2, old_y2)})
    clicked_x = clicked_position[0]
    clicked_y = clicked_position[1]

    # Get the moved position.
    moved_position = get_the_differences_from_sets_for_sumitos({(old_x1, old_y1), (old_x2, old_y2)},
                                                               {(new_x1, new_y1), (new_x2, new_y2)})
    removed_x = moved_position[0]
    removed_y = moved_position[1]

    # Store 2 advanced coordinates for piece advancement.
    advanced_coordinates = []

    # Find out the directions and populate advanced_coordinates.
    if removed_y == clicked_y:

        if clicked_x > removed_x:
            advanced_coordinates.append((clicked_x + 1, clicked_y))
            advanced_coordinates.append((clicked_x + 2, clicked_y))
        elif clicked_x < removed_x:
            advanced_coordinates.append((clicked_x - 1, clicked_y))
            advanced_coordinates.append((clicked_x - 2, clicked_y))

    elif removed_x == clicked_x:

        if clicked_y > removed_y:
            advanced_coordinates.append((clicked_x, clicked_y + 1))
            advanced_coordinates.append((clicked_x, clicked_y + 2))
        elif clicked_y < removed_y:
            advanced_coordinates.append((clicked_x, clicked_y - 1))
            advanced_coordinates.append((clicked_x, clicked_y - 2))
    else:

        if clicked_x > removed_x:
            advanced_coordinates.append((clicked_x + 1, clicked_y - 1))
            advanced_coordinates.append((clicked_x + 2, clicked_y - 2))
        elif clicked_x < removed_x:
            advanced_coordinates.append((clicked_x - 1, clicked_y + 1))
            advanced_coordinates.append((clicked_x - 2, clicked_y + 2))

    # Memorize the opponent piece.
    piece_opponent = model.global_game_board_state[clicked_x][clicked_y]

    # Memorize the old pieces.
    piece1 = model.global_game_board_state[old_x1][old_y1]
    piece2 = model.global_game_board_state[old_x2][old_y2]

    # Remove the old pieces.
    model.global_game_board_state[old_x1][old_y1] = 0
    model.global_game_board_state[old_x2][old_y2] = 0

    # Place the pieces to new location.
    model.global_game_board_state[new_x1][new_y1] = piece1
    model.global_game_board_state[new_x2][new_y2] = piece2

    # Place the opponent piece to the advanced position.
    if (rules.is_the_position_inside_of_the_board([advanced_coordinates[0]])):
        adv_x = advanced_coordinates[0][0]
        adv_y = advanced_coordinates[0][1]
        model.global_game_board_state[adv_x][adv_y] = piece_opponent

# Move 3 to 1 or 3 to 2 sumito.
def move_3_to_1_or_3_to_2_sumito(old_x1, old_y1, new_x1, new_y1,
                                 old_x2, old_y2, new_x2, new_y2,
                                 old_x3, old_y3, new_x3, new_y3):
    # Get the clicked position.
    clicked_position = get_the_differences_from_sets_for_sumitos({(new_x1, new_y1), (new_x2, new_y2), (new_x3, new_y3)},
                                                                 {(old_x1, old_y1), (old_x2, old_y2), (old_x3, old_y3)})
    clicked_x = clicked_position[0]
    clicked_y = clicked_position[1]

    # Get the moved position.
    moved_position = get_the_differences_from_sets_for_sumitos({(old_x1, old_y1), (old_x2, old_y2), (old_x3, old_y3)},
                                                               {(new_x1, new_y1), (new_x2, new_y2), (new_x3, new_y3)})
    removed_x = moved_position[0]
    removed_y = moved_position[1]

    # Store 3 advanced coordinates for piece advancement.
    advanced_coordinates = []

    # Find out the directions and populate advanced_coordinates.
    if removed_y == clicked_y:

        if clicked_x > removed_x:
            advanced_coordinates.append((clicked_x + 1, clicked_y))
            advanced_coordinates.append((clicked_x + 2, clicked_y))
            advanced_coordinates.append((clicked_x + 3, clicked_y))
        elif clicked_x < removed_x:
            advanced_coordinates.append((clicked_x - 1, clicked_y))
            advanced_coordinates.append((clicked_x - 2, clicked_y))
            advanced_coordinates.append((clicked_x - 3, clicked_y))

    elif removed_x == clicked_x:

        if clicked_y > removed_y:
            advanced_coordinates.append((clicked_x, clicked_y + 1))
            advanced_coordinates.append((clicked_x, clicked_y + 2))
            advanced_coordinates.append((clicked_x, clicked_y + 3))
        elif clicked_y < removed_y:
            advanced_coordinates.append((clicked_x, clicked_y - 1))
            advanced_coordinates.append((clicked_x, clicked_y - 2))
            advanced_coordinates.append((clicked_x, clicked_y - 3))
    else:

        if clicked_x > removed_x:
            advanced_coordinates.append((clicked_x + 1, clicked_y - 1))
            advanced_coordinates.append((clicked_x + 2, clicked_y - 2))
            advanced_coordinates.append((clicked_x + 3, clicked_y - 3))
        elif clicked_x < removed_x:
            advanced_coordinates.append((clicked_x - 1, clicked_y + 1))
            advanced_coordinates.append((clicked_x - 2, clicked_y + 2))
            advanced_coordinates.append((clicked_x - 3, clicked_y + 3))

    # Find whether this is 3 to 1 or 3 to 2 sumito.
    # 1. 3 to 1 sumito.
    if rules.generate_all_3_to_1_legal_sumitos(old_x1, old_y1, old_x2, old_y2, old_x3, old_y3) != set():

        print("3-1")
        print(rules.generate_all_3_to_1_legal_sumitos(old_x1, old_y1, old_x2, old_y2, old_x3, old_y3))

        # Memorize the opponent piece.
        piece_opponent = model.global_game_board_state[clicked_x][clicked_y]

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

        # Place the opponent piece to the advanced position.
        if (rules.is_the_position_inside_of_the_board([advanced_coordinates[0]])):
            adv_x = advanced_coordinates[0][0]
            adv_y = advanced_coordinates[0][1]
            model.global_game_board_state[adv_x][adv_y] = piece_opponent


    # 2. 3 to 2 sumito (Normal descriptive statements omitted for computing efficiency).
    else:

        # Memorize the opponent pieces.
        piece_opponent_1 = model.global_game_board_state[clicked_x][clicked_y]
        piece_opponent_2 = model.global_game_board_state[advanced_coordinates[0][0]][advanced_coordinates[0][1]]

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

        # Place the opponent piece 1 to the advanced position.
        if (rules.is_the_position_inside_of_the_board([advanced_coordinates[0]])):
            adv_x_1 = advanced_coordinates[0][0]
            adv_y_1 = advanced_coordinates[0][1]
            model.global_game_board_state[adv_x_1][adv_y_1] = piece_opponent_1

        # Place the opponent piece 2 to the advanced position.
        if (rules.is_the_position_inside_of_the_board([advanced_coordinates[1]])):
            adv_x_2 = advanced_coordinates[1][0]
            adv_y_2 = advanced_coordinates[1][1]
            model.global_game_board_state[adv_x_2][adv_y_2] = piece_opponent_2

        print("3-2")

# ================ ================ Utility Functions ================ ================


# Get the differences from sets for sumitos to get rid of clicked input from gui.
def get_the_differences_from_sets_for_sumitos(positions_1, positions_2):

    new_set = positions_1.difference(positions_2)
    return new_set.pop()



##################################### TEMPORARY TESTS #########################################



