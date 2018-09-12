import random, math

class Sample:
    def __init__(self, max):
        self.max = max
        self.n = 0
        self.sorted = False
        self.some = []

    def sample_inc(self, x):
        self.n = self.n + 1
        now = len(self.some)
        if now < self.max:
            self.sorted = False
            self.some.append(x)
        elif random.random() < now/self.n:
            self.sorted = False
            self.some[math.floor(random.random() * now)]
        return x

    def sample_sorted(self):
        if not self.sorted:
            self.sorted = True
            self.some.sort()
        return self.some

    def nth(self, n):
        s = self.sample_sorted()
        return s[min(len(s), max(0, math.floor(len(s)*n)))]

    def nths(self, ns=[0.1,0.3,0.5,0.7,0.9]):
        out = []
        for n in ns:
            out.append(self.nth(n))
        return out
