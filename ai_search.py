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

import model, math
import ai_state_space_generator
import ai_evaluation_function_Champion
import ai_evaluation_function_Challenger
import ai_evaluation_function_Challenger_1
import ai_evaluation_function_Challenger_2
import ai_evaluation_function_Challenger_3
import ai_evaluation_function_Challenger_4
import ai_evaluation_function_Challenger_5

# ================ ================ Global Variables for Search Process ================ ================

# Transposition table to store explored states to prevent infinite repetition.
# IT MUST BE CLEARED AFTER EACH FINAL MOVE.
global_transposition_table = dict()

# ================ ================ Search Parameters for Optimization ================ ================

# Constants that represent positive and negative infinity.
POSITIVE_INFINITY = math.inf
NEGATIVE_INFINITY = -math.inf

# Minimum and maximum depth for iterative deepening search.
MINIMUM_DEPTH_FOR_ITERATIVE_DEEPENING_SEARCH = 0
MAXIMUM_DEPTH_FOR_ITERATIVE_DEEPENING_SEARCH = 100

# Maximum states for the forward pruning.
MAXIMUM_STATES_FOR_FORWARD_PRUNING = 10

# ================ ================ Search Functions ================ ================

# Updates the next move and state by performing Iterative Deepening Minimax Search with time constraint.
# The following functionalities are implemented for efficiency.
# 1. Hard-coded Playbook of 5 Inital Movement for 3 Board Configuration
# 2. For More Moves, Iterative Deepening Search with Time Constraint
# 3. Main Search Strategy: Minimax Tree Search with Alpha-Beta Pruning
def get_next_move_and_state_from_ai_search(player, state_from, moves_taken, context):

    # Perform Iterative Deepening Search with time constraint to update the best move.
    # This function updates the global_best_next_move_and_state directly, and terminates
    # after the time specified in the global setting.
    iterative_deepening_search_with_time_constraint(player, state_from, moves_taken, context)

    # Get the global_best_next_move_and_state and return the value.
    best_next_move_and_state = model.global_game_play_state[player]['best_next_move_and_state']

    return best_next_move_and_state

# Iterative deepening tree search with a given time constraint.
def iterative_deepening_search_with_time_constraint(player, state_from, moves_taken, context):

    # Clear the candidate moves before start searching.
    model.global_game_play_state[player]['best_next_move_and_state'][0] = []
    model.global_game_play_state[player]['best_next_move_and_state'][1] = []

    # Use the global transposition table.
    global global_transposition_table

    # Perform Iterative Deepening Search with time constraint to update the best move.
    for depth in range(MINIMUM_DEPTH_FOR_ITERATIVE_DEEPENING_SEARCH, MAXIMUM_DEPTH_FOR_ITERATIVE_DEEPENING_SEARCH):
        print("ITERATION DEPTH: " + str(depth) + " for " + player + " player")

        # Clear the transposition table at the beginning of each depth iteration.
        global_transposition_table.clear()

        # Generate the search space.
        all_next_moves_and_states = generate_pruned_and_ordered_next_moves_and_states(player, state_from)
        all_next_moves = all_next_moves_and_states[0]
        all_next_states = all_next_moves_and_states[1]

        # If the player can FINALLY finish the fucking game, PLEASE do so!
        final_blow_index = 0
        for successor_state in all_next_states:
            if is_terminal_state_to_finish_up(player, successor_state):
                model.global_game_play_state[player]['best_next_move_and_state'][0] = all_next_moves[final_blow_index]
                model.global_game_play_state[player]['best_next_move_and_state'][1] = all_next_states[final_blow_index]
                print("AI *FINISHES*: " + str(model.global_game_play_state[player]['best_next_move_and_state']))
                return
            final_blow_index += 1

        # Start search and update the best move & state.
        value = NEGATIVE_INFINITY
        all_next_moves_and_states_index = 0
        temp_best_next_move_and_state = [[], []]
        for successor_state in all_next_states:
            score = minimax_tree_search_with_alpha_beta_pruning(player, successor_state, NEGATIVE_INFINITY, POSITIVE_INFINITY, depth)
            if score > value:
                value = score
                temp_best_next_move_and_state[0] = all_next_moves[all_next_moves_and_states_index]
                temp_best_next_move_and_state[1] = all_next_states[all_next_moves_and_states_index]
            all_next_moves_and_states_index += 1

        # Time-over setting.
        if "started_" not in model.global_game_play_state['all']['game_state'] \
            or model.global_game_configuration[player]['time_limitation'] \
                <= model.global_game_play_state[player]['time_taken_for_last_move']:
            return

        # Update the search result if they are upgraded.
        if model.global_game_play_state[player]['best_next_move_and_state'][0] != temp_best_next_move_and_state[0]:
            model.global_game_play_state[player]['best_next_move_and_state'][0] = temp_best_next_move_and_state[0]
            model.global_game_play_state[player]['best_next_move_and_state'][1] = temp_best_next_move_and_state[1]
            print("AI UPDATED MOVES: " + str(model.global_game_play_state[player]['best_next_move_and_state']))

            #TODO: FOR DEBUG, NOT PRODUCTION.
            context.clear_all_selection()
            context.select_candidate_positions_for_ai(temp_best_next_move_and_state[0])

# Minimax tree search with alpha-beta pruning with a depth limitation.
def minimax_tree_search_with_alpha_beta_pruning(player, state_from, alpha, beta, depth):

    return max_value(player, state_from, alpha, beta, depth)


