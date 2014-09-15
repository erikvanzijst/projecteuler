target = 1000
for a in xrange(1, target - 2):
    for b in xrange(a + 1, target - 1):
        for c in xrange(b + 1, target):
            if a + b + c == target and a**2 + b**2 == c**2:
                print a * b * c
                exit()
