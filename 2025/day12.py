from inputs import inp12

def parse_input(inp):
    lines = inp.split("\n")
    i = [i for i in range(len(lines)) if 'x' in lines[i]][0]
    section2 = lines[i:]
    i = [i for i in range(len(inp)) if inp[i] == "x"][0]
    new_i = i
    while inp[new_i] != '.' and inp[new_i] != '#':
        new_i -= 1
    section1 = inp[:new_i + 1]
    section1 = section1.split('\n\n')
    section1 = [(int(line.split(":")[0]), line.split(":")[1][1:].split("\n")) for line in section1]
    section2 = [x.split(': ') for x in section2]
    section2 = [[[int(x) for x in a.split('x')]] + [[int(y) for y in b.split()]] for a, b in section2]
    return dict(section1), section2

def draw(shape):
    for line in shape:
        print("".join(line))
    print()

def rotate(shape):
    new_shape = create_board(len(shape[0]), len(shape))
    for i in range(len(shape)):
        for j in range(len(shape[0])):
            new_shape[j][len(shape) - 1 - i] = shape[i][j]
    return ["".join(row) for row in new_shape]


def all_shape_rotation(shape):
    result = {tuple(shape)}
    s = shape
    for _ in range(3):
        s = rotate(s)
        result.add(tuple(s))
    return result

def fit(i, j, board, shape):
    n = len(shape)
    if i + n > len(board) or j + n > len(board[0]):
        return False
    for x in range(n):
        for y in range(n):
            if shape[x][y] == "#" and board[i + x][j + y] == "#":
                return False
    return True

def can_put(board, shape):
    indices = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if fit(i, j, board, shape):
                indices.append((i, j))
    return indices

def no_empty_space(board):
    for current in [board, rotate(board)]:
        empty = False
        for line in current:
            line_empty = all(x == '.' for x in line)
            if empty and not line_empty:
                return False
            if line_empty:
                empty = True
    return True

def all_new_boards(board, shape):
    boards = []
    for s in all_shape_rotation(shape):
        for i, j in can_put(board, s):
            new_board = [[r for r in row] for row in board]
            for x in range(len(s)):
                for y in range(len(s)):
                    new_board[i + x][j + y] = "#" if "#" == s[x][y] or "#" == new_board[i + x][j + y] else "."
            boards.append(new_board)
    boards = [b for b in boards if no_empty_space(b)]
    # boards.sort(key = lambda b: [row.count("#") for row in b], reverse=True)
    # boards.sort(key = lambda b: count_columns(b), reverse=True)
    boards.sort(key = lambda b: list(zip([row.count("#") for row in b], distances_to_begin(b))), reverse = True)
    return boards

def create_board(i, j):
    return [['.'] * j for _ in range(i)]

def board_to_str(board):
    board = ["".join(row) for row in board]
    return "".join(board)

def distances_to_begin(shape):
    result = []
    start_points = []
    i, j = 0, 0
    while i < len(shape) and j < len(shape[0]):
        start_points.append((i, j))
        if j + 1 < len(shape[0]):
            j += 1
        else:
            i += 1
    for i, j in start_points:
        count = 0
        x, y = i, j
        while x < len(shape) and y >= 0:
            if shape[x][y] == "#":
                count += 1
            x += 1
            y -= 1
        result.append(count)
    return result

index = 0
def fit_all_shapes(board, needed_shapes, shapes):
    global index
    # if index == 100:
    #     exit(0)
    index += 1
    # if index % 5000 == 0:
    if index % 1 == 0:
        print(index)
        print(needed_shapes)
        # print(board_to_str(board))
        # print(board)
        draw(board)
    t = (board_to_str(board), tuple(needed_shapes))
    if all(x == 0 for x in needed_shapes):
        return True
    shapes_to_visit = [i for i, v in enumerate(needed_shapes) if v > 0]
    for i in shapes_to_visit:
        needed_shapes[i] -= 1
        for b in all_new_boards(board, shapes[i]):
            # print("wstawiam")
            # draw(shapes[i])
            if fit_all_shapes(b, needed_shapes, shapes):
                return True
        needed_shapes[i] += 1
    return False

def part1(arg):
    print(arg)
    shapes, required_boards = arg

    for shape_id, shape in shapes.items():
        print(shape_id, shape)
        draw(shape)
        draw(rotate(shape))

    board = create_board(4, 4)
    for b in all_new_boards(board, shapes[0]):
        draw(b)

    # print("shapessss")
    # for s in shapes.values():
    #     print("shape")
    #     draw(s)
    #     print('rotations')
    #     for ss in all_shape_rotation(s):
    #         draw(ss)
    #     print()

    result = 0
    for (i, j), needed_shapes in required_boards:
        board = create_board(i, j)
        if fit_all_shapes(board, needed_shapes, shapes):
            result += 1
        print(result)

    return result

# print(part1(parse_input(inp12.test_input)))
print(part1(parse_input(inp12.raw_input)))
