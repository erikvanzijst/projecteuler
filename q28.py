from itertools import count, islice


def corners(dimension):
    counter = count(1)
    yield next(counter)
    for i in xrange(2, dimension, 2):
        for j in xrange(4):
            list(islice(counter, i - 1))
            yield next(counter)

print sum(corners(1001))