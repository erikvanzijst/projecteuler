from itertools import count, islice


def decimals(i):
    while i:
        yield i % 10
        i /= 10


def gen():
    for i in count(1):
        for j in tuple(decimals(i))[::-1]:
            yield j

targets = {10**i for i in xrange(7)}
print reduce(lambda a, b: a * b,
             islice((d for _i, d in enumerate(gen(), 1)
                     if _i in targets), 0, 7))
