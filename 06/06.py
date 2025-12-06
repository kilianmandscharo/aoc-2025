from math import prod


def calculate(op, nums):
    match op:
        case "*":
            return prod(nums)
        case "+":
            return sum(nums)
    return 0


def a():
    with open("./06.txt", "r") as f:
        data = list((map(lambda l: l.split(), f.readlines())))

    lines = data[:-1]
    ops = data[-1]

    count = 0

    for i, op in enumerate(ops):
        nums = [int(line[i]) for line in lines]
        count += calculate(op, nums)

    return count


def b():
    with open("./06.txt", "r") as f:
        data = f.readlines()

    lines = [[] for _ in range(0, len(data) - 1)]

    last = data[-1]
    rest = data[:-1]

    start = 0

    for i, c in enumerate(last):
        if i == 0 or c == " ":
            continue
        for j, line in enumerate(rest):
            offset = -1 if c != "\n" else 0
            lines[j].append(line[start : i + offset])
        start = i

    count = 0

    for i, op in enumerate(last.split()):
        max_len = max([len(lines[j][i]) for j in range(0, len(lines))])
        nums = ["" for _ in range(0, max_len)]
        for line in lines:
            val = line[i]
            for idx in range(0, max_len):
                nums[idx] += val[idx]
        nums = map(int, nums)
        count += calculate(op, nums)

    return count


print("a:", a())
print("b:", b())
