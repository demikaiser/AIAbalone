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

import ai_state_space_generator, model
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

    weight_list_variable =   [1000000, 100000, 1000, 10, 1.5, 1, 1, 1, 1, 1, 1, 1]

    WEIGHT_LIST_DEFAULT =    [1000000, 100000, 1000, 10, 1.5, 1, 1, 1, 1, 1, 1, 1]
    WEIGHT_LIST_AGGRESSIVE = [1000000, 200000, 1500, 10, 1.2, 1.5, 1, 1.5, 1, 1, 1, 1]
    WEIGHT_LIST_SPECIAL =    [1000000, 100000, 1000, 10, 1.5, 1, 1, 1, 1, 1, 1, 1]

    # Adjust weight based on the board configuration and moves.
    if 'standard' == model.global_game_configuration['all']['initial_board_layout']:
        if 10 < model.global_game_play_state['black']['moves_taken']:
            weight_list_variable = WEIGHT_LIST_AGGRESSIVE
        elif 20 < model.global_game_play_state['black']['moves_taken']:
            weight_list_variable = WEIGHT_LIST_AGGRESSIVE
        elif 30 < model.global_game_play_state['black']['moves_taken']:
            weight_list_variable = WEIGHT_LIST_AGGRESSIVE

    elif 'german_daisy' == model.global_game_configuration['all']['initial_board_layout']:
        if 10 < model.global_game_play_state['black']['moves_taken']:
            weight_list_variable = WEIGHT_LIST_DEFAULT
        elif 20 < model.global_game_play_state['black']['moves_taken']:
            weight_list_variable = WEIGHT_LIST_DEFAULT
        elif 30 < model.global_game_play_state['black']['moves_taken']:
            weight_list_variable = WEIGHT_LIST_DEFAULT

    elif 'belgian_daisy' == model.global_game_configuration['all']['initial_board_layout']:
        if 0 <= model.global_game_play_state['black']['moves_taken']:
            weight_list_variable = WEIGHT_LIST_SPECIAL
        elif 10 < model.global_game_play_state['black']['moves_taken']:
            weight_list_variable = WEIGHT_LIST_SPECIAL
        elif 20 < model.global_game_play_state['black']['moves_taken']:
            weight_list_variable = WEIGHT_LIST_SPECIAL


    # Tier 00. has someone won this state? This function returns 1000000 if win, -1000000 if loss.
    score += weight_list_variable[0] * terminal_state(player, state)
    if abs(score) > 1000000:
        return score
    # Tier 01. Calculates the score from the amount of pieces.
    score += weight_list_variable[1] * piece_count(player, state)
    if abs(score) > 1000000:
        return score

    # Tier 02. Can you push the marble to the danger zone?
    score += weight_list_variable[2] * in_danger_zone(player, state, ally, opponent)
    if abs(score) > 1000000:
        return score

    # Tier 03. Calculates the distance from the center.
    score += weight_list_variable[3] * manhattan_distance(player, state, ally, opponent)
    if abs(score) > 1000000:
        return score

    # Tier 04. Calculates how condensed the allied pieces are.
    score += weight_list_variable[4] * (clumping(player, opponent_color, ally_pieces_locations, opp_pieces_locations, state))
    if abs(score) > 1000000:
        return score

    # Tier 05. Calculates how many sumitos are available.
    score += weight_list_variable[5] * sumito_num(player, ally_pieces_locations, opp_pieces_locations, state)
    if abs(score) > 1000000:
        return score

    # Tier 06. Calculates how many pairs are available.
    score += weight_list_variable[6] * pairs(player, ally_pieces_locations, opp_pieces_locations, state)
    if abs(score) > 1000000:
        return score

    # Tier 07. Calculates how many triplets are available.
    score += weight_list_variable[7] * triplets(player, ally_pieces_locations, opp_pieces_locations, state)
    if abs(score) > 1000000:
        return score

    # Tier 08. Calculates how the allied marbles strengthen against the opposing formation.
    score += weight_list_variable[8] * strengthen_group(player, ally_pieces_locations, state)
    if abs(score) > 1000000:
        return score

    # Tier 09. Calculates how the allied marbles strengthen against the opposing formation.
    #score -= weight_list_variable[9] * strengthen_group(opponent_color, state)

    # Tier 10. Calculates how the allied marbles split the opposing formation.
    #score += weight_list_variable[10] * attack_modifier * split(player, ally_pieces_locations, opp_pieces_locations, state)

    # Tier 11. score += single_marble_edge(player, ally_pieces_locations, state)
    #score -= weight_list_variable[11] * single_marble_edge(opponent_color, state)

    # Return the score evaluated.
    return score


