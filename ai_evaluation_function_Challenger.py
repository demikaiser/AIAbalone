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
from ai_rules import is_three_pieces_inline
from ai_rules import is_two_pieces_inline


def get_evaluation_score(player, state):

    # inits
    row_count = len(state)
    col_count = len(state)
    ally = 0
    opponent = 0
    ally_color = 'black'  # color set according to player being 'black;
    opponent_colorP = 'white'  # color set according to player being 'black;
    rows = range(row_count)
    cols = range(col_count)

    # will store pieces on board, for easy lookups
    ally_pieces = set()
    opponent_pieces = set()
    # Check the side.
    if player == 'black':
        ally = 1
        opponent = 2
        opponent_color = 'white'
    elif player == 'white':
        ally = 2
        opponent = 1
        opponent_color = 'black'

        ally_color = 'white'
        opponent_colorP = 'black'

    ally_pieces_locations = copy.copy(ai_state_space_generator.get_all_ally_positions(state, player))
    opp_pieces_locations = copy.copy(ai_state_space_generator.get_all_ally_positions(state, opponent_color))



    # count pieces and construct sets
    for i in rows:
        for j in cols:

            if state[i][j] == ally:
                ally_pieces.add((j, i, ally_color))  # switching coordinates to match the human's eye of a 2d array

            elif state[i][j] == opponent:
                opponent_pieces.add((j, i, opponent_color))  # switching coordinates to match the human's eye of a 2d array

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
    scores = get_score(player, state, ally, opponent, opponent_color, ally_pieces_locations, opp_pieces_locations)
    terminal_state_score = scores[0]
    piece_count_score = scores[1]
    in_danger_zone_score = scores[2]
    manhattan_distance_score = scores[3]
    clumping_score = scores[4]
    strengthen_group_score = scores[5]

    # look at the board and get battles
    battles = read_battles(ally_pieces, opponent_pieces, ally_color)

    # get allies on edge
    allies_on_edge = on_edge(ally_pieces)

    # enemies on edge
    enemy_on_edge = on_edge(opponent_pieces)
    # print(str(allies_on_edge) + ",\n" + str(enemy_on_edge) + ",\n" + str(battles))
    # use the info gather and analyze
    analyze_result = analyis(allies_on_edge, enemy_on_edge, battles, ally_color)

    groups_in_danger = analyze_result[0]
    enemy_groups_in_danger = analyze_result[1]
    losing_sumitos = analyze_result[2]
    wining_sumitos = analyze_result[3]

    score += weight_list_variable[0] * terminal_state_score # terminal_state(player, state)

    # Tier 01. Calculates the score from the amount of pieces.
    score += weight_list_variable[1] * piece_count_score #piece_count(player, state)

    # Tier 02. Can you push the marble to the danger zone?
    score += weight_list_variable[2] * in_danger_zone_score #in_danger_zone(player, state, ally, opponent)

    # Tier 03. Calculates the distance from the center.
    score += weight_list_variable[3] * manhattan_distance_score #manhattan_distance(player, state, ally, opponent)

    # Tier 04. Calculates how condensed the allied pieces are.
    score += weight_list_variable[4] * clumping_score # (clumping(player, opponent_color, ally_pieces_locations, opp_pieces_locations, state))

    # Tier 05. Calculates how many sumitos are available.
    score += weight_list_variable[5] * sumito_num(player, ally_pieces_locations, opp_pieces_locations, state)

    # Tier 06. Calculates how many pairs are available.
    score += weight_list_variable[6] * pairs(player, ally_pieces_locations, opp_pieces_locations, state)

    # Tier 07. Calculates how many triplets are available.
    score += weight_list_variable[7] * triplets(player, ally_pieces_locations, opp_pieces_locations, state)

    # Tier 08. Calculates how the allied marbles strengthen against the opposing formation.
    score += weight_list_variable[8] * strengthen_group_score # strengthen_group(player, ally_pieces_locations, state)

    score += groups_in_danger * -8000000000
    score += enemy_groups_in_danger * 10000
    score += losing_sumitos * -1000
    score += wining_sumitos * 1000
   # print("groups_in_danger: " + str(groups_in_danger))
    #print("enemy_groups_in_danger: " + str(enemy_groups_in_danger))
   # print("losing_sumitos: " + str(losing_sumitos))
   # print("wining_sumitos: " + str(wining_sumitos))
   # print(score)
    # Tier 09. Calculates how the allied marbles strengthen against the opposing formation.
    #score -= weight_list_variable[9] * strengthen_group(opponent_color, state)

    # Tier 10. Calculates how the allied marbles split the opposing formation.
    #score += weight_list_variable[10] * attack_modifier * split(player, ally_pieces_locations, opp_pieces_locations, state)

    # Tier 11. score += single_marble_edge(player, ally_pieces_locations, state)
    #score -= weight_list_variable[11] * single_marble_edge(opponent_color, state)

    # Return the score evaluated.
    return score


FDZ = -10
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




