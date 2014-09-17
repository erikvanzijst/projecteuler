def fact(i):
    if i == 1:
        return i
    return i * fact(i-1)

print sum(int(c) for c in str(fact(100)))
