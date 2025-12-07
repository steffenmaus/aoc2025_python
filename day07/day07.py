with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

cache = {}


def f(p):
    if p in cache:
        return cache[p]
    x, y = p
    if y >= Y:
        return 1
    if p in splitters:
        cache[p] = f((x - 1, y + 1)) + f((x + 1, y + 1))
        return cache[p]
    else:
        cache[p] = f((x, y + 1))
        return cache[p]


X = len(lines[0])
Y = len(lines)

start = None
splitters = set()
for y in range(0, Y):
    for x in range(0, X):
        p = (x, y)
        c = lines[y][x]
        if c == "S":
            start = p
        elif c == "^":
            splitters.add(p)

open = {start}
splitted = set()
while open:
    p = open.pop()
    x, y = p
    if y < Y:
        if p in splitters:
            splitted.add(p)
            open.add((x + 1, y + 1))
            open.add((x - 1, y + 1))
        else:
            open.add((x, y + 1))

p1 = len(splitted)
p2 = f(start)

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
