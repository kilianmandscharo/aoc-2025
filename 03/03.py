with open("./03.txt", "r") as f:
    lines = f.readlines()


def get_max_num_idx(nums, start, end):
    max_num = -1
    max_num_idx = -1

    for i in range(start, end):
        if nums[i] > max_num:
            max_num = nums[i]
            max_num_idx = i

    return max_num_idx


def get_count(width):
    count = 0
    for line in lines:
        nums = [int(val) for val in line.strip()]
        picked = [False for _ in nums]

        start = 0
        end = len(nums) - width + 1

        for _ in range(0, width):
            idx = get_max_num_idx(nums, start, end)
            picked[idx] = True
            start = idx + 1
            end += 1

        count += int("".join([str(x) for i, x in enumerate(nums) if picked[i]]))
    return count


def a():
    return get_count(2)


def b():
    return get_count(12)


print("a:", a())
print("b:", b())
