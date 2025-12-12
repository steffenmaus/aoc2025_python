groups = [group.split("\n") for group in open("input.txt").read().split("\n\n")]

gift_sizes = {}

for g in groups[:-1]:
    id = int(g[0][:-1])
    size = sum([r.count("#") for r in g])
    gift_sizes[id] = size

p1 = 0

for r in groups[-1]:
    width, length = r.split(":")[0].split("x")
    space = int(width) * int(length)
    required = r.split(" ")[1:]
    space_req = 0
    for i, v in enumerate(required):
        space_req += int(v) * gift_sizes[i]
    p1 += space >= space_req

print("Part 1: " + str(p1))