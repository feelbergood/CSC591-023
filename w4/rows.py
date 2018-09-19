from num import Num
from sym import Sym
from test_engine import O
import re, sys

class Data:
    
    def __init__(self):
        self.w = {}
        self.syms = {}
        self.nums = {}
        self._class = None
        self.rows = []
        self.name = []
        self._use = []
        self.indeps = []

    def indep(self, c):
        return not c in self.w and self._class!=c

    def dep(self, c):
        return not self.indep(c)

    def header(self, cells):
        for c0, x in enumerate(cells):
            if not "?" in x:
                c = len(self._use)
                self._use.append(c0)
                self.name.append(x)
                if re.search("[<>$]", x):
                    self.nums[c] = Num([])
                else: 
                    self.syms[c] = Sym([])
            if re.search("<", x):
                self.w[c] = -1
            elif re.search(">", x):
                self.w[c] = 1
            elif re.search("!", x):
                self._class = c
            else:
                self.indeps.append(c)
        return self

    def row(self, cells):
        r = len(self.rows)
        self.rows.append([])
        for c, c0 in enumerate(self._use):
            x = cells[c0]
            if x != "?":
                if c in self.nums:
                    try: 
                        x = int(x)
                    except ValueError:
                        x = float(x)
                    self.nums[c].num_inc(x)
                else:
                    self.syms[c].sym_inc(x)
            self.rows[r].append(x)
        return self

def lines(src=None):
    if src == None:
        for line in sys.stdin:
            yield line
    elif src[-3:] in ["csv", ".dat"]:
        with open(src) as fs:
            for line in fs:
                yield line
    else:
        for line in src.splitlines():
            yield line

def rows1(src):
    data = Data()
    first = True
    for line in src:
        line = re.sub(r'([\n\r\t]|#.*)', "", line)
        cells = line.split(",")
        if len(cells) > 0 and cells[0] != "":
            if first: 
                data.header(cells)
            else: 
                data.row(cells)
            first = False
    print("\t\t\t\t\t\tn\tmode\tfrequency")
    for k,v in data.syms.items():
        print(f'{k+1}\t{data.name[k]}\t{v.n}\t{v.mode}\t{v.most}')
    print("\n\t\t\t\t\t\tn\tmu\tsd")
    for k,v in data.nums.items():
        print(f'{k+1}\t{data.name[k]}\t{v.n}\t{v.mu:.2f}\t{v.sd:.2f}')
    return data


def rows(src):
    return rows1(lines(src))

@O.k
def testRows():
    print("\nweather.csv,")
    rows("weather.csv")
    print("\nweatherLong.csv,")
    rows("weatherLong.csv")
    print("\nauto.csv,")
    rows("auto.csv")
    