from inputs import inp13
import re, math

'''
x * a + y * c = p
x * b + y * d = v
'''
def solve_eq(button_a, button_b, prize):
    a, b = button_a
    c, d = button_b
    p, v = prize
    y = (v * a - b * p) / (d * a - b * c)
    x = (p - y * c) / a
    if math.ceil(x) == math.floor(x) and math.ceil(y) == math.floor(y):
        return int(x), int(y)
    return 0, 0


def solve(arg, predicate):
    result = 0
    for machine in arg:
        x, y = solve_eq(machine[0], machine[1], machine[2])
        if predicate(x, y):
            result += (x * 3 + y)
    return result


def parse_input(arg):
    arg = arg.strip()
    arg = arg.split('\n')
    result = []
    i = 0
    while i < len(arg):
        tmp = []
        if arg[i]:
            for j in range(3):
                tmp.append([int(x) for x in re.findall(r'\d+', arg[i+j])])
            result.append(tmp)
            i += 3
        else:
            i += 1
    return result


day_input = parse_input(inp13.raw_input)
# day_input = parse_input(inp13.test_input)

print(solve(day_input, lambda a, b: a <= 100 and b <= 100))
print(solve([(a, b, (c[0] + 10000000000000, c[1] + 10000000000000)) for a, b, c in day_input], lambda a, b: True))
