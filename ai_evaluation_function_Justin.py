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

import ai_state_space_generator
import copy


# Initial board configuration state for testing.
test_state = [
    [-9, -9, -9, -9,  0,  0,  0,  1,  1],
    [-9, -9, -9,  0,  0,  0,  0,  1,  1],
    [-9, -9,  0,  0,  0,  0,  1,  1,  1],
    [-9,  2,  0,  0,  0,  0,  1,  1,  1],
    [2,   2,  2,  0,  0,  0,  1,  1,  1],
    [2,   2,  2,  0,  0,  0,  0,  1, -9],
    [2,   2,  2,  0,  0,  0,  0, -9, -9],
    [2,   2,  0,  0,  0,  0, -9, -9, -9],
    [2,   2,  0,  0,  0, -9, -9, -9, -9]
]

# A board configuration which is advantageous for black.
good_state_black = [
    [-9, -9, -9, -9,  0,  0,  0,  0,  0],
    [-9, -9, -9,  0,  0,  1,  1,  1,  0],
    [-9, -9,  0,  0,  0,  1,  1,  1,  0],
    [-9,  2,  0,  0,  0,  1,  1,  1,  0],
    [2,   2,  2,  0,  0,  0,  0,  1,  0],
    [2,   2,  2,  0,  0,  0,  0,  0, -9],
    [2,   2,  2,  0,  0,  0,  0, -9, -9],
    [2,   2,  0,  0,  0,  0, -9, -9, -9],
    [2,   2,  1,  1,  1, -9, -9, -9, -9]
]


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

    # First off, has someone won this state?
    if terminal_state(player, state) == 'win':
        score += 1000000
    elif terminal_state(player, state) == 'lose':
        score += -1000000

    # Calculates the score from the amount of pieces.
    score += piece_count(player, state)

    # Calculates the distance from the center.
    score += manhattan_distance(player, state)

    # Calculates how condensed the allied pieces are.
    score += clumping(player, state)

    # Calculates how many sumitos are available.
    score += sumito_num(player, state)

    # Return the score evaluated.
    return score


def terminal_state(player, state):
    # Check the side.
    if player == 'black':
        ally = 1
        opponent = 2
    elif player == 'white':
        ally = 2
        opponent = 1
    ally_pieces_count = 0
    opponent_pieces_count = 0

    for j in range(9):
        for i in range(9):
            if state[i][j] == ally:
                ally_pieces_count += 1

    for j in range(9):
        for i in range(9):
            if state[i][j] == opponent:
                opponent_pieces_count += 1

    if ally_pieces_count < 9:
        return 'lose'
    if opponent_pieces_count < 9:
        return 'win'


def manhattan_distance(player, state):
    distance = 0
    ally_pieces_locations = copy.copy(ai_state_space_generator.get_all_ally_positions(state, player))

    for location in ally_pieces_locations:
        distance += abs(location[0] - 4) + abs(location[1] - 4)

    if distance < 24:
        return 400
    elif distance < 30:
        return 300
    elif distance < 35:
        return 200
    elif distance < 40:
        return 100
    elif distance < 45:
        return 50
    elif distance < 60:
        return 25
    elif distance < 70:
        return 12
    else:
        return 0


def clumping(player, state):
    robustness = 0
    ally_pieces_locations = copy.copy(ai_state_space_generator.get_all_ally_positions(state, player))

    for location in ally_pieces_locations:
        x = location[0]
        y = location[1]

        if x < 8:
            if state[x][y] == state[x+1][y]:
                robustness += 1
            if y > 0:
                if state[x][y] == state[x + 1][y - 1]:
                    robustness += 1
        if y < 8:
            if state[x][y] == state[x][y+1]:
                robustness += 1
        if y > 0:
            if state[x][y] == state[x][y-1]:
                robustness += 1
        if x > 0:
            if state[x][y] == state[x-1][y]:
                robustness += 1
            if y < 8:
                if state[x][y] == state[x - 1][y + 1]:
                    robustness += 1

    if robustness > 55:
        return 320
    elif robustness > 50:
        return 240
    elif robustness > 45:
        return 160
    elif robustness > 40:
        return 80
    elif robustness > 35:
        return 40
    elif robustness > 30:
        return 20
    return 0


def piece_count(player, state):

    pieces_score = 0

    # Check the side.
    if player == 'black':
        ally = 1
        opponent = 2
    elif player == 'white':
        ally = 2
        opponent = 1
    for j in range(9):
        for i in range(9):
            if state[i][j] == ally:
                pieces_score += 1000
    return pieces_score


def sumito_num(player, state):
    ally_pieces_locations = copy.copy(ai_state_space_generator.get_all_ally_positions(state, player))
    sumito_power = 0

    two_piece_list = ai_state_space_generator.select_two_pieces_combination_from_ally_locations(ally_pieces_locations)
    three_piece_list = ai_state_space_generator.select_three_pieces_combination_from_ally_locations(ally_pieces_locations)

    two_to_one_sumito_list = ai_state_space_generator.generate_move_candidates_for_2_to_1_sumito(state, two_piece_list)
    three_to_one_sumito_list = ai_state_space_generator.generate_move_candidates_for_3_to_1_sumito(state, three_piece_list)
    three_to_two_sumito_list = ai_state_space_generator.generate_move_candidates_for_3_to_2_sumito(state, three_piece_list)

    for sumito in two_to_one_sumito_list:
        sumito_power += 40

    for sumito in three_to_one_sumito_list:
        sumito_power += 40

    for sumito in three_to_two_sumito_list:
        sumito_power += 40

    return sumito_power


all_next_states = copy.copy(ai_state_space_generator.generate_all_next_moves_and_states('black', test_state))

if __name__ == '__main__':
    count = 0
    score = 0
    highest = get_evaluation_score('black', all_next_states[1][0])
    highest_count = 0
    best_state = []
    for each_state in all_next_states[1]:
        score = get_evaluation_score('black', each_state)
        if score > highest:
            highest = score
            highest_count = count
        count += 1
    print('Highest score')
    print('State ' + str(highest_count) + ': ' + str(highest))

    #print(get_evaluation_score('black', good_state_black))
