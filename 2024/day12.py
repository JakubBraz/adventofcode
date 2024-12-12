from collections import defaultdict
from inputs import inp12


def travel(grid, x, y, visited, all_visited):
    if grid[x][y] == '.' or (x, y) in all_visited:
        return
    to_visit = {(i, j) for i, j in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)] if grid[i][j] == grid[x][y] and (i, j) not in visited}
    visited.update(to_visit)
    for i, j in to_visit:
        travel(grid, i, j, visited, all_visited)


def get_sides(grid, points):
    sides = []
    for x, y in points:
        if grid[x][y] != grid[x+1][y]:
            sides.append((x+1, y, '^'))
        if grid[x][y] != grid[x-1][y]:
            sides.append((x-1, y, 'v'))
        if grid[x][y] != grid[x][y+1]:
            sides.append((x, y+1, '>'))
        if grid[x][y] != grid[x][y-1]:
            sides.append((x, y-1, '<'))
    return sides


def sort_sides(d, sides):
    if d == '^' or d == 'v':
        return sides[0], sides[1]
    return sides[1], sides[0]


def group_sides(sides):
    grouped = defaultdict(list)
    for x, y, d in sides:
        grouped[d].append((x, y))
    for d in grouped.keys(): grouped[d].sort(key=lambda a: sort_sides(d, a))
    result = 0
    for (_direction, g) in grouped.items():
        x, y = -1, -1
        tmp = 0
        for i, j in g:
            if not ((x == i and j - y == 1) or (y == j and i - x == 1)):
                tmp += 1
            x, y = i, j
        result += tmp
    return result


def solve(arg, side_function):
    grid, regions = arg
    result = 0
    for region in regions:
        sides = get_sides(grid, region)
        result += len(region) * side_function(sides)
    return result


def parse_input(arg):
    arg = arg.strip()
    arg = arg.split('\n')
    arg = [f'.{x}.' for x in arg]
    arg = ['.' * len(arg[0])] + arg + ['.' * len(arg[0])]
    all_visited = set()
    regions = []
    for x in range(len(arg)):
        for y in range(len(arg[x])):
            if arg[x][y] != '.' and (x, y) not in all_visited:
                visited = {(x, y)}
                travel(arg, x, y, visited, all_visited)
                regions.append(visited)
                all_visited.update(visited)
    return arg, regions


# day_input = parse_input(inp12.test_input)
day_input = parse_input(inp12.raw_input)

print(solve(day_input, lambda x: len(x)))
print(solve(day_input, lambda x: group_sides(x)))
