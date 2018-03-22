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

# <GUIDE TO MAKE THE EVALUATION FUNCTION INDIVIDUALLY>
#
# The evaluation function MUST have a very strict format, the signature of the pseudocode:
# int EvaluationFunction(BoardConfiguration board)
#
# It has to take a board configuration as input, and return the evaluated integer value.
# Only integer values are allowed to return because of the efficiency of the sorting later.
# Technically there is no range limit, but too big number slows the system down.
# The realistic range would be 0 to 10000, and you can't use any deduction or negative values.
#
# If you want to make some multiple evaluation functions, you have to add all scores up at the end.
# There are ways to do it, but one example should be:
#
# TotalEvaluationFunction = EvaluationFunction1 + EvaluationFunction2 + EvaluationFunction3
#
# So the final score would be evaluated from the individual functions.
# You can do whatever you want to do ONLY in this file, but the AI framework will call
# this get_evaluation_score function to evaluate the state, so do NOT change it.
#
# Input: State representation (Game board configuration).
# Output: Total evaluated score (Integer).


def get_evaluation_score(player, state):
    row_count = len(current_state)
    col_count = len(current_state)

    rows = range(row_count)
    cols = range(col_count)

    # will store pieces on board, for easy lookups
    pieces = set()

    # Check the side.
    if player == 'black':
        ally = 1
        opponent = 2
    elif player == 'white':
        ally = 2
        opponent = 1

    # Initialize the score.
    score = 0

    # player counts
    black_player_count = 0
    white_player_count = 0

    # count pieces
    for i in rows:
        for j in cols:

            if current_state[i][j] == 1:
                black_player_count += 1
                pieces.add((i, j, 'B'))

            elif current_state[i][j] == 2:
                white_player_count += 1
                pieces.add((i, j, 'W'))

    print(str(black_player_count) + ", " + str(white_player_count))

    # Return the score evaluated.
    return score


print('started')

current_state = [
            [-9, -9, -9, -9,  0,  0,  0,  1,  1],
            [-9, -9, -9,  0,  0,  0,  1,  1,  1],
            [-9, -9,  0,  0,  0,  0,  0,  0,  0],
            [-9,  0,  0,  0,  0,  0,  0,  0,  0],
            [ 0,  0,  0,  0,  0,  0,  0,  0,  0],
            [ 2,  0,  0,  0,  0,  0,  0,  0, -9],
            [ 2,  0,  0,  0,  0,  0,  0, -9, -9],
            [ 2,  0,  0,  0,  0,  0, -9, -9, -9],
            [ 2,  0,  0,  0,  0, -9, -9, -9, -9]
        ]

get_evaluation_score('black', current_state)