# The max value function for Minimax search.
def max_value(player, state_from, alpha, beta, depth):

    # Recursion termination conditions.
    if depth <= 0 \
        or "started_" not in model.global_game_play_state['all']['game_state'] \
        or model.global_game_configuration[player]['time_limitation'] \
                <= model.global_game_play_state[player]['time_taken_for_last_move'] \
        or is_this_terminal_state(state_from):
        return evaluation_function_interface(player, state_from)

    # Minimax evaluation with alpha-beta pruning.
    value = NEGATIVE_INFINITY
    for successor_state in generate_pruned_and_ordered_next_moves_and_states(player, state_from)[1]:
        value = max(value, min_value(player, successor_state, alpha, beta, depth - 1))
        if value >= beta:
            return value
        alpha = max(alpha, value)
    return value

# The min value function for Minimax search.
def min_value(player, state_from, alpha, beta, depth):

    # Recursion termination conditions.
    if depth <= 0 \
        or "started_" not in model.global_game_play_state['all']['game_state'] \
        or model.global_game_configuration[player]['time_limitation'] \
                <= model.global_game_play_state[player]['time_taken_for_last_move'] \
        or is_this_terminal_state(state_from):
        return evaluation_function_interface(player, state_from)

    # Minimax evaluation with alpha-beta pruning.
    value = POSITIVE_INFINITY

    opponent_player = ''
    if 'black' == player:
        opponent_player = 'white'
    elif 'white' == player:
        opponent_player = 'black'

    for successor_state in generate_pruned_and_ordered_next_moves_and_states(opponent_player, state_from)[1]:
        value = min(value, max_value(player, successor_state, alpha, beta, depth - 1))
        if value <= alpha:
            return value
        beta = min(beta, value)
    return value

# Generate pruned and ordered next moves and states.
# The following functionalities are implemented for efficiency.
# 1. Forward Pruning with Evaluation Functions
# 2. Move Re-Ordering for ABP Efficiency (Best-Move First Policy)
# 3. Repeated States Removal by Using Transposition Table
def generate_pruned_and_ordered_next_moves_and_states(player, state_from):

    # Use the global transposition table.
    global global_transposition_table

    # Get all moves and states first.
    all_next_moves_and_states = ai_state_space_generator.generate_all_next_moves_and_states(player, state_from)

    # Initialize the variable to return at the end.
    pruned_and_ordered_next_moves_and_states = [[], []]

    # Initialize the evaluation score list.
    evaluation_score_list = []

    # Use the transposition table, put all repeated states to the lowest priority,
    # so those won't be selected at the end.
    for next_state in all_next_moves_and_states[1]:
        if repr(next_state) not in global_transposition_table:
            global_transposition_table[repr(next_state)] = 1
            evaluation_score_list.append(evaluation_function_interface(player, next_state))
        else:
            evaluation_score_list.append(NEGATIVE_INFINITY)

    # Make a dictionary for index processing.
    evaluation_score_dictionary = dict()
    index = 0
    for score in evaluation_score_list:
        evaluation_score_dictionary[score] = index
        index += 1

    # Select the move and state with the highest score.
    index_for_forward_pruning = 0

    for key, value in sorted(evaluation_score_dictionary.items(), reverse=True):

        # Only count n numbers of next moves & states.
        if index_for_forward_pruning >= MAXIMUM_STATES_FOR_FORWARD_PRUNING:
            break

        if key != NEGATIVE_INFINITY:
            pruned_and_ordered_next_moves_and_states[0].append(all_next_moves_and_states[0][value])
            pruned_and_ordered_next_moves_and_states[1].append(all_next_moves_and_states[1][value])
            index_for_forward_pruning += 1

    return pruned_and_ordered_next_moves_and_states

# Return true if the state is the terminal state.
def is_this_terminal_state(state_from):
    # Setup the variables needed.
    flag = False
    black_number = 0
    white_number = 0

    # Count marbles for each side.
    for j in range(9):
        for i in range(9):
            if state_from[i][j] == 1:
                black_number += 1
            elif state_from[i][j] == 2:
                white_number += 1

    # Define the terminal state of the game.
    if black_number < 9 or white_number < 9:
        flag = True

    return flag

# Return true if the state is the terminal state.
def is_terminal_state_to_finish_up(player, state):
    if player == 'black':
        ally = 1
        opponent = 2
    elif player == 'white':
        ally = 2
        opponent = 1

    opponent_pieces_count = 0

    for j in range(9):
        for i in range(9):
            if state[i][j] == opponent:
                opponent_pieces_count += 1

    if opponent_pieces_count < 9:
        return True
    else:
        return False

# The interface for evaluation function testers.
# IMPORTANT: HOW TO UPGRADE (IMPROVE) EVAL FUNCTION.
# 1. Champion eval function is the one already proven to be the best.
# 2. Challenger eval function is what is needed to be test, therefore,
#    it has to be white (which is a disadvantageous position, because
#    we want it to be super better than the Champion one to replace it.
# 3. First, develop the Challenger function with experiments.
# 4. Second, do a lot of simulations to see the Challenger wins all the time.
# 5. Finally, if it does, promote the Challenger to the Champion,
#    by putting the contents of the Challenger to the Champion.
# 6. Start experimenting with a new Challenger, repeat the process.
def evaluation_function_interface(player, state_from):

    if '_B_' in model.global_game_play_state['all']['game_state']:
        return ai_evaluation_function_Champion.get_evaluation_score(player, state_from)
    elif '_W_' in model.global_game_play_state['all']['game_state']:
        return ai_evaluation_function_Challenger.get_evaluation_score(player, state_from)


