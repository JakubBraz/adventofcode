from collections import Counter
from inputs import inp11


def rules(x):
    s = str(x)
    if x == 0:
        return [1]
    if len(s) % 2 == 0:
        return [int(s[:len(s)//2]), int(s[len(s) // 2:])]
    return [x * 2024]


def simulate(n, stones):
    for i in range(n):
        new_stones = Counter()
        for v, c in stones.items():
            for new_val in rules(v):
                new_stones[new_val] += c
        stones = new_stones
    return stones


def part1(arg):
    for i in range(25):
        arg = [x for s in arg for x in rules(s)]
    return len(arg)


def part2(arg):
    res = simulate(75, Counter(arg))
    return sum(res.values())


def parse_input(arg):
    arg = arg.strip()
    return [int(x) for x in arg.split()]


# day_input = parse_input(inp11.test_input)
day_input = parse_input(inp11.raw_input)


print(part1(day_input))
print(part2(day_input))
