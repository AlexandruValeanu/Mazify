import pygame
from maze import Maze
from solvers import astar_solver
from random import randint

import tkinter as tk
from tkinter import messagebox

from datetime import datetime
import math


def __get_time(seconds):
    seconds = math.ceil(seconds)
    minutes = 0

    while seconds >= 60:
        minutes += 1
        seconds -= 60

    if minutes > 0 and seconds > 0:
        return str(minutes) + ' minute(s)' + ' ' + str(seconds) + ' second(s)'

    if minutes > 0:
        return str(minutes) + ' minute(s)'
    else:
        return str(seconds) + ' second(s)'


def __screen_resolution():
    root = tk.Tk()
    root.withdraw()
    return root.winfo_screenwidth(), root.winfo_screenheight()


def run_game(filename, start=None, end=None):
    maze = Maze.load_from_file(filename)

    if start is None:
        while True:
            a, b = randint(0, maze.nrows - 1), randint(0, maze.ncolumns - 1)
            c, d = randint(0, maze.nrows - 1), randint(0, maze.ncolumns - 1)

            if (a, b) != (c, d) and not maze.is_wall(a, b) and not maze.is_wall(c, d) and \
                    len(astar_solver.solve_maze(maze, (a, b), (c, d))):
                start = (a, b)
                end = (c, d)
                break

    current = start

    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    PURPLE = (186, 85, 211)
    GREEN = (127, 255, 0)
    BLUE = (30, 144, 255)

    # This sets the WIDTH and HEIGHT of each grid location
    WIDTH = 1
    HEIGHT = 1

    screen_width, screen_height = __screen_resolution()
    while (WIDTH + 2) * maze.ncolumns < screen_width and (HEIGHT + 2) * maze.nrows < screen_height:
        WIDTH += 1
        HEIGHT += 1

    # Initialize pygame
    pygame.init()

    # Set the HEIGHT and WIDTH of the screen
    WINDOW_SIZE = [WIDTH * maze.ncolumns, HEIGHT * maze.nrows]
    screen = pygame.display.set_mode(WINDOW_SIZE)

    # Set title of screen
    pygame.display.set_caption("Mazify")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # grid of colors
    color_grid = [[WHITE for column in range(maze.ncolumns)] for row in range(maze.nrows)]

    start_time = datetime.now()

    MIN_FRAME_RATE = 10
    MAX_FRAME_RATE = 1000
    frame_rate = 60

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                root = tk.Tk()
                root.withdraw()

                if messagebox.askyesno('Verify', 'Really quit?'):
                    done = True  # Flag that we are done so we exit this loop
                else:
                    messagebox.showinfo('No', 'Quit has been cancelled')

        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            # print("DOWN")
            if maze.in_maze(current[0] + 1, current[1]) and not maze.is_wall(current[0] + 1, current[1]):
                current = (current[0] + 1, current[1])

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            # print("UP")
            if maze.in_maze(current[0] - 1, current[1]) and not maze.is_wall(current[0] - 1, current[1]):
                current = (current[0] - 1, current[1])

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            # print("LEFT")
            if maze.in_maze(current[0], current[1] - 1) and not maze.is_wall(current[0], current[1] - 1):
                current = (current[0], current[1] - 1)

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            # print("RIGHT")
            if maze.in_maze(current[0], current[1] + 1) and not maze.is_wall(current[0], current[1] + 1):
                current = (current[0], current[1] + 1)

        if current == end:
            root = tk.Tk()
            root.withdraw()

            end_time = datetime.now()
            messagebox.showwarning('', 'Maze solved in {}. Congratulations!'.format(
                __get_time((end_time - start_time).total_seconds())))

            if not messagebox.askyesno('', 'Do you want to play another game?'):
                break

            while True:
                x, y = randint(0, maze.nrows - 1), randint(0, maze.ncolumns - 1)

                if not maze.is_wall(x, y) and len(astar_solver.solve_maze(maze, current, (x, y))):
                    end = (x, y)
                    break

            start_time = datetime.now()
            continue

        # Set the screen background
        screen.fill(BLACK)

        # set the color_grid
        for row in range(maze.nrows):
            for column in range(maze.ncolumns):
                color = WHITE

                if maze.is_wall(row, column):
                    color = BLACK

                if (row, column) == end:
                    color = BLUE

                if (row, column) == current:
                    color = PURPLE

                color_grid[row][column] = color

        if keys[pygame.K_t]:
            # print("solution")
            path = astar_solver.solve_maze(maze, current, end)

            for (x, y) in path:
                if (x, y) != current and (x, y) != end:
                    color_grid[x][y] = RED

        # Draw the grid
        for row in range(maze.nrows):
            for column in range(maze.ncolumns):
                pygame.draw.rect(screen, color_grid[row][column], [WIDTH * column, HEIGHT * row, WIDTH, HEIGHT])

        if keys[pygame.K_z]:
            pygame.draw.circle(screen, PURPLE, (WIDTH * current[1], HEIGHT * current[0]), 25)

        if keys[pygame.K_x]:
            pygame.draw.circle(screen, BLUE, (WIDTH * end[1], HEIGHT * end[0]), 25)

        if keys[pygame.K_c]:
            frame_rate -= 1
            frame_rate = max(frame_rate, MIN_FRAME_RATE)

        if keys[pygame.K_v]:
            frame_rate += 1
            frame_rate = min(frame_rate, MAX_FRAME_RATE)

        if keys[pygame.K_f]:
            print("Frame rate:", frame_rate)

        # Limit to frame_rate frames per second
        clock.tick(frame_rate)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang' on exit.
    pygame.quit()
