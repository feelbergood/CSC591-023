from test_engine import O
from sample import Sample
from sym import Sym
from num import Num
import random

@O.k
def sample_test():
    random.seed(1)
    s = []
    
    for i in range(5, 10):
        s.append(Sample(2**i))

    for i in range(1, 10000):
        y = random.random()
        for t in s:
            t.sample_inc(y)

    for t in s:
        print(t.max, t.nth(0.5)) 
        assert abs(t.nth(0.5)-0.5) < 0.2

@O.k
def num_test():
    n = Num([4,10,15,38,54,57,62,83,100,100,174,190,215,225,
       233,250,260,270,299,300,306,333,350,375,443,475,
       525,583,780,1000])

    print(n.mu, n.sd)
    assert abs(n.mu - 270.3) < 0.01
    assert abs(n.sd - 231.946) < 0.01

@O.k
def sym_test():
    s = Sym(['y','y','y','y','y','y','y','y','y',
	        'n','n','n','n','n'])
    print(s.sym_ent())
    assert abs(s.sym_ent() - 0.9403) < 0.0001