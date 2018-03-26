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

    # inits
    row_count = len(state)
    col_count = len(state)
    ally = 0
    opponent = 0
    ally_color = 'B'  # color set according to player being 'black;
    opponent_color = 'W' # color set according to player being 'black;
    rows = range(row_count)
    cols = range(col_count)

    # will store pieces on board, for easy lookups
    ally_pieces = set()
    opponent_pieces = set()

    # Check the side.
    if player == 'black':
        ally = 1
        opponent = 2
    elif player == 'white':
        ally = 2
        opponent = 1

        # change colors to be based on the player being 'white'
        ally_color = 'W'
        opponent_color = 'B'

    # Initialize the score.
    score = 0

    # player counts
    ally_player_count = 0
    opponent_player_count = 0

    # count pieces and construct sets
    for i in rows:
        for j in cols:

            if state[i][j] == ally:
                ally_player_count += 1
                ally_pieces.add((j, i, ally_color))  # switching coordinates to match the human's eye of a 2d array

            elif state[i][j] == opponent:
                opponent_player_count += 1
                opponent_pieces.add((j, i, opponent_color))  # switching coordinates to match the human's eye of a 2d array

    # give score based on the number of players
    if ally_player_count == opponent_player_count:
        score += 10
    elif ally_player_count > opponent_player_count:
        score += 10
        score += ally_player_count - opponent_player_count
    elif ally_player_count < opponent_player_count:
        score += 10
        score -= opponent_player_count - ally_player_count

    # print("ally_player_count: " + str(ally_player_count))
    # print("opponent_player_count: " + str(opponent_player_count))

    # look at the board and get battles
    battles = read_battles(ally_pieces, opponent_pieces, ally_color)

    # get allies on edge
    allies_on_edge = on_edge(ally_pieces)

    # enemies on edge
    enemy_on_edge = on_edge(opponent_pieces)

    # use the info gather and analyze
    analyze_result = analyis(allies_on_edge, enemy_on_edge, battles, ally_color)

    groups_in_danger = analyze_result[0]
    enemy_groups_in_danger = analyze_result[1]
    losing_sumitos = analyze_result[2]
    wining_sumitos = analyze_result[3]

    # print("groups_in_danger: " + str(groups_in_danger))
    # print("enemy_groups_in_danger: " + str(enemy_groups_in_danger))
    # print("losing_sumitos: " + str(losing_sumitos))
    # print("wining_sumitos: " + str(wining_sumitos))

    score += groups_in_danger * -20
    score += enemy_groups_in_danger * 10
    score += losing_sumitos * -10
    score += wining_sumitos * 10

    # Return the score evaluated.
    return score


# will return an int array of length 3:
# (groups in danger of being booted,
# enemy groups to be booted,
# number of ally wining groups,
# number of ally losing groups)
def analyis(allies_on_edge, enemeny_on_edge, battles, ally_color):
    count = 0
    losing_sumitos = 0
    enemy_groups_in_danger = 0
    wining_sumitos = 0

    # look at each battle and get stats
    for battle in battles:
        if not battle[1]:
            if battle[2] == ally_color:
                losing_sumitos += 1
            else:
                wining_sumitos += 1
            for i in range(3, len(battle)):
                for ally in allies_on_edge:
                    if ally == battle[i]:
                        count += 1
                for enemey in enemeny_on_edge:
                    if enemey == battle[i]:
                        enemy_groups_in_danger += 1


    return [count, enemy_groups_in_danger,losing_sumitos, wining_sumitos]



def read_battles(ally_pieces, opponent_pieces, ally_color):
    touching_pieces = touching(ally_pieces, opponent_pieces)

    result = []
    for combo in touching_pieces:
        temp = generate_groups_based_on_battle(combo, ally_color, ally_pieces, opponent_pieces)
        result.append(temp[0])
        result.append(temp[1])

    return result


# returns the pieces on the edge of the board
def on_edge(pieces):
    result = set()
    for p in pieces:
        if p[0] == 0 \
                or p[0] == 8 \
                or p[1] == 0 \
                or p[1] == 8\
                or (p[0] == 3 and p[1] == 1) \
                or (p[0] == 2 and p[1] == 2) \
                or (p[0] == 1 and p[1] == 3) \
                or (p[0] == 5 and p[1] == 7) \
                or (p[0] == 6 and p[1] == 6) \
                or (p[0] == 7 and p[1] == 5):
            result.add(p)

    return result

# look at the battles and make groups of who's fighting who
def generate_groups_based_on_battle(combo, ally_color, ally_pieces, opponent_pieces):
    ally = combo[0] if combo[0][2] == ally_color else combo[1]
    opponent = combo[1] if combo[1][2] != ally_color else combo[0]
    dir = combo[0][0] - combo[1][0] if combo[0][0] - combo[1][0] != 0 else combo[0][1] - combo[1][1]
    x_or_y = 0 if combo[0][0] - combo[1][0] != 0 else 1

    al = create_group(ally, dir, x_or_y, ally_pieces)
    opp = create_group(opponent, -1 * dir, x_or_y, opponent_pieces)

    win = al[0] >= opp[0]
    al[1] = win
    opp[1] = not win
    al[2] = ally_color
    opp[2] = 'B' if ally_color == 'W' else 'W'
    return al, opp

# will return true/false followed byb pieces. true indicating it will win the current battle
def create_group(piece, dir, x_or_y, pieces):
    a = get_strength(piece, dir, x_or_y, 0, pieces, [0, 0, 'C'])

    return a

# dir 0 means check x, 1 means check y, negative means go
def get_strength(piece, dir, x_or_y, count, ally_pieces, group):
    x = piece[0]
    y = piece[1]
    color = piece[2]

    count += 1
    group[0] = count
    group.append(piece)

    if count == 3:
        return group

    check_piece = (x + dir, y, color)

    if x_or_y == 1:
        check_piece = (x, y + dir, color)

    if check_piece not in ally_pieces:
        return group

    get_strength(check_piece, dir, x_or_y, count, ally_pieces, group)

    return group


def touching(ally_pieces, opponent_pieces):
    result = set()
    for p in ally_pieces:
        x = p[0]
        y = p[1]
        color = 'W' if p[2] == 'B' else 'B'

        if (x, y + 1, color) in opponent_pieces: result.add((p, (x, y + 1, color)))
        if (x, y - 1, color) in opponent_pieces: result.add((p, (x, y - 1, color)))
        if (x + 1, y, color) in opponent_pieces: result.add((p, (x + 1, y, color)))
        if (x - 1, y, color) in opponent_pieces: result.add((p, (x - 1, y, color)))

    return result



initial_game_board_state_german_daisy = [
    [-9, -9, -9, -9,  0,  0,  0,  1,  0],
    [-9, -9, -9,  0,  0,  1,  1,  1,  0],
    [-9, -9,  2,  2,  0,  1,  1,  0,  0],
    [-9,  2,  2,  2,  0,  0,  1,  0,  0],
    [ 0,  2,  2,  0,  0,  0,  2,  2,  0],
    [ 0,  0,  0,  0,  0,  2,  2,  2, -9],
    [ 0,  0,  1,  1,  0,  2,  2, -9, -9],
    [ 0,  1,  1,  1,  0,  0, -9, -9, -9],
    [ 0,  1,  1,  0,  0, -9, -9, -9, -9]
]

print(get_evaluation_score('black', initial_game_board_state_german_daisy))
