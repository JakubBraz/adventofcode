"""
My result:
 5    2887   4012  ***
"""

from inputs import inp05


def parse_input(inp):
    res = inp.split("\n\n")
    rgs = [[int(i) for i in x.split("-")] for x in res[0].split("\n")]
    ids = [int(x) for x in res[1].split("\n")]
    return rgs, ids


def check(rgs, i):
    for a, b in rgs:
        if a <= i <= b:
            return True
    return False


def part1(inp):
    rgs, ids = inp
    return sum(check(rgs, i) for i in ids)


def part2(inp):
    rgs, _ = inp
    rgs.sort()
    last = 0
    result = 0
    for a, b in rgs:
        ind = (a - 1) if a > last else last
        last = max(ind, b)
        if ind <= b:
            result += b - ind
    return result


print(part1(parse_input(inp05.raw_input)))
print(part2(parse_input(inp05.raw_input)))
