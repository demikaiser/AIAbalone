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

import ai_state_space_generator, ai_search_distributed, copy


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
    manhattan_score = 0
    cluster_score = 0

    manhattan_score = manhattan_distance(state, ally, opponent)

    cluster_score = clumping(ally_pieces_locations, opp_pieces_locations, state)

    #                         W/L      AllyP EnemyP  Danger Manhattan Clumping Sumito            Evade
    weight_list_variable =   [1000000, 1000, 1000,   50,    10,       3,       1, 1, 1, 1, 1, 1, 2000]

    WEIGHT_LIST_DEFAULT =    [1000000, 1000, 1000,   50,    10,       3,       1, 1, 1, 1, 1, 1, 2000]
    WEIGHT_LIST_AGGRESSIVE = [1000000, 1000, 2000,   50,    8,        2,       1, 1, 1, 1, 1, 1, 2000]
    WEIGHT_LIST_DEFENSIVE =  [1000000, 2000, 1000,   50,    15,       5,       1, 1, 1, 1, 1, 1, 3000]

    # Adjust weight based on the board configuration and moves.
    if 'standard' == ai_search_distributed.global_init_board_configuration:
        if manhattan_score + cluster_score < 0:
            weight_list_variable = WEIGHT_LIST_DEFENSIVE
        elif manhattan_score + cluster_score > 5:
            weight_list_variable = WEIGHT_LIST_DEFAULT
        elif manhattan_score + cluster_score > 8:
            weight_list_variable = WEIGHT_LIST_AGGRESSIVE

    elif 'german_daisy' == ai_search_distributed.global_init_board_configuration:
        if manhattan_score + cluster_score < 0:
            weight_list_variable = WEIGHT_LIST_DEFENSIVE
        elif manhattan_score + cluster_score > 5:
            weight_list_variable = WEIGHT_LIST_DEFAULT
        elif manhattan_score + cluster_score > 8:
            weight_list_variable = WEIGHT_LIST_AGGRESSIVE

    elif 'belgian_daisy' == ai_search_distributed.global_init_board_configuration:
        if manhattan_score + cluster_score < 0:
            weight_list_variable = WEIGHT_LIST_AGGRESSIVE
        elif manhattan_score + cluster_score > 5:
            weight_list_variable = WEIGHT_LIST_AGGRESSIVE
        elif manhattan_score + cluster_score > 8:
            weight_list_variable = WEIGHT_LIST_AGGRESSIVE

    manhattan_score *= weight_list_variable[4]
    cluster_score *= weight_list_variable[5]

    # Tier 00. has someone won this state? This function returns 1000000 if win, -1000000 if loss.
    score += weight_list_variable[0] * terminal_state(ally, opponent, state)

    if score == 1000000 or score == -1000000:
        return score

    print("================================")

    print("Manhattan: ", manhattan_score)

    print("Clustering", cluster_score)

    ally_pieces = weight_list_variable[1] * piece_count(ally, state)
    print("Ally pieces: ", ally_pieces)

    opp_pieces = weight_list_variable[2] * piece_count(opponent, state)
    print("Opp pieces: ", opp_pieces)

    sumito_score= weight_list_variable[6] * sumito_num(ally_pieces_locations, opp_pieces_locations, state)
    print("Sumito score: ", sumito_score)

    evade_score = weight_list_variable[12] * evade(ally, opponent, ally_pieces_locations, state)
    print("Evade score: ", evade_score * -1)

    score += ally_pieces
    score -= opp_pieces
    score += sumito_score
    score -= evade_score

    score += manhattan_score
    score += cluster_score

    print("Total score: ", score)

    # score += weight_list_variable[3] * in_danger_zone(ally, opponent, state)

    #score += weight_list_variable[7] * pairs(player, ally_pieces_locations, opp_pieces_locations, state)


    #score += weight_list_variable[8] * triplets(player, ally_pieces_locations, opp_pieces_locations, state)


    #score += weight_list_variable[9] * strengthen_group(player, ally_pieces_locations, state)


    #score -= weight_list_variable[10] * strengthen_group(opponent_color, state)


    #score += weight_list_variable[11] * attack_modifier * split(player, ally_pieces_locations, opp_pieces_locations, state)

    # Return the score evaluated.
    return score


def terminal_state(ally, opponent, state):

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

FDZ = -2
SDZ = -1

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


