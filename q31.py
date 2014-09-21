from itertools import count, takewhile


def perms(target=200, coins=(), val=0, denom=(200, 100, 50, 20, 10, 5, 2, 1),
          results=None):
    if val == target:
        results = results if results else []
        results.append(coins)
    elif val <= target and denom:
        for j in takewhile(lambda i: val + i * denom[0] <= target, count()):
            results = perms(target, (coins or []) + j * [denom[0]],
                            val + j * denom[0], denom[1:], results)
    return results

print len(perms())
