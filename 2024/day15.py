from inputs import inp15


def grid_to_string(grid, x:int, y:int):
    new_grid = [[c for c in line] for line in grid]
    if new_grid[x][y] != '.':
        raise BaseException(f"Unexpected {x} {y} {new_grid[x][y]}")
    new_grid[x][y] = '@'
    result = ''
    for line in new_grid:
        result += f"{''.join(line)}\n"
    return result


def field_to_move(grid, x, y, v):
    if grid[x][y] in '.O':
        return [(x, y)]
    if grid[x][y] == '#':
        return [-1]
    if grid[x][y] == '[':
        return [(x, y), (x, y + 1)] if v[1] == 0 else [(x, y)]
    return [(x, y), (x, y - 1)] if v[1] == 0 else [(x, y)]


def is_move_possible(grid, nx, y, v, visited):
    fields = field_to_move(grid, nx, y, v)
    if -1 in fields:
        return False
    to_check = [(fx, fy) for fx, fy in fields if grid[fx][fy] != '.']
    visited.update(to_check)
    if not to_check:
        return True
    return all(is_move_possible(grid, fx + v[0], fy + v[1], v, visited) for fx, fy in to_check)


def move_robot_recursively(grid, nx, ny, v):
    visited = {(nx - v[0], ny - v[1])}
    if is_move_possible(grid, nx, ny, v, visited):
        new_grid = [[grid[i][j] if (i, j) not in visited else '.' for j in range(len(grid[i]))] for i in range(len(grid))]
        for i, j in visited:
            new_grid[i + v[0]][j + v[1]] = grid[i][j]
        return new_grid, nx, ny
    else:
        return grid, nx - v[0], ny - v[1]


def move_robot(grid, x, y, move):
    v = (1, 0)
    if move == '<': v = (0, -1)
    elif move == '>': v = (0, 1)
    elif move == '^': v = (-1, 0)
    nx, ny = x + v[0], y + v[1]
    grid, x, y = move_robot_recursively(grid, nx, ny, v)
    return grid, x, y


def last_field(grid, x, y, v):
    while grid[x][y] != '.' and grid[x][y] != '#':
        x += v[0]
        y += v[1]
    if grid[x][y] == '.':
        return x, y
    return None


def move_robot_fast(grid, x, y, move):
    grid = [[x for x in line] for line in grid]
    v = (1, 0)
    if move == '<': v = (0, -1)
    elif move == '>': v = (0, 1)
    elif move == '^': v = (-1, 0)
    nx, ny = x + v[0], y + v[1]
    r = last_field(grid, nx, ny, v)
    if r:
        grid[r[0]][r[1]] = grid[nx][ny]
        grid[nx][ny] = '.'
        return grid, nx, ny
    return grid, x, y


def solve_fast(x, y, grid, moves):
    for m in moves:
        grid, x, y = move_robot_fast(grid, x, y, m)
    return sum((100 * x + y) for x in range(len(grid)) for y in range(len(grid[x])) if grid[x][y] in 'O[')


def solve(x, y, grid, moves):
    for m in moves:
        grid, x, y = move_robot(grid, x, y, m)
    return sum((100 * x + y) for x in range(len(grid)) for y in range(len(grid[x])) if grid[x][y] in 'O[')


def double_grid(grid, x, y):
    grid = [''.join(['[]' if c == 'O' else 2 * c for c in line]) for line in grid]
    return grid, x, 2 * y


def parse_input(arg):
    arg = arg.strip()
    grid, moves = arg.split('\n\n')
    grid = grid.split('\n')
    robot = [[x, y] for x in range(len(grid)) for y in range(len(grid[x])) if grid[x][y] == '@'][0]
    grid = [[c if c != '@' else '.' for c in line] for line in grid]
    moves = [c for c in moves if c in '<>^v']
    return robot, grid, moves


def main():
    (x, y), grid, moves = parse_input(inp15.raw_input)
    # (x, y), grid, moves = parse_input(inp15.test_input)

    print(solve_fast(x, y, grid, moves))
    grid, x, y = double_grid(grid, x, y)
    print(solve(x, y, grid, moves))


if __name__ == '__main__':
    main()
