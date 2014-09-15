factors = range(1, 21)
i = 20
while 1:
    for j in factors:
        if i % j:
            break
    else:
        print i
        break
    i += 1
