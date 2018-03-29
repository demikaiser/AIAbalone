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

import copy

def get_evaluation_score(player, state):
    # Check the side.
    if player == 'black':
        ally = 1
        opponent = 2
        opponent_color = 'white'
    elif player == 'white':
        ally = 2
        opponent = 1
        opponent_color = 'black'


    # Initialize the score.
    score = 0

    # Return the score evaluated.
    return score
