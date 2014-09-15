import math


def is_prime(num):
    for j in range(2, int(math.sqrt(num) + 1)):
        if (num % j) == 0:
            return False
    return True


def primes():
    yield 2
    i = 3
    while True:
        if is_prime(i):
            yield i
        i += 2

p = primes()
for _ in xrange(10000):
    next(p)
print next(p)
