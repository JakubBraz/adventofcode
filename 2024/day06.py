from inputs import inp06


def make_move(grid, x, y, d):
    if d == '^':
        if x - 1 < 0 or grid[x-1][y] == '.':
            x = x - 1
        else:
            d = '>'
    elif d == '<':
        if y - 1 < 0 or grid[x][y - 1] == '.':
            y = y - 1
        else:
            d = '^'
    elif d == '>':
        if y + 1 == len(grid[0]) or grid[x][y + 1] == '.':
            y = y + 1
        else:
            d = 'v'
    elif d == 'v':
        if x + 1 == len(grid) or grid[x + 1][y] == '.':
            x = x + 1
        else:
            d = '<'
    else:
        raise "UNREACHABLE"
    return x, y, d


def part1(arg):
    grid, x, y = arg
    d = '^'
    visited = {(x, y)}
    while 0 <= x < len(grid) and 0 <= y < len(grid[0]):
        x, y, d = make_move(grid, x, y, d)
        visited.add((x, y))
    visited.remove((x, y))
    return visited


def is_loop(x, y, grid):
    d = '^'
    visited = {(x, y, d)}
    while True:
        x, y, d = make_move(grid, x, y, d)
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return False
        if (x, y, d) in visited:
            return True
        visited.add((x, y, d))


def part2(arg, candidates):
    grid, x, y = arg
    result = 0
    for (i, j) in candidates:
        grid[i][j] = '#'
        if is_loop(x, y, grid):
            result += 1
        grid[i][j] = '.'
    return result


def parse_input(arg):
    arg = arg.strip()
    arg = arg.split('\n')
    arg = [[c for c in line] for line in arg]
    x = [i for i in range(len(arg)) if '^' in arg[i]][0]
    y = [i for i, v in enumerate(arg[x]) if v == '^'][0]
    arg[x] = [i if i != '^' else '.' for i in arg[x]]
    return arg, x, y


# day_input = parse_input(inp06.test_input)
day_input = parse_input(inp06.raw_input)


res = part1(day_input)
print(len(res))
print(part2(day_input, res))
