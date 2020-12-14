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
        self.generator_instance = None

    def start_generation(self):
        self.generator_instance = self.generate()

    def step_generation(self):
        if self.generator_instance is None:
            return
        
        try:
            self.generator_instance.__next__()
        except StopIteration:
            self.generator_instance = None

    def clear_maze(self):
        # self.maze.cells[0][0].color = "red"
        # self.maze.cells[-1][-1].color = "green"
        for x in range(self.maze.width):
            for y in range(self.maze.height):
                self.maze.cells[x][y].right_wall = True
                self.maze.cells[x][y].bottom_wall = True
                self.maze.cells[x][y].color = None

    def generate(self):
        self.clear_maze()

        open_vertices = []
        closed_vertices = [[None for _ in range(self.maze.height)] for _ in range(self.maze.width)]

        # pomocné funkce
        def cell_exists(x, y):
            if x < 0 or x >= self.maze.width: return False
            if y < 0 or y >= self.maze.height: return False
            return True

        def cell_closed(x, y):
            return closed_vertices[x][y] is not None

        def cell_openned(x, y):
            return (x, y) in open_vertices

        def close_vertex(x, y, parent):
            closed_vertices[x][y] = parent

            self.maze.cells[x][y].color = "blue"

            # zbouráme zeď
            if parent == "right":
                self.maze.cells[x][y].right_wall = False
            elif parent == "bottom":
                self.maze.cells[x][y].bottom_wall = False
            elif parent == "left" and x > 0: 
                self.maze.cells[x - 1][y].right_wall = False
            elif parent == "top" and y > 0:
                self.maze.cells[x][y - 1].bottom_wall = False

        def open_vertex(x, y):
            if not cell_exists(x, y): return
            if cell_closed(x, y): return
            if cell_openned(x, y): return
            open_vertices.append((x, y))
            self.maze.cells[x][y].color = "green"

        # počáteční stav
        close_vertex(0, 0, "left")
        open_vertex(1, 0)
        open_vertex(0, 1)

        while len(open_vertices) > 0:
            yield None

            # náhodný otevřený vrchol
            i = random.randint(0, len(open_vertices) - 1)
            v = open_vertices[i]
            del open_vertices[i]
            
            # seznam uzavřených sousedů pro vybírání rodiče
            closed_neighbours = []
            if cell_exists(v[0], v[1] - 1) and cell_closed(v[0], v[1] - 1):
                closed_neighbours.append("top")
            if cell_exists(v[0], v[1] + 1) and cell_closed(v[0], v[1] + 1):
                closed_neighbours.append("bottom")
            if cell_exists(v[0] - 1, v[1]) and cell_closed(v[0] - 1, v[1]):
                closed_neighbours.append("left")
            if cell_exists(v[0] + 1, v[1]) and cell_closed(v[0] + 1, v[1]):
                closed_neighbours.append("right")
            
            assert len(closed_neighbours) > 0, "No viable parent exists"

            # zavřeme vybraný vrchol
            picked_parent = random.choice(closed_neighbours)
            close_vertex(v[0], v[1], picked_parent)

            # otevřeme sousední vrcholy (pokud jsou volné)
            open_vertex(v[0] + 1, v[1])
            open_vertex(v[0] - 1, v[1])
            open_vertex(v[0], v[1] + 1)
            open_vertex(v[0], v[1] - 1)


class Game(PyGame):
    def __init__(self):
        PyGame.__init__(self, 960, 720)
        
        self.maze = Maze(30  , 22)
        self.generator = MazeGenerator(self.maze)
    
    def intialize(self):
        self.generator.start_generation()

    def update(self):
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.generator.start_generation()

        for _ in range(2):
            self.generator.step_generation()

    def draw(self):
        self.screen.fill("#444444")
        self.maze.draw(self.screen)


def main():
    game = Game()
    game.run()


main()
