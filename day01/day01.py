with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

p1 = 0
p2 = 0
pos = 50
for line in lines:
    offset = 1
    if line[0] == "R":
        offset = -1

    clicks = int(line[1:])
    p2 += clicks // 100
    clicks = clicks % 100

    if clicks > 0:
        prev = pos
        pos -= offset * clicks
        if prev != 0 and pos <= 0 or pos > 99:
            p2 += 1
        pos %= 100
    p1 += pos == 0

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
