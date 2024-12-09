from inputs import inp09


def to_ids(f):
    result = []
    for i, v in enumerate(f):
        val = [i // 2] * int(v) if i % 2 == 0 else ['.'] * int(v)
        if val:
            result.append(val)
    return result


def replace(f):
    l = 0
    r = len(f) - 1
    res = [c for c in f]
    while res[l] != '.':
        l += 1
    while res[r] == '.':
        r -= 1
    while l < r:
        res[l], res[r] = res[r], '.'
        l += 1
        r -= 1
        while l < len(res) and res[l] != '.':
            l += 1
        while r >=0 and res[r] == '.':
            r -= 1
    return res


def find_l_ind(arr, l, r):
    while arr[l][0] != '.' or len(arr[r]) > len(arr[l]):
        l += 1
        if l == len(arr) or l >= r:
            return -1
    return l


def move_file(arr):
    arr = [x for x in arr]
    num_set = {x for file in arr for x in file if x != '.'}
    num_set = sorted(num_set)
    r = len(arr) - 1
    while num_set:
        while arr[r][0] != num_set[-1]:
            r -= 1
        l = find_l_ind(arr, 0, r)
        if l != -1:
            old_len_l = len(arr[l])
            old_len_r = len(arr[r])
            arr[l] = arr[r]
            arr[r] = ['.'] * old_len_r
            if old_len_l - old_len_r > 0:
                arr.insert(l + 1, ['.'] * (old_len_l - old_len_r))
        num_set.pop()
    return arr


def part1(arg):
    arg = to_ids(arg)
    arg = [x for file in arg for x in file]
    res = replace(arg)
    return sum(int(v) * i for i, v in enumerate(res) if v != '.')


def part2(arg):
    arg = to_ids(arg)
    res = move_file(arg)
    res = [x for file in res for x in file]
    return sum(v * i for i, v in enumerate(res) if v != '.')


# day_input = inp09.test_input
day_input = inp09.raw_input


print(part1(day_input))
print(part2(day_input))
