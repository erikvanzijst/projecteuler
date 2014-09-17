class Node(object):
    def __init__(self, cost, children=()):
        self.children = children
        self._cost = cost
        self._best_path = None

    def get_cost(self):
        if not self.children:
            return self._cost
        if self._best_path is None:
            self._best_path = max(c.get_cost() for c in self.children)
        return self._best_path + self._cost

with open('p067_triangle.txt') as f:
    nodes = []
    for l in f.readlines()[::-1]:
        nodes = [Node(int(num), nodes[i:i+2]) for i, num in enumerate(l.split())]

print nodes[0].get_cost()
