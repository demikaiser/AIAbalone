'''
Copyright (C) BCIT AI/ML Option 2018 Team with Members Following - All Rights Reserved.
- Jake Jonghun Choi     jchoi179@my.bcit.ca
- Justin Carey          justinthomascarey@gmail.com
- Pashan Irani          pashanirani@gmail.com
- Tony Huang	        tonyhuang1996@hotmail.ca
- Chil Yuqing Qiu       yuqingqiu93@gmail.com
Unauthorized copying of this file, via any medium is strictly prohibited.
Written by Justin Carey <justinthomascarey@gmail.com>
'''

import ai_state_space_generator
import copy


def get_evaluation_score(player, state):
    # Check the side.
    if player == 'black':
        ally = 1
        opponent = 2
        opponent_color = 'white'
    elif player == 'white':
        ally = 2
        opponent = 1
        opponent_color = 'black'

    ally_pieces_locations = copy.copy(ai_state_space_generator.get_all_ally_positions(state, player))
    opp_pieces_locations = copy.copy(ai_state_space_generator.get_all_ally_positions(state, opponent_color))

    # Initialize the score.
    score = 0

    weight_list_variable = [10, 5]

    # Tier 03. Calculates the distance from the center.
    score += weight_list_variable[0] * manhattan_distance(state, ally, opponent)

    # Tier 05. Calculates how many sumitos are available.
    score += weight_list_variable[1] * sumito_num(player, ally_pieces_locations, opp_pieces_locations, state)

    # Return the score evaluated.
    return score

def manhattan_distance(state, ally, opponent):
    score = 0

    for i in range(9):
        for j in range(9):
            if state[i][j] == ally:
                score += 60
                score += 30 / (abs(i - 4) + abs(j - 4) + 1)
            if state[i][j] == opponent:
                score -= 40
                score -= 30 / (abs(i - 4) + abs(j - 4) + 1)

    return score

def sumito_num(player, ally_pieces_locations, opp_pieces_locations, state):

    sumito_power = 0

    two_piece_list = ai_state_space_generator.select_two_pieces_combination_from_ally_locations(ally_pieces_locations)
    three_piece_list = ai_state_space_generator.select_three_pieces_combination_from_ally_locations(ally_pieces_locations)

    two_to_one_sumito_list = ai_state_space_generator.generate_move_candidates_for_2_to_1_sumito(state, two_piece_list)
    three_to_one_sumito_list = ai_state_space_generator.generate_move_candidates_for_3_to_1_sumito(state, three_piece_list)
    three_to_two_sumito_list = ai_state_space_generator.generate_move_candidates_for_3_to_2_sumito(state, three_piece_list)

    sumito_power += 10 * two_to_one_sumito_list.__len__()
    sumito_power += 20 * three_to_one_sumito_list.__len__()
    sumito_power += 20 * three_to_two_sumito_list.__len__()

    two_piece_list_oppo = ai_state_space_generator.select_two_pieces_combination_from_ally_locations(opp_pieces_locations)
    three_piece_list_oppo = ai_state_space_generator.select_three_pieces_combination_from_ally_locations(opp_pieces_locations)

    two_to_one_sumito_list_oppo = ai_state_space_generator.generate_move_candidates_for_2_to_1_sumito(state, two_piece_list_oppo)
    three_to_one_sumito_list_oppo = ai_state_space_generator.generate_move_candidates_for_3_to_1_sumito(state,
                                                                                                   three_piece_list_oppo)
    three_to_two_sumito_list_oppo = ai_state_space_generator.generate_move_candidates_for_3_to_2_sumito(state,
                                                                                                  three_piece_list_oppo)

    sumito_power -= 10 * two_to_one_sumito_list_oppo.__len__()
    sumito_power -= 30 * three_to_one_sumito_list_oppo.__len__()
    sumito_power -= 30 * three_to_two_sumito_list_oppo.__len__()

    return sumito_power
