import math
from itertools import count, takewhile


def is_prime(num):
    if num == 2:
        return True
    if not num & 1:
        return False
    for j in xrange(2, int(math.sqrt(num) + 1)):
        if (num % j) == 0:
            return False
    return True


def gen():
    primes = []
    for n, is_p in ((i, is_prime(i)) for i in count(2)):
        if is_p:
            primes.append(n)
        elif n & 1:
            composable = False
            for p in primes:
                for j in takewhile(lambda x: x <= n,
                                   (_j**2 * 2 + p for _j in count(1))):
                    if j == n:
                        composable = True
                        break
                if composable:
                    break
            if not composable:
                yield n

print next(gen())
