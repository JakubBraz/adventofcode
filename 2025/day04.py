"""
My result:
 4    1859   1417  **
"""

from inputs import inp04


def parse_input(inp):
    return [[x for x in row] for row in inp.split("\n")]


def count_neighbours(grid, i, j):
    neigh = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j),
             (i + 1, j + 1)]
    return sum(grid[i][j] == "@" for i, j in neigh if 0 <= i < len(grid) and 0 <= j < len(grid[0]))


def all_indices(inp):
    indices = []
    for i in range(len(inp)):
        for j in range(len(inp[i])):
            if inp[i][j] == '@' and count_neighbours(inp, i, j) < 4:
                indices.append((i, j))
    return indices


def solve(inp):
    return len(all_indices(inp))


def solve2(inp):
    result = 0
    removed = True
    while removed:
        removed = False
        indices = all_indices(inp)
        for i, j in indices:
            removed = True
            inp[i][j] = '.'
            result += 1
    return result


print(solve(parse_input(inp04.raw_input)))
print(solve2(parse_input(inp04.raw_input)))
