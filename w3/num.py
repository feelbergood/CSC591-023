from sample import Sample
import math

class Num:
    def __init__(self, nums, f=lambda x:x):
        self.max = len(nums)
        self.n=0
        self.mu=0
        self.m2=0
        self.sd=0 
        self.lo=10**32 
        self.hi=-10**32 
        self.some=Sample(self.max)
        self.w=1
        for n in nums:
            self.num_inc(f(n))

    def num_inc(self,x):
        if x == "?":
            return x
        self.n  = self.n + 1
        self.some.sample_inc(x)
        d = x - self.mu
        self.mu = self.mu + d/self.n
        self.m2 = self.m2 + d*(x - self.mu)
        self.hi = max(self.hi, x)
        self.lo = min(self.lo, x)
        if (self.n>=2):
            self.sd = (self.m2/(self.n - 1 + 10**-32))**0.5
        return x 

    def num_dec(self, x):
        if x == "?":
            return x
        if self.n == 1:
            return x
        self.n = self.n - 1
        d = x - self.mu
        self.mu = self.mu - d/self.n
        self.m2 = self.m2 - d*(x-self.mu)
        if self.n >= 2:
           self.sd = (self.m2/(self.n - 1 + 10**-32))**0.5
        return x
    
    def num_norm(self, x): 
        return 0,5 if x=="?" else (x-self.lo)/(self.hi-self.lo + 10**-32)

    def num_xpect(self, i, j):
        n = i.n + j.n + 0.0001
        return i.n/n * i.sd+ j.n/n * j.sd
