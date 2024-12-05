from collections import defaultdict
from functools import cmp_to_key

from inputs import inp05


def is_less(x, y, rules):
    if y in rules[x]:
        return True
    if x in rules[y]:
        return False
    return any(is_less(x, a, rules) for a in rules[y])


def is_update_correct(upd, rules):
    for i in range(1, len(upd)):
        if not is_less(upd[i-1], upd[i], rules):
            return False
    return True


def part1(arg):
    rules, updates = arg
    result = [upd for upd in updates if is_update_correct(upd, rules)]
    return sum(x[len(x) // 2] for x in result)


def part2(arg):
    rules, updates = arg
    result = [upd for upd in updates if not is_update_correct(upd, rules)]
    my_cmp = lambda a, b: -1 if is_less(a, b, rules) else 1
    sorted_upd = [sorted(x, key=cmp_to_key(my_cmp)) for x in result]
    return sum(x[len(x) // 2] for x in sorted_upd)


def parse_input(arg):
    arg = arg.strip()
    arg = arg.split('\n\n')
    rules = arg[0]
    rules = rules.split('\n')
    rules = [[int(y) for y in x.split('|')] for x in rules]
    updates = arg[1]
    updates = updates.split('\n')
    updates = [[int(x) for x in line.split(',')] for line in updates]
    less_than = defaultdict(set)
    for x, y in rules:
        less_than[x].add(y)
    return less_than, updates


# day_input = parse_input(inp05.test_input)
day_input = parse_input(inp05.raw_input)


print(part1(day_input))
print(part2(day_input))
