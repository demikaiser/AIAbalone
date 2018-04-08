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

def get_evaluation_score(player, state):
    # Check the side.
    if player == 'black':
        ally = 1
        opponent = 2
    elif player == 'white':
        ally = 2
        opponent = 1

    # Initialize the two scores.
    score_closeness_to_center_by_manhattan = 0
    score_adjacency = 0
    score_number = 0

    # One loop for everything!
    for i in range(9):
        for j in range(9):
            if state[i][j] == ally:
                score_number += 3
                score_closeness_to_center_by_manhattan -= abs(i - 4) + abs(j - 4)
                if (i + 1) > -1 and (i + 1) < 9 and (j - 1) > -1 and (j - 1) < 9 and state[i + 1][j - 1] == ally:
                    score_adjacency += 1
                if (i + 1) > -1 and (i + 1) < 9 and (j) > -1 and (j) < 9 and state[i + 1][j] == ally:
                    score_adjacency += 1
                if (i) > -1 and (i) < 9 and (j + 1) > -1 and (j + 1) < 9 and state[i][j + 1] == ally:
                    score_adjacency += 1
                if (i - 1) > -1 and (i - 1) < 9 and (j + 1) > -1 and (j + 1) < 9 and state[i - 1][j + 1] == ally:
                    score_adjacency += 1
                if (i - 1) > -1 and (i - 1) < 9 and (j) > -1 and (j) < 9 and state[i - 1][j] == ally:
                    score_adjacency += 1
                if (i) > -1 and (i) < 9 and (j - 1) > -1 and (j - 1) < 9 and state[i][j - 1] == ally:
                    score_adjacency += 1
            elif state[i][j] == opponent:
                score_number -= 2
                score_closeness_to_center_by_manhattan += abs(i - 4) + abs(j - 4)
                if (i + 1) > -1 and (i + 1) < 9 and (j - 1) > -1 and (j - 1) < 9 and state[i + 1][j - 1] == opponent:
                    score_adjacency -= 1
                if (i + 1) > -1 and (i + 1) < 9 and (j) > -1 and (j) < 9 and state[i + 1][j] == opponent:
                    score_adjacency -= 1
                if (i) > -1 and (i) < 9 and (j + 1) > -1 and (j + 1) < 9 and state[i][j + 1] == opponent:
                    score_adjacency -= 1
                if (i - 1) > -1 and (i - 1) < 9 and (j + 1) > -1 and (j + 1) < 9 and state[i - 1][j + 1] == opponent:
                    score_adjacency -= 1
                if (i - 1) > -1 and (i - 1) < 9 and (j) > -1 and (j) < 9 and state[i - 1][j] == opponent:
                    score_adjacency -= 1
                if (i) > -1 and (i) < 9 and (j - 1) > -1 and (j - 1) < 9 and state[i][j - 1] == opponent:
                    score_adjacency -= 1

    # Return the score evaluated.
    return 100 * score_number + score_closeness_to_center_by_manhattan + 10 * score_adjacency

