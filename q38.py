from itertools import count, permutations


def decimals(i):
    while i:
        yield i % 10
        i /= 10


def gen():
    for pan in permutations(xrange(1, 10)):
        for n, pos in ((sum(10**i * _n for i, _n in enumerate(pan[9-j:])), 9-j)
                       for j in xrange(1, 6)):
            for m in count(2):
                decs = tuple(decimals(n * m))
                if pan[pos - len(decs):pos] != decs:
                    break
                pos -= len(decs)
                if pos < 0:
                    break
                elif pos == 0:
                    yield sum(10**i * _n for i, _n in enumerate(pan))
                    break

print max(gen())
