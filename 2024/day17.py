from inputs import inp17


def combo(operand, a, b, c):
    if operand <= 3:
        return operand
    if operand == 4:
        return a
    if operand == 5:
        return b
    if operand == 6:
        return c
    raise BaseException(f"Unexpected {operand}")


def instruction(a, b, c, program, pointer, output):
    op = program[pointer]
    o = program[pointer + 1]
    if op == 0:
        a = a // (1 << (combo(o, a, b, c)))
    elif op == 1:
        b = b ^ o
    elif op == 2:
        b = combo(o, a, b, c) & 7
    elif op == 3:
        if a != 0:
            pointer = o
        else:
            pointer += 2
    elif op == 4:
        b = b ^ c
    elif op == 5:
        output.append(combo(o, a, b, c) & 7)
    elif op == 6:
        b = a // (1 << (combo(o, a, b, c)))
    elif op == 7:
        c = a // (1 << (combo(o, a, b, c)))
    return a, b, c, pointer + (2 if op != 3 else 0)


def calculate(a, b, c, program):
    pointer = 0
    output = []
    while pointer < len(program):
        a, b, c, pointer = instruction(a, b, c, program, pointer, output)
    return output


def part1(arg):
    a, b, c, program = arg
    result = calculate(a, b, c, program)
    return ','.join(str(c) for c in result)


def digit_range(x):
    return x * 8, x * 8 + 8


def solve(level, check_from, check_to, digits, tmp):
    if level == len(digits):
        return tmp
    candidates = [i for i in range(check_from, check_to) if calculate(i, 0, 0, digits[::-1])[0] == digits[level]]
    for num in candidates:
        new_check = digit_range(num)
        res = solve(level + 1, new_check[0], new_check[1], digits, num)
        if res != -1:
            return res
    return -1


def part2(arg):
    a, b, c, program = arg
    result = solve(0, 0, 8, program[::-1], -1)
    program_output = calculate(result, b, c, program)
    assert program_output == program
    return result


def parse_input(arg):
    arg = arg.strip()
    arg = arg.split('\n')
    a = int(arg[0].split(' ')[-1])
    b = int(arg[1].split(' ')[-1])
    c = int(arg[2].split(' ')[-1])
    program = [int(x) for x in arg[4].split(' ')[-1].split(',')]
    return a, b, c, program


day_input = parse_input(inp17.raw_input)
# day_input = parse_input(inp17.test_input)
# day_input = parse_input(inp17.test_input2)


print(part1(day_input))
print(part2(day_input))
