from itertools import count


def triangle_numbers():
    num = 0
    for i in count(1):
        num += i
        yield num


def factor(n):
    # taken from: http://stackoverflow.com/a/6800214
    return set(reduce(
        list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

for t in triangle_numbers():
    if len(factor(t)) > 500:
        print t
        break
