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


class Cell:
    SIZE_PX = 30
    WALL_WIDTH_PX = 4
    WALL_COLOR = "black"

    def __init__(self):
        self.right_wall = True
        self.bottom_wall = True
        self.color = None

    def draw_background(self, screen, x, y):
        screen.fill(
            self.color if self.color is not None else "#888888",
            Rect(Cell.SIZE_PX * x, Cell.SIZE_PX * y, Cell.SIZE_PX, Cell.SIZE_PX)
        )

    def draw_walls(self, screen, x, y):
        if self.bottom_wall:
            pygame.draw.line(
                screen,
                Cell.WALL_COLOR,
                (Cell.SIZE_PX * x, Cell.SIZE_PX * (y + 1)),
                (Cell.SIZE_PX * (x + 1), Cell.SIZE_PX * (y + 1)),
                Cell.WALL_WIDTH_PX
            )
        if self.right_wall:
            pygame.draw.line(
                screen,
                Cell.WALL_COLOR,
                (Cell.SIZE_PX * (x + 1), Cell.SIZE_PX * y),
                (Cell.SIZE_PX * (x + 1), Cell.SIZE_PX * (y + 1)),
                Cell.WALL_WIDTH_PX
            )


class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[Cell() for _ in range(height)] for _ in range(width)]

    def draw(self, screen):
        for x in range(self.width):
            for y in range(self.height):
                self.cells[x][y].draw_background(screen, x, y)
        for x in range(self.width):
            for y in range(self.height):
                self.cells[x][y].draw_walls(screen, x, y)
        pygame.draw.line(
            screen,
            Cell.WALL_COLOR,
            (0, 0),
            (Cell.SIZE_PX * self.width, 0),
            Cell.WALL_WIDTH_PX
        )
        pygame.draw.line(
            screen,
            Cell.WALL_COLOR,
            (0, 0),
            (0, Cell.SIZE_PX * self.height),
            Cell.WALL_WIDTH_PX
        )


class MazeGenerator:
    def __init__(self, maze):
        self.maze = maze

    def generate(self):
        self.maze.cells[0][0].color = "red"
        self.maze.cells[-1][-1].color = "green"
        for x in range(self.maze.width):
            for y in range(self.maze.height):
                self.maze.cells[x][y].right_wall = random.choice([True, False])
                self.maze.cells[x][y].bottom_wall = random.choice([True, False])


class Game(PyGame):
    def __init__(self):
        PyGame.__init__(self, 960, 720)
        
        self.maze = Maze(30  , 22)
        self.generator = MazeGenerator(self.maze)
    
    def intialize(self):
        self.generator.generate()

    def update(self):
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.generator.generate()

    def draw(self):
        self.screen.fill("#444444")
        self.maze.draw(self.screen)


def main():
    game = Game()
    game.run()


main()
