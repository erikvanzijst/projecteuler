def collatz(i):
    while i != 1:
        yield i
        i = i / 2 if i % 2 == 0 else 3 * i + 1
    yield 1

print max(((i, sum(1 for _ in collatz(i))) for i in xrange(1, 1000000)),
          key=lambda tup: tup[1])[0]
