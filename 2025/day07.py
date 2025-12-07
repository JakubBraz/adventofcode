"""
My result:
 7    4453   2675  ***
"""

from inputs import inp07


def parse_input(inp):
    inp = inp.split("\n")
    s = [i for i in range(len(inp[0])) if inp[0][i] == "S"][0]
    splitters = [(i, j) for i in range(len(inp)) for j in range(len(inp[0])) if inp[i][j] == "^"]
    return (0, s), splitters, len(inp)


def solve(splitters, n, x, y, memo, splits):
    if (x, y) in memo:
        return memo[(x, y)]
    if x == n:
        return 1
    x += 1
    if (x, y) in splitters:
        splits[0] += 1
        memo[(x, y)] = solve(splitters, n, x, y - 1, memo, splits) + solve(splitters, n, x, y + 1, memo, splits)
        return memo[(x, y)]
    memo[(x, y)] = solve(splitters, n, x, y, memo, splits)
    return memo[(x, y)]


def part1(arg):
    (x, y), splitters, n = arg
    splits = [0]
    solve(splitters, n, x, y, {}, splits)
    return splits[0]


def part2(arg):
    (x, y), splitters, n = arg
    return solve(splitters, n, x, y, {}, [0])


print(part1(parse_input(inp07.raw_input)))
print(part2(parse_input(inp07.raw_input)))
