import math
from itertools import chain, dropwhile, permutations


def is_prime(num):
    for j in xrange(2, int(math.sqrt(num) + 1)):
        if (num % j) == 0:
            return False
    return True


def pandigital_primes(n):
    for pan in permutations(xrange(1, n + 1)):
        pan = sum(10**i * _n for i, _n in enumerate(pan))
        if is_prime(pan):
            yield pan

print next(dropwhile(lambda j: j == 0,
                     (max(chain((0,), pandigital_primes(n))) for n
                      in xrange(9, 0, -1))))
