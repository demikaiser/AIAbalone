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

import math

def get_evaluation_score(player, state):
    # Check the side.
    if player == 'black':
        ally = 1
        opponent = 2
    elif player == 'white':
        ally = 2
        opponent = 1

    # Initialize the score.
    score = 0

    # Weights to be used.
    w1 = 5
    w2 = 3
    w3 = 1
    w4 = 2

    # Count ally's marbles.
    score += w1 * count_ally_marbles(state, ally, opponent)

    # Count opponent's marbles.
    score += w2 * count_opponent_marbles(state, ally, opponent)

    # Evaluate the position.
    score += w3 * evaluate_positions_from_center(state, ally, opponent)

    # Evaluate the position.
    score += w4 * in_danger_zone(state, ally, opponent)

    # Return the score evaluated.
    return score

def count_ally_marbles(state, ally, opponent):

    score_for_count_ally_marbles = 0

    for i in range(0, 9):
        for j in range (0, 9):
            if state[i][j] == ally:
                score_for_count_ally_marbles += 1

    return score_for_count_ally_marbles

def count_opponent_marbles(state, ally, opponent):
    score_for_count_opponent_marbles = 0

    for i in range(0, 9):
        for j in range(0, 9):
            if state[i][j] == opponent:
                score_for_count_opponent_marbles -= 1

    return score_for_count_opponent_marbles

def evaluate_positions_from_center(state, ally, opponent):
    score_for_evaluate_positions = 0

    for i in range(0, 9):
        for j in range(0, 9):
            if state[i][j] == ally:
                score_for_evaluate_positions -= math.sqrt((i - 4)**2 + (j - 4)**2)
            elif state[i][j] == opponent:
                score_for_evaluate_positions += math.sqrt((i - 4) ** 2 + (j - 4) ** 2)

    return score_for_evaluate_positions

FIRST_DANGER_ZONE = -2
SECOND_DANGER_ZONE = -1

DANGER_ZONES = [
    [-9,    -9,   -9,  -9,  FIRST_DANGER_ZONE, FIRST_DANGER_ZONE, FIRST_DANGER_ZONE, FIRST_DANGER_ZONE, FIRST_DANGER_ZONE],
    [-9,    -9,   -9,  FIRST_DANGER_ZONE, SECOND_DANGER_ZONE, SECOND_DANGER_ZONE, SECOND_DANGER_ZONE, SECOND_DANGER_ZONE, FIRST_DANGER_ZONE],
    [-9,    -9,   FIRST_DANGER_ZONE, SECOND_DANGER_ZONE,   0,   0,   0, SECOND_DANGER_ZONE, FIRST_DANGER_ZONE],
    [-9,    FIRST_DANGER_ZONE,  SECOND_DANGER_ZONE,   0,   0,   0,   0, SECOND_DANGER_ZONE, FIRST_DANGER_ZONE],
    [ FIRST_DANGER_ZONE,  SECOND_DANGER_ZONE,  0,     0,   0,   0,   0, SECOND_DANGER_ZONE, FIRST_DANGER_ZONE],
    [ FIRST_DANGER_ZONE,  SECOND_DANGER_ZONE,  0,     0,   0,   0, SECOND_DANGER_ZONE, FIRST_DANGER_ZONE,  -9],
    [ FIRST_DANGER_ZONE,  SECOND_DANGER_ZONE,  0,     0,   0, SECOND_DANGER_ZONE, FIRST_DANGER_ZONE,  -9,  -9],
    [ FIRST_DANGER_ZONE,  SECOND_DANGER_ZONE,  SECOND_DANGER_ZONE, SECOND_DANGER_ZONE, SECOND_DANGER_ZONE, FIRST_DANGER_ZONE,  -9,  -9,  -9],
    [ FIRST_DANGER_ZONE,  FIRST_DANGER_ZONE,  FIRST_DANGER_ZONE, FIRST_DANGER_ZONE, FIRST_DANGER_ZONE,  -9,  -9,  -9,  -9]
]

def in_danger_zone(state, ally, opponent):
    global DANGER_ZONES

    score = 0

    for i in range(9):
        for j in range(9):
            if state[i][j] == ally:
                score += DANGER_ZONES[i][j]
            elif state[i][j] == opponent:
                score -= DANGER_ZONES[i][j]

    return score
