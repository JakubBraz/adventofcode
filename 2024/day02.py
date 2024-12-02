from inputs.inp02 import raw_input


def check_line(nums):
    sorted_increasing = sorted(nums)
    sorted_decreasing = sorted(nums, reverse=True)
    if nums != sorted_increasing and nums != sorted_decreasing:
        return False
    return all(1 <= abs(nums[i] - nums[i+1]) <= 3 for i in range(len(nums) - 1))


def part1(arg):
    result = [line for line in arg if check_line(line)]
    return len(result)


def part2(arg):
    result = [line for line in arg if any(check_line(line[:i] + line[i+1:]) for i in range(len(line) + 1))]
    return len(result)


def parse_input(day_input):
    result = day_input.strip()
    result = result.split('\n')
    result = [line.split() for line in result]
    result = [[int(x) for x in line] for line in result]
    return result


test_input = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''

inp = parse_input(raw_input)
# inp = parse_input(test_input)

print(part1(inp))
print(part2(inp))
