with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

p1 = 0
p2 = 0
current = 50
for line in lines:
    offset = 1
    if line[0] == "R":
        offset = -1

    clicks = int(line[1:])
    # print(clicks)
    p2 += clicks // 100
    clicks = clicks % 100

    if clicks > 0:
        prev = current
        current -= offset * clicks
        if prev != 0 and current <= 0 or current > 99:
            p2 += 1
        current %= 100
    p1 += current == 0

print(p1)
print(p2)
