with open("./05.txt", "r") as f:
    lines = f.readlines()

ranges = []
ids = []

for line in lines:
    line = line.strip()
    if "-" in line:
        lower, upper = line.split("-")
        ranges.append((int(lower), int(upper)))
    elif len(line) > 0:
        ids.append(int(line))


def is_fresh(id, ranges):
    for lower, upper in ranges:
        if id >= lower and id <= upper:
            return True
    return False


def a():
    count = 0
    for id in ids:
        if is_fresh(id, ranges):
            count += 1
    return count


def can_be_merged_with(idx, ranges):
    lower_a, upper_a = ranges[idx]
    for i, (lower_b, upper_b) in enumerate(ranges):
        if i == idx:
            continue
        if lower_a > upper_b or upper_a < lower_b:
            continue
        return i, (
            min(lower_a, upper_a, lower_b, upper_b),
            max(lower_a, upper_a, lower_b, upper_b),
        )
    return None


def b():
    b_ranges = ranges

    while True:
        found_merge = False

        for i in range(0, len(b_ranges)):
            result = can_be_merged_with(i, b_ranges)
            if result is None:
                continue
            idx, new_r = result
            b_ranges[i] = new_r
            b_ranges = b_ranges[:idx] + b_ranges[idx + 1 :]
            found_merge = True
            break

        if not found_merge:
            break

    count = 0

    for lower, upper in b_ranges:
        count += upper - lower + 1

    return count


print("a:", a())
print("b:", b())
