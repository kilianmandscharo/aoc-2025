def a():
    with open("./07.txt", "r") as f:
        lines = list(map(lambda l: [c for c in l.strip()], f.readlines()))

    count = 0

    for y, line in enumerate(lines[:-1]):
        for x, c in enumerate(line):
            next_line = lines[y + 1]
            if c == "S":
                next_line[x] = "|"
            if c == "|" and next_line[x] != "^":
                next_line[x] = "|"
            elif c == "|" and next_line[x] == "^":
                next_line[x - 1] = "|"
                next_line[x + 1] = "|"
                count += 1

    return count


def b():
    with open("./07.txt", "r") as f:
        lines = list(map(lambda l: [c for c in l.strip()], f.readlines()))

    count = 1

    for y, line in enumerate(lines[:-1]):
        for x, c in enumerate(line):
            next_line = lines[y + 1]
            if c == "S":
                next_line[x] = 1
            if type(c) is int and next_line[x] != "^":
                next_line[x] = c if next_line[x] == "." else next_line[x] + c
            elif type(c) is int and next_line[x] == "^":
                count += c
                left = next_line[x - 1]
                next_line[x - 1] = c if left == "." else left + c
                right = next_line[x + 1]
                next_line[x + 1] = c if right == "." else right + c

    return count


print("a:", a())
print("b:", b())
