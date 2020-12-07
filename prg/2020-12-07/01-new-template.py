"""
Šablona pro rychlý start v pygame - implementuj třídu Game
"""

import sys
import os
import random
import pygame
from pygame import Rect, Vector2, Color


def fix_path(p):
    return os.path.dirname(os.path.realpath(__file__)) + "/" + p


pygame.init()


class PyGame:
    def __init__(self, screen_width, screen_height):
        self.screen_size = Vector2(screen_width, screen_height)
        self.target_fps = 30
        
        self.screen = pygame.display.set_mode((
            int(self.screen_size.x),
            int(self.screen_size.y)
        ))
        self.clock = pygame.time.Clock()

    def run(self):
        self.intialize()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            self.update()
            self.draw()
            
            pygame.display.flip()
            self.clock.tick(self.target_fps)

    def intialize(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass


class Game(PyGame):
    def __init__(self):
        PyGame.__init__(self, 960, 720)
    
    def intialize(self):
        pass

    def update(self):
        pass

    def draw(self):
        self.screen.fill(pygame.Color(0, 0, 0))
        self.screen.fill(
            Color(0, 255, 0),
            Rect(100, 50, 200, 10)
        )
        pygame.draw.polygon(
            self.screen,
            Color(255, 0, 0),
            [Vector2(random.randint(100, 400), random.randint(100, 400)) for _ in range(10)],
            width=3
        )


def main():
    game = Game()
    game.run()


main()
