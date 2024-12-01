from inputs.inp01 import raw_input
from collections import Counter


def parse_input(inp):
    res = inp.strip()
    res = res.split('\n')
    lefts = []
    rights = []
    for line in res:
        l, r = line.split()
        lefts.append(int(l))
        rights.append(int(r))
    return lefts, rights


def part1(inp):
    left, right = inp
    left.sort()
    right.sort()
    s = [abs(x - y) for x, y in zip(left, right)]
    print(sum(s))


def part2(inp):
    left, right = inp
    c = Counter(right)
    result = 0
    for l in left:
        result += l * c[l]
    print(result)


parsed_input = parse_input(raw_input)

part1(parsed_input)
part2(parsed_input)
