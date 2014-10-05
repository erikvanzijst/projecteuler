def digits(n):
    while n:
        n, d = n / 10, n % 10
        yield d


def is_prime(num):
    if not num & 1:
        return False
    for j in xrange(3, int(num**.5) + 1, 2):
        if num % j == 0:
            return False
    return True

primes = [(pp, dpp) for pp, dpp
          in ((p, set(digits(p))) for p in xrange(1000, 10000)
              if is_prime(p) and p not in (1487, 4817, 8147))]


for i, (a, da) in enumerate(primes):
    for j, (b, db) in enumerate(primes[i+1:], i+1):
        if da != db:
            continue
        for c, dc in primes[j+1:]:
            if c - b > b - a:
                break
            if dc == db and c - b == b - a:
                print a * 10**8 + b * 10**4 + c
                exit()
