def step(head, tail, controller):
    if not tail:
        controller.offer(head)
        if controller.stop():
            return False
    else:
        for i in range(len(tail)):
            if not step(head + [tail[i]], tail[:i] + tail[i+1:], controller):
                return False
    return True


class Controller(object):
    def __init__(self, max):
        self.max = max
        self.values = []

    def offer(self, value):
        self.values.append(value)

    def stop(self):
        return len(self.values) >= self.max

c = Controller(1000000)
step([], range(10), c)
print ''.join(str(i) for i in c.values[-1])
