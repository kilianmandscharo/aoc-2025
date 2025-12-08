from math import sqrt, prod
from sys import argv

is_test_mode = len(argv) > 1 and argv[1] == "test"
file_name = "./08.test.txt" if is_test_mode else "./08.txt"
iterations = 10 if is_test_mode else 1000

with open(file_name, "r") as f:
    boxes = list(
        map(lambda l: [int(val) for val in l.strip().split(",")], f.readlines())
    )

size = len(boxes)

m = [[0] * size for _ in range(size)]

distances = []

for i in range(0, size - 1):
    for j in range(i + 1, size):
        if i == j:
            continue
        box_a = boxes[i]
        box_b = boxes[j]
        dis = sqrt(
            (box_a[0] - box_b[0]) ** 2
            + (box_a[1] - box_b[1]) ** 2
            + (box_a[2] - box_b[2]) ** 2
        )
        distances.append((dis, i, j))

distances.sort(key=lambda d: d[0], reverse=True)


def connect_closest():
    _, i, j = distances.pop()
    m[i][j] = 1
    m[j][i] = 1
    return i, j


for _ in range(iterations):
    connect_closest()


def get_count(m, id, seen):
    q = [id]
    count = 0
    while len(q) > 0:
        i = q.pop()
        for j in range(len(m[i])):
            if i == j or j in seen:
                continue
            elif m[i][j] == 1:
                q.append(j)
                seen.add(j)
                count += 1
    return count


def get_circuit_counts(m):
    seen = set()
    counts = []
    for id in range(size):
        if id in seen:
            continue
        counts.append(get_count(m, id, seen))
    return counts


def a():
    counts = get_circuit_counts(m)
    counts.sort()
    return prod(counts[-3:])


def b():
    while True:
        i, j = connect_closest()
        counts = get_circuit_counts(m)
        if len(counts) == 1:
            return boxes[i][0] * boxes[j][0]


print("a:", a())
print("b:", b())