FDZ = -15
SDZ = -5

DANGER_ZONE_INDICATOR = [
    [-9,    -9,   -9,  -9,  FDZ, FDZ, FDZ, FDZ, FDZ],
    [-9,    -9,   -9,  FDZ, SDZ, SDZ, SDZ, SDZ, FDZ],
    [-9,    -9,   FDZ, SDZ,   0,   0,   0, SDZ, FDZ],
    [-9,    FDZ,  SDZ,   0,   0,   0,   0, SDZ, FDZ],
    [ FDZ,  SDZ,  0,     0,   0,   0,   0, SDZ, FDZ],
    [ FDZ,  SDZ,  0,     0,   0,   0, SDZ, FDZ,  -9],
    [ FDZ,  SDZ,  0,     0,   0, SDZ, FDZ,  -9,  -9],
    [ FDZ,  SDZ,  SDZ, SDZ, SDZ, FDZ,  -9,  -9,  -9],
    [ FDZ,  FDZ,  FDZ, FDZ, FDZ,  -9,  -9,  -9,  -9]
]

def in_danger_zone(player, state, ally, opponent):
    global DANGER_ZONE_INDICATOR

    score = 0

    for i in range(9):
        for j in range(9):
            if state[i][j] == ally:
                score += DANGER_ZONE_INDICATOR[i][j]
            if state[i][j] == opponent:
                score -= DANGER_ZONE_INDICATOR[i][j]

    return score


def terminal_state(player, state):
    # Check the side.
    if player == 'black':
        ally = 1
        opponent = 2
    elif player == 'white':
        ally = 2
        opponent = 1

    ally_pieces_count = 0
    opponent_pieces_count = 0

    for i in range(9):
        for j in range(9):
            if state[i][j] == ally:
                ally_pieces_count += 1
            if state[i][j] == opponent:
                opponent_pieces_count += 1

    if ally_pieces_count < 9:
        return -1
    if opponent_pieces_count < 9:
        return 1
    else:
        return 0


