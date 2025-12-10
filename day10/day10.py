from z3 import *

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]


def f(target, buttons):
    open = {frozenset()}
    completed = set()
    clicks = 0
    while True:
        next_open = set()
        completed |= open
        for current in open:
            if current == target:
                return clicks
            for b in buttons:
                next = set(current)
                for i in b:
                    if i in next:
                        next.remove(i)
                    else:
                        next.add(i)
                if next not in completed:
                    next_open.add(frozenset(next))
        open = next_open
        clicks += 1


def solve(target, buttons):
    my_optimizer = z3.Optimize()

    clicks = [Int(i) for i in range(len(buttons))]

    for i, target_i in enumerate(target):
        count = 0
        for j, b in enumerate(buttons):
            if i in b:
                count += clicks[j]
        my_optimizer.add(count == target_i)

    my_optimizer.add(And([c >= 0 for c in clicks]))

    my_optimizer.minimize(sum(clicks))
    my_optimizer.check()
    model = my_optimizer.model()
    return sum([model.eval(c).as_long() for c in clicks])


p1 = 0
p2 = 0

for line in lines:
    target_raw = line.split(" ")[0][1:-1]
    target = set()
    for i, v in enumerate(target_raw):
        if v == "#":
            target.add(i)

    buttons = []
    for buttons_raw in line.split(" ")[1:-1]:
        buttons.append([int(b) for b in buttons_raw[1:-1].split(",")])

    joltage = [int(j) for j in line.split("{")[1][:-1].split(",")]

    p1 += f(target, buttons)
    p2 += solve(joltage, buttons)

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
