from itertools import takewhile, count


class Primes(object):
    def __init__(self):
        self._primes = [2]
        self._prime_set = {2}

    def _is_prime(self, num):
        if not num & 1:
            return False
        for j in xrange(3, int(num**.5) + 1, 2):
            if num % j == 0:
                return False
        return True

    def __iter__(self):
        def gen():
            for p in self._primes:
                yield p
            for p in (i for i in count(self._primes[-1] + 1) if self._is_prime(i)):
                self._primes.append(p)
                self._prime_set.add(p)
                yield p
        return gen()

    def __contains__(self, n):
        if n > self._primes[-1]:
            for p in (i for i in count(self._primes[-1] + 1) if self._is_prime(i)):
                self._primes.append(p)
                self._prime_set.add(p)
                if p >= n:
                    break
        return n in self._prime_set

    def factorize(self, p):
        while p > 1:
            if p in self:
                yield p
                break
            ceil = p/2+1
            for pp in takewhile(lambda ppp: ppp <= ceil, self):
                if p % pp == 0:
                    p /= pp
                    yield pp
                    break
            else:
                break

primes = Primes()
nums = []
for n in count(2):
    if len(set(primes.factorize(n))) == 4:
        nums.append(n)
        if len(nums) == 4:
            break
    elif len(nums) > 0:
        nums = []

print nums[0]
