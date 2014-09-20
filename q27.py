import math
from itertools import dropwhile, islice


def compute_primes(ceil):
    def is_prime(num):
        for j in range(2, int(math.sqrt(num) + 1)):
            if (num % j) == 0:
                return False
        return True

    def primes():
        i = 2
        while True:
            if is_prime(i):
                yield i
            i += 1
    primes = set(islice(primes(), ceil))
    return lambda i: i in primes
is_prime = compute_primes(10000)

def series():
    for a in xrange(-999, 1000):
        for b in xrange(-999, 1000):
            yield (a, b), next(dropwhile(
                lambda (i, n): is_prime(n ** 2 + a * n + b),
                enumerate(xrange(1000))))[0]

(a, b), length = max(series(), key=lambda ((a, b), length): length)
print a * b
