xx, yy = 20, 20
steps = {}


def step(x, y):
    if (x, y) in steps:
        return steps[(x, y)]
    if x == xx and y == yy:
        return 1
    total = 0
    if x < xx:
        total += step(x + 1, y)
    if y < yy:
        total += step(x, y + 1)
    steps[(x, y)] = total
    return total

print step(0, 0)
