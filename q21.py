def factors(i):
    for j in xrange(1, i):
        if i % j == 0:
            yield j


def partner(i):
    p = sum(factors(i))
    if i != p and sum(factors(p)) == i:
        return p


print sum(x for x, y in {i: partner(i) for i in xrange(1, 10000)}.iteritems()
          if y and y < 10000)
