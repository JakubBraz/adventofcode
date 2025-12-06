"""
My result:

part 1: 2284
6     343   2284  **

part 2: 1583
6    1583   3853  **
"""

from functools import reduce

from inputs import inp06


def parse_part_1(inp):
    inp = [[x for x in line.split(" ") if x != ""] for line in inp.split("\n")]
    inp = [[int(inp[i][j]) if inp[i][j].isdigit() else inp[i][j] for i in range(len(inp))] for j in range(len(inp[0]))]
    return inp


def parse_part_2(arg):
    arg = [line for line in arg.split("\n")]
    arg = [[arg[i][j] for i in range(len(arg))] for j in range(len(arg[0]))]
    ops = [x for line in arg for x in line if x in "+*"]
    arg = [[x for x in line if x.isdigit()] for line in arg]
    arg = ["".join(line) for line in arg]
    final_args = []
    tmp = []
    for x in arg:
        if x != "":
            tmp.append(int(x))
        else:
            final_args.append(tmp)
            tmp = []
    final_args.append(tmp)
    return ops, final_args


def compute(ops, args):
    func = {
        "+": lambda a, b: a + b,
        "*": lambda a, b: a * b
    }
    return sum(reduce(lambda acc, val: func[op](acc, val), arg, op == "*") for op, arg in zip(ops, args))


def part1(arg):
    return compute((line[-1] for line in arg), (line[:-1] for line in arg))


def part2(arg):
    return compute(arg[0], arg[1])


print(part1(parse_part_1(inp06.raw_input)))
print(part2(parse_part_2(inp06.raw_input)))
