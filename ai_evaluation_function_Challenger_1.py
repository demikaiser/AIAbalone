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

import model

def get_evaluation_score(player, state):
    # Check the side.
    if player == 'black':
        ally = 1
        opponent = 2
    elif player == 'white':
        ally = 2
        opponent = 1

    # Initialize the two scores.
    score = 0

    # Adjust weight based on the board configuration and moves.
    if 'standard' == model.global_game_configuration['all']['initial_board_layout']:
        if 10 > model.global_game_play_state['black']['moves_taken']:
            score += initial_game(state, ally, opponent)
        elif 20 > model.global_game_play_state['black']['moves_taken']:
            score += middle_game(state, ally, opponent)
        elif 30 > model.global_game_play_state['black']['moves_taken']:
            score += end_game(state, ally, opponent)

    elif 'german_daisy' == model.global_game_configuration['all']['initial_board_layout']:
        if 10 > model.global_game_play_state['black']['moves_taken']:
            score += initial_game(state, ally, opponent)
        elif 20 > model.global_game_play_state['black']['moves_taken']:
            score += middle_game(state, ally, opponent)
        elif 30 > model.global_game_play_state['black']['moves_taken']:
            score += end_game(state, ally, opponent)

    elif 'belgian_daisy' == model.global_game_configuration['all']['initial_board_layout']:
        if 10 > model.global_game_play_state['black']['moves_taken']:
            score += initial_game(state, ally, opponent)
        elif 20 > model.global_game_play_state['black']['moves_taken']:
            score += middle_game(state, ally, opponent)
        elif 30 > model.global_game_play_state['black']['moves_taken']:
            score += end_game(state, ally, opponent)


    # Return the score evaluated.
    return score


FDZ = -5
SDZ = -3

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

def initial_game(state, ally, opponent):
    global DANGER_ZONE_INDICATOR
    global MANHATTAN_WEIGHT

    # Initialize the two scores.
    score = 0

    # One loop for everything!
    for i in range(9):
        for j in range(9):
            if state[i][j] == ally:
                score += 10
                score += MANHATTAN_WEIGHT[i][j]
                score += DANGER_ZONE_INDICATOR[i][j]
            elif state[i][j] == opponent:
                score -= 10
                score -= MANHATTAN_WEIGHT[i][j]
                score -= DANGER_ZONE_INDICATOR[i][j]

    # Return the score evaluated.
    return score


def middle_game(state, ally, opponent):
    score = 0

    ally_center_of_mass_i = 0
    ally_center_of_mass_j = 0
    ally_number = 0

    opponent_center_of_mass_i = 0
    opponent_center_of_mass_j = 0
    opponent_number = 0

    # Compute the centers of masses.
    for i in range(9):
        for j in range(9):
            if state[i][j] == ally:
                score += 100
                ally_center_of_mass_i += i
                ally_center_of_mass_j += j
                ally_number += 1
            elif state[i][j] == opponent:
                opponent_center_of_mass_i += i
                opponent_center_of_mass_j += j
                opponent_number += 1

    ally_center_of_mass_i /= ally_number
    ally_center_of_mass_j /= ally_number
    opponent_center_of_mass_i /= ally_number
    opponent_center_of_mass_j /= ally_number

    ally_r_i = (ally_center_of_mass_i + 4) / 2
    ally_r_j = (ally_center_of_mass_j + 4) / 2
    opponent_r_i = (opponent_center_of_mass_i + 4) / 2
    opponent_r_j = (opponent_center_of_mass_j + 4) / 2

    for i in range(9):
        for j in range(9):
            if state[i][j] == ally:
                score -= abs(i - ally_r_i) + abs(j - ally_r_j)
            elif state[i][j] == opponent:
                score += abs(i - opponent_r_i) + abs(j - opponent_r_j)

    return score


def end_game(state, ally, opponent):
    # Initialize the two scores.
    score_closeness_to_center_by_manhattan = 0
    score_number = 0

    # One loop for everything!
    for i in range(9):
        for j in range(9):
            if state[i][j] == ally:
                score_number += 1000
                score_closeness_to_center_by_manhattan += 10 / (abs(i - 4) + abs(j - 4) + 1)
            elif state[i][j] == opponent:
                score_number -= 1000
                score_closeness_to_center_by_manhattan -= 10 / (abs(i - 4) + abs(j - 4) + 1)

    # Return the score evaluated.
    return score_closeness_to_center_by_manhattan