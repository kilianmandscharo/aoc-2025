with open("./02.txt", "r") as f:
    lines = f.readlines()

count_a = 0
count_b = 0


def is_invalid_a(num):
    val = str(num)
    half_point = len(val) // 2
    return val[:half_point] == val[half_point:]


def is_invalid_b(num):
    val = str(num)
    val_len = len(val)
    if val_len == 1:
        return False

    for chunk_size in range(val_len // 2, 0, -1):
        max_chunk_idx = val_len / chunk_size
        if max_chunk_idx % 1 != 0:
            continue

        curr_slice = val[:chunk_size]
        for chunk_idx in range(1, int(max_chunk_idx)):
            start = chunk_size * chunk_idx
            slice = val[start : start + chunk_size]
            if curr_slice != slice:
                break
            if chunk_idx == max_chunk_idx - 1:
                return True
            curr_slice = slice

    return False


for item in lines[0].split(","):
    left, right = item.split("-")
    for num in range(int(left), int(right) + 1):
        if is_invalid_a(num):
            count_a += num
        if is_invalid_b(num):
            count_b += num

print("a:", count_a)
print("b:", count_b)
