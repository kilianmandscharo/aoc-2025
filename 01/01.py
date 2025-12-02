with open("./01.txt", "r") as f:
    lines = f.readlines()

count_a = 0
count_b = 0

dial = 50

for line in lines:
    line = line.strip()
    sign = -1 if line[0] == "L" else 1
    amount = int(line[1:])

    dial_before = dial
    dial = dial + amount * sign

    seen_zero = 0
    if dial == 0:
        seen_zero = 1
    elif dial < 0 and dial_before == 0:
        seen_zero = abs(dial) // 100
    elif dial < 0:
        seen_zero = abs(dial) // 100 + 1
    elif dial > 99:
        seen_zero = dial // 100

    count_b += seen_zero
    dial = dial % 100
    count_a += 1 if dial == 0 else 0

print("a:", count_a)
print("b:", count_b)
