"""
Přepíšeme tuhle šablonu, aby se s ní líp pracovalo.
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
# ...

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # aktualizuj stav hry (UPDATE)
    # ...

    # vykresli stav hry (DRAW)
    screen.fill(pygame.Color(0, 0, 0))
    screen.fill(
        Color(0, 255, 0),
        Rect(100, 50, 200, 10)
    )
    pygame.draw.polygon(
        screen,
        Color(255, 0, 0),
        [Vector2(random.randint(100, 400), random.randint(100, 400)) for _ in range(10)],
        width=3
    )
    # ...
    
    pygame.display.flip()
    clock.tick(30)
