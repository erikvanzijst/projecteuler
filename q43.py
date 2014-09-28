from itertools import imap, permutations


print sum(sum(10**e * pan[i] for i, e in enumerate(xrange(9, -1, -1)))
          for pan in permutations(xrange(10))
          if all(imap(lambda a, b: a % b == 0,
                      (sum(pan[_i] * 10**exp for exp, _i
                           in enumerate(xrange(pos + 2, pos - 1, -1)))
                       for pos in xrange(1, 8)),
                      (2, 3, 5, 7, 11, 13, 17))))
