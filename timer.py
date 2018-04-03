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

import _thread
import time
import model
import pygame



def time_oscillator(context):

    try:
        while True:
            pygame.time.delay(500)

            if model.global_game_play_state['all']['game_state'] == 'started_B_Human':
                model.global_game_play_state['black']['time_taken_for_last_move'] += 0.5
                model.global_game_play_state['black']['time_taken_total'] += 0.5
            elif model.global_game_play_state['all']['game_state'] == 'started_B_Computer':
                model.global_game_play_state['black']['time_taken_for_last_move'] += 0.5
                model.global_game_play_state['black']['time_taken_total'] += 0.5
            elif model.global_game_play_state['all']['game_state'] == 'started_W_Human':
                model.global_game_play_state['white']['time_taken_for_last_move'] += 0.5
                model.global_game_play_state['white']['time_taken_total'] += 0.5
            elif model.global_game_play_state['all']['game_state'] == 'started_W_Computer':
                model.global_game_play_state['white']['time_taken_for_last_move'] += 0.5
                model.global_game_play_state['white']['time_taken_total'] += 0.5

            context.update_time('black', model.global_game_play_state['black']['time_taken_for_last_move'])
            context.update_time('white', model.global_game_play_state['white']['time_taken_for_last_move'])
            context.update_total_time('black', model.global_game_play_state['black']['time_taken_total'])
            context.update_total_time('white', model.global_game_play_state['white']['time_taken_total'])

    except RuntimeError:
        print("RuntimeError from time_oscillator.")


def start_time_oscillator(context):
    _thread.start_new_thread(time_oscillator, (context, ))
