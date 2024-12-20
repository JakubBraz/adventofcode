from inputs import inp19


def count(design, patterns, memo):
    if design in memo:
        return memo[design]
    if not design:
        return 1
    memo[design] = sum(count(design[len(p):], patterns, memo) for p in patterns if p == design[:len(p)])
    return memo[design]


def part1(arg):
    patterns, designs = arg
    memo = {}
    return sum(count(d, patterns, memo) > 0 for d in designs), memo


def part2(arg, memo):
    _patterns, designs = arg
    return sum(memo[d] for d in designs)


def parse_input(arg):
    arg = arg.strip().split('\n\n')
    patterns, arg = arg
    return set(patterns.split(', ')), arg.split('\n')


day_input = parse_input(inp19.raw_input)
# day_input = parse_input(inp19.test_input)

result, mapping = part1(day_input)
print(result)
print(part2(day_input, mapping))
