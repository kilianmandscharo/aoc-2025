with open("./03.test.txt", "r") as f:
    lines = f.readlines()


def get_max_num_idx(nums, picked, start):
    max_num = -1
    max_num_idx = -1

    for i in range(start, len(nums)):
        if picked[i]:
            continue
        if nums[i] >= max_num:
            max_num = nums[i]
            max_num_idx = i

    return max_num_idx


def get_count(width):
    count = 0
    for line in lines:
        nums = [int(val) for val in line.strip()]
        picked = [False for _ in nums]

        print(line.strip())

        start = 0

        for _ in range(0, width):
            idx = get_max_num_idx(nums, picked, start)
            print(f"{idx} ({nums[idx]}), start: {start}")
            picked[idx] = True
            if len(nums) - idx >= width and nums[idx] > nums[start]:
                start = idx + 1

        num = ""
        for i, p in enumerate(picked):
            if p:
                num += str(nums[i])

        print(num)
        print()
        count += int(num)
    return count


def a():
    return get_count(2)


def b():
    return get_count(12)


print("a:", a())

# this answer is not correct yet
print("b:", b())
