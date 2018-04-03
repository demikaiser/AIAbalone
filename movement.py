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

import model, rules, gameboard

# Representation converter from this project's
# to chiens board representation (Output Processing Data Structure - 2D Lists).
chiens_board_representation_output = [
    [-9, -9, -9, -9, "E1", "D1", "C1", "B1", "A1"],
    [-9, -9, -9, "F2", "E2", "D2", "C2", "B2", "A2"],
    [-9, -9, "G3", "F3", "E3", "D3", "C3", "B3", "A3"],
    [-9, "H4", "G4", "F4", "E4", "D4", "C4", "B4", "A4"],
    ["I5", "H5", "G5", "F5", "E5", "D5", "C5", "B5", "A5"],
    ["I6", "H6", "G6", "F6", "E6", "D6", "C6", "B6", -9],
    ["I7", "H7", "G7", "F7", "E7", "D7", "C7", -9, -9],
    ["I8", "H8", "G8", "F8", "E8", "D8", -9, -9, -9],
    ["I9", "H9", "G9", "F9", "E9", -9, -9, -9, -9]
]

# Move one piece.
def move_one_piece(old_x, old_y, new_x, new_y, context):

    # Memorize the old piece.
    piece = model.global_game_board_state[old_x][old_y]

    # Remove the old piece.
    model.global_game_board_state[old_x][old_y] = 0

    # Place the piece to new location.
    model.global_game_board_state[new_x][new_y] = piece

    # Increase the score and taken moves for each side.
    if model.global_game_board_state[new_x][new_y] == 1:
        gameboard.update_moves_taken_for('black')
    elif model.global_game_board_state[new_x][new_y] == 2:
        gameboard.update_moves_taken_for('white')
    gameboard.update_game_score()

    # Log the movement information.
    messages = []
    if model.global_game_board_state[new_x][new_y] == 1:
        messages.append("Black made movement as the following:")
    elif model.global_game_board_state[new_x][new_y] == 2:
        messages.append("White made movement as the following:")

    messages.append("STD From : " + str(chiens_board_representation_output[old_x][old_y]))
    messages.append("STD To   : " + str(chiens_board_representation_output[new_x][new_y]))

    messages.append("From : (" + str(old_x) + "," + str(old_y) + ")")
    messages.append("To   : (" + str(new_x) + "," + str(new_y) + ")")

    context.log(messages)

# Move two pieces.
def move_two_pieces(old_x1, old_y1, new_x1, new_y1,
                    old_x2, old_y2, new_x2, new_y2, context):

    # Memorize the old pieces.
    piece1 = model.global_game_board_state[old_x1][old_y1]
    piece2 = model.global_game_board_state[old_x2][old_y2]

    # Remove the old pieces.
    model.global_game_board_state[old_x1][old_y1] = 0
    model.global_game_board_state[old_x2][old_y2] = 0

    # Place the pieces to new location.
    model.global_game_board_state[new_x1][new_y1] = piece1
    model.global_game_board_state[new_x2][new_y2] = piece2

    # Increase the score and taken moves for each side.
    if model.global_game_board_state[new_x1][new_y1] == 1:
        gameboard.update_moves_taken_for('black')
    elif model.global_game_board_state[new_x1][new_y1] == 2:
        gameboard.update_moves_taken_for('white')
    gameboard.update_game_score()

    # Log the movement information.
    messages = []
    if model.global_game_board_state[new_x1][new_y1] == 1:
        messages.append("Black made movement as the following:")
    elif model.global_game_board_state[new_x1][new_y1] == 2:
        messages.append("White made movement as the following:")

    messages.append("STD From : "
                    + str(chiens_board_representation_output[old_x1][old_y1]) + ', '
                    + str(chiens_board_representation_output[old_x2][old_y2]))
    messages.append("STD To   : "
                    + str(chiens_board_representation_output[new_x1][new_y1]) + ', '
                    + str(chiens_board_representation_output[new_x2][new_y2]))

    messages.append("From : (" + str(old_x1) + "," + str(old_y1) + ")"
                   + " " + "(" + str(old_x2) + "," + str(old_y2) + ")")
    messages.append("To   : (" + str(new_x1) + "," + str(new_y1) + ")"
                   + " " + "(" + str(new_x2) + "," + str(new_y2) + ")")
    context.log(messages)

