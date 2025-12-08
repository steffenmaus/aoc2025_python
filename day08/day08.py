import math

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

points = set()
for line in lines:
    a, b, c = line.split(",")
    points.add((int(a), int(b), int(c)))

networks = []
open = []

for p in points:
    for p2 in points:
        if p > p2:
            a, b, c = p
            a2, b2, c2 = p2
            d = math.sqrt(abs(a - a2) * abs(a - a2) + abs(b - b2) * abs(b - b2) + abs(c - c2) * abs(c - c2))
            open.append((d, p, p2))

open.sort()
DONE = set()
last_connection = None
for i in range(len(open)):
    if len(DONE) == len(points):
        break
    _, p, p2 = open[i]
    if i == 1000:
        lens = []
        for n in networks:
            lens.append(len(n))
        print("Part 1: " + str(math.prod(sorted(lens, reverse=True)[:3])))

    if p in DONE and p2 in DONE:
        for n in networks:
            if p in n:
                break
        for n2 in networks:
            if p2 in n2:
                break
        if n != n2:
            n |= n2
            networks.remove(n2)
        continue
    elif p in DONE:
        for n in networks:
            if p in n:
                n.add(p2)
                DONE.add(p2)
                break
    elif p2 in DONE:
        for n in networks:
            if p2 in n:
                n.add(p)
                DONE.add(p)
                break
    else:
        networks.append({p, p2})
        DONE.add(p)
        DONE.add(p2)
    last_connection = (p, p2)

print("Part 2: " + str(last_connection[0][0] * last_connection[1][0]))