def get_score(player, state, ally, opponent, opponent_color, ally_pieces_locations, opp_pieces_locations):
    global DANGER_ZONE_INDICATOR
    fscore = [0,0,0,0,0,0,0,0,0,0]
    # Check the side.
    if player == 'black':
        ally = 1
        opponent = 2
    elif player == 'white':
        ally = 2
        opponent = 1

    pieces_score = 0
    ally_pieces_count = 0
    opponent_pieces_count = 0
    danger = 0
    manhattan = 0
    ally_robustness = 0
    opp_robustness = 0
    strength_score = 0

    for i in range(9):
        for j in range(9):
            if state[i][j] == ally:
                ally_pieces_count += 1
                pieces_score += 1
                danger += DANGER_ZONE_INDICATOR[i][j]
                manhattan += MANHATTAN_WEIGHT[i][j]
            if state[i][j] == opponent:
                opponent_pieces_count += 1
                pieces_score -= 1
                danger -= DANGER_ZONE_INDICATOR[i][j]
                manhattan -= MANHATTAN_WEIGHT[i][j]

    if ally_pieces_count < 9:
        fscore[0] = -1
    if opponent_pieces_count < 9:
        fscore[0] = 1
    else:
        fscore[0] = 0

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

    fscore[1] = pieces_score
    fscore[2] = danger
    fscore[3] = manhattan
    fscore[4] = ally_robustness - opp_robustness
    fscore[5] = strength_score
    return fscore

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

# will return an int array of length 3:
# (groups in danger of being booted,
# enemy groups to be booted,
# number of ally wining groups,
# number of ally losing groups)
def analyis(allies_on_edge, enemeny_on_edge, battles, ally_color):
    count = 0
    losing_sumitos = 0
    enemy_groups_in_danger = 0
    wining_sumitos = 0

    # look at each battle and get stats
    for battle in battles:
        if not battle[1]:
            if battle[1] != None and battle[2] == ally_color:
                losing_sumitos += 1
            elif battle[1] != None:
                wining_sumitos += 1
            for i in range(3, len(battle)):
                for ally in allies_on_edge:
                    if ally == battle[i]:
                        count += 1
                for enemey in enemeny_on_edge:
                    if enemey == battle[i]:
                        enemy_groups_in_danger += 1


    return [count, enemy_groups_in_danger,losing_sumitos, wining_sumitos]



def read_battles(ally_pieces, opponent_pieces, ally_color):
    touching_pieces = touching(ally_pieces, opponent_pieces)

    result = []
    for combo in touching_pieces:
        temp = generate_groups_based_on_battle(combo, ally_color, ally_pieces, opponent_pieces)
        result.append(temp[0])
        result.append(temp[1])

    return result


# returns the pieces on the edge of the board
def on_edge(pieces):
    result = set()
    for p in pieces:
        if p[0] == 0 \
                or p[0] == 8 \
                or p[1] == 0 \
                or p[1] == 8\
                or (p[0] == 3 and p[1] == 1) \
                or (p[0] == 2 and p[1] == 2) \
                or (p[0] == 1 and p[1] == 3) \
                or (p[0] == 5 and p[1] == 7) \
                or (p[0] == 6 and p[1] == 6) \
                or (p[0] == 7 and p[1] == 5):
            result.add(p)

    return result

# look at the battles and make groups of who's fighting who
def generate_groups_based_on_battle(combo, ally_color, ally_pieces, opponent_pieces):
    ally = combo[0] if combo[0][2] == ally_color else combo[1]
    opponent = combo[1] if combo[1][2] != ally_color else combo[0]
    dir = combo[0][0] - combo[1][0] if combo[0][0] - combo[1][0] != 0 else combo[0][1] - combo[1][1]
    x_or_y = 0 if combo[0][0] - combo[1][0] != 0 else 1

    al = create_group(ally, dir, x_or_y, ally_pieces)
    opp = create_group(opponent, -1 * dir, x_or_y, opponent_pieces)

    win = al[0] > opp[0]
    if win and al[0] == opp[0]:
        win = None

    al[1] = win
    opp[1] = not win
    al[2] = ally_color
    opp[2] = 'black' if ally_color == 'white' else 'white'
    return al, opp

# will return true/false followed byb pieces. true indicating it will win the current battle
def create_group(piece, dir, x_or_y, pieces):
    a = get_strength(piece, dir, x_or_y, 0, pieces, [0, 0, 'C'])

    return a

# dir 0 means check x, 1 means check y, negative means go
def get_strength(piece, dir, x_or_y, count, ally_pieces, group):
    x = piece[0]
    y = piece[1]
    color = piece[2]

    count += 1
    group[0] = count
    group.append(piece)

    if count == 3:
        return group

    check_piece = (x + dir, y, color)

    if x_or_y == 1:
        check_piece = (x, y + dir, color)

    if check_piece not in ally_pieces:
        return group

    get_strength(check_piece, dir, x_or_y, count, ally_pieces, group)

    return group


def touching(ally_pieces, opponent_pieces):
    result = set()
    for p in ally_pieces:
        x = p[0]
        y = p[1]
        color = 'white' if p[2] == 'black' else 'black'

        if (x, y + 1, color) in opponent_pieces: result.add((p, (x, y + 1, color)))
        if (x, y - 1, color) in opponent_pieces: result.add((p, (x, y - 1, color)))
        if (x + 1, y, color) in opponent_pieces: result.add((p, (x + 1, y, color)))
        if (x - 1, y, color) in opponent_pieces: result.add((p, (x - 1, y, color)))

    return result