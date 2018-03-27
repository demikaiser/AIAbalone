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
    # Check the side.
    if player == 'black':
        ally = 1
        opponent = 2
    elif player == 'white':
        ally = 2
        opponent = 1

    # Initialize the score.
    score = 0

    #TODO: Write your evaluation function(s) here.

    #Value pieces in the middle over other pieces
    def evaluation_function_middle(player,state):
        counter1 = 0
        counter2 = 0
        for i in range(0,9):
            for j in range(0,9):
                if state[i][j] == player:
                    counter1 += i - 5
                    counter2 += j -5

        total = (counter1 + counter2)*100
        return total

    #Check the edges and see where the piece is. Give a score according to how many pieces
    #are on the corner

    def evaluation_function_outer(player,state):
        counter = 0
        if state[0][4] == player:
            counter+=1
        if state[1][3] == player:
            counter+=1
        if state[2][2] == player:
            counter+=1
        if state[3][1] == player:
            counter+=1
        if state[4][0] == player:
            counter+=1
        if state[8][4] == player:
            counter+=1
        if state[7][5] == player:
            counter+=1
        if state[6][6] == player:
            counter+=1
        if state[5][7] == player:
            counter+=1
        if state[4][8] == player:
            counter+=1

        return counter*100

    #Sumito move
    #Evaluate the moves ahead to check if opponent pieces are endangering the edge pieces
    def evaluation_function_sumito_ally(state):
        counter = 0
        if state[0][4] == 1:
            if state[1][5] == 2:
                if state[2][6] == 2:
                    counter+=1
        if state[1][3] == 1:
            if state[2][4] == 2:
                if state[3][5] == 2:
                    counter+=1
        if state[2][2] == 1:
            if state[3][3] == 2:
                if state[4][4] == 2:
                    counter+=1
        if state[3][1] == 1:
            if state[4][2] == 2:
                if state[5][3] == 2:
                    counter+=1
        if state[4][0] == 1:
            if state[5][1] == 2:
                if state[6][2] == 2:
                    counter+=1
        if state[8][4] == 1:
            if state[7][3] == 2:
                if state[6][2] == 2:
                    counter+=1
        if state[7][5] == 1:
            if state[6][4] == 2:
                if state[5][3] == 2:
                    counter+=1
        if state[6][6] == 1:
            if state[5][5] == 2:
                if state[4][4] == 2:
                    counter+=1
        if state[5][7] == 1:
            if state[4][6] == 2:
                if state[3][5] == 2:
                    counter+=1
        if state[4][8] == 1:
            if state[3][7] == 2:
                if state[2][6] == 2:
                    counter+=1
        return counter*100

    # Sumito move
    # Evaluate the moves ahead to check if ally pieces are endangering the edge pieces for the opponent
    def evaluation_function_sumito_opponent(state):
        counter = 0
        if state[0][4] == 2:
            if state[1][5] == 1:
                if state[2][6] == 1:
                    counter += 1
        if state[1][3] == 2:
            if state[2][4] == 1:
                if state[3][5] == 1:
                    counter += 1
        if state[2][2] == 2:
            if state[3][3] == 1:
                if state[4][4] == 1:
                    counter += 1
        if state[3][1] == 2:
            if state[4][2] == 1:
                if state[5][3] == 1:
                    counter += 1
        if state[4][0] == 2:
            if state[5][1] == 1:
                if state[6][2] == 1:
                    counter += 1
        if state[8][4] == 2:
            if state[7][3] == 1:
                if state[6][2] == 1:
                    counter += 1
        if state[7][5] == 2:
            if state[6][4] == 1:
                if state[5][3] == 1:
                    counter += 1
        if state[6][6] == 2:
            if state[5][5] == 1:
                if state[4][4] == 1:
                    counter += 1
        if state[5][7] == 2:
            if state[4][6] == 1:
                if state[3][5] == 1:
                    counter += 1
        if state[4][8] == 2:
            if state[3][7] == 1:
                if state[2][6] == 1:
                    counter += 1
        return counter * 100

    #evaluate all neighboring marbles and provide an evaluation score relative to the opponent's grouping
    def evaluation_function_marble_grouping(player, state):
        counter = 0
        for i in range(1,8):
            for j in range(1,8):
                if state[i][j] == player:
                    if state[i+1][j] == player:
                        counter+=1
                    if state[i-1][j] == player:
                        counter+=1
                    if state[i][j+1] == player:
                        counter+=1
                    if state[i][j-1] == player:
                        counter+=1
                    if state[i+1][j+1] == player:
                        counter+=1
                    if state[i+1][j-1] == player:
                        counter+=1
                    if state[i-1][j+1] == player:
                        counter+=1
                    if state[i-1][j-1] == player:
                        counter+=1
        return counter*50

    score += evaluation_function_middle(ally,state)
    score -= evaluation_function_middle(opponent,state)
    score += evaluation_function_outer(opponent,state)
    score -= evaluation_function_outer(ally, state)
    score -= evaluation_function_sumito_ally(state)
    score += evaluation_function_sumito_opponent(state)
    score += evaluation_function_marble_grouping(ally, state)
    score -= evaluation_function_marble_grouping(opponent, state)

    # Return the score evaluated.
    return score


