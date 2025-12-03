with open("input.txt") as file:
    lines = [line.rstrip() for line in file]


def f(input, length):
    pos1 = 0
    pos2 = len(input) + 1 - length
    out_str = ""
    while len(out_str) < length:
        temp = input[pos1:pos2]
        v = max(temp)
        i = temp.index(v)
        out_str += v
        pos1 += i + 1
        pos2 += 1
    return int(out_str)


p1 = 0
p2 = 0
for line in lines:
    p1 += f(line, 2)
    p2 += f(line, 12)

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
