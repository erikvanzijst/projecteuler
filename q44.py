from itertools import permutations


def gen():
    pents = {((3 * n - 1) * n) / 2 for n in xrange(1, 10000)}
    for a, b in permutations(pents, 2):
        if (a + b) in pents and (b - a) in pents:
            yield b - a

print min(gen())
