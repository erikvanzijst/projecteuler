import math


def primes(max_n):
    numbers = range(3, max_n + 1, 2)
    half = max_n // 2
    initial = 4

    for step in xrange(3, max_n + 1, 2):
        for i in xrange(initial, half, step):
            numbers[i - 1] = 0
        initial += 2 * (step + 1)

        if initial > half:
            return [2] + filter(None, numbers)

primes = set(primes(1000000))


def test(p):
    i = p
    while i and i in primes:
        i /= 10
    if i == 0:
        i, mag = p, int(math.log10(p))
        while i and i in primes:
            i, mag = i % 10**mag, mag - 1
    return i == 0


print sum(_p for _p in primes if _p > 10 and test(_p))
