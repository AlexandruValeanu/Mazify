import resource
import sys

from numpy.random import shuffle

resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, -1))
sys.setrecursionlimit(10 ** 6)

found_solution = False
nodes = 0
dist = -1


def dfs(maze, current, end, parent, visited, d):
    global found_solution
    global nodes
    global dist

    nodes += 1

    if not found_solution:
        if current == end:
            found_solution = True
            dist = d
        else:
            visited.add(current)

            dirs = [(-1, 0), (0, +1), (+1, 0), (0, -1)]
            shuffle(dirs)
            for dx, dy in dirs:
                a, b = current[0] + dx, current[1] + dy

                if maze.in_maze(a, b) and not maze.is_wall(a, b) and (a, b) not in visited:
                    parent[(a, b)] = current
                    dfs(maze, (a, b), end, parent, visited, d + 1)


def solve_maze(maze, start, end, print_info=False):
    assert not maze.is_wall(start[0], start[1])
    assert not maze.is_wall(end[0], end[1])

    parent = dict()
    visited = set()

    global found_solution
    found_solution = False

    global nodes
    nodes = 0

    global dist
    dist = 0

    dfs(maze, start, end, parent, visited, 1)

    if print_info:
        print("Nodes:", nodes)
        print("Distance:", dist)

    if end not in parent:
        return []
    else:
        path = []
        while start != end:
            path.append(end)
            end = parent[end]

        path.append(start)
        path.reverse()
        return path
