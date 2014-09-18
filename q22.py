with open('p022_names.txt') as f:
    names = sorted(n.strip('"') for n in f.read().split(','))
    print sum(sum(ord(c) - ord('A') + 1 for c in name) * (names.index(name) + 1)
              for name in names)
