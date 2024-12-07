from inputs import inp07


def solve_line(target, nums, tmp, operations):
    if tmp > target:
        return False
    if not nums:
        return tmp == target
    return any(solve_line(target, nums[1:], f(tmp, nums[0]), operations) for f in operations)


def solve(arg, operations):
    return sum(target for target, nums in arg if solve_line(target, nums[1:], nums[0], operations))


def part1(arg):
    return solve(arg, [lambda a, b: a + b, lambda a, b: a * b])


def part2(arg):
    return solve(arg, [lambda a, b: a + b, lambda a, b: a * b, lambda a, b: int(f'{a}{b}')])


def parse_input(arg):
    arg = arg.strip()
    arg = arg.split('\n')
    arg = [line.split(': ') for line in arg]
    arg = [(int(line[0]), [int(x) for x in line[1].split()]) for line in arg]
    return arg


# parsed_input = parse_input(inp07.test_input)
parsed_input = parse_input(inp07.raw_input)


print(part1(parsed_input))
print(part2(parsed_input))
