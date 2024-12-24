import re
from inputs import inp24


def one_operation(vals, op):
    (x, op, y), res = op
    if x in vals and y in vals:
        f = lambda a, b: a ^ b
        if op == 'AND':
            f = lambda a, b: a & b
        elif op == 'OR':
            f = lambda a, b: a | b
        elif op != 'XOR':
            raise Exception(f"Not expected operation: {op}")
        vals[res] = f(vals[x], vals[y])
        return True
    return False


def calculate(old_vals, ops):
    ops = {(v, k) for k, v in ops.items()}
    vals = dict(old_vals)
    while ops:
        op = ops.pop()
        if not one_operation(vals, op):
            ops.add(op)
    vals = {k: v for k, v in vals.items() if k[0] in 'xyz'}
    return vals


def part1(arg):
    vals, ops, graph = arg
    vals = calculate(vals, graph)
    return get_val(vals, 'z')


def get_val(vals, c):
    res = sorted([k for k in vals if k[0] == c], reverse=True)
    return int(''.join(str(vals[x]) for x in sorted(res, reverse=True)), 2)


def get_graph(ops, filter = lambda a, b, c: True):
    res = []
    for (x, _, y), z in ops:
        if filter(x, y, z):
            res.append(f'{x} -> {z};')
            res.append(f'{y} -> {z};')
    return '\n'.join(res)


def to_final_str_level(graph, item, level):
    if level == 0:
        return item
    x, o, y = graph[item]
    if x[0] not in 'xy':
        x = to_final_str_level(graph, x, level - 1)
    if y[0] not in 'xy':
        y = to_final_str_level(graph, y, level - 1)
    left = x if x < y else y
    right = x if x >= y else y
    return f"({left}) {o} ({right})"


def part2(arg):
    vals, ops, graph = arg
    potential_problems = try_print(graph)
    print("Potential error:", potential_problems)

    # array deducted from the potential problematic field, then fixed after analyzing the input itself and the graph visualized by https://magjac.com/graphviz-visual-editor/
    arr = ['rds', 'jss',
           'wss', 'z18',
           'bmn', 'z23',
           'mvb', 'z08']

    vals = {x: 1 for x in vals}
    vals = calculate(vals, graph)
    x = get_val(vals, 'x')
    y = get_val(vals, 'y')
    z = get_val(vals, 'z')
    print("x + y == z", x + y == z)
    print(f"{x} + {y} == {z}", x + y == z)
    graph[arr[0]], graph[arr[1]] = graph[arr[1]], graph[arr[0]]
    graph[arr[2]], graph[arr[3]] = graph[arr[3]], graph[arr[2]]
    graph[arr[4]], graph[arr[5]] = graph[arr[5]], graph[arr[4]]
    graph[arr[6]], graph[arr[7]] = graph[arr[7]], graph[arr[6]]
    vals = calculate(vals, graph)
    z = get_val(vals, 'z')
    print("x + y == z", x + y == z)
    print(f"{x} + {y} == {z}", x + y == z)

    return ','.join(sorted(arr))


def try_print(graph):
    potential_problem = []
    for i in range(2, 45):
        current = 'z' + str(i).zfill(2)
        # operation1 = to_final_str_level(graph, current, 1)
        # operation2 = to_final_str_level(graph, current, 2)
        operation3 = to_final_str_level(graph, current, 3)
        # operation4 = to_final_str_level(graph, current, 4)

        res = re.match("\(\(\(\w\w\w\) AND \(\w\w\w\)\) OR \(\(x\d\d\) AND \(y\d\d\)\)\) XOR \(\(x\d\d\) XOR \(y\d\d\)\)", operation3)
        if not res:
            potential_problem.append(current)
        try:
            left = operation3[3:6]
            final_left = to_final_str_level(graph, left, 2)
            right = operation3[13:16]
            final_right = to_final_str_level(graph, right, 2)
            if len(final_left) < len(final_right):
                print(left, '->', final_left)
                print(right, '->', final_right)
            else:
                print(right, '->', final_right)
                print(left, '->', final_left)
        except Exception as ex:
            print("Error", current, '->', operation3)
            print(current, "ERROR:", repr(ex))
        finally:
            print(current, '->', operation3)
    return potential_problem


def parse_input(arg):
    vals, ops = arg.strip().split('\n\n')
    vals = vals.split('\n')
    ops = ops.split('\n')
    vals = [x.split(': ') for x in vals]
    vals = {x[0]: int(x[1]) for x in vals}
    ops = [x.split(' -> ') for x in ops]
    ops = {(tuple(x.split(' ')), y) for x, y in ops}
    graph = {z: rest for rest, z in ops}
    return vals, ops, graph


day_input = parse_input(inp24.raw_input)
# day_input = parse_input(inp24.test_input)

print(part1(day_input))
print(part2(day_input))
