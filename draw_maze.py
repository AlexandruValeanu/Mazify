from matplotlib import pyplot
from matplotlib import colors
import constants


def draw_maze(maze, path=None, figsize=(20, 10), file_path=None):
    if path is None:
        path = []

    pyplot.figure(figsize=figsize)

    color_path(maze, path)

    # make a color map of fixed colors
    cmap = colors.ListedColormap(['black', 'white', 'red', 'blue'])
    bounds = [0, 1, 2, 3, 4]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    # tell imshow about color map so that only set colors are used
    pyplot.imshow(maze.board, interpolation='nearest',
                  cmap=cmap, norm=norm)

    pyplot.xticks([]), pyplot.yticks([])

    if file_path is not None:
        pyplot.savefig(file_path + ".png")
        maze.write_to_file(file_path + '.txt')
    else:
        pyplot.show()


def ascii_representation(maze):
    rep = ''
    for i in range(maze.nrows):
        for j in range(maze.ncolumns):
            if maze.is_wall(i, j):
                rep += 'X'
            else:
                rep += ' '
        rep += '\n'
    return rep


def color_path(maze, path):
    for (x, y) in path:
        maze.board[x][y] = constants.RED

    if len(path):
        maze.board[path[0][0], path[0][1]] = constants.BLUE
        maze.board[path[-1][0], path[-1][1]] = constants.BLUE
