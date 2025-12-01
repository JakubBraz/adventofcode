from inputs import inp01


def parse_input(inp):
    return [(x[0], int(x[1:])) for x in inp.split("\n")]


def solve(inp, part1):
    current = 50
    result = 0
    for c, num in inp:
        for i in range(num):
            if c == "L":
                current -= 1
                if current == 0 and not part1:
                    result += 1
                elif current < 0:
                    current = 99
            else:
                current += 1
                if current == 100:
                    if not part1:
                        result += 1
                    current = 0
        if part1 and current == 0:
            result += 1
    return result


print(solve(parse_input(inp01.inp), True))
print(solve(parse_input(inp01.inp), False))
