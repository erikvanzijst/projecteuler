import hashlib


def fractions(b):
    a = 1
    while a:
        a = (a % b) * 10
        yield a / b


def reciprocal_cycle(b):
    a = 1
    nums = []
    while a and a not in nums:
        nums.append(a)
        a = (a % b) * 10
    if a in nums:
        return len(nums) - nums.index(a)

d = max(((i, reciprocal_cycle(d)) for i, d in enumerate(xrange(1, 1000), 1)),
        key=lambda j: j[1])[0]
assert ('6aab1270668d8cac7cef2566a1c5f569' ==
        hashlib.md5(str(d)).hexdigest()), 'Wrong answer'
print d