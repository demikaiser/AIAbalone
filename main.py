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

import view
import pygame

# Take this out of main later.
pygame.init()
pygame.mixer.init()
# pygame.mixer.music.load('music/getDown.ogg')
pygame.mixer.music.load('music/getDown.ogg')
pygame.mixer.music.play(-1)

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
    pygame.event.get()
    view = view.GUI()
    view.start_gui()
