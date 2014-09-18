from itertools import dropwhile


def fib(a=1, b=1):
    while 1:
        yield a
        a, b = b, a + b

print next(dropwhile(lambda i: i[1] < 10**999, enumerate(fib(), 1)))[0]
