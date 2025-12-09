with open("input.txt") as file:
    lines = [line.rstrip() for line in file]


def is_valid(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    top = min(y1, y2)
    right = max(x1, x2)
    lower = max(y1, y2)
    left = min(x1, x2)

    for w in walls:
        c1, c2 = w
        wall_top = min(c1[1], c2[1])
        wall_lower = max(c1[1], c2[1])
        wall_left = min(c1[0], c2[0])
        wall_right = max(c1[0], c2[0])
        if left < wall_right and wall_left < right and top < wall_lower and wall_top < lower:
            return False

    return True


corners = []

for l in lines:
    a, b = l.split(",")
    a = int(a)
    b = int(b)
    corners.append((a, b))

walls = list(zip(corners, corners[1:]))
walls.append((corners[-1], corners[0]))

p1 = 0
p2 = 0

for c1 in corners:
    for c2 in corners:
        if c1 > c2:
            x1, y1 = c1
            x2, y2 = c2
            size = (abs(x1 - x2) + 1) * (1 + abs(y1 - y2))
            p1 = max(size, p1)
            if size > p2:
                if is_valid(c1, c2):
                    p2 = size

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
