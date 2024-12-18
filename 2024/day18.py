import heapq
import math
from collections import defaultdict
from inputs import inp18


def dijkstra(corrupted, n, m):
    q = [(0, 0, 0)]
    dist = defaultdict(lambda: math.inf)
    dist[(0, 0)] = 0
    while q:
        x, y, d = heapq.heappop(q)
        neighbours = [(i, j) for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)] if (i, j) not in corrupted and 0 <= i <= n and 0 <= j <= m]
        for i, j in neighbours:
            if d + 1 < dist[(i, j)]:
                dist[(i, j)] = d + 1
                heapq.heappush(q, (i, j, d + 1))
    return dist


def part1(arg):
    board, n, m, to_take = arg
    board = set(board[:to_take])
    d = dijkstra(board, n, m)
    return d[(n, m)]


def part2(arg):
    board, n, m, _ = arg
    result = -1
    l = 0
    r = len(board) - 1
    while l <= r:
        m = (l + r) // 2
        grid = set(board[:m + 1])
        d = dijkstra(grid, n, m)
        if d[(n, m)] < math.inf:
            l = m + 1
        else:
            r = m - 1
            result = m
    x, y = board[result]
    return f'{x},{y}'


def parse_input(arg):
    arg = arg.strip()
    arg = arg.split('\n')
    arg = [x.split(',') for x in arg]
    arg = [(int(x), int(y)) for x, y in arg]
    return arg


day_input = (parse_input(inp18.raw_input), 70, 70, 1024)
# day_input = (parse_input(inp18.test_input), 6, 6, 12)


print(part1(day_input))
print(part2(day_input))
