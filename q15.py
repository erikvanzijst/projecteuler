xx, yy = 4, 4


def step(x, y, total=0):
    if x < 13 and x == y:
        print '(%d, %d)' % (x, y)
    if x == xx and y == yy:
        return total + 1
    if x < xx:
        total = step(x + 1, y, total)
    if y < yy:
        total = step(x, y + 1, total)
    return total

print step(0, 0)
