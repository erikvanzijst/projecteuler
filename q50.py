def is_prime(num):
    if not num & 1:
        return False
    for j in xrange(3, int(num**.5) + 1, 2):
        if num % j == 0:
            return False
    return True

ceil = 1000000
primes = [2] + [i for i in xrange(3, ceil) if is_prime(i)]
primes_set = set(primes)

end = len(primes) / 2

sigma = sum(primes[:end+1])
for ln in xrange(end, 0, -1):
    sigma -= primes[ln]
    s = sigma
    for pos in xrange(end+1 - ln):
        if s in primes_set:
            print sum(primes[pos:pos+ln])
            exit()
        s -= primes[pos]
        s += primes[pos+ln]
