def step(exp, x=0, f=0, results=None, depth=0):
    if depth >= 7:  # max depth is rather arbitrary
        if x == f and x > 1:
            return (results or []) + [x]
    else:
        for j in xrange(10):
            results = step(exp, x * 10 + j, f + j**exp, results, depth+1)
    return results

print sum(step(5))
