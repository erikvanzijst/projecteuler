from collections import defaultdict
import math


def gen(p):
    for i in xrange(1, p-1):
        for j in xrange(1, i + 1):
            s = math.sqrt(i**2 + j**2)
            _p = i + j + s
            if s % 1 == 0 and _p <= p:
                yield int(_p), (j, i, int(s))
            elif _p > p:
                break

perimeters = defaultdict(list)
for p, sides in gen(1000):
    perimeters[p].append(sides)

print max(perimeters.iteritems(), key=lambda (p, sides): len(sides))[0]
