from os import read
from sys import argv

is_test_mode = len(argv) > 1 and argv[1] == "test"
file_name = "./09.test.txt" if is_test_mode else "./09.txt"


def a():
    with open(file_name, "r") as f:
        points = [tuple(map(int, l.strip().split(","))) for l in f.readlines()]

    largest = -1

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            (x1, y1), (x2, y2) = points[i], points[j]
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            largest = max(largest, area)

    return largest


# def is_point_in_polygon(p, vertices, points, min_x, cache):
#     if p in cache:
#         return cache[p]
#     if p in vertices or p in points:
#         return True
#     x, y = p
#     count = 0
#     vertex = None
#     while x >= min_x - 1:
#         if (x, y) in vertices:
#             vertex_dir = -1 if (x, y - 1) in points or (x, y - 1) in vertices else 1
#             if vertex is None:
#                 vertex = vertex_dir
#             elif vertex != vertex_dir:
#                 count += 1
#                 vertex = None
#         if (x, y) in points and vertex is None:
#             count += 1
#         x -= 1
#     ret = count % 2 != 0
#     cache[p] = ret
#     return ret
#
#
# def b():
#     with open(file_name, "r") as f:
#         data = [tuple(map(int, l.strip().split(","))) for l in f.readlines()]
#         points_min_x = min([p[0] for p in data])
#
#     vertices = set(data)
#     points = set()
#
#     for i in range(len(data)):
#         p1 = data[i]
#         p2 = data[(i + 1) % len(data)]
#         min_x = min(p1[0], p2[0])
#         max_x = max(p1[0], p2[0])
#         min_y = min(p1[1], p2[1])
#         max_y = max(p1[1], p2[1])
#         direction = "h" if min_y == max_y else "v"
#         if direction == "h":
#             for x in range(min_x + 1, max_x):
#                 points.add((x, min_y))
#         else:
#             for y in range(min_y + 1, max_y):
#                 points.add((min_x, y))
#
#     largest = -1
#
#     cache = dict()
#
#     for i in range(len(data)):
#         for j in range(i + 1, len(data)):
#             (x1, y1), (x2, y2) = data[i], data[j]
#             a, b = (x1, y2), (x2, y1)
#             if is_point_in_polygon(
#                 a, vertices, points, points_min_x, cache
#             ) and is_point_in_polygon(b, vertices, points, points_min_x, cache):
#                 area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
#                 largest = max(largest, area)
#
#     return largest


def b():
    with open(file_name, "r") as f:
        data = [tuple(map(int, l.strip().split(","))) for l in f.readlines()]
        verteces = set(data)
        points = set()

        for i in range(len(data)):
            p1 = data[i]
            p2 = data[(i + 1) % len(data)]
            min_x = min(p1[0], p2[0])
            max_x = max(p1[0], p2[0])
            min_y = min(p1[1], p2[1])
            max_y = max(p1[1], p2[1])
            direction = "h" if min_y == max_y else "v"
            if direction == "h":
                for x in range(min_x + 1, max_x):
                    points.add((x, min_y))
            else:
                for y in range(min_y + 1, max_y):
                    points.add((min_x, y))

    largest = -1

    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            (x1, y1), (x2, y2) = data[i], data[j]

            if x1 == x2 or y1 == y2:
                continue

            p3 = (x1, y2)
            p4 = (x2, y1)

            if p3 not in verteces and p4 not in verteces:
                continue

            (target_x, target_y) = p4 if p3 in verteces else p3

            x_dir = 1 if x1 < target_x else -1 if x1 > target_x else 0
            y_dir = 1 if y1 < target_y else -1 if y1 > target_y else 0

            x, y = x1, y1

            reached_target = False
            outside = False
            while True:
                x += x_dir
                y += y_dir
                if not outside and (x, y) in verteces:
                    outside = True
                elif outside and ((x, y) in points or (x, y) in verteces):
                    break
                elif x == target_x and y == target_y:
                    reached_target = True
                    break

            if not reached_target:
                continue

            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

            print(f"{data[i]}, {data[j]}, target: {(target_x, target_y)}, area: {area}")

            largest = max(largest, area)

    return largest


print("a:", a())
print("b:", b())