def in_danger_zone(ally, opponent, state):
    global DANGER_ZONE_INDICATOR

    score = 0

    for i in range(9):
        for j in range(9):
            if state[i][j] == ally:
                score += DANGER_ZONE_INDICATOR[i][j]
            if state[i][j] == opponent:
                score -= DANGER_ZONE_INDICATOR[i][j]

    return score


def piece_count(side, state):

    pieces_score = 0

    for i in range(9):
        for j in range(9):
            if state[i][j] == side:
                pieces_score += 1

    return pieces_score


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


def manhattan_distance(state, ally, opponent):

    score = 0

    for i in range(9):
        for j in range(9):
            if state[i][j] == ally:
                score += MANHATTAN_WEIGHT[i][j]
            if state[i][j] == opponent:
                score -= MANHATTAN_WEIGHT[i][j]

    return score


def clumping(ally_pieces_locations, opp_pieces_locations, state):
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


def sumito_num(ally_pieces_locations, opp_pieces_locations, state):

    sumito_power = 0

    two_piece_list = ai_state_space_generator.select_two_pieces_combination_from_ally_locations(ally_pieces_locations)
    three_piece_list = ai_state_space_generator.select_three_pieces_combination_from_ally_locations(ally_pieces_locations)

    two_to_one_sumito_list = ai_state_space_generator.generate_move_candidates_for_2_to_1_sumito(state, two_piece_list)
    three_to_one_sumito_list = ai_state_space_generator.generate_move_candidates_for_3_to_1_sumito(state, three_piece_list)
    three_to_two_sumito_list = ai_state_space_generator.generate_move_candidates_for_3_to_2_sumito(state, three_piece_list)

    for sumito in two_to_one_sumito_list:
        sumito_power += 1

    for sumito in three_to_one_sumito_list:
        sumito_power += 1

    for sumito in three_to_two_sumito_list:
        sumito_power += 1

    two_piece_list = ai_state_space_generator.select_two_pieces_combination_from_ally_locations(opp_pieces_locations)
    three_piece_list = ai_state_space_generator.select_three_pieces_combination_from_ally_locations(
        opp_pieces_locations)

    two_to_one_sumito_list = ai_state_space_generator.generate_move_candidates_for_2_to_1_sumito(state, two_piece_list)
    three_to_one_sumito_list = ai_state_space_generator.generate_move_candidates_for_3_to_1_sumito(state,
                                                                                                   three_piece_list)
    three_to_two_sumito_list = ai_state_space_generator.generate_move_candidates_for_3_to_2_sumito(state,
                                                                                                   three_piece_list)

    for sumito in two_to_one_sumito_list:
        sumito_power -= 1

    for sumito in three_to_one_sumito_list:
        sumito_power -= 1

    for sumito in three_to_two_sumito_list:
        sumito_power -= 1

    return sumito_power


def pairs(ally_pieces_locations, opp_pieces_locations):
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


def triplets(ally_pieces_locations, opp_pieces_locations):
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


def split(opponent, ally_pieces_locations, opp_pieces_locations, state):

    ally_split_score = 0
    opp_split_score = 0

    for location in ally_pieces_locations:
        x = location[0]
        y = location[1]

        if 8 > x > 0:
            if state[x + 1][y] == opponent and state[x - 1][y] == opponent:
                ally_split_score += 1
        if 8 > y > 0:
            if state[x][y + 1] == opponent and state[x][y - 1] == opponent:
                ally_split_score += 1
        if 8 > x > 0 and 8 > y > 0:
            if state[x + 1][y - 1] == opponent and state[x - 1][y + 1] == opponent:
                ally_split_score += 1

    for location in opp_pieces_locations:
        x = location[0]
        y = location[1]

        if 8 > x > 0:
            if state[x + 1][y] == opponent and state[x - 1][y] == opponent:
                opp_split_score += 1
        if 8 > y > 0:
            if state[x][y + 1] == opponent and state[x][y - 1] == opponent:
                opp_split_score += 1
        if 8 > x > 0 and 8 > y > 0:
            if state[x + 1][y - 1] == opponent and state[x - 1][y + 1] == opponent:
                opp_split_score += 1

    return ally_split_score - opp_split_score


def strengthen_group(ally, opponent, ally_pieces_locations, state):

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


