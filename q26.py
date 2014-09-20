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

print max(((i, reciprocal_cycle(d)) for i, d in enumerate(xrange(1, 1000), 1)),
          key=lambda j: j[1])[0]