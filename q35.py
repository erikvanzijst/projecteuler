import math


def is_prime(num):
    for j in xrange(2, int(math.sqrt(num) + 1)):
        if (num % j) == 0:
            return False
    return True


def rotate(n):
    mag = int(math.log10(n))
    for _ in xrange(mag + 1):
        yield n
        n = (n % 10) * 10**mag + n / 10

primes = set(i for i in xrange(2, 1000000) if is_prime(i))
print sum(1 for p in primes if all((pp in primes) for pp in rotate(p)))
