def factors(i):
    for j in xrange(1, i):
        if i % j == 0:
            yield j


def gen():
    terms = set(i for i in xrange(12, 28123) if sum(factors(i)) > i)
    for j in xrange(1, 28124):
        for i in terms:
            if (j - i) in terms:
                break
        else:
            yield j

print sum(gen())