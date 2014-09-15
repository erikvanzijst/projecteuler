def fib(a, b, ceil):
    while a < ceil:
        yield a
        a, b = b, a + b

print sum(i for i in fib(1, 2, 4000000) if i % 2 == 0)