MANHATTAN_WEIGHT = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 2, 2, 2, 1, 0],
    [0, 0, 1, 2, 3, 3, 2, 1, 0],
    [0, 1, 2, 3, 4, 3, 2, 1, 0],
    [0, 1, 2, 3, 3, 2, 1, 0, 0],
    [0, 1, 2, 2, 2, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


def manhattan_distance(player, state, ally, opponent):
    score = 0

    for i in range(9):
        for j in range(9):
            if state[i][j] == ally:
                score += MANHATTAN_WEIGHT[i][j]
            if state[i][j] == opponent:
                score -= MANHATTAN_WEIGHT[i][j]

    return score


def clumping(player, opponent_color, ally_pieces_locations, opp_pieces_locations, state):
    ally_robustness = 0
    opp_robustness = 0

    for location in ally_pieces_locations:
        x = location[0]
        y = location[1]

        if x < 8:
            if state[x][y] == state[x + 1][y]:
                ally_robustness += 1
            if y > 0:
                if state[x][y] == state[x + 1][y - 1]:
                    ally_robustness += 1
        if y < 8:
            if state[x][y] == state[x][y + 1]:
                ally_robustness += 1
        if y > 0:
            if state[x][y] == state[x][y - 1]:
                ally_robustness += 1
        if x > 0:
            if state[x][y] == state[x - 1][y]:
                ally_robustness += 1
            if y < 8:
                if state[x][y] == state[x - 1][y + 1]:
                    ally_robustness += 1

    for location in opp_pieces_locations:
        x = location[0]
        y = location[1]

        if x < 8:
            if state[x][y] == state[x + 1][y]:
                opp_robustness += 1
            if y > 0:
                if state[x][y] == state[x + 1][y - 1]:
                    opp_robustness += 1
        if y < 8:
            if state[x][y] == state[x][y + 1]:
                opp_robustness += 1
        if y > 0:
            if state[x][y] == state[x][y - 1]:
                opp_robustness += 1
        if x > 0:
            if state[x][y] == state[x - 1][y]:
                opp_robustness += 1
            if y < 8:
                if state[x][y] == state[x - 1][y + 1]:
                    opp_robustness += 1

    return ally_robustness - opp_robustness


def piece_count(player, state):

    pieces_score = 0

    # Check the side.
    if player == 'black':
        ally = 1
        opponent = 2
    elif player == 'white':
        ally = 2
        opponent = 1

    for i in range(9):
        for j in range(9):
            if state[i][j] == ally:
                pieces_score += 1
            if state[i][j] == opponent:
                pieces_score -= 1

    return pieces_score


def sumito_num(player, ally_pieces_locations, opp_pieces_locations, state):

    sumito_power = 0

    two_piece_list = ai_state_space_generator.select_two_pieces_combination_from_ally_locations(ally_pieces_locations)
    three_piece_list = ai_state_space_generator.select_three_pieces_combination_from_ally_locations(ally_pieces_locations)

    two_to_one_sumito_list = ai_state_space_generator.generate_move_candidates_for_2_to_1_sumito(state, two_piece_list)
    three_to_one_sumito_list = ai_state_space_generator.generate_move_candidates_for_3_to_1_sumito(state, three_piece_list)
    three_to_two_sumito_list = ai_state_space_generator.generate_move_candidates_for_3_to_2_sumito(state, three_piece_list)

    for sumito in two_to_one_sumito_list:
        sumito_power += 20

    for sumito in three_to_one_sumito_list:
        sumito_power += 20

    for sumito in three_to_two_sumito_list:
        sumito_power += 20

    two_piece_list = ai_state_space_generator.select_two_pieces_combination_from_ally_locations(opp_pieces_locations)
    three_piece_list = ai_state_space_generator.select_three_pieces_combination_from_ally_locations(
        opp_pieces_locations)

    two_to_one_sumito_list = ai_state_space_generator.generate_move_candidates_for_2_to_1_sumito(state, two_piece_list)
    three_to_one_sumito_list = ai_state_space_generator.generate_move_candidates_for_3_to_1_sumito(state,
                                                                                                   three_piece_list)
    three_to_two_sumito_list = ai_state_space_generator.generate_move_candidates_for_3_to_2_sumito(state,
                                                                                                   three_piece_list)

    for sumito in two_to_one_sumito_list:
        sumito_power -= 20

    for sumito in three_to_one_sumito_list:
        sumito_power -= 20

    for sumito in three_to_two_sumito_list:
        sumito_power -= 20

    return sumito_power


def pairs(player, ally_pieces_locations, opp_pieces_locations, state):
    pair_score = 0

    locations = ai_state_space_generator.select_two_pieces_combination_from_ally_locations(ally_pieces_locations)
    for location in locations:
        if is_two_pieces_inline(location[0], location[1], location[2], location[3]):
            pair_score += 1

    locations = ai_state_space_generator.select_two_pieces_combination_from_ally_locations(opp_pieces_locations)
    for location in locations:
        if is_two_pieces_inline(location[0], location[1], location[2], location[3]):
            pair_score -= 1

    return pair_score


def triplets(player, ally_pieces_locations, opp_pieces_locations, state):
    triplet_score = 0

    locations = ai_state_space_generator.select_three_pieces_combination_from_ally_locations(ally_pieces_locations)
    for location in locations:
        if is_three_pieces_inline(location[0], location[1], location[2], location[3], location[4], location[5]):
            triplet_score += 3

    locations = ai_state_space_generator.select_three_pieces_combination_from_ally_locations(opp_pieces_locations)
    for location in locations:
        if is_three_pieces_inline(location[0], location[1], location[2], location[3], location[4], location[5]):
            triplet_score -= 3

    return triplet_score


def split(player, ally_pieces_locations, opp_pieces_locations, state):
    # Check the side.
    if player == 'black':
        ally = 1
        opponent = 2
        opponent_color = 'white'
    elif player == 'white':
        ally = 2
        opponent = 1
        opponent_color = 'black'

    ally_split_score = 0
    opp_split_score = 0

    for location in ally_pieces_locations:
        x = location[0]
        y = location[1]

        if 8 > x > 0:
            if state[x + 1][y] == opponent and state[x - 1][y] == opponent:
                ally_split_score += 15
        if 8 > y > 0:
            if state[x][y + 1] == opponent and state[x][y - 1] == opponent:
                ally_split_score += 15
        if 8 > x > 0 and 8 > y > 0:
            if state[x + 1][y - 1] == opponent and state[x - 1][y + 1] == opponent:
                ally_split_score += 15

    for location in opp_pieces_locations:
        x = location[0]
        y = location[1]

        if 8 > x > 0:
            if state[x + 1][y] == opponent and state[x - 1][y] == opponent:
                opp_split_score += 15
        if 8 > y > 0:
            if state[x][y + 1] == opponent and state[x][y - 1] == opponent:
                opp_split_score += 15
        if 8 > x > 0 and 8 > y > 0:
            if state[x + 1][y - 1] == opponent and state[x - 1][y + 1] == opponent:
                opp_split_score += 15

    return ally_split_score - opp_split_score


def strengthen_group(player, ally_pieces_locations, state):
    # Check the side.
    if player == 'black':
        ally = 1
        opponent = 2
    elif player == 'white':
        ally = 2
        opponent = 1

    strength_score = 0

    for location in ally_pieces_locations:
        x = location[0]
        y = location[1]

        if 8 > x > 0:
            if state[x + 1][y] == opponent and state[x - 1][y] == ally:
                strength_score += 1
            if state[x + 1][y] == ally and state[x - 1][y] == opponent:
                strength_score += 1
        if 8 > y > 0:
            if state[x][y + 1] == opponent and state[x][y - 1] == ally:
                strength_score += 1
            if state[x][y + 1] == ally and state[x][y - 1] == opponent:
                strength_score += 1
        if 8 > x > 0 and 8 > y > 0:
            if state[x + 1][y - 1] == opponent and state[x - 1][y + 1] == ally:
                strength_score += 1
            if state[x + 1][y - 1] == ally and state[x - 1][y + 1] == opponent:
                strength_score += 1

    return strength_score


def single_marble_edge(player, ally_pieces_locations, state):
    # Check the side.
    if player == 'black':
        ally = 1
        opponent = 2
    elif player == 'white':
        ally = 2
        opponent = 1

    edge_score = 0

    for location in ally_pieces_locations:
        x = location[0]
        y = location[1]

        if x == 0 and y > 3:
            edge_score -= 5
        if x == 1 and (y == 3 or y == 8):
            edge_score -= 5
        if x == 2 and (y == 2 or y == 8):
            edge_score -= 5
        if x == 3 and (y == 1 or y == 8):
            edge_score -= 5
        if x == 4 and (y == 0 or y == 8):
            edge_score -= 5
        if x == 5 and (y == 0 or y == 7):
            edge_score -= 5
        if x == 6 and (y == 0 or y == 6):
            edge_score -= 5
        if x == 7 and (y == 0 or y == 5):
            edge_score -= 5
        if x == 8 and y < 5:
            edge_score -= 5

    return edge_score

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
