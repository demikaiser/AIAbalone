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

import itertools, copy # For copy.deepcopy() function as Python is "pass-by-ref" by default.
import ai_rules,  ai_movement

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

# Get all the ally positions at the board.
# RETURN: A list contains positional tuples [(x1, y1), (x2, y2), ...].
cpdef inline get_all_ally_positions(state, player_color):

    cpdef ally, opponent, i, j

    # Check the side.
    if player_color == 'black':
        ally = 1
        opponent = 2
    elif player_color == 'white':
        ally = 2
        opponent = 1

    ally_pieces_locations = []

    for i in range(9):
        for j in range(9):
            if state[i][j] == ally:
                ally_pieces_locations.append((i, j))

    return ally_pieces_locations
# Select all possible combinations for three pieces.
cpdef inline select_two_pieces_combination_from_ally_locations(ally_pieces_locations):
    list = []
    for subset in itertools.combinations(ally_pieces_locations, 2):
        list.append((subset[0][0], subset[0][1], subset[1][0], subset[1][1]))
    return list

# Select all possible combinations for two pieces.
cpdef inline select_three_pieces_combination_from_ally_locations(ally_pieces_locations):
    list = []
    for subset in itertools.combinations(ally_pieces_locations, 3):
        list.append((subset[0][0], subset[0][1], subset[1][0], subset[1][1], subset[2][0], subset[2][1]))
    return list

# Generate all possible move for one piece.
cpdef inline generate_move_candidates_for_one_piece(state, ally_pieces_locations_for_one_piece):
    move_candidates_for_one_piece = []

    for location in ally_pieces_locations_for_one_piece:
        possible_moves = ai_rules.generate_all_possible_legal_moves_for_one_piece(state, location[0], location[1])
        for move in possible_moves:
            move_candidates_for_one_piece.append((location[0], location[1], move[0], move[1]))

    return move_candidates_for_one_piece

# Generate all possible move for two pieces.
cpdef inline generate_move_candidates_for_two_pieces(state, ally_pieces_locations_for_two_pieces):
    move_candidates_for_two_pieces = []

    for location in ally_pieces_locations_for_two_pieces:
        possible_moves = ai_rules.generate_all_possible_legal_moves_for_two_pieces(state, location[0], location[1],
                                                                                          location[2], location[3])
        for move in possible_moves:
            move_candidates_for_two_pieces.append((location[0], location[1], location[2], location[3],
                                                    move[0], move[1], move[2], move[3]))

    return move_candidates_for_two_pieces

# Generate all possible move for three pieces.
cpdef inline generate_move_candidates_for_three_pieces(state, ally_pieces_locations_for_three_pieces):
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
cpdef inline generate_move_candidates_for_2_to_1_sumito(state, ally_pieces_locations_for_two_pieces):
    move_candidates_for_2_to_1_sumito = []

    for location in ally_pieces_locations_for_two_pieces:
        possible_moves = ai_rules.generate_all_2_to_1_legal_sumitos(state, location[0], location[1],
                                                                           location[2], location[3])
        for move in possible_moves:
            move_candidates_for_2_to_1_sumito.append((location[0], location[1], location[2], location[3],
                                                    move[0], move[1], move[2], move[3]))

    return move_candidates_for_2_to_1_sumito

# Generate all possible move for 3 to 1 sumito.
cpdef inline generate_move_candidates_for_3_to_1_sumito(state, ally_pieces_locations_for_three_pieces):
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
cpdef inline generate_move_candidates_for_3_to_2_sumito(state, ally_pieces_locations_for_three_pieces):
    move_candidates_for_3_to_2_sumito = []

    for location in ally_pieces_locations_for_three_pieces:
        possible_moves = ai_rules.generate_all_3_to_2_legal_sumitos(state, location[0], location[1],
                                                                           location[2], location[3],
                                                                           location[4], location[5])
        for move in possible_moves:
            move_candidates_for_3_to_2_sumito.append((location[0], location[1], location[2], location[3], location[4], location[5],
                                                    move[0], move[1], move[2], move[3], move[4], move[5]))

    return move_candidates_for_3_to_2_sumito

# Generate all states from a state for AI search.
# Returns a list: [total_movement_collection, total_state_space_collection]
cpdef inline generate_all_next_moves_and_states(player, state_to_expand):

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

    total_movement_collection = []
    total_state_space_collection = []

    # Generate all states for one piece movement.
    for move in move_candidates_for_one_piece:
        new_state = copy.deepcopy(state_to_expand)
        ai_movement.move_one_piece(new_state, move[0], move[1], move[2], move[3])
        total_movement_collection.append(move)
        total_state_space_collection.append(new_state)

    # Generate all states for two pieces movement.
    for move in move_candidates_for_two_pieces:
        new_state = copy.deepcopy(state_to_expand)
        ai_movement.move_two_pieces(new_state, move[0], move[1], move[4], move[5],
                                    move[2], move[3], move[6], move[7])
        total_movement_collection.append(move)
        total_state_space_collection.append(new_state)

    # Generate all states for three pieces movement.
    for move in move_candidates_for_three_pieces:
        new_state = copy.deepcopy(state_to_expand)
        ai_movement.move_three_pieces(new_state, move[0], move[1], move[6], move[7],
                                      move[2], move[3], move[8], move[9],
                                      move[4], move[5], move[10], move[11])
        total_movement_collection.append(move)
        total_state_space_collection.append(new_state)

    # Generate all states for 2 to 1 sumitos.
    for move in move_candidates_for_2_to_1_sumito:
        new_state = copy.deepcopy(state_to_expand)
        ai_movement.move_2_to_1_sumito(new_state, move[0], move[1], move[4], move[5],
                                       move[2], move[3], move[6], move[7])
        total_movement_collection.append(move)
        total_state_space_collection.append(new_state)

    # Generate all states for 3 to 1 sumitos.
    for move in move_candidates_for_3_to_1_sumito:
        new_state = copy.deepcopy(state_to_expand)
        ai_movement.move_3_to_1_sumito(new_state, move[0], move[1], move[6], move[7],
                                                 move[2], move[3], move[8], move[9],
                                                 move[4], move[5], move[10], move[11])
        total_movement_collection.append(move)
        total_state_space_collection.append(new_state)

    # Generate all states for 3 to 2 sumitos.
    for move in move_candidates_for_3_to_2_sumito:
        new_state = copy.deepcopy(state_to_expand)
        ai_movement.move_3_to_2_sumito(new_state, move[0], move[1], move[6], move[7],
                                                 move[2], move[3], move[8], move[9],
                                                 move[4], move[5], move[10], move[11])
        total_movement_collection.append(move)
        total_state_space_collection.append(new_state)

    # ================ ================ Return the Result ================ ================

    return [total_movement_collection, total_state_space_collection]










