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

    # Initialize the score.
    score = 0

    # Count ally's marbles.
    score += count_ally_marbles(state)

    # Count opponent's marbles.
    score += count_opponent_marbles(state)

    # Evaluate the position.
    score += evaluate_positions(state)

    # Return the score evaluated.
    return score

def count_ally_marbles(state):

    score_for_count_ally_marbles = 0

    for i in range(0, 9):
        for j in range (0, 9):
            if state[i][j] == 1:
                score_for_count_ally_marbles += 1

    return score_for_count_ally_marbles


def count_opponent_marbles(state):
    score_for_count_opponent_marbles = 0

    for i in range(0, 9):
        for j in range(0, 9):
            if state[i][j] == 2:
                score_for_count_opponent_marbles -= 1

    return score_for_count_opponent_marbles


def evaluate_positions(state):
    score_for_evaluate_positions = 0

    for i in range(0, 9):
        for j in range(0, 9):
            if state[i][j] == 1:

                score_for_evaluate_positions -= math.sqrt((i - 4)**2 + (j - 4)**2)

    return score_for_evaluate_positions

