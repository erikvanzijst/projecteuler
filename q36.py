def bits(i):
    while i:
        yield i & 0x1
        i >>= 1


def decimals(i):
    while i:
        yield i % 10
        i /= 10


def is_palindrome(items):
    for j in range(len(items) / 2):
        if items[j] != items[-(j + 1)]:
            return False
    return True


print sum(n for n in xrange(1, 1000000) if (is_palindrome(tuple(decimals(n)))
                                            and is_palindrome(tuple(bits(n)))))
