from itertools import count, cycle, dropwhile


def matches():
    n = 1
    cnt = 0
    for gen in cycle((
            (((a+1)*a)/2 for a in count(1)),
            (((3*b-1)*b)/2 for b in count(1)),
            ((2*c-1)*c for c in count(1)))):
        for m in gen:
            if m > n:
                cnt = 1
                n = m
                break
            if m == n:
                cnt += 1
                if cnt == 3:
                    yield n
                    cnt = 0
                    n += 1
                break

print next(dropwhile(lambda i: i <= 40755, matches()))
