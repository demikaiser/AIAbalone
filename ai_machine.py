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

import _thread, copy
import gameboard, model, ai_search

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
        # ================ ================ An Empty State Initialization ================ ================

        new_state = [
            [-9, -9, -9, -9,  0,  0,  0,  0,  0],
            [-9, -9, -9,  0,  0,  0,  0,  0,  0],
            [-9, -9,  0,  0,  0,  0,  0,  0,  0],
            [-9,  0,  0,  0,  0,  0,  0,  0,  0],
            [ 0,  0,  0,  0,  0,  0,  0,  0,  0],
            [ 0,  0,  0,  0,  0,  0,  0,  0, -9],
            [ 0,  0,  0,  0,  0,  0,  0, -9, -9],
            [ 0,  0,  0,  0,  0,  0, -9, -9, -9],
            [ 0,  0,  0,  0,  0, -9, -9, -9, -9]
        ]

        # ================ ================ AI Search to Get Next Move & State ================ ================
        new_move_and_state = ai_search.get_next_move_and_state_from_ai_search(color,
                                                                              model.global_game_board_state,
                                                                              model.global_game_play_state[color]['moves_taken'],
                                                                              context)
        new_move = new_move_and_state[0]
        new_state = new_move_and_state[1]

        # ================ ================ Print & Log Movement ================ ================
        print_and_log_move_tuple(context, color, new_move)

        # ================ ================ Update the Global State ================ ================
        model.global_game_board_state = copy.deepcopy(new_state)

        # Increase the score and taken moves for each side.
        gameboard.update_game_score()
        if 'black' == color:
            gameboard.update_moves_taken_for('black')
        elif 'white' == color:
            gameboard.update_moves_taken_for('white')

        # ================ ================ Prolog for GUI ================ ================
        # Update the game graphic
        context.update_canvas()

        # Update gameboard after movement.
        gameboard.update_gui_game_panel(context)

        # AI finishes a turn.
        model.update_turn_state(context)
    except Exception:
        print("RuntimeError from ai_calculation_thread.")

# Representation converter from this project's
# to chiens board representation (Output Processing Data Structure - 2D Lists).
chiens_board_representation_output = [
    [-9, -9, -9, -9,  "E1",  "D1",  "C1",  "B1",  "A1"],
    [-9, -9, -9,  "F2",  "E2",  "D2",  "C2",  "B2",  "A2"],
    [-9, -9,  "G3",  "F3",  "E3",  "D3",  "C3",  "B3",  "A3"],
    [-9,  "H4",  "G4",  "F4",  "E4",  "D4",  "C4",  "B4",  "A4"],
    [ "I5",  "H5",  "G5",  "F5",  "E5",  "D5",  "C5",  "B5",  "A5"],
    [ "I6",  "H6",  "G6",  "F6",  "E6",  "D6",  "C6",  "B6", -9],
    [ "I7",  "H7",  "G7",  "F7",  "E7",  "D7",  "C7", -9, -9],
    [ "I8",  "H8",  "G8",  "F8",  "E8",  "D8", -9, -9, -9],
    [ "I9",  "H9",  "G9",  "F9",  "E9", -9, -9, -9, -9]
]

# Print and log the movement of AI.
def print_and_log_move_tuple(context, color, move_tuple):

    length_of_move_tuple = len(move_tuple)
    messages = []

    if 4 == length_of_move_tuple:
        if color == 'black':
            messages.append("Black AI made movement as the following:")
        elif color == 'white':
            messages.append("White AI made movement as the following:")

        messages.append("STD From : " + str(chiens_board_representation_output[move_tuple[0]][move_tuple[1]]))
        messages.append("STD To   : " + str(chiens_board_representation_output[move_tuple[2]][move_tuple[3]]))

        messages.append("From : (" + str(move_tuple[0]) + "," + str(move_tuple[1]) + ")")
        messages.append("To   : (" + str(move_tuple[2]) + "," + str(move_tuple[3]) + ")")

    elif 8 == length_of_move_tuple:
        if color == 'black':
            messages.append("Black AI made movement as the following:")
        elif color == 'white':
            messages.append("White AI made movement as the following:")

        messages.append("STD From : "
                        + str(chiens_board_representation_output[move_tuple[0]][move_tuple[1]]) + ', '
                        + str(chiens_board_representation_output[move_tuple[2]][move_tuple[3]]))
        messages.append("STD To   : "
                        + str(chiens_board_representation_output[move_tuple[4]][move_tuple[5]]) + ', '
                        + str(chiens_board_representation_output[move_tuple[6]][move_tuple[7]]))

        messages.append("From : (" + str(move_tuple[0]) + "," + str(move_tuple[1]) + ")"
                        + " " + "(" + str(move_tuple[2]) + "," + str(move_tuple[3]) + ")")
        messages.append("To   : (" + str(move_tuple[4]) + "," + str(move_tuple[5]) + ")"
                        + " " + "(" + str(move_tuple[6]) + "," + str(move_tuple[7]) + ")")

    elif 12 == length_of_move_tuple:
        if color == 'black':
            messages.append("Black AI made movement as the following:")
        elif color == 'white':
            messages.append("White AI made movement as the following:")

        messages.append("STD From : "
                        + str(chiens_board_representation_output[move_tuple[0]][move_tuple[1]]) + ', '
                        + str(chiens_board_representation_output[move_tuple[2]][move_tuple[3]]) + ', '
                        + str(chiens_board_representation_output[move_tuple[4]][move_tuple[5]]))
        messages.append("STD To   : "
                        + str(chiens_board_representation_output[move_tuple[6]][move_tuple[7]]) + ', '
                        + str(chiens_board_representation_output[move_tuple[8]][move_tuple[9]]) + ', '
                        + str(chiens_board_representation_output[move_tuple[10]][move_tuple[11]]))

        messages.append("From : (" + str(move_tuple[0]) + "," + str(move_tuple[1]) + ")"
                        + " " + "(" + str(move_tuple[2]) + "," + str(move_tuple[3]) + ")"
                        + " " + "(" + str(move_tuple[4]) + "," + str(move_tuple[5]) + ")")
        messages.append("To   : (" + str(move_tuple[6]) + "," + str(move_tuple[7]) + ")"
                        + " " + "(" + str(move_tuple[8]) + "," + str(move_tuple[9]) + ")"
                        + " " + "(" + str(move_tuple[10]) + "," + str(move_tuple[11]) + ")")

    # Add the game information.
    messages.append("Score: <Black> " + str(model.global_game_play_state['black']['score'])
                    + " : " + str(model.global_game_play_state['white']['score']) + " <White>")
    messages.append("Moved: <Black> " + str(model.global_game_play_state['black']['moves_taken'])
                    + " : " + str(model.global_game_play_state['white']['moves_taken']) + " <White>")
    messages.append("Time: <Black> " + str('{0: >#7.1f}'.format(float(model.global_game_play_state['black']['time_taken_for_last_move'])))
                    + " : " + str('{0: >#7.1f}'.format(float(model.global_game_play_state['white']['time_taken_for_last_move']))) + " <White>")
    messages.append("T-Time: <Black> " + str('{0: >#7.1f}'.format(float(model.global_game_play_state['black']['time_taken_total'])))
                    + " : " + str('{0: >#7.1f}'.format(float(model.global_game_play_state['white']['time_taken_total']))) + " <White>")

    # Log all messages.
    context.log(messages)




