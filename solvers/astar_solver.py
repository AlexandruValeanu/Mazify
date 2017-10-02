import heapq

nodes = 0


def h(loc1, loc2):
    return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])


def solve_maze(maze, start, end, print_info=False):
    assert not maze.is_wall(start[0], start[1])
    assert not maze.is_wall(end[0], end[1])

    global nodes
    nodes = 0

    queue = []
    parent, dist = dict(), dict()

    parent[start], dist[start] = start, 1
    heapq.heappush(queue, (h(start, end) + dist[start], start))

    while len(queue):
        d, current = heapq.heappop(queue)
        nodes += 1

        if current == end:
            break

        for dx, dy in [(-1, 0), (0, +1), (+1, 0), (0, -1)]:
            a, b = current[0] + dx, current[1] + dy

            if maze.in_maze(a, b) and not maze.is_wall(a, b):

                if (a, b) not in dist or dist[(a, b)] > dist[current] + 1:
                    dist[(a, b)] = dist[current] + 1
                    parent[(a, b)] = current
                    heapq.heappush(queue, (h((a, b), end) + dist[current] + 1, (a, b)))

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
