"""
Máme obrazovku a ta na některých pixelech hoří.
Každý snímek se požár rozšíří do okolních pixelů.
"""

import sys
import os
import random
import pygame
from pygame import Rect, Vector2, Color

def fix_path(p):
    return os.path.dirname(os.path.realpath(__file__)) + "/" + p

pygame.init()

width = 960
height = 720

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# definuj stav hry (INITIALIZE)
FIRE_COLOR = pygame.Color(255, 0, 0)
PAPER_COLOR = pygame.Color(255, 255, 255)

screen.fill(PAPER_COLOR)
screen.set_at((200, 100), FIRE_COLOR) # zažehni požár

# načti pixel:
# screen.get_at((x, y)) -> color

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # aktualizuj stav hry (UPDATE)
    # ...

    # DRAW vlastně nebude, kreslíme už během UPDATE
    
    pygame.display.flip()
    clock.tick(30)
