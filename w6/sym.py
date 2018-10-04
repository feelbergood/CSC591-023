import math

class Sym:
    def __init__(self, syms, f=lambda x:x):
        self.counts = {}
        self.mode = None
        self.most = 0
        self.n = 0
        self._ent = None
        self.syms = syms
        for s in self.syms:
            self.sym_inc(f(s))

    def sym_inc(self, x):
        if x == '?':
            return x
        self._ent = None
        self.n = self.n + 1
        old = self.counts.get(x, 0)
        new = old+1 if old else 1
        self.counts[x] = new
        if new > self.most:
            self.most, self.mode = new, x
        return x

    def sym_dec(self, x):
        self._ent = None
        self.n = self.n -1
        self.counts[x] = self.counts[x] - 1
        return x

    def sym_ent(self):
        if self._ent == None:
            self._ent = 0
            p = 0
            for _, val in self.counts.items():
                p = val / self.n
                self._ent = self._ent - p * math.log(p,2)
        return self._ent
