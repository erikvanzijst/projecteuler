def terms(ceil):
    for a in xrange(2, ceil + 1):
        for b in xrange(2, ceil + 1):
            yield a**b

print sum(1 for _ in set(terms(100)))