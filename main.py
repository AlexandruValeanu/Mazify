import sys

import game
from solvers import astar_solver
from ast import literal_eval as make_tuple
from maze import Maze
from draw_maze import draw_maze


def get_param(type):
    for arg in sys.argv:
        tokens = arg.split('=')

        if tokens[0] == type:
            return tokens[1]

    return None


if sys.argv[1].startswith('create'):
    nrows = int(get_param('rows'))
    ncols = int(get_param('columns'))
    filepath = get_param('file-path')

    maze = Maze.create_maze(nrows, ncols)
    draw_maze(maze, file_path=filepath)


elif sys.argv[1].startswith('solve'):
    start = make_tuple(get_param('start'))
    end = make_tuple(get_param('end'))

    maze = Maze.load_from_file(get_param('file-path'))
    path = astar_solver.solve_maze(maze, start, end)
    draw_maze(maze, path)
elif sys.argv[1].startswith('play'):
    game.run_game(get_param('file-path'))
elif sys.argv[1] == 'help':
    print('Key controls')
    print('z    Highlight current location')
    print('x    Highlight destination')
    print('t    Show solution from current location')
    print('c    Decrease frame rate')
    print('v    Increase frame rate')
    print('f    Show frame rate')
    print('Arrows or WASD for movement')

