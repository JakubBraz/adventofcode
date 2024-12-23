from collections import defaultdict, deque
from inputs import inp23


def visit(graph):
    result = set()
    for node in graph.keys():
        stack = deque([(node, 0, [node])])
        while stack:
            node, level, path = stack.popleft()
            if level == 3 and node == path[0]:
                result.add(tuple(sorted(path[:-1])))
            if level < 3:
                for n in graph[node]:
                    stack.append((n, level + 1, path + [n]))
    return result


def part1(graph):
    connections = visit(graph)
    result = [c for c in connections if any(x[0] == 't' for x in c)]
    return len(result)


def part2(graph):
    networks = defaultdict(set)
    for n in graph:
        network1 = {n} | graph[n]
        for x in network1:
            network2 = {x} | graph[x]
            inter = tuple(sorted(network1.intersection(network2)))
            networks[inter].add(n)
    result = [list(k) for k, v in networks.items() if list(k) == sorted(v)]
    result = max(result, key=len)
    return ','.join(result)


def parse_input(arg):
    arg = arg.strip().split('\n')
    arg = [x.split('-') for x in arg]
    graph = defaultdict(set)
    for p1, p2 in arg:
        graph[p1].add(p2)
        graph[p2].add(p1)
    return graph


day_input = parse_input(inp23.raw_input)
# day_input = parse_input(inp23.test_input)

print(part1(day_input))
print(part2(day_input))
