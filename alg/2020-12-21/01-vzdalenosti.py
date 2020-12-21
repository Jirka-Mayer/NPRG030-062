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

    def __getitem__(self, c):
        x, y = c
        return self.cells[x][y]

    def draw(self, screen):
        for x in range(self.width):
            for y in range(self.height):
                self[x, y].draw_background(screen, x, y)
        for x in range(self.width):
            for y in range(self.height):
                self[x, y].draw_walls(screen, x, y)
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

    def generate_at_once(self):
        for _ in self.generate():
            pass

    def clear_maze(self):
        for x in range(self.maze.width):
            for y in range(self.maze.height):
                self.maze[x, y].right_wall = True
                self.maze[x, y].bottom_wall = True
                self.maze[x, y].color = None

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

            self.maze[x, y].color = "blue"

            # zbouráme zeď
            if parent == "right":
                self.maze[x, y].right_wall = False
            elif parent == "bottom":
                self.maze[x, y].bottom_wall = False
            elif parent == "left" and x > 0: 
                self.maze[x - 1, y].right_wall = False
            elif parent == "top" and y > 0:
                self.maze[x, y - 1].bottom_wall = False

        def open_vertex(x, y):
            if not cell_exists(x, y): return
            if cell_closed(x, y): return
            if cell_openned(x, y): return
            open_vertices.append((x, y))
            self.maze[x, y].color = "green"

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


class DeadEndRemover:
    def __init__(self, maze):
        self.maze = maze

    def remove_dead_ends(self):
        for x in range(1, self.maze.width - 1):
            for y in range(1, self.maze.height - 1):
                self.check_cell(x, y)

    def check_cell(self, x, y):
        wall_count = sum([
            int(self.has_wall(x, y, i))
            for i in range(4)
        ])

        if wall_count < 3:
            return

        if random.random() > 0.33:
            return

        indices = list(range(4))
        random.shuffle(indices)
        for i in indices:
            if self.has_wall(x, y, i):
                self.break_wall(x, y, i)
                break

    def has_wall(self, x, y, i):
        if i == 0: return self.maze[x, y].right_wall
        if i == 1: return self.maze[x, y].bottom_wall
        if i == 2: return self.maze[x - 1, y].right_wall
        if i == 3: return self.maze[x, y - 1].bottom_wall
        raise Exception("Invalid value of 'i'.")

    def break_wall(self, x, y, i):
        if i == 0: self.maze[x, y].right_wall = False
        elif i == 1: self.maze[x, y].bottom_wall = False
        elif i == 2: self.maze[x - 1, y].right_wall = False
        elif i == 3: self.maze[x, y - 1].bottom_wall = False
        else: raise Exception("Invalid value of 'i'.")

class DistanceComputer:
    def __init__(self, maze):
        self.maze = maze

        self.distances = None # 2D array of ints/Nones
        self.open_vertices = None # [(x, y, distance), ...]

    def compute_distance(self):
        self.distances = [[None for _ in range(self.maze.height)] for _ in range(self.maze.width)]
        self.open_vertices = [(0, 0, 0)] # [(x, y, distance), ...]

        while len(self.open_vertices) > 0:
            x, y, distance = self.open_vertices.pop(0)

            for nx, ny in self.get_unseen_neighbour_coords(x, y):
                self.open_vertices.append((nx, ny, distance + 1))

            self.distances[x][y] = distance

        self.color_maze()

        return self.distances

    def color_maze(self):
        for x in range(self.maze.width):
            for y in range(self.maze.height):
                distance = self.distances[x][y]
                intensity = int((distance / 70) * 255)
                self.maze[x, y].color = pygame.Color(intensity, intensity, intensity)

    def get_unseen_neighbour_coords(self, x, y):
        for nx, ny in self.get_neighbour_coords(x, y):
            if self.distances[nx][ny] is not None:
                continue
            
            if self.is_open(nx, ny):
                continue

            yield (nx, ny)

    def is_open(self, x, y):
        for v in self.open_vertices:
            if v[0] == x and v[1] == y:
                return True
        return False

    def get_neighbour_coords(self, x, y):
        if x < self.maze.width - 1 and not self.maze[x, y].right_wall:
            yield (x + 1, y)
        if y < self.maze.height - 1 and not self.maze[x, y].bottom_wall:
            yield (x, y + 1)
        if x > 0 and not self.maze[x - 1, y].right_wall:
            yield (x - 1, y)
        if y > 0 and not self.maze[x, y - 1].bottom_wall:
            yield (x, y - 1)


class Game(PyGame):
    def __init__(self):
        PyGame.__init__(self, 960, 720)
        
        self.maze = Maze(30, 22)
        self.generator = MazeGenerator(self.maze)
        self.dead_end_remover = DeadEndRemover(self.maze)
        self.distance_computer = DistanceComputer(self.maze)
    
    def intialize(self):
        self.generator.generate_at_once()
        self.dead_end_remover.remove_dead_ends()
        self.distance_computer.compute_distance()

    def update(self):
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.generator.generate_at_once()
            self.dead_end_remover.remove_dead_ends()
            self.distance_computer.compute_distance()

    def draw(self):
        self.screen.fill("#444444")
        self.maze.draw(self.screen)


def main():
    game = Game()
    game.run()


main()
