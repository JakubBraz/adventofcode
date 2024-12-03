from inputs import inp03
import re


def part1(arg):
    res = re.findall('mul\\(([0-9]{1,3}),([0-9]{1,3})\\)', arg)
    result = 0
    for i, j in res:
        result += int(i) * int(j)
    return result


def part2(arg):
    r1 = re.finditer("don't\\(\\)", arg)
    r2 = re.finditer("do\\(\\)", arg)
    donts = {x.start() for x in r1} | {len(arg)}
    dos = {x.start() for x in r2} | {0}
    all_range = sorted(dos | donts)
    result = 0
    for i in range(len(all_range)):
        if all_range[i] in dos:
            result += part1(arg[all_range[i]:all_range[i+1]])
    return result


def parse_input(inp):
    inp = inp.strip()
    return inp


day_input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
day_input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
day_input = inp03.raw_input
day_input = parse_input(day_input)

print(part1(day_input))
print(part2(day_input))
