from inputs import inp20


def get_neighbours(grid, x, y):
    return [(i, j) for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)] if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '.']


def points_in_distance(grid, x, y, d):
    return [(x + i, y + j, abs(i) + abs(j)) for i in range(-d, d + 1) for j in range(-d, d + 1)
            if abs(i) + abs(j) <= d and
            0 <= x + i < len(grid) and
            0 <= y + j < len(grid[0]) and
            grid[x + i][y + j] == '.']


def distance_to(grid, start_point, end_point):
    distance_to_point = {start_point: 0}
    x, y = start_point
    prev = 0
    while (x, y) != end_point:
        x, y = [(i, j) for i, j in get_neighbours(grid, x, y) if (i, j) not in distance_to_point][0]
        distance_to_point[(x, y)] = prev + 1
        prev = prev + 1
    return distance_to_point


def solve(arg, time_in_wall):
    grid, start, end = arg
    distance_to_start = distance_to(grid, start, end)
    distance_to_end = distance_to(grid, end, start)
    result = 0
    for x, y in [(i, j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] == '.']:
        points = points_in_distance(grid, x, y, time_in_wall)
        for i, j, d in points:
            cheat_distance = distance_to_start[(x, y)] + d + distance_to_end[(i, j)]
            gain = distance_to_end[start] - cheat_distance
            if gain >= 100:
                result += 1
    return result


def parse_input(arg):
    arg = [[c for c in line] for line in arg.strip().split('\n')]
    start = (-1, -1)
    end = (-1, -1)
    for i in range(len(arg)):
        for j in range(len(arg[0])):
            if arg[i][j] == 'S':
                start = (i, j)
                arg[i][j] = '.'
            elif arg[i][j] == 'E':
                end = (i, j)
                arg[i][j] = '.'
    return arg, start, end


# day_input = parse_input(inp20.inputs[0])
day_input = parse_input(inp20.inputs[1])


print(solve(day_input, 2))
print(solve(day_input, 20))
