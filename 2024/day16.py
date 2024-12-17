from collections import defaultdict
from inputs import inp16
import heapq


def to_visit(board, x, y, d):
    result = []
    if d == 'e':
        if board[x][y + 1] == '.': result.append((x, y + 1, 'e', 1))
        if board[x - 1][y] == '.': result.append((x - 1, y, 'n', 1001))
        if board[x + 1][y] == '.': result.append((x + 1, y, 's', 1001))
    elif d == 'w':
        if board[x][y - 1] == '.': result.append((x, y - 1, 'w', 1))
        if board[x - 1][y] == '.': result.append((x - 1, y, 'n', 1001))
        if board[x + 1][y] == '.': result.append((x + 1, y, 's', 1001))
    elif d == 'n':
        if board[x - 1][y] == '.': result.append((x - 1, y, 'n', 1))
        if board[x][y + 1] == '.': result.append((x, y + 1, 'e', 1001))
        if board[x][y - 1] == '.': result.append((x, y - 1, 'w', 1001))
    elif d == 's':
        if board[x + 1][y] == '.': result.append((x + 1, y, 's', 1))
        if board[x][y + 1] == '.': result.append((x, y + 1, 'e', 1001))
        if board[x][y - 1] == '.': result.append((x, y - 1, 'w', 1001))
    return result


def dijkstra(start, board, d):
    x, y = start
    dists = defaultdict(lambda: len(board) * len(board[0]) * 1000)
    dists[(x, y)] = 0
    q = [(x, y, d, 0)]
    while q:
        x, y, d, current_dist = heapq.heappop(q)
        visit = to_visit(board, x, y, d)
        for nx, ny, nd, score in visit:
            if dists[(nx, ny)] > score + current_dist:
                dists[(nx, ny)] = score + current_dist
                heapq.heappush(q, (nx, ny, nd, dists[(nx, ny)]))
    return dists


def part1(arg):
    start, stop, board = arg
    result = dijkstra(start, board, 'e')
    return result[stop]


def part2(arg):
    start, stop, board = arg
    dist_start = dijkstra(start, board, 'e')
    dist_stop = dijkstra(stop, board, 'e')
    total = dist_start[stop]
    visited = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '.':
                d_start = dist_start[(i, j)]
                d_stop = dist_stop[(i, j)]
                if (d_start + d_stop) in [total, total + 1000, total - 1000]:
                    visited.add((i, j))
    return len(visited)


def parse_input(arg):
    arg = arg.strip()
    arg = arg.split('\n')
    arg = [[c for c in row] for row in arg]
    start = [(x, y) for x in range(len(arg)) for y in range(len(arg[x])) if arg[x][y] == 'S'][0]
    end = [(x, y) for x in range(len(arg)) for y in range(len(arg[x])) if arg[x][y] == 'E'][0]
    for x in range(len(arg)):
        for y in range(len(arg)):
            if arg[x][y] in 'SE':
                arg[x][y] = '.'
    return start, end, arg


# day_input = parse_input(inp16.test_input)
# day_input = parse_input(inp16.test_input2)
day_input = parse_input(inp16.raw_input)

print(part1(day_input))
print(part2(day_input))