# Move three pieces.
def move_three_pieces(old_x1, old_y1, new_x1, new_y1,
                      old_x2, old_y2, new_x2, new_y2,
                      old_x3, old_y3, new_x3, new_y3, context):

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

    # Increase the score and taken moves for each side.
    if model.global_game_board_state[new_x1][new_y1] == 1:
        gameboard.update_moves_taken_for('black')
    elif model.global_game_board_state[new_x1][new_y1] == 2:
        gameboard.update_moves_taken_for('white')
    gameboard.update_game_score()

    # Log the movement information.
    messages = []
    if model.global_game_board_state[new_x1][new_y1] == 1:
        messages.append("Black made movement as the following:")
    elif model.global_game_board_state[new_x1][new_y1] == 2:
        messages.append("White made movement as the following:")

    messages.append("STD From : "
                    + str(chiens_board_representation_output[old_x1][old_y1]) + ', '
                    + str(chiens_board_representation_output[old_x2][old_y2]) + ', '
                    + str(chiens_board_representation_output[old_x3][old_y3]))
    messages.append("STD To   : "
                    + str(chiens_board_representation_output[new_x1][new_y1]) + ', '
                    + str(chiens_board_representation_output[new_x2][new_y2]) + ', '
                    + str(chiens_board_representation_output[new_x3][new_y3]))

    messages.append("From : (" + str(old_x1) + "," + str(old_y1) + ")"
                    + " " + "(" + str(old_x2) + "," + str(old_y2) + ")"
                    + " " + "(" + str(old_x3) + "," + str(old_y3) + ")")
    messages.append("To   : (" + str(new_x1) + "," + str(new_y1) + ")"
                    + " " + "(" + str(new_x2) + "," + str(new_y2) + ")"
                    + " " + "(" + str(new_x3) + "," + str(new_y3) + ")")
    context.log(messages)

# Move 2 to 1 sumito.
def move_2_to_1_sumito(old_x1, old_y1, new_x1, new_y1,
                       old_x2, old_y2, new_x2, new_y2, context):
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

    # Increase the score and taken moves for each side.
    if model.global_game_board_state[new_x1][new_y1] == 1:
        gameboard.update_moves_taken_for('black')
    elif model.global_game_board_state[new_x1][new_y1] == 2:
        gameboard.update_moves_taken_for('white')
    gameboard.update_game_score()

    # Log the movement information.
    messages = []
    if model.global_game_board_state[new_x1][new_y1] == 1:
        messages.append("Black made movement (SUMITO!):")
    elif model.global_game_board_state[new_x1][new_y1] == 2:
        messages.append("White made movement (SUMITO!):")

    messages.append("STD From : "
                    + str(chiens_board_representation_output[old_x1][old_y1]) + ', '
                    + str(chiens_board_representation_output[old_x2][old_y2]))
    messages.append("STD To   : "
                    + str(chiens_board_representation_output[new_x1][new_y1]) + ', '
                    + str(chiens_board_representation_output[new_x2][new_y2]))

    messages.append("From : (" + str(old_x1) + "," + str(old_y1) + ")"
                    + " " + "(" + str(old_x2) + "," + str(old_y2) + ")")
    messages.append("To   : (" + str(new_x1) + "," + str(new_y1) + ")"
                    + " " + "(" + str(new_x2) + "," + str(new_y2) + ")")
    context.log(messages)

