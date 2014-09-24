from math import factorial

factorials = [factorial(i) for i in xrange(10)]


def digits(n):
    while n:
        n, d = n / 10, n % 10
        yield d


print sum(a for a, b
          in ((j, sum(map(lambda _j: factorials[_j], digits(j)))) for j
              in xrange(3, 1000000)) if a == b)
