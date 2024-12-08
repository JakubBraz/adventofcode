from collections import defaultdict
from inputs import inp08


def travel(vec, x, y, n, m):
    while 0 <= x < n and 0 <= y < m:
        yield x, y
        x, y = x + vec[0], y + vec[1]


def generate_anti_nodes(positions, n, m, node_filter):
    result = set()
    for (x, y) in positions:
        for (i, j) in positions:
            dist = (x - i, y - j)
            if dist != (0, 0):
                result.update({p for p in travel(dist, x, y, n, m) if node_filter(p, (x, y), (i, j))})
                result.update({p for p in travel((-dist[0], -dist[1]), x, y, n, m) if node_filter(p, (x, y), (i, j))})
    return result


def filter_nodes(p, a1, a2):
    if p == a1 or p == a2:
        return False
    d1 = p[0] - a1[0], p[1] - a1[1]
    d2 = p[0] - a2[0], p[1] - a2[1]
    return d1 == (2 * d2[0], 2 * d2[1]) or d2 == (2 * d1[0], 2 * d1[0])


def solve(arg, node_filter):
    antennas, n, m = arg
    result = set()
    for antenna in antennas:
        result.update(generate_anti_nodes(antenna, n, m, node_filter))
    return len(result)


def parse_input(arg):
    arg = arg.strip()
    arg = arg.split('\n')
    arg = [[x for x in line] for line in arg]
    all_chars = defaultdict(list)
    for x in range(len(arg)):
        for y in range(len(arg[x])):
            all_chars[arg[x][y]].append((x, y))
    all_chars.pop('.')
    return all_chars.values(), len(arg), len(arg[0])


day_input = parse_input(inp08.raw_input)
# day_input = parse_input(inp08.test_input)


print(solve(day_input, filter_nodes))
print(solve(day_input, lambda x, y, z: True))
