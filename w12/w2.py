import re,traceback

DATA1 ="""
outlook,$temp,?humidity,windy,play
sunny,85,85,FALSE,no
sunny,80,90,TRUE,no
overcast,83,86,FALSE,yes
rainy,70,96,FALSE,yes
rainy,68,80,FALSE,yes
rainy,65,70,TRUE,no
overcast,64,65,TRUE,yes
sunny,72,95,FALSE,no
sunny,69,70,FALSE,yes
rainy,75,80,FALSE,yes
sunny,75,70,TRUE,yes
overcast,100,90,TRUE,yes
overcast,81,75,FALSE,yes
rainy,71,91,TRUE,no"""

DATA2 ="""
    outlook,   # weather forecast.
    $temp,     # degrees farenheit
    ?humidity, # relative humidity
    windy,     # wind is high
    play       # yes,no
    sunny,85,85,FALSE,no
    sunny,80,90,TRUE,no
    overcast,83,86,FALSE,yes

    rainy,70,96,FALSE,yes
    rainy,68,80,FALSE,yes
    rainy,65,70,TRUE,no
    overcast,64,

                  65,TRUE,yes
    sunny,72,95,FALSE,no
    sunny,69,70,FALSE,yes
    rainy,75,80,FALSE,yes
          sunny,
                75,70,TRUE,yes
    overcast,100,90,TRUE,yes
    overcast,81,75,FALSE,yes # unique day
    rainy,71,91,TRUE,no"""

class O:
    y=n=0
    @staticmethod
    def report():
        print("\n# pass= %s fail= %s %%pass = %s%%"  % (
            O.y,O.n, int(round(O.y*100/(O.y+O.n+0.001)))))

    @staticmethod
    def k(f):
        try:
            print("\n-----| %s |-----------------------" % f.__name__)
            if f.__doc__:
                print("# "+ re.sub(r'\n[ \t]*',"\n# ",f.__doc__))
            f()
            print("# pass")
            O.y += 1
        except:
            O.n += 1
            print(traceback.format_exc()) 
        return f

def lines(s):
    "Return contents, one line at a time."
    return s.splitlines()

def rows(src):
    """Kill bad characters. If line ends in ',' 
    then join to next. Skip blank lines."""
    my_list = []
    # Kill bad characters(comments here) and skip blank spaces
    for line in src:
        my_list.append(line.split('#', 1)[0].strip())
    # Join to next if endswith ','
    i = 0
    while i < len(my_list)-1:
        if my_list[i].endswith(','):
            my_list[i] += my_list.pop(i+1)
        else:
            i += 1
    # Remove empty lines
    my_list = list(filter(None, my_list))
    return my_list

def cols(src):
    """ If a column name on row1 contains '?', 
    then skip over that column."""
    result = []
    skip_cols = []
    for index, col in enumerate(src[0].split(',')):
        if col.find('?') > -1:
            skip_cols.append(index)
    for row in src:
        row_list = row.split(',')
        for skip_col in skip_cols:
            del row_list[skip_col]
        result.append(row_list)
    return result

def prep(src):
    """ If a column name on row1 contains '$', 
    coerce strings in that column to a float."""
    result = []
    float_cols = []
    for index, col in enumerate(src[0]):
        if col.find('$') > -1:
            float_cols.append(index)
    for row in src:
        for float_col in float_cols:
            float_col = float(float_col)
        result.append(row)
    return result

def ok0(s):
    for row in prep(cols(rows(lines(s)))):
        print(row)

@O.k
def ok1(): ok0(DATA1)

@O.k
def ok2(): ok0(DATA2)
