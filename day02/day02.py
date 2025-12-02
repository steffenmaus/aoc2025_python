with open("input.txt") as file:
    lines = [line.rstrip() for line in file]


def invalid_p1(n):
    s = str(n)
    L = len(s)
    if L % 2 == 0:
        if s[:L // 2] == s[L // 2:]:
            return True
    return False


def invalid_p2(n):
    s = str(n)
    L = len(s)
    for d in range(1, L):
        if L % d == 0:
            if s == s[:d] * (L // d):
                return True
    return False


p1 = 0
p2 = 0
for t in lines[0].split(","):
    a, b = t.split("-")
    for n in range(int(a), int(b) + 1):
        if invalid_p1(n):
            p1 += n
        if invalid_p2(n):
            p2 += n

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
