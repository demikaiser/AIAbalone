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
    score = 0
    ally_marbles_coordinates = []
    opponent_marbles_coordinates = []

    # Compute the centers of masses.
    for i in range(9):
        for j in range(9):
            if state[i][j] == ally:
                ally_marbles_coordinates.append((i, j))
                score += 100
            elif state[i][j] == opponent:
                opponent_marbles_coordinates.append((i, j))
                score -= 100

    for coordinates in ally_marbles_coordinates:
        for other_coordinates in ally_marbles_coordinates:
            score -= abs(coordinates[0] - other_coordinates[0]) + abs(coordinates[1] - other_coordinates[1])

    for coordinates in opponent_marbles_coordinates:
        for other_coordinates in opponent_marbles_coordinates:
            score += abs(coordinates[0] - other_coordinates[0]) + abs(coordinates[1] - other_coordinates[1])

    # Return the score evaluated.
    return score


