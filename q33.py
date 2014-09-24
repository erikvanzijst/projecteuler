from itertools import product


def factors(i):
    for j in xrange(i, 1, -1):
        if i % j == 0:
            yield j


def simplify(n, d):
    fn = set(factors(n))
    for i in factors(d):
        if i in fn:
            return n / i, d / i
    return n, d

digits = lambda _i: tuple(_j for _j in (_i / 10, _i % 10) if _j)


def fractions():
    for n in xrange(10, 100):
        t_n = digits(n)
        for d in xrange(n + 1, 100):
            t_d = digits(d)
            if len(t_d) == len(t_n):
                for (i, tn), (j, td) in product(enumerate(t_n), enumerate(t_d)):
                    if tn == td and simplify(n, d) == simplify(t_n[(i+1) % 2],
                                                               t_d[(j+1) % 2]):
                        yield n, d
                        break

print simplify(*reduce(lambda (n1, d1), (n2, d2): simplify(n1 * n2, d1 * d2),
                       fractions()))[1]
