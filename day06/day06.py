import math
import re

with open("input.txt") as file:
    lines = [line for line in file]
    intlines = [[int(n) for n in re.findall(r'-?\d+', line)] for line in lines]

ops = [op for op in lines[-1].split(" ") if op != ""]

p1 = 0
p2 = 0

for i, op in enumerate(ops):
    nums = [li[i] for li in intlines[:-1]]
    if op == "+":
        p1 += sum(nums)
    else:
        p1 += math.prod(nums)

op_idx = 0
temp = []
X = max(len(line) for line in lines)
for x in range(X):
    current = ""
    for y in range(len(lines) - 1):
        if x < len(lines[y]) and lines[y][x].isnumeric():
            current += lines[y][x]
    if current.isnumeric():
        temp.append(int(current))
    if current == "" or x == X - 1:
        if ops[op_idx] == "+":
            p2 += sum(temp)
        else:
            p2 += math.prod(temp)
        op_idx += 1
        temp = []

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