# Move 3 to 1 or 3 to 2 sumito.
def move_3_to_1_or_3_to_2_sumito(old_x1, old_y1, new_x1, new_y1,
                                 old_x2, old_y2, new_x2, new_y2,
                                 old_x3, old_y3, new_x3, new_y3, context):
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
    # A set will be generated: ((x1, y1, x2, y2, x3, y3))
    all_3_to_1_sumitos_set = rules.generate_all_3_to_1_legal_sumitos(old_x1, old_y1, old_x2, old_y2, old_x3, old_y3)
    all_3_to_2_sumitos_set = rules.generate_all_3_to_2_legal_sumitos(old_x1, old_y1, old_x2, old_y2, old_x3, old_y3)

    new_coordinates_set_1 = set()
    new_coordinates_set_1.add((new_x1, new_y1, new_x2, new_y2, new_x3, new_y3))

    new_coordinates_set_2 = set()
    new_coordinates_set_2.add((new_x1, new_y1, new_x3, new_y3, new_x2, new_y2))

    new_coordinates_set_3 = set()
    new_coordinates_set_3.add((new_x2, new_y2, new_x1, new_y1, new_x3, new_y3))

    new_coordinates_set_4 = set()
    new_coordinates_set_4.add((new_x2, new_y2, new_x3, new_y3, new_x1, new_y1))

    new_coordinates_set_5 = set()
    new_coordinates_set_5.add((new_x3, new_y3, new_x2, new_y2, new_x1, new_y1))

    new_coordinates_set_6 = set()
    new_coordinates_set_6.add((new_x3, new_y3, new_x1, new_y1, new_x2, new_y2))

    # 1. 3 to 1 sumito.
    if all_3_to_1_sumitos_set != set() and \
            (all_3_to_1_sumitos_set.issuperset(new_coordinates_set_1)
             or all_3_to_1_sumitos_set.issuperset(new_coordinates_set_2)
             or all_3_to_1_sumitos_set.issuperset(new_coordinates_set_3)
             or all_3_to_1_sumitos_set.issuperset(new_coordinates_set_4)
             or all_3_to_1_sumitos_set.issuperset(new_coordinates_set_5)
             or all_3_to_1_sumitos_set.issuperset(new_coordinates_set_6)
            ):

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
    elif all_3_to_2_sumitos_set != set() and \
            (all_3_to_2_sumitos_set.issuperset(new_coordinates_set_1)
             or all_3_to_2_sumitos_set.issuperset(new_coordinates_set_2)
             or all_3_to_2_sumitos_set.issuperset(new_coordinates_set_3)
             or all_3_to_2_sumitos_set.issuperset(new_coordinates_set_4)
             or all_3_to_2_sumitos_set.issuperset(new_coordinates_set_5)
             or all_3_to_2_sumitos_set.issuperset(new_coordinates_set_6)
            ):

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

    # Increase the score and taken moves for each side.
    if model.global_game_board_state[new_x1][new_y1] == 1:
        gameboard.update_moves_taken_for('black')
    elif model.global_game_board_state[new_x1][new_y1] == 2:
        gameboard.update_moves_taken_for('white')
    gameboard.update_game_score()

    # Log the movement information.
    messages = []
    if model.global_game_board_state[new_x1][new_y1] == 1:
        messages.append("Black made movement (SUMITO!):")
    elif model.global_game_board_state[new_x1][new_y1] == 2:
        messages.append("White made movement (SUMITO!):")

    messages.append("STD From : "
                    + str(chiens_board_representation_output[old_x1][old_y1]) + ', '
                    + str(chiens_board_representation_output[old_x2][old_y2]) + ', '
                    + str(chiens_board_representation_output[old_x3][old_y3]))
    messages.append("STD To   : "
                    + str(chiens_board_representation_output[new_x1][new_y1]) + ', '
                    + str(chiens_board_representation_output[new_x2][new_y2]) + ', '
                    + str(chiens_board_representation_output[new_x3][new_y3]))

    messages.append("From : (" + str(old_x1) + "," + str(old_y1) + ")"
                    + " " + "(" + str(old_x2) + "," + str(old_y2) + ")"
                    + " " + "(" + str(old_x3) + "," + str(old_y3) + ")")
    messages.append("To   : (" + str(new_x1) + "," + str(new_y1) + ")"
                    + " " + "(" + str(new_x2) + "," + str(new_y2) + ")"
                    + " " + "(" + str(new_x3) + "," + str(new_y3) + ")")
    context.log(messages)

# ================ ================ Utility Functions ================ ================


# Get the differences from sets for sumitos to get rid of clicked input from gui.
def get_the_differences_from_sets_for_sumitos(positions_1, positions_2):

    new_set = positions_1.difference(positions_2)
    return new_set.pop()



if __name__ == '__main__':

    s = set()
    s.add((1, 2, 3, 4, 5, 6))
    s.add((7, 8, 9, 10, 11, 12))

    t = set()
    t.add((1, 2, 3, 4, 5, 6))
    print(s.issuperset(t))




