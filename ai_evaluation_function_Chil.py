"""
Copyright (C) BCIT AI/ML Option 2018 Team with Members Following - All Rights Reserved.
- Jake Jonghun Choi     jchoi179@my.bcit.ca
- Justin Carey          justinthomascarey@gmail.com
- Pashan Irani          pashanirani@gmail.com
- Tony Huang	        tonyhuang1996@hotmail.ca
- Chil Yuqing Qiu       yuqingqiu93@gmail.com
Unauthorized copying of this file, via any medium is strictly prohibited.
Written by Chil Yuqing Qiu <yuqingqiu93@gmail.com>
"""


import os


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
def get_evaluation_score(player, state, piece_weight=0.5):
    # Check the side.
    # if player == 'black':
    #     ally = 1
    #     opponent = 2
    # elif player == 'white':
    #     ally = 2
    #     opponent = 1
    piece_heuristics = evaluate_pieces(state)
    position_heuristics = evaluate_position(state)
    # if any side has lost 6 pieces
    if (piece_heuristics == 1) or (piece_heuristics == 0):
        return 1
    # if no side has lost 6 pieces yet
    else:
        return piece_heuristics * piece_weight + position_heuristics * (1 - piece_weight)


"""
============================================================================================
|    Tools for Evaluation Functions
============================================================================================
"""


# count the marbles of given color
# PRE: color has to be 'b' for black or 'w' for white
def count_marbles(state, color):
    num_marble = 0
    for marble in state:
        if color in marble:
            num_marble += 1
    return num_marble


# separate state of one line into a list of marbles representing the state
# PARAM: one_line - one line representing current state
# RETURN: a list of marbles representing current state
def one_state(one_line):
    state = one_line.split(",")
    return state


"""
============================================================================================
|    Evaluation Functions
============================================================================================
"""


# black_remain indicates how many losable pieces for black side(MAX player) remains, initial state value: 6, losing state value: 0
# white_remain indicates how many losable pieces for white side(MIN player) remains, initial state value: 6, losing state value: 0
def evaluate_pieces(current_state):
    black_remain = count_marbles(current_state, 'b') - 8
    white_remain = count_marbles(current_state, 'w') - 8
    return black_remain/(black_remain+white_remain)


# evaluates the position of current state
# return range (0, 1), 0.5 means symmetrical,
# closer to one means more centered and grouped, closer to 0 means close to edge and split
# PARAM:
#   current_state: the board state
#   importance_ratio: default 0.5, how important is the cluster state to the center state
#   (if it is more important for the marbles to gather together, raise the ratio, otherwise lower the ratio)
def evaluate_position(current_state, importance_ratio=0.5):
    blacks = []
    whites = []
    # split the marbles into each side's list
    for marble in current_state:
        if 'b' in marble:
            blacks.append(marble)
        if 'w' in marble:
            whites.append(marble)
    return determine_cluster_state() * importance_ratio + determine_center_state() * (1 - importance_ratio)


def determine_cluster_state():
    return 0.5


def determine_center_state():
    return 0.5


# manually debug mode: put the testing board under this directory and test with file name Test.board
if __name__ == "__main__":
    # for redirect file location
    this_dir = os.path.dirname(os.path.realpath('__file__'))
    # for change test files
    file_name = "ssg_tester_output/Test.board"
    test_file = this_dir + '/' + file_name
    try:
        with open(test_file) as file:
            content = file.readlines()
        content = [x.strip() for x in content]
        for line in content:
            print(line)
            print(get_evaluation_score('', one_state(line)))

    except FileNotFoundError:
        print("test file not found:")
        print(test_file)
