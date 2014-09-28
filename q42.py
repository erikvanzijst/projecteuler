from itertools import count, takewhile


with open('p042_words.txt') as f:
    words = [sum(ord(c) - ord('A') + 1 for c in w) for w in
             (n.strip('"') for n in f.read().split(','))]

triangles = set(takewhile(lambda i: i <= max(words),
                          ((n + 1) * n / 2 for n in count(1))))
print sum(1 for c in words if c in triangles)
