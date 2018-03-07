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

import time, _thread, random
import gameboard, model, rules, movement

# Main function that actually makes movement.
def make_movement(context, color):

    # Different AI strategies can be assigned for some experiments.
    if color == 'black':
        _thread.start_new_thread(ai_calculation_thread, (context, color, ))
    elif color == 'white':
        _thread.start_new_thread(ai_calculation_thread, (context, color, ))


# Calculation thread for artificial intelligence.
def ai_calculation_thread(context, color):
    try:
        # Check the side.
        if color == 'black':
            ally = 1
            opponent = 2
        elif color == 'white':
            ally = 2
            opponent = 1

        # TEMPORARY FUNCTIONALITY (DELETE THIS LATER).
        # Currently it moves just one piece randomly.
        ally_pieces_locations = []

        for j in range(9):
            for i in range(9):
                if model.global_game_board_state[i][j] == ally:
                    ally_pieces_locations.append((i, j))

        move_candidates = []
        for location in ally_pieces_locations:
            possible_moves = rules.generate_all_possible_legal_moves_for_one_piece(location[0], location[1])
            for move in possible_moves:
                move_candidates.append((location[0], location[1], move[0], move[1]))

        random_integer = random.randint(-1, len(move_candidates) - 1)
        movement.move_one_piece(move_candidates[random_integer][0],
                                move_candidates[random_integer][1],
                                move_candidates[random_integer][2],
                                move_candidates[random_integer][3],
                                context)


        # Generate all possible moves.
        #TODO


        # Evaluate moves generated.
        #TODO


        # Choose the most strong move for winning (Goal State).
        #TODO


        # Make an actual move for the game.
        #TODO



        # ================ ================ Prolog for GUI ================ ================
        # Update the game graphic
        context.update_canvas()

        # Update gameboard after movement.
        gameboard.update_gui_game_panel(context)

        # AI finishes a turn.
        model.update_turn_state(context)
    except RuntimeError:
        print("RuntimeError from ai_calculation_thread.")


