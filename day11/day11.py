from collections import defaultdict

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

outputs = defaultdict(list)

for line in lines:
    a, b = line.split(": ")
    outputs[a] = b.split(" ")

cache = {}


def f(current, target):
    key = (current, target)
    if key in cache:
        return cache[key]
    if current == target:
        return 1
    out = 0
    for n in outputs[current]:
        out += f(n, target)
    cache[key] = out
    return out


p1 = f("you", "out")

if f("dac", "out") > 0:
    p2 = f("svr", "fft") * f("fft", "dac") * f("dac", "out")
else:
    p2 = f("svr", "dac") * f("dac", "fft") * f("fft", "out")

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
