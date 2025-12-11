"""
My score:
part 1: 11     496   1593  **
part 2: 11    1183   2251  **
"""

from inputs import inp11


def parse_input(inp):
    inp = [line.split(": ") for line in inp.split("\n")]
    return {a: b.split(" ") for a, b in inp}


def solve(graph, x, must_see, memo):
    t = (x, tuple(must_see))
    if t in memo:
        return memo[t]
    if x == "out":
        return len(must_see) == 0
    must_see = [i for i in must_see if i != x]
    memo[t] = sum(solve(graph, n, must_see, memo) for n in graph[x])
    return memo[t]


def part1(arg):
    res = solve(arg, "you", [], {})
    return res


def part2(arg):
    res = solve(arg, "svr", ["dac", "fft"], {})
    return res


print(part1(parse_input(inp11.raw_input)))
print(part2(parse_input(inp11.raw_input)))
