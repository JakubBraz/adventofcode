"""
My result:
 3   2371   3649  ***
"""

from inputs import inp03


def parse_input(inp):
    return inp.split("\n")


def solve(inp, limit):
    result = 0
    for line in inp:
        res = []
        max_i = -1
        for i in range(limit, -1, -1):
            max_i = max(range(max_i + 1, len(line) - i), key=lambda x: line[x])
            res.append(line[max_i])
        result += int("".join(res))
    return result


print(solve(parse_input(inp03.raw_input), 1))
print(solve(parse_input(inp03.raw_input), 11))
