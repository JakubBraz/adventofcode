from inputs import inp10


def count_top(x, y, memo):
    if (x, y) not in memo:
        memo.add((x, y))
        return 1
    return 0


def travel(grid, x, y, f, memo):
    if grid[x][y] == 9:
        return f(x, y, memo)
    to_visit = [(i, j) for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)] if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == grid[x][y] + 1]
    return sum(travel(grid, i, j, f, memo) for i, j in to_visit)


def part1(arg):
    return sum(travel(arg, x, y, count_top, set()) for x in range(len(arg)) for y in range(len(arg[x])) if arg[x][y] == 0)


def part2(arg):
    return sum(travel(arg, x, y, lambda a, b, c: 1, set()) for x in range(len(arg)) for y in range(len(arg[x])) if arg[x][y] == 0)


def parse_input(arg):
    arg = arg.strip()
    arg = arg.split('\n')
    return [[int(c) for c in line] for line in arg]


day_input = parse_input(inp10.raw_input)
# day_input = parse_input(inp10.test_input)


print(part1(day_input))
print(part2(day_input))
