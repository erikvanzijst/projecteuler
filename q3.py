import math


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


def factor(i):
    if is_prime(i):
        return [i]
    for p in primes():
        if i % p == 0:
            return [p] + factor(i / p)

print max(factor(600851475143))