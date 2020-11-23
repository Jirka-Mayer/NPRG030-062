"""
1) Napište aplikaci, která vám umožní kreslit (myší).
- rozmyslet, co teda přesně chci, ať neprogramujete něco zbytečně složitého
- jak budeme reprezentovat stav tabule?
- co to znamená "kreslit"?
- myš?
2) Aplikace bude umět vyčistit tabuli po stisku mezerníku.
- klávesnice?
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
previous_mouse_position = (0, 0)
current_mouse_position = (0, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    previous_mouse_position = current_mouse_position
    current_mouse_position = pygame.mouse.get_pos()

    if pygame.key.get_pressed()[pygame.K_SPACE]:
        screen.fill((0, 0, 0))

    if pygame.mouse.get_pressed()[0]:
        pygame.draw.line(
            screen,
            pygame.Color(255, 255, 255),
            previous_mouse_position,
            current_mouse_position,
            3
        )
        pygame.draw.circle(
            screen,
            pygame.Color(255, 255, 255),
            pygame.mouse.get_pos(),
            5.0
        )
    
    pygame.display.flip()
    clock.tick(30)
