from collections import defaultdict

from inputs import inp22


def calculate(secret):
    modular = 16777216
    new_secret = ((secret * 64) ^ secret) % modular
    new_secret = ((new_secret // 32) ^ new_secret) % modular
    new_secret = ((new_secret * 2048) ^ new_secret) % modular
    return new_secret


def part1(arg):
    result = 0
    for num in arg:
        for i in range(2000):
            num = calculate(num)
        result += num
    return result


def secret_to_list(secret):
    result = []
    nums = []
    for i in range(2000):
        prev = secret % 10
        secret = calculate(secret)
        result.append(secret % 10 - prev)
        nums.append(secret % 10)
    return result, nums


def part2(arg):
    all_sequences = [secret_to_list(x) for x in arg]
    cost = defaultdict(int)
    for n in range(len(all_sequences)):
        seq, nums = all_sequences[n]
        s = set()
        for i in range(4, len(seq)):
            t = tuple(seq[i - 4: i])
            if t not in s:
                s.add(t)
                cost[t] += nums[i-1]

    return max(cost.values())


def parse_input(arg):
    arg = arg.strip().split('\n')
    arg = [int(x) for x in arg]
    return arg


day_input = parse_input(inp22.raw_input)
# day_input = parse_input(inp22.test_input2)
# day_input = parse_input(inp22.test_input)

print(part1(day_input))
print(part2(day_input))
