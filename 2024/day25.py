from collections import defaultdict

from inputs import inp25


def get_to_height(lock):
    results = defaultdict(int)
    for col in range(len(lock[0])):
        for i in range(len(lock)):
            if lock[i][col] == '#':
                results[col] += 1
    results = {k: v - 1 for k, v in results.items()}
    return results


def solve(arg):
    keys, locks, total_height = arg
    locks_heights = [get_to_height(lock) for lock in locks]
    keys_heights = [get_to_height(key) for key in keys]
    result = 0
    for key in keys_heights:
        for lock in locks_heights:
            if all(key[i] + lock[i] < total_height - 1 for i in range(len(keys[0][0]))):
                result += 1
    return result


def parse_input(arg):
    arg = arg.strip().split('\n\n')
    arg = [x.split('\n') for x in arg]
    keys = [x for x in arg if x[0][0] == '.']
    locks = [x for x in arg if x[0][0] == '#']
    return keys, locks, len(arg[0])


# day_input = parse_input(inp25.test_input)
day_input = parse_input(inp25.raw_input)

print(solve(day_input))
