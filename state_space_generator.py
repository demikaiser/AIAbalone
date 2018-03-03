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

import glob, ai_rules, itertools, ai_movement, re, os
import copy    # For copy.deepcopy() function as Python is "pass-by-ref" by default.

# A game board state used by AI to evaluate utilities
# of the board configuration.
experimental_game_board_state = [
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

# Representation converter from chiens board representation
# to this project's (Input Processing Data Structure - Dictionary).
chiens_board_representation_input = {
    "I5": (4, 0), "I6": (5, 0), "I7": (6, 0), "I8": (7, 0), "I9": (8, 0),
    "H4": (3, 1), "H5": (4, 1), "H6": (5, 1), "H7": (6, 1), "H8": (7, 1), "H9": (8, 1),
    "G3": (2, 2), "G4": (3, 2), "G5": (4, 2), "G6": (5, 2), "G7": (6, 2), "G8": (7, 2), "G9": (8, 2),
    "F2": (1, 3), "F3": (2, 3), "F4": (3, 3), "F5": (4, 3), "F6": (5, 3), "F7": (6, 3), "F8": (7, 3), "F9": (8, 3),
    "E1": (0, 4), "E2": (1, 4), "E3": (2, 4), "E4": (3, 4), "E5": (4, 4), "E6": (5, 4), "E7": (6, 4), "E8": (7, 4), "E9": (8, 4),
    "D1": (0, 5), "D2": (1, 5), "D3": (2, 5), "D4": (3, 5), "D5": (4, 5), "D6": (5, 5), "D7": (6, 5), "D8": (7, 5),
    "C1": (0, 6), "C2": (1, 6), "C3": (2, 6), "C4": (3, 6), "C5": (4, 6), "C6": (5, 6), "C7": (6, 6),
    "B1": (0, 7), "B2": (1, 7), "B3": (2, 7), "B4": (3, 7), "B5": (4, 7), "B6": (5, 7),
    "A1": (0, 8), "A2": (1, 8), "A3": (2, 8), "A4": (3, 8), "A5": (4, 8),
}

# Representation converter from this project's
# to chiens board representation (Output Processing Data Structure - 2D Lists).
chiens_board_representation_output = [
    [-9, -9, -9, -9,  "E1",  "D1",  "C1",  "B1",  "A1"],
    [-9, -9, -9,  "F2",  "E2",  "D2",  "C2",  "B2",  "A2"],
    [-9, -9,  "G3",  "F3",  "E3",  "D3",  "C3",  "B3",  "A3"],
    [-9,  "H4",  "G4",  "F4",  "E4",  "D4",  "C4",  "B4",  "A4"],
    [ "I5",  "H5",  "G5",  "F5",  "E5",  "D5",  "C5",  "B5",  "A5"],
    [ "I6",  "H6",  "G6",  "F6",  "E6",  "D6",  "C6",  "B6", -9],
    [ "I7",  "H7",  "G7",  "F7",  "E7",  "D7",  "C7", -9, -9],
    [ "I8",  "H8",  "G8",  "F8",  "E8",  "D8", -9, -9, -9],
    [ "I9",  "H9",  "G9",  "F9",  "E9", -9, -9, -9, -9]
]

# Representation converter from this project's
# to chiens board representation (Output Processing Data Structure - 2D Lists).
# This is extensively for the output file generation that matches Chien's exactly.
chiens_board_representation_output_for_file_generation = {
    "A1": (0, 8), "A2": (1, 8), "A3": (2, 8), "A4": (3, 8), "A5": (4, 8),
    "B1": (0, 7), "B2": (1, 7), "B3": (2, 7), "B4": (3, 7), "B5": (4, 7), "B6": (5, 7),
    "C1": (0, 6), "C2": (1, 6), "C3": (2, 6), "C4": (3, 6), "C5": (4, 6), "C6": (5, 6), "C7": (6, 6),
    "D1": (0, 5), "D2": (1, 5), "D3": (2, 5), "D4": (3, 5), "D5": (4, 5), "D6": (5, 5), "D7": (6, 5), "D8": (7, 5),
    "E1": (0, 4), "E2": (1, 4), "E3": (2, 4), "E4": (3, 4), "E5": (4, 4), "E6": (5, 4), "E7": (6, 4), "E8": (7, 4), "E9": (8, 4),
    "F2": (1, 3), "F3": (2, 3), "F4": (3, 3), "F5": (4, 3), "F6": (5, 3), "F7": (6, 3), "F8": (7, 3), "F9": (8, 3),
    "G3": (2, 2), "G4": (3, 2), "G5": (4, 2), "G6": (5, 2), "G7": (6, 2), "G8": (7, 2), "G9": (8, 2),
    "H4": (3, 1), "H5": (4, 1), "H6": (5, 1), "H7": (6, 1), "H8": (7, 1), "H9": (8, 1),
    "I5": (4, 0), "I6": (5, 0), "I7": (6, 0), "I8": (7, 0), "I9": (8, 0),
}

# Get the player information (black or white) from the given input file.
def get_player_info_from_the_input_file_contents(file_contents_first_line):
    player = ""

    if "b" in file_contents_first_line:
        player = "black"
    elif "w" in file_contents_first_line:
        player = "white"

    return player


# Get the board state from the given input file.
def get_state_from_the_input_file_contents(file_contents_second_line):
    state = copy.deepcopy(experimental_game_board_state)

    # Get rid of the newline character.
    file_contents_second_line = file_contents_second_line.rstrip('\n')

    # Split the marbles list with the delimiter ','.
    raw_marbles_list = file_contents_second_line.split(",")
    marbles_dictionary = {}

    # Convert raw_marbles_list to marbles_dictionary for fast processing.
    for raw_marble in raw_marbles_list:
        if 'b' == raw_marble[2]:
            player_color = 1
        elif 'w' == raw_marble[2]:
            player_color = 2
        marbles_dictionary[raw_marble[0] + raw_marble[1]] = player_color

    # Update the state with marbles_dictionary.
    for marble in marbles_dictionary:
        x_coordinate = chiens_board_representation_input[marble][0]
        y_coordinate = chiens_board_representation_input[marble][1]
        state[x_coordinate][y_coordinate] = marbles_dictionary[marble]

    return state

# Get all the ally positions at the board.
# RETURN: A list contains positional tuples [(x1, y1), (x2, y2), ...].
def get_all_ally_positions(state, player_color):
    # Check the side.
    if player_color == 'black':
        ally = 1
        opponent = 2
    elif player_color == 'white':
        ally = 2
        opponent = 1

    ally_pieces_locations = []

    for j in range(9):
        for i in range(9):
            if state[i][j] == ally:
                ally_pieces_locations.append((i, j))

    return ally_pieces_locations

# Select all possible combinations for three pieces.
def select_two_pieces_combination_from_ally_locations(ally_pieces_locations):
    list = []
    for subset in itertools.combinations(ally_pieces_locations, 2):
        list.append((subset[0][0], subset[0][1], subset[1][0], subset[1][1]))
    return list

# Select all possible combinations for two pieces.
def select_three_pieces_combination_from_ally_locations(ally_pieces_locations):
    list = []
    for subset in itertools.combinations(ally_pieces_locations, 3):
        list.append((subset[0][0], subset[0][1], subset[1][0], subset[1][1], subset[2][0], subset[2][1]))
    return list

# Generate all possible move for one piece.
def generate_move_candidates_for_one_piece(state, ally_pieces_locations_for_one_piece):
    move_candidates_for_one_piece = []

    for location in ally_pieces_locations_for_one_piece:
        possible_moves = ai_rules.generate_all_possible_legal_moves_for_one_piece(state, location[0], location[1])
        for move in possible_moves:
            move_candidates_for_one_piece.append((location[0], location[1], move[0], move[1]))

    return move_candidates_for_one_piece

# Generate all possible move for two pieces.
def generate_move_candidates_for_two_pieces(state, ally_pieces_locations_for_two_pieces):
    move_candidates_for_two_pieces = []

    for location in ally_pieces_locations_for_two_pieces:
        possible_moves = ai_rules.generate_all_possible_legal_moves_for_two_pieces(state, location[0], location[1],
                                                                                          location[2], location[3])
        for move in possible_moves:
            move_candidates_for_two_pieces.append((location[0], location[1], location[2], location[3],
                                                    move[0], move[1], move[2], move[3]))

    return move_candidates_for_two_pieces

# Generate all possible move for three pieces.
def generate_move_candidates_for_three_pieces(state, ally_pieces_locations_for_three_pieces):
    move_candidates_for_three_pieces = []

    for location in ally_pieces_locations_for_three_pieces:
        possible_moves = ai_rules.generate_all_possible_legal_moves_for_three_pieces(state, location[0], location[1],
                                                                                          location[2], location[3],
                                                                                          location[4], location[5])
        for move in possible_moves:
            move_candidates_for_three_pieces.append((location[0], location[1], location[2], location[3], location[4], location[5],
                                                    move[0], move[1], move[2], move[3], move[4], move[5]))

    return move_candidates_for_three_pieces

# Generate all possible move for 2 to 1 sumito.
def generate_move_candidates_for_2_to_1_sumito(state, ally_pieces_locations_for_two_pieces):
    move_candidates_for_2_to_1_sumito = []

    for location in ally_pieces_locations_for_two_pieces:
        possible_moves = ai_rules.generate_all_2_to_1_legal_sumitos(state, location[0], location[1],
                                                                           location[2], location[3])
        for move in possible_moves:
            move_candidates_for_2_to_1_sumito.append((location[0], location[1], location[2], location[3],
                                                    move[0], move[1], move[2], move[3]))

    return move_candidates_for_2_to_1_sumito

# Generate all possible move for 3 to 1 sumito.
def generate_move_candidates_for_3_to_1_sumito(state, ally_pieces_locations_for_three_pieces):
    move_candidates_for_3_to_1_sumito = []

    for location in ally_pieces_locations_for_three_pieces:
        possible_moves = ai_rules.generate_all_3_to_1_legal_sumitos(state, location[0], location[1],
                                                                           location[2], location[3],
                                                                           location[4], location[5])
        for move in possible_moves:
            move_candidates_for_3_to_1_sumito.append((location[0], location[1], location[2], location[3], location[4], location[5],
                                                    move[0], move[1], move[2], move[3], move[4], move[5]))

    return move_candidates_for_3_to_1_sumito

# Generate all possible move for 3 to 2 sumito.
def generate_move_candidates_for_3_to_2_sumito(state, ally_pieces_locations_for_three_pieces):
    move_candidates_for_3_to_2_sumito = []

    for location in ally_pieces_locations_for_three_pieces:
        possible_moves = ai_rules.generate_all_3_to_2_legal_sumitos(state, location[0], location[1],
                                                                           location[2], location[3],
                                                                           location[4], location[5])
        for move in possible_moves:
            move_candidates_for_3_to_2_sumito.append((location[0], location[1], location[2], location[3], location[4], location[5],
                                                    move[0], move[1], move[2], move[3], move[4], move[5]))

    return move_candidates_for_3_to_2_sumito

# Convert the state representations to the Chien's assignment evaluation form.
def convert_state_representation_list_to_chiens(total_state_space_collection):

    output = []

    for state in total_state_space_collection:

        sub_output_black = []
        sub_output_white = []
        sub_output = []

        for position in chiens_board_representation_output_for_file_generation:

            if 1 == state[chiens_board_representation_input[position][0]][chiens_board_representation_input[position][1]]:
                sub_output_black.append(position + 'b')
            elif 2 == state[chiens_board_representation_input[position][0]][chiens_board_representation_input[position][1]]:
                sub_output_white.append(position + 'w')

        for element in sub_output_black:
            sub_output.append(element)

        for element in sub_output_white:
            sub_output.append(element)

        output.append(sub_output)

    return output

# Write a file to record all possible leagal next-ply moves for Test<#>.move file.
def write_a_file_all_possible_leagal_next_ply_moves(move_list_final, name_for_output_file):

    # Specify the relative path to save the file.
    save_path = 'ssg_tester_output'

    # Join the path with the complete file name.
    complete_path = os.path.join(save_path, name_for_output_file)

    # Open the file for writing.
    file = open(complete_path, "w")
    contents_to_write = ""

    # Process the move list and store it to a string.
    for move in move_list_final:
        temp_string = "("
        flag = False
        for int in move:
            if flag:
                temp_string += ", "
            temp_string += str(int)
            flag = True
        temp_string += ")\n"
        file.write(temp_string)

    # Write to the file and close it.
    file.write(contents_to_write)
    file.close()

# Write a file to record all possible board states for Test<#>.board file.
def write_a_file_all_possible_board_states(output_list_final, name_for_output_file):

    # Specify the relative path to save the file.
    save_path = 'ssg_tester_output'

    # Join the path with the complete file name.
    complete_path = os.path.join(save_path, name_for_output_file)

    # Open the file for writing.
    file = open(complete_path, "w")
    contents_to_write = ""

    print(output_list_final)

    # Process the move list and store it to a string.
    for output in output_list_final:
        temp_string = ""
        flag = False
        for str in output:
            if flag:
                temp_string += ","
            temp_string += str
            flag = True
        temp_string += "\n"
        file.write(temp_string)

    # Write to the file and close it.
    file.write(contents_to_write)
    file.close()

# Generate all states from the Chien's representation and write files for Chien's evaluation.
def generate_all_states_from_chiens_file_to_chiens_file(file_to_read):
    file = open(file_to_read, 'r')
    file_contents_first_line = file.readline()
    file_contents_second_line = file.readline()
    file.close()

    # Update the state board from the given information.
    player = get_player_info_from_the_input_file_contents(file_contents_first_line)
    state_to_expand = get_state_from_the_input_file_contents(file_contents_second_line)

    # ================ ================ Generate All Possible Piece Selections ================ ================

    # Get all ally pieces information.
    ally_pieces_locations = get_all_ally_positions(state_to_expand, player)

    # Get all ally pieces combination for two pieces.
    ally_pieces_combination_two_pieces = select_two_pieces_combination_from_ally_locations(ally_pieces_locations)

    # Get all ally pieces combination for three pieces.
    ally_pieces_combination_three_pieces = select_three_pieces_combination_from_ally_locations(ally_pieces_locations)

    # ================ ================ Generate All Possible Move Candidates ================ ================

    # Generate all move for one piece.
    move_candidates_for_one_piece = generate_move_candidates_for_one_piece(state_to_expand, ally_pieces_locations)

    # Generate all move for two pieces.
    move_candidates_for_two_pieces = generate_move_candidates_for_two_pieces(state_to_expand,
                                                                             ally_pieces_combination_two_pieces)

    # Generate all move for three pieces.
    move_candidates_for_three_pieces = generate_move_candidates_for_three_pieces(state_to_expand,
                                                                                 ally_pieces_combination_three_pieces)

    # Generate all move for 2 to 1 sumito.
    move_candidates_for_2_to_1_sumito = generate_move_candidates_for_2_to_1_sumito(state_to_expand,
                                                                                   ally_pieces_combination_two_pieces)

    # Generate all move for 3 to 1 sumito.
    move_candidates_for_3_to_1_sumito = generate_move_candidates_for_3_to_1_sumito(state_to_expand,
                                                                                   ally_pieces_combination_three_pieces)

    # Generate all move for 3 to 2 sumito.
    move_candidates_for_3_to_2_sumito = generate_move_candidates_for_3_to_2_sumito(state_to_expand,
                                                                                   ally_pieces_combination_three_pieces)

    # ================ ================ Generate All Possible State Space ================ ================

    total_state_space_collection = []

    # Generate all states for one piece movement.
    for move in move_candidates_for_one_piece:
        new_state = copy.deepcopy(state_to_expand)
        ai_movement.move_one_piece(new_state, move[0], move[1], move[2], move[3])
        total_state_space_collection.append(new_state)

    # Generate all states for two pieces movement.
    for move in move_candidates_for_two_pieces:
        new_state = copy.deepcopy(state_to_expand)
        ai_movement.move_two_pieces(new_state, move[0], move[1], move[4], move[5],
                                    move[2], move[3], move[6], move[7])
        total_state_space_collection.append(new_state)

    # Generate all states for three pieces movement.
    for move in move_candidates_for_three_pieces:
        new_state = copy.deepcopy(state_to_expand)
        ai_movement.move_three_pieces(new_state, move[0], move[1], move[6], move[7],
                                      move[2], move[3], move[8], move[9],
                                      move[4], move[5], move[10], move[11])
        total_state_space_collection.append(new_state)

    # Generate all states for 2 to 1 sumitos.
    for move in move_candidates_for_2_to_1_sumito:
        new_state = copy.deepcopy(state_to_expand)
        ai_movement.move_2_to_1_sumito(new_state, move[0], move[1], move[4], move[5],
                                       move[2], move[3], move[6], move[7])
        total_state_space_collection.append(new_state)

    # Generate all states for 3 to 1 sumitos.
    for move in move_candidates_for_3_to_1_sumito:
        new_state = copy.deepcopy(state_to_expand)
        ai_movement.move_3_to_1_or_3_to_2_sumito(new_state, move[0], move[1], move[6], move[7],
                                                 move[2], move[3], move[8], move[9],
                                                 move[4], move[5], move[10], move[11])
        total_state_space_collection.append(new_state)

    # Generate all states for 3 to 2 sumitos.
    for move in move_candidates_for_3_to_2_sumito:
        new_state = copy.deepcopy(state_to_expand)
        ai_movement.move_3_to_1_or_3_to_2_sumito(new_state, move[0], move[1], move[6], move[7],
                                                 move[2], move[3], move[8], move[9],
                                                 move[4], move[5], move[10], move[11])
        total_state_space_collection.append(new_state)

    # ================ ================ Output to a File ================ ================

    # Record moves to generate Test<#>.move file.
    move_list_final = []
    for move in move_candidates_for_one_piece:
        move_list_final.append(move)
    for move in move_candidates_for_two_pieces:
        move_list_final.append(move)
    for move in move_candidates_for_three_pieces:
        move_list_final.append(move)
    for move in move_candidates_for_2_to_1_sumito:
        move_list_final.append(move)
    for move in move_candidates_for_3_to_1_sumito:
        move_list_final.append(move)
    for move in move_candidates_for_3_to_2_sumito:
        move_list_final.append(move)

    # Convert the state representation list for the class evaluation.
    output_list_final = convert_state_representation_list_to_chiens(total_state_space_collection)

    # Get names for the output files.
    file_name_without_extension = re.search('Test\d+', file_to_read).group(0)

    # Make a file name with "Test<#>.move".
    name_for_output_file_move = file_name_without_extension + ".move"

    # Make a file name with "Test<#>.board".
    name_for_output_file_board = file_name_without_extension + ".board"

    # Write to final output files.
    write_a_file_all_possible_leagal_next_ply_moves(move_list_final, name_for_output_file_move)
    write_a_file_all_possible_board_states(output_list_final, name_for_output_file_board)

# The entry point of this file.
if __name__ == '__main__':

    # Open and read the file.
    file_list = glob.glob("ssg_tester_input/*.input")

    # Execute the generation process.
    for file_to_read in file_list:
        generate_all_states_from_chiens_file_to_chiens_file(file_to_read)

