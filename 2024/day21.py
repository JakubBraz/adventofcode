import math
from itertools import permutations
from inputs import inp21

num_coordinates = {
    "A": (3, 2),
    "0": (3, 1),
    "3": (2, 2),
    "2": (2, 1),
    "1": (2, 0),
    "6": (1, 2),
    "5": (1, 1),
    "4": (1, 0),
    "9": (0, 2),
    "8": (0, 1),
    "7": (0, 0)
}
illegal_num = (3, 0)

direction_coordinates = {
    "A": (0, 2),
    "^": (0, 1),
    ">": (1, 2),
    "v": (1, 1),
    "<": (1, 0)
}
illegal_direction = (0, 0)


def get_direction(diff_x, diff_y):
    result = ''
    if diff_y <= 0:
        result += '>' * (-diff_y)
    elif diff_y > 0:
        result += '<' * diff_y
    if diff_x <= 0:
        result += 'v' * (-diff_x)
    elif diff_x > 0:
        result += '^' * diff_x
    return result


def one_path(start_key, target_key, coordinates):
    x, y = coordinates[start_key]
    i, j = coordinates[target_key]
    return get_direction(x - i, y - j)


def path_permutation(start_key, target_key, coordinates, illegal_position):
    paths = permutations(one_path(start_key, target_key, coordinates))
    return {''.join(p) for p in paths if is_combination_legal(coordinates[start_key], p, illegal_position)}


def is_combination_legal(current, path, illegal_position):
    x, y = current
    for c in path:
        if c == '<':
            y -= 1
        elif c == '>':
            y += 1
        elif c == '^':
            x -= 1
        elif c == 'v':
            x += 1
        if (x, y) == illegal_position:
            return False
    return True


def go_deep(code, level, memo):
    t = (code, level)
    if t in memo:
        return memo[t]
    if level == 0:
        return len(code) - 1
    result = 0
    for i in range(1, len(code)):
        res = math.inf
        for c in path_permutation(code[i - 1], code[i], direction_coordinates, illegal_direction):
            res = min(res, go_deep(f"A{c}A", level - 1, memo))
        result += res
    memo[t] = result
    return memo[t]


def solve(arg, level):
    result = 0
    memo = {}
    for code in arg:
        code = 'A' + code
        codes = ['A']
        for i in range(1, len(code)):
            codes = [r + f'{path}A' for r in codes for path in
                     path_permutation(code[i - 1], code[i], num_coordinates, illegal_num)]
        res = min(go_deep(c, level, memo) for c in codes)
        result += int(code[1:-1]) * res
    return result


def parse_input(arg):
    arg = arg.strip()
    arg = arg.split('\n')
    return arg


# day_input = parse_input(inp21.inputs[0])
day_input = parse_input(inp21.inputs[1])

print(solve(day_input, 2))
print(solve(day_input, 25))
