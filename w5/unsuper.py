from num import Num
from sym import Sym
from rows import Data, rows
from test_engine import O
import re, sys, random, math

param_enough = 0.5
param_margin = 1.05

def dump(a):
    for i in a:
        print("\t".join(str(r) for r in i))

def ksort(k, t):
    t = sorted(t, key=lambda x: str(x[k]))
    return t

def unsuper(data):
    rows = data.rows
    enough = len(rows)**param_enough

    def band(c, lo, hi):
        if lo == 0:
            return ".."+str(rows[hi][c])
        elif hi == most:
            return str(rows[lo][c])+".."
        else:
            return str(rows[lo][c])+".."+str(rows[hi][c])

    def argmin(c, lo, hi):
        cut = None
        if (hi-lo > 2*enough):
            l = Num([])
            r = Num([])
            for i in range(lo,hi+1):
                r.num_inc(rows[i][c])
            best = r.sd
            for i in range(lo,hi+1):
                x = rows[i][c]
                l.num_inc(x)
                r.num_dec(x)
                if l.n >= enough and r.n >= enough:
                    tmp = Num.num_xpect(data, l, r) * param_margin
                    if tmp < best:
                        cut, best = i, tmp
        return cut

    def cuts(c, lo, hi, pre):
        txt = pre + str(rows[lo][c])+".. "+str(rows[hi][c])
        cut = argmin(c, lo, hi)
        if cut:
            print(txt)
            cuts(c, lo, cut, pre + "|.. ")
            cuts(c, cut+1, hi, pre + "|.. ")
        else:
            b = band(c,lo,hi)
            print(txt + " (" + b + ")")
            for r in range(lo,hi+1):
                rows[r][c]=b

    def stop(c, t):
        for i in range(len(t)-1, -1, -1):
            if t[i][c] != "?":
                return i
        return 0

    for c in data.indeps:
        if c in data.nums:
            rows = ksort(c, rows)
            most = stop(c, rows)
            print("\n-- "+data.name[c]+": "+str(most)+"----------")
            cuts(c, 0, most, "|..")
    print(", ".join(data.name).replace("$",""))
    dump(rows)

def mainUnsuper(s):
    unsuper(rows(s))

@O.k
def test():
    print("\nweatherLong.csv\n")
    mainUnsuper("weatherLong.csv")
