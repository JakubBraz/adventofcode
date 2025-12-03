"""
My result:
 2    852   1575  **
"""

from inputs import inp02
import math


def parse_input(inp):
    inp = inp.split(",")
    inp = [(int(x[0]), int(x[1])) for x in [z.split("-") for z in inp]]
    return inp


def is_valid(x, all_values):
    x = str(x)
    l = len(x) // 2
    for i in range(1, l + 1) if all_values else range(math.ceil(len(x) / 2.0), l + 1):
        if x.count(x[:i]) * i == len(x):
            return False
    return True


def solve(inp, all_values):
    result = 0
    for a, b in inp:
        for x in range(a, b + 1):
            if not is_valid(x, all_values):
                result += x
    return result


print(solve(parse_input(inp02.raw_input), False))
print(solve(parse_input(inp02.raw_input), True))
