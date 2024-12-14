from inputs import inp14


def print_robots(r, w, h):
    board = [[0 for _ in range(w)] for _ in range(h)]
    for x, y in r:
        board[x][y] += 1
    lines = [''.join(['.' if x == 0 else str(x) for x in line]) for line in board]
    return '\n'.join(lines)


def get_quadrants(coordinates, w, h):
    q1 = len([1 for x, y in coordinates if 0 <= x < h // 2 and 0 <= y < w // 2])
    q2 = len([1 for x, y in coordinates if 0 <= x < h // 2 and w // 2 < y < w])
    q3 = len([1 for x, y in coordinates if h // 2 < x < h and 0 <= y < w // 2])
    q4 = len([1 for x, y in coordinates if h // 2 < x < h and w // 2 < y < w])
    return q1 * q2 * q3 * q4


def part1(arg, w, h):
    steps = 100
    robots = [((r[0] + r[2] * steps) % h, (r[1] + r[3] * steps) % w) for r in arg]
    return get_quadrants(robots, w, h)


def simulate(robots, w, h, steps):
    return [((r[0] + r[2] * steps) % h, (r[1] + r[3] * steps) % w, r[2], r[3]) for r in robots]


def part2(arg, w, h):
    robots = arg
    step = 1
    min_quadrant = (get_quadrants([(r[0], r[1]) for r in robots], w, h), 0)
    for i in range(1, 15_000):
        robots = simulate(robots, w, h, step)
        q = (get_quadrants([(r[0], r[1]) for r in robots], w, h), i)
        min_quadrant = min(min_quadrant, q)
    _q, i = min_quadrant
    final_state = simulate(arg, w, h, i)
    return i, print_robots([(x, y) for x, y, _, _ in final_state], w, h)


def parse_input(arg):
    arg = arg.strip()
    arg = arg.split('\n')
    arg = [x.split(',') for line in arg for x in line.split()]
    arg = [x for line in arg for x in line]
    arg = [int(''.join([c for c in x if c in '0123456789-'])) for x in arg]
    i = 0
    result = []
    while i < len(arg):
        result.append((arg[i+1], arg[i], arg[i+3], arg[i+2]))
        i += 4
    return result


day_input = parse_input(inp14.raw_input)
# day_input = parse_input(inp14.test_input)

# print(part1(day_input, 11, 7))
print(part1(day_input, 101, 103))
result2, christmas_tree = part2(day_input, 101, 103)
print(result2)
print(christmas_tree)
