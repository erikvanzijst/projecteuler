def decimals(i):
    while i > 0:
        yield i % 10
        i /= 10


def is_palindrome(i):
    nums = list(decimals(i))
    for j in range(len(nums) / 2):
        if nums[j] != nums[-(j + 1)]:
            return False
    return True


def palindromes(low, high):
    for i in xrange(low, high):
        for j in xrange(low, high):
            if is_palindrome(i * j):
                yield i, j, i * j

print max(palindromes(100, 1000), key=lambda tup: tup[2])
