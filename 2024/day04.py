from inputs import inp04


def find_vector(vec, x, y, grid, to_find):
    for c in to_find:
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == c:
            x += vec[0]
            y += vec[1]
        else:
            return 0
    return 1


def part1(arg):
    result = 0
    for i in range(len(arg)):
        for j in range(len(arg[i])):
            for vec in [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]:
                result += find_vector(vec, i, j, arg, "XMAS")
    return result


def part2(arg):
    result = 0
    for i in range(len(arg)):
        for j in range(len(arg[0])):
            if (
                    (find_vector([1, 1], i, j, arg, "MAS") == 1 or find_vector([1, 1], i, j, arg, "SAM") == 1 ) and
                    (find_vector([-1, 1], i + 2, j, arg, "MAS") == 1 or find_vector([-1, 1], i + 2, j, arg, "SAM") == 1 )
            ):
                result += 1
    return result


def parse_input(arg):
    arg = arg.strip()
    arg = arg.split('\n')
    return arg


day_input = parse_input(inp04.raw_input)
print(part1(day_input))
print(part2(day_input))
