"""
my score:
part 1: 8    6319    833  ***
part 2: 8    6637    855  ***
"""

from collections import Counter

from inputs import inp08


def parse_input(inp):
    inp = [(int(x[0]), int(x[1]), int(x[2])) for x in [line.split(',') for line in inp.split("\n")]]
    return inp


def dist(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2) + (z1 - z2) * (z1 - z2)


def solve(arg, iters):
    d_map = {}
    for i in range(len(arg)):
        for j in range(i + 1, len(arg)):
            d = dist(arg[i], arg[j])
            d_map[d] = (arg[i], arg[j])
    keys = sorted(d_map.keys())

    group_id = {p: -1 for p in arg}

    p1 = 0, 0, 0
    p2 = 0, 0, 0
    i = 0
    while iters(i, group_id):
        p1, p2 = d_map[keys[i]]
        if group_id[p1] == group_id[p2] and group_id[p1] != -1:
            pass
        elif group_id[p1] == -1 and group_id[p2] == -1:
            group_id[p1] = i
            group_id[p2] = i
        elif group_id[p1] != -1 and group_id[p2] != -1:
            old_id = group_id[p2]
            for p in arg:
                if group_id[p] == old_id:
                    group_id[p] = group_id[p1]
        elif group_id[p1] == -1:
            group_id[p1] = group_id[p2]
        elif group_id[p2] == -1:
            group_id[p2] = group_id[p1]
        else:
            raise "unreachable"
        i += 1

    return Counter(group_id.values()), p1, p2


def part1(arg):
    counter, _, _ = solve(arg, lambda a, b: a < 1000)
    top = sorted((v for k, v in counter.items() if k != -1), reverse=True)
    return top[0] * top[1] * top[2]


def part2(arg):
    _, p1, p2 = solve(arg, lambda a, b: -1 in b.values())
    return p1[0] * p2[0]


print(part1(parse_input(inp08.raw_input)))
print(part2(parse_input(inp08.raw_input)))
