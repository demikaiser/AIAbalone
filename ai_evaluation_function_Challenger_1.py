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

    # Return the score evaluated.
    return score


