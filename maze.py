from numpy.random import random_integers as rand
from draw_maze import ascii_representation

from constants import *


class Maze:
    def __init__(self, rows, columns):
        assert rows >= 1 and columns >= 1

        self.nrows = rows
        self.ncolumns = columns
        self.board = np.zeros((rows, columns), dtype=WALL_TYPE)
        self.board.fill(EMPTY)

    def set_borders(self):
        self.board[0, :] = self.board[-1, :] = WALL
        self.board[:, 0] = self.board[:, -1] = WALL

    def is_wall(self, x, y):
        assert self.in_maze(x, y)
        return self.board[x][y] == WALL

    def set_wall(self, x, y):
        assert self.in_maze(x, y)
        self.board[x][y] = WALL

    def remove_wall(self, x, y):
        assert self.in_maze(x, y)
        self.board[x][y] = EMPTY

    def in_maze(self, x, y):
        return 0 <= x < self.nrows and 0 <= y < self.ncolumns

    def write_to_file(self, filename):
        f = open(filename, 'w')
        f.write(ascii_representation(self))
        f.close()

    @staticmethod
    def load_from_file(filename):
        with open(filename, 'r') as f:
            content = f.readlines()

        # remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content]

        xss = []
        for line in content:
            xs = []

            for c in line:
                if c == ' ':
                    xs.append(EMPTY)
                elif c == 'X':
                    xs.append(WALL)
                else:
                    raise ValueError('unexpected character found: ' + c)

            xss.append(xs)

        maze = Maze(len(xss), len(xss[0]))

        for xs in xss:
            assert len(xs) == maze.ncolumns

        for i in range(maze.nrows):
            for j in range(maze.ncolumns):
                if xss[i][j] == EMPTY:
                    maze.remove_wall(i, j)
                else:
                    maze.set_wall(i, j)

        return maze

    @staticmethod
    def complete_maze(rows, columns):
        maze = Maze(rows, columns)

        for i in range(rows):
            for j in range(columns):
                maze.board[i][j] = WALL

        return maze

    @staticmethod
    def create_maze(rows, columns, seed=None, complexity=.5, density=.2):
        rows = (rows // 2) * 2 + 1
        columns = (columns // 2) * 2 + 1

        if seed is not None:
            np.random.seed(seed)

        # Adjust complexity and density relative to maze size
        complexity = int(complexity * (5 * (rows + columns)))
        density = int(density * ((rows // 2) * (columns // 2)))

        maze = Maze(rows, columns)
        maze.set_borders()

        # Make aisles
        for i in range(density):
            x, y = rand(0, rows // 2) * 2, rand(0, columns // 2) * 2
            maze.set_wall(x, y)

            for j in range(complexity):
                neighbours = []

                if maze.in_maze(x - 2, y):
                    neighbours.append((x - 2, y))

                if maze.in_maze(x + 2, y):
                    neighbours.append((x + 2, y))

                if maze.in_maze(x, y - 2):
                    neighbours.append((x, y - 2))

                if maze.in_maze(x, y + 2):
                    neighbours.append((x, y + 2))

                if len(neighbours):
                    next_x, next_y = neighbours[rand(0, len(neighbours) - 1)]

                    if not maze.is_wall(next_x, next_y):
                        maze.set_wall(next_x, next_y)
                        maze.set_wall(next_x + (x - next_x) // 2, next_y + (y - next_y) // 2)
                        x, y = next_x, next_y

        return maze
