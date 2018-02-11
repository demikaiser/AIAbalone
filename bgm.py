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

import pygame, random

class BGM:
    # Volume amount to increase or decrease.
    VOLUME_AMOUNT = 0.1

    # A list contains all music for the game. (Feel free to add more music, but it has to be funky!)
    music_list = ['music/getDown.ogg', 'music/neverTooMuch.ogg', 'music/rockWithYou.ogg']

    # Global variable indicates the index of current playing music.
    current_playing_music = 0

    # Setup the environment and play the first song (Theme song).
    def initial_play(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.music_list[0])
        pygame.mixer.music.play(-1)

    # Start music randomly.
    def start_music(self):
        new_index = random.randint(0, len(self.music_list) - 1)
        pygame.mixer.music.load(self.music_list[new_index])
        self.current_playing_music = new_index
        pygame.mixer.music.play(-1)

    # Stop the current music.
    def stop_music(self):
        pygame.mixer.music.stop()

    # Play the next song.
    def next_music(self):
        pygame.mixer.music.stop()
        self.current_playing_music += 1
        if self.current_playing_music == len(self.music_list):
            self.current_playing_music = 0
        pygame.mixer.music.load(self.music_list[self.current_playing_music])
        pygame.mixer.music.play(-1)

    # Volume up.
    def volume_up(self):
        current_volume = pygame.mixer.music.get_volume()
        current_volume = current_volume + self.VOLUME_AMOUNT
        pygame.mixer.music.set_volume(current_volume)

    # Volume down.
    def volume_down(self):
        current_volume = pygame.mixer.music.get_volume()
        current_volume = current_volume - self.VOLUME_AMOUNT
        pygame.mixer.music.set_volume(current_volume)

    # Get funk!
    def get_funk(self):
        pass

    # Secret.
    def secret(self):
        pass