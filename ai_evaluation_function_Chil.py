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


# black_remain indicates how many losable pieces for black side(MAX player) remains,
# initial state value: 6, losing state value: 0
# white_remain indicates how many losable pieces for white side(MIN player) remains,
# initial state value: 6, losing state value: 0
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
    return determine_cluster_state(blacks, whites) * importance_ratio \
        + determine_center_state(blacks, whites, False) * (1 - importance_ratio)


# finds out how does the state look for each side
# the more pieces are connected together the better
# if one side's pieces are split up, this side will have low value
def determine_cluster_state(blacks, whites):
    b_value = 1
    w_value = 1
    return b_value/(b_value + w_value)


# finds out how close the pieces are to the center
def determine_center_state(blacks, whites, calculating_average_value=False):
    # calculate black side
    b_value = 0
    b_num = 0
    for p in blacks:
        b_num += 1
        b1 = ord(p[0]) - ord('E')
        b2 = int(p[1]) - 5
        # if the marbles locate on the outer ring, plus 0
        if abs(b1) == 4 or abs(b2) == 4 or abs(b1 - b2) == 4:
            pass
        # if the marbles locate on 2nd outer ring, plus 1
        elif abs(b1) == 3 or abs(b2) == 3 or abs(b1 - b2) == 3:
            b_value += 1
        elif abs(b1) == 2 or abs(b2) == 2 or abs(b1 - b2) == 2:
            b_value += 2
        elif abs(b1) == 1 or abs(b2) == 1 or abs(b1 - b2) == 1:
            b_value += 3
        else:  # if no conditions have made, the marble sits on center
            b_value += 4
    # calculate white side
    w_value = 0
    w_num = 0
    for p in whites:
        w_num += 1
        w1 = abs(ord(p[0]) - ord('E'))
        w2 = abs(int(p[1]) - 5)
        if abs(w1) == 4 or abs(w2) == 4 or abs(w1 - w2) == 4:
            pass
        elif abs(w1) == 3 or abs(w2) == 3 or abs(w1 - w2) == 3:
            w_value += 1
        elif abs(w1) == 2 or abs(w2) == 2 or abs(w1 - w2) == 2:
            w_value += 2
        elif abs(w1) == 1 or abs(w2) == 1 or abs(w1 - w2) == 1:
            w_value += 3
        else:
            w_value += 4

    # decide if the final value is calculated based on the average value of each piece? or the total value
    if calculating_average_value:
        b_value /= b_num
        w_value /= w_num
    print("b values: %s ; w values: %s" % (b_value, w_value))
    return b_value/(b_value + w_value)


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
