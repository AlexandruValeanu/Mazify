from collections import deque

nodes = 0


def solve_maze(maze, start, end, print_info=False):
    assert not maze.is_wall(start[0], start[1])
    assert not maze.is_wall(end[0], end[1])

    global nodes
    nodes = 0

    queue = deque()
    parent, dist = dict(), dict()

    queue.append(start)
    parent[start], dist[start] = start, 1

    while len(queue):
        current = queue.popleft()
        nodes += 1

        if current == end:
            break

        for dx, dy in [(-1, 0), (0, +1), (+1, 0), (0, -1)]:
            a, b = current[0] + dx, current[1] + dy

            if maze.in_maze(a, b) and not maze.is_wall(a, b) and (a, b) not in parent:
                parent[(a, b)] = current
                dist[(a, b)] = dist[current] + 1;
                queue.append((a, b))

    if print_info:
        print("Distance:", dist[end])
        print("Nodes:", nodes)

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
