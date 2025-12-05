groups = [group.split("\n") for group in open("input.txt").read().split("\n\n")]

fresh = []
for f in groups[0]:
    a, b = f.split("-")
    fresh.append((int(a), int(b)))

p1 = 0
p2 = 0

for a in groups[1]:
    p1 += any([int(a) in range(f[0], f[1]) for f in fresh])

fresh.sort()
prev = -1
for a, b in fresh:
    if b > prev:
        p2 += b + 1 - max(prev + 1, a)
        prev = b

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
