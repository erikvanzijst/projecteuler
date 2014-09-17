import sys

s = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""


class Node(object):
    def __init__(self, cost, children=()):
        self.children = children
        self._cost = cost
        self._most_expensive_path = None

    def get_cost(self):
        if not self.children:
            return self._cost
        if self._most_expensive_path is None:
            self._most_expensive_path = max(c.get_cost() for c in self.children)
        return self._most_expensive_path + self._cost

    def __str__(self):
        return str(self._cost)


def print_graph(node):
    seen = set()
    todo = [node]
    prev_line_length, count = 0, 0
    while todo:
        n = todo.pop(0)
        if n not in seen:
            seen.add(n)
            count += 1
            sys.stdout.write('%d ' % n._cost)
            todo += n.children
            if count > prev_line_length:
                prev_line_length = count
                count = 0
                sys.stdout.write('\n')


nodes = []
for l in s.splitlines()[::-1]:
    nodes = [Node(int(num), nodes[i:i+2]) for i, num in enumerate(l.split())]

print_graph(nodes[0])
print nodes[0].get_cost()
