with open("input.txt") as file:
    lines = [line.rstrip() for line in file]


def get_all_nei(p):
    x, y = p
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if (dx, dy) != (0, 0):
                yield (x + dx, y + dy)


X = len(lines[0])
Y = len(lines)

paper = set()
for y in range(0, Y):
    for x in range(0, X):
        p = (x, y)
        if lines[y][x] == "@":
            paper.add(p)

p1 = 0
p2 = 0

progress = True
while progress:
    progress = False
    drop = set()
    for p in paper:
        if len([n for n in get_all_nei(p) if n in paper]) < 4:
            drop.add(p)
    if p1 == 0:
        p1 = len(drop)
    p2 += len(drop)
    for d in drop:
        paper.remove(d)
        progress = True

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
