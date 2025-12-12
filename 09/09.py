from sys import argv

is_test_mode = len(argv) > 1 and argv[1] == "test"
file_name = "./09.test.txt" if is_test_mode else "./09.txt"

with open(file_name, "r") as f:
    points = [tuple(map(int, l.strip().split(","))) for l in f.readlines()]
    sides = [(points[i], points[(i + 1) % len(points)]) for i in range(len(points))]
    point_set = set(points)


def a():
    largest = -1

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            (x1, y1), (x2, y2) = points[i], points[j]
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            largest = max(largest, area)

    return largest


v = "VERTICAL"
h = "HORIZONTAL"


def is_point_on_line(p, l):
    min_x = min(l[0][0], l[1][0])
    max_x = max(l[0][0], l[1][0])

    min_y = min(l[0][1], l[1][1])
    max_y = max(l[0][1], l[1][1])

    x, y = p

    return x >= min_x and x <= max_x and y >= min_y and y <= max_y


def is_point_on_polygon(p):
    for side in sides:
        if is_point_on_line(p, side):
            return True
    return False


def do_lines_intersect(a, b):
    (a1, a2), (b1, b2) = a, b

    # a_dir = v if a1[0] == a2[0] else h
    # b_dir = v if b1[0] == b2[0] else h
    #
    # if a_dir == b_dir:
    #     return False

    a_min_y = min(a1[1], a2[1])
    a_max_y = max(a1[1], a2[1])
    b_min_y = min(b1[1], b2[1])
    b_max_y = max(b1[1], b2[1])
    do_not_overlap_y = a_min_y > b_max_y or a_max_y < b_min_y

    a_min_x = min(a1[0], a2[0])
    a_max_x = max(a1[0], a2[0])
    b_min_x = min(b1[0], b2[0])
    b_max_x = max(b1[0], b2[0])
    do_not_overlap_x = a_min_x > b_max_x or a_max_x < b_min_x

    return not do_not_overlap_y and not do_not_overlap_x


def is_point_in_polygon(p):
    count = 0
    ray = ((0, p[1]), p)
    print()
    print(p)
    for side in sides:
        if do_lines_intersect(ray, side):
            print(ray, side)
            count += 1
    return count % 2 != 0


width = 14
height = 9


def print_grid():
    grid = [["."] * width for _ in range(height)]
    for x in range(width):
        for y in range(height):
            point = (x, y)
            if is_point_on_polygon(point):
                if point in point_set:
                    grid[point[1]][point[0]] = "#"
                else:
                    grid[point[1]][point[0]] = "O"
            elif is_point_in_polygon(point):
                grid[point[1]][point[0]] = "i"
    for l in grid:
        print("".join(l))
    print()


def b():
    print_grid()

    return 0


print("a:", a())
print("b:", b())