def evade(ally, opponent, ally_pieces_locations, state):

    threat_level = 0

    for location in ally_pieces_locations:
        x = location[0]
        y = location[1]

        if x == 4 and y == 0:
            if state[5][0] == opponent and state[6][0] == opponent:
                threat_level += 1
            if state[5][0] == ally and state[6][0] == opponent and state[7][0] == opponent and state[8][0] == opponent:
                threat_level += 1

            if state[4][1] == opponent and state[4][2] == opponent:
                threat_level += 1
            if state[4][1] == ally and state[4][2] == opponent and state[4][3] == opponent and state[4][4] == opponent:
                threat_level += 1

            if state[3][1] == opponent and state[2][2] == opponent:
                threat_level += 1
            if state[3][1] == ally and state[2][2] == opponent and state[1][3] == opponent and state[0][4] == opponent:
                threat_level += 1

        if x == 5 and y == 0:
            if state[4][1] == opponent and state[3][2] == opponent:
                threat_level += 1
            if state[4][1] == ally and state[3][2] == opponent and state[2][3] == opponent and state[1][4] == opponent:
                threat_level += 1

            if state[5][1] == opponent and state[5][2] == opponent:
                threat_level += 1
            if state[5][1] == ally and state[5][2] == opponent and state[5][3] == opponent and state[5][4] == opponent:
                threat_level += 1

        if x == 6 and y == 0:
            if state[5][1] == opponent and state[4][2] == opponent:
                threat_level += 1
            if state[5][1] == ally and state[4][2] == opponent and state[3][3] == opponent and state[2][4] == opponent:
                threat_level += 1

            if state[6][1] == opponent and state[6][2] == opponent:
                threat_level += 1
            if state[6][1] == ally and state[6][2] == opponent and state[6][3] == opponent and state[6][4] == opponent:
                threat_level += 1

        if x == 7 and y == 0:
            if state[6][1] == opponent and state[5][2] == opponent:
                threat_level += 1
            if state[6][1] == ally and state[5][2] == opponent and state[4][3] == opponent and state[3][4] == opponent:
                threat_level += 1

            if state[7][1] == opponent and state[7][2] == opponent:
                threat_level += 1
            if state[7][1] == ally and state[7][2] == opponent and state[7][3] == opponent and state[7][4] == opponent:
                threat_level += 1

        if x == 8 and y == 0:
            if state[7][0] == opponent and state[6][0] == opponent:
                threat_level += 1
            if state[7][0] == ally and state[6][0] == opponent and state[5][0] == opponent and state[4][0] == opponent:
                threat_level += 1

            if state[7][1] == opponent and state[6][2] == opponent:
                threat_level += 1
            if state[7][1] == ally and state[6][2] == opponent and state[5][3] == opponent and state[4][4] == opponent:
                threat_level += 1

            if state[8][1] == opponent and state[8][2] == opponent:
                threat_level += 1
            if state[8][1] == ally and state[8][2] == opponent and state[8][3] == opponent and state[8][4] == opponent:
                threat_level += 1

        if x == 8 and y == 1:
            if state[7][1] == opponent and state[6][1] == opponent:
                threat_level += 1
            if state[7][1] == ally and state[6][1] == opponent and state[5][1] == opponent and state[4][1] == opponent:
                threat_level += 1

            if state[7][2] == opponent and state[6][3] == opponent:
                threat_level += 1
            if state[7][2] == ally and state[6][3] == opponent and state[5][4] == opponent and state[4][5] == opponent:
                threat_level += 1

        if x == 8 and y == 2:
            if state[7][2] == opponent and state[6][2] == opponent:
                threat_level += 1
            if state[7][2] == ally and state[6][2] == opponent and state[5][2] == opponent and state[4][2] == opponent:
                threat_level += 1

            if state[7][3] == opponent and state[6][4] == opponent:
                threat_level += 1
            if state[7][3] == ally and state[6][4] == opponent and state[5][4] == opponent and state[4][6] == opponent:
                threat_level += 1

        if x == 8 and y == 3:
            if state[7][3] == opponent and state[6][3] == opponent:
                threat_level += 1
            if state[7][3] == ally and state[6][3] == opponent and state[5][3] == opponent and state[4][3] == opponent:
                threat_level += 1

            if state[7][4] == opponent and state[6][5] == opponent:
                threat_level += 1
            if state[7][4] == ally and state[6][5] == opponent and state[5][6] == opponent and state[4][7] == opponent:
                threat_level += 1

        if x == 8 and y == 4:
            if state[7][5] == opponent and state[6][6] == opponent:
                threat_level += 1
            if state[7][5] == ally and state[6][6] == opponent and state[5][7] == opponent and state[4][8] == opponent:
                threat_level += 1

            if state[7][4] == opponent and state[6][4] == opponent:
                threat_level += 1
            if state[7][4] == ally and state[6][4] == opponent and state[5][4] == opponent and state[4][4] == opponent:
                threat_level += 1

            if state[8][3] == opponent and state[8][2] == opponent:
                threat_level += 1
            if state[8][3] == ally and state[8][2] == opponent and state[8][1] == opponent and state[8][0] == opponent:
                threat_level += 1

        if x == 7 and y == 5:
            if state[6][5] == opponent and state[5][5] == opponent:
                threat_level += 1
            if state[6][5] == ally and state[5][5] == opponent and state[4][5] == opponent and state[3][5] == opponent:
                threat_level += 1

            if state[7][4] == opponent and state[7][3] == opponent:
                threat_level += 1
            if state[7][4] == ally and state[7][3] == opponent and state[7][2] == opponent and state[7][1] == opponent:
                threat_level += 1

        if x == 6 and y == 6:
            if state[5][6] == opponent and state[4][6] == opponent:
                threat_level += 1
            if state[5][6] == ally and state[4][6] == opponent and state[3][6] == opponent and state[2][6] == opponent:
                threat_level += 1

            if state[6][5] == opponent and state[6][4] == opponent:
                threat_level += 1
            if state[6][5] == ally and state[6][4] == opponent and state[6][3] == opponent and state[6][2] == opponent:
                threat_level += 1

        if x == 5 and y == 7:
            if state[4][7] == opponent and state[3][7] == opponent:
                threat_level += 1
            if state[4][7] == ally and state[3][7] == opponent and state[2][7] == opponent and state[1][7] == opponent:
                threat_level += 1

            if state[5][6] == opponent and state[5][5] == opponent:
                threat_level += 1
            if state[5][6] == ally and state[5][5] == opponent and state[5][4] == opponent and state[5][3] == opponent:
                threat_level += 1

        if x == 4 and y == 8:
            if state[3][8] == opponent and state[2][8] == opponent:
                threat_level += 1
            if state[3][8] == ally and state[2][8] == opponent and state[1][8] == opponent and state[0][8] == opponent:
                threat_level += 1

            if state[4][7] == opponent and state[4][6] == opponent:
                threat_level += 1
            if state[4][7] == ally and state[4][6] == opponent and state[4][5] == opponent and state[4][4] == opponent:
                threat_level += 1

            if state[5][7] == opponent and state[6][6] == opponent:
                threat_level += 1
            if state[5][7] == ally and state[6][6] == opponent and state[7][5] == opponent and state[8][4] == opponent:
                threat_level += 1

        if x == 3 and y == 8:
            if state[3][7] == opponent and state[3][6] == opponent:
                threat_level += 1
            if state[3][7] == ally and state[3][6] == opponent and state[3][5] == opponent and state[3][4] == opponent:
                threat_level += 1

            if state[4][7] == opponent and state[5][6] == opponent:
                threat_level += 1
            if state[4][7] == ally and state[5][6] == opponent and state[6][5] == opponent and state[7][4] == opponent:
                threat_level += 1

        if x == 2 and y == 8:
            if state[2][7] == opponent and state[2][6] == opponent:
                threat_level += 1
            if state[2][7] == ally and state[2][6] == opponent and state[2][5] == opponent and state[2][4] == opponent:
                threat_level += 1

            if state[3][7] == opponent and state[4][6] == opponent:
                threat_level += 1
            if state[3][7] == ally and state[4][6] == opponent and state[5][5] == opponent and state[6][4] == opponent:
                threat_level += 1

        if x == 1 and y == 8:
            if state[1][7] == opponent and state[1][6] == opponent:
                threat_level += 1
            if state[1][7] == ally and state[1][6] == opponent and state[1][5] == opponent and state[1][4] == opponent:
                threat_level += 1

            if state[2][7] == opponent and state[3][6] == opponent:
                threat_level += 1
            if state[2][7] == ally and state[3][6] == opponent and state[4][5] == opponent and state[5][4] == opponent:
                threat_level += 1

        if x == 0 and y == 8:
            if state[0][7] == opponent and state[0][6] == opponent:
                threat_level += 1
            if state[0][7] == ally and state[0][6] == opponent and state[0][5] == opponent and state[0][4] == opponent:
                threat_level += 1

            if state[1][7] == opponent and state[2][6] == opponent:
                threat_level += 1
            if state[1][7] == ally and state[2][6] == opponent and state[3][5] == opponent and state[4][4] == opponent:
                threat_level += 1

            if state[1][8] == opponent and state[2][8] == opponent:
                threat_level += 1
            if state[1][8] == ally and state[2][8] == opponent and state[3][8] == opponent and state[4][8] == opponent:
                threat_level += 1

        if x == 0 and y == 7:
            if state[1][7] == opponent and state[2][7] == opponent:
                threat_level += 1
            if state[1][7] == ally and state[2][7] == opponent and state[3][7] == opponent and state[4][7] == opponent:
                threat_level += 1

            if state[1][6] == opponent and state[2][5] == opponent:
                threat_level += 1
            if state[1][6] == ally and state[2][5] == opponent and state[3][4] == opponent and state[4][3] == opponent:
                threat_level += 1

        if x == 0 and y == 6:
            if state[1][6] == opponent and state[2][6] == opponent:
                threat_level += 1
            if state[1][6] == ally and state[2][6] == opponent and state[3][6] == opponent and state[4][6] == opponent:
                threat_level += 1

            if state[1][5] == opponent and state[2][4] == opponent:
                threat_level += 1
            if state[1][5] == ally and state[2][4] == opponent and state[3][3] == opponent and state[4][2] == opponent:
                threat_level += 1

        if x == 0 and y == 5:
            if state[1][5] == opponent and state[2][5] == opponent:
                threat_level += 1
            if state[1][5] == ally and state[2][5] == opponent and state[3][5] == opponent and state[4][5] == opponent:
                threat_level += 1

            if state[1][4] == opponent and state[2][3] == opponent:
                threat_level += 1
            if state[1][4] == ally and state[2][3] == opponent and state[3][2] == opponent and state[4][1] == opponent:
                threat_level += 1

        if x == 0 and y == 4:
            if state[0][5] == opponent and state[0][6] == opponent:
                threat_level += 1
            if state[0][5] == ally and state[0][6] == opponent and state[0][7] == opponent and state[0][8] == opponent:
                threat_level += 1

            if state[1][4] == opponent and state[2][4] == opponent:
                threat_level += 1
            if state[1][4] == ally and state[2][4] == opponent and state[3][4] == opponent and state[4][4] == opponent:
                threat_level += 1

            if state[1][3] == opponent and state[2][2] == opponent:
                threat_level += 1
            if state[1][3] == ally and state[2][2] == opponent and state[3][1] == opponent and state[4][1] == opponent:
                threat_level += 1

        if x == 1 and y == 3:
            if state[1][4] == opponent and state[1][5] == opponent:
                threat_level += 1
            if state[1][4] == ally and state[1][5] == opponent and state[1][6] == opponent and state[1][7] == opponent:
                threat_level += 1

            if state[2][3] == opponent and state[3][3] == opponent:
                threat_level += 1
            if state[2][3] == ally and state[3][3] == opponent and state[4][3] == opponent and state[5][3] == opponent:
                threat_level += 1

        if x == 2 and y == 2:
            if state[2][3] == opponent and state[2][4] == opponent:
                threat_level += 1
            if state[2][3] == ally and state[2][4] == opponent and state[2][5] == opponent and state[2][6] == opponent:
                threat_level += 1

            if state[3][2] == opponent and state[4][2] == opponent:
                threat_level += 1
            if state[3][2] == ally and state[4][2] == opponent and state[5][2] == opponent and state[6][2] == opponent:
                threat_level += 1

        if x == 3 and y == 1:
            if state[3][2] == opponent and state[3][3] == opponent:
                threat_level += 1
            if state[3][2] == ally and state[3][3] == opponent and state[3][4] == opponent and state[3][5] == opponent:
                threat_level += 1

            if state[4][1] == opponent and state[5][1] == opponent:
                threat_level += 1
            if state[4][1] == ally and state[4][2] == opponent and state[4][3] == opponent and state[4][4] == opponent:
                threat_level += 1

    return threat_level


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