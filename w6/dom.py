from num import Num
from sym import Sym
from rows import Data, rows
from test_engine import O
import re, sys, random, math

samples = 100

def cap(x, lo, hi):
    return min(max(lo,x), hi)

def dump(rows):
    for row in rows:
        row[len(row)-1] = str("%.2f"%row[len(row)-1])
        # print("\t".join(str(r) for r in row))

def another(r, rows):
    ar = cap(math.floor(random.random()*len(rows)),0,len(rows)-1)
    if r == ar:
        return another(r, rows)
    else:
        return rows[ar]
    return another(r, rows)

def dom(data, row1, row2):
    s1 = 0
    s2 = 0
    n = len(data.w)
    for c, w in data.w.items():
        a0 = row1[c]
        b0 = row2[c]
        a = data.nums[c].num_norm(a0)
        b = data.nums[c].num_norm(b0)
        s1 = s1 - 10 ** (w * (a-b)/n)
        s2 = s2 - 10 ** (w * (b-a)/n)
    return s1/n < s2/n

def doms(data):
    n = samples
    c = len(data.name)
    # print("\t".join(data.name)+"\t>dom")
    for r1, row1 in enumerate(data.rows):
        row1.append(0)
        for i in range(n):
            row2 = another(r1, data.rows)
            s = dom(data, row1, row2) and 1/n or 0
            row1[c] = row1[c] + s
    dump(data.rows)
    return data

def mainDom(csv):
    doms(rows(csv))