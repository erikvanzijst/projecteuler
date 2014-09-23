from itertools import permutations


def test(num):
    for i in xrange(1, 5):
        exp = 10**i
        multiplicant, rest = num % exp, num / exp
        for j in xrange(1, 6-i):
            exp2 = 10**j
            multiplier, product = rest % exp2, rest / exp2
            p = multiplicant * multiplier
            if p > product:
                break
            elif p == product:
                return product

print sum(set(product for product in
              (test(sum(10**i * n for i, n in enumerate(p))) for p
               in permutations(range(1, 10)))
              if product))
