from test_engine import O
from num import Num
from rows import rows
from sym import Sym
from dom import doms
import math, random

param_enough, param_margin = 0.5, 1.05
param_lo = 10**-32
param_hi = 10**32

def dump(a):
    for i in a:
        print("  ".join(str(r) for r in i))

def ksort(k, t):
    t = sorted(t, key=lambda x: str(x[k]))
    return t

def split(sds):
    sum, res = 0, 0
    for _, (n,sd) in sds.items():
        sum = sum + n
    for _, (n,sd) in sds.items():
        res = res + n/(sum+param_lo)*sd
    return res

def super(data, goal=None, enough=None):
    rows = data.rows
    sds = {}
    if goal is None:
        goal = len(rows[0])-1
    if enough is None:
        enough = len(rows)**param_enough

    def band(c, lo, hi):
        if lo == 1:
            return ".."+str(rows[hi][c])
        elif hi == most:
            return str(rows[lo][c])+".."
        else:
            return str(rows[lo][c])+".."+str(rows[hi][c])

    def argmin(c, lo, hi):
        cut = None
        xl,xr = Num([]), Num([])
        yl,yr = Num([]), Num([])
        for i in range(lo, hi+1):
            xr.num_inc(rows[i][c])
            yr.num_inc(rows[i][goal])
        bestx = xr.sd
        besty = yr.sd
        mu    = yr.mu
        n     = yr.n
        if (hi - lo > 2*enough):
            for i in range(lo, hi+1):
                x = rows[i][c]
                y = rows[i][goal]
                xl.num_inc(x)
                xr.num_dec(x) 
                yl.num_inc(y)
                yr.num_dec(y)
                if xl.n >= enough and xr.n >= enough:
                    tmpx = Num.num_xpect(data,xl,xr) * param_margin
                    tmpy = Num.num_xpect(data,yl,yr) * param_margin
                    if tmpx < bestx and tmpy < besty:
                        cut,bestx,besty = i, tmpx, tmpy
        return cut,mu,n,besty

    def cuts(c, lo, hi, pre):
        txt = pre+str(rows[lo][c])+".."+str(rows[hi][c])
        cut,mu,n,sd = argmin(c,lo,hi)
        if cut:
            print(txt)
            cuts(c,lo,   cut, pre+"|.. ")
            cuts(c,cut+1, hi, pre+"|.. ")
        else:
            s = band(c,lo,hi)
            sds[c] = {}
            sds[c][s] = (n, sd)
            print(txt+" = " + str(math.floor(100*mu)))
            for r in range(lo,hi+1):
                rows[r][c]=s

    def stop(c, t):
        for i in range(len(t)-1,-1,-1):
            if t[i][c] != "?":
                return i
        return 0

    for c in data.indeps:
        if c in data.nums:
            rows = ksort(c,rows)
            most = stop(c,rows)
            print("\n-- "+data.name[c]+" ----------")
            cuts(c,1,most,"|.. ")
    print("  ".join(str("%10s" % e) for e in data.name).replace(",",""))
    dump(rows)

    splitter =None, 
    min_sd = math.inf
    for c  in data.indeps:
        if c in data.nums:
            cur_sd = split(sds[c])
            if cur_sd < min_sd:
                min_sd = cur_sd
                splitter = data.name[c]
    print("Splitter is: " + splitter + " with expected standard deviation " + str(min_sd) + "\n")

def mainSuper(s):
    super(doms(rows(s)))

@O.k
def testWeatherLong():
    print("\nweatherLong.csv\n")
    mainSuper("data/weatherLong.csv")
@O.k
def testAuto():
    print("\nauto.csv\n")
    mainSuper("data/auto.csv")
