import re,traceback

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

# Page 5
@O.k
def test5():
    """Whitespace Formatting"""
    product = (1 * 2 * 3)
    assert product == 6

# Page 6
@O.k
def test6():
    """Modules"""
    from math import ceil
    num = ceil(2.7)
    assert num == 3

# Page 7
@O.k
def test7():
    """Arithmetic"""
    num = 1 / 5
    assert num == 0.2

# Page 8
@O.k
def test8():
    """Functions"""
    def sum(a, b):
        return a + b
    num = sum(1,1)
    assert num == 2

# Page 9
@O.k
def test9():
    """Strings"""
    str = "\t"+r"\t"
    assert len(str) == 3

# Page 10
@O.k
def test10():
    """Exceptions"""
    try:
        print(num=2)
    except TypeError:
        error = "'=' should be '=='"
    assert error == "'=' should be '=='"

# Page 11
@O.k
def test11():
    """Lists"""
    x = [0,1,2]
    x.extend([3,4,5])
    y = x+[6,7,8]
    y.append(9)
    assert y[-1]==9

# Page 12
@O.k
def test12():
    """Lists Cont"""
    my_list = [1,2]
    _, y = my_list
    assert y==2

# Page 13
@O.k
def test13():
    """Tuples"""
    def swap_sum_and_product(x, y):
        a, b = (x+y), (x*y)
        a, b = b, a
        return a, b
    my_tuple = swap_sum_and_product(2, 3)
    assert my_tuple[0] == 6
    assert my_tuple[1] == 5

# Page 14
@O.k
def test14():
    """Dictionaries"""
    account_info = {
        "username": "john doe",
        "email": "123@ncsu.edu",
        "hashtag": ["#student", "#csc591"]
    }
    num_hashtag = len(account_info["hashtag"])
    assert num_hashtag == 2

# Page 15
@O.k
def test15():
    """defaultdict"""
    from collections import defaultdict

    counts = {}
    dd_counts = defaultdict(int)
    
    def isDefaultDict(dict):
        try:
            dict[2] += 1
            return True
        except KeyError: 
            return False   

    assert isDefaultDict(counts) == False
    assert isDefaultDict(dd_counts) == True

# Page 16
@O.k
def test16():
    """Counter"""
    from collections import Counter

    document = ["who", "am", "I", "I", "am", "me"]
    word_counts = Counter(document)

    assert word_counts["am"] == 2

# Page 17
@O.k
def test17():
    """Sets"""
    words_list = ["a", "a", "b", "c", "c", "c"]
    words_set = set(words_list)

    assert ("a" in words_set) == True
    assert len(words_set) == 3

# Page 18
@O.k
def test18():
    """Control Flow"""
    count_two = 0
    count_three = 0
    count_other = 0
    for x in range(10):
        if x%3 == 0:
            count_three+=1
        elif x%2 == 0:
            count_two+=1
        else:
            count_other+=1
    assert count_two == 3
    assert count_three == 4
    assert count_other == 3

# Page 19
@O.k
def test19():
    """Truthiness"""
    str = "This is a string"
    non = None
    assert non or str[0] == "T"
    assert str and str[0] == "T"

# Page 20
@O.k
def test20():
    """Truthiness Cont"""
    assert all([None, 1, [2, "test"]]) == False
    assert any([None, 1, [2, "test"]]) == True

# Page 22
@O.k
def test22():
    """Sorting"""
    my_list = [-5, 12, -3, 6, -7]
    sorted_my_list = sorted(my_list, key=abs, reverse=True)
    assert sorted_my_list == [12, -7, 6, -5, -3]

# Page 23
@O.k
def test23():
    """List Comprehensions"""
    my_dict = {x: x+x for x in range(3)}
    my_set = {x for x in [1, 1, 1, 3, 2, 2]}
    decreasing_pairs = [(x, y)
                        for x in range(3)
                        for y in range(1, x)]
    assert my_dict == {0:0, 1:2, 2:4}
    assert my_set == {1, 3, 2}
    assert decreasing_pairs == [(2, 1)]

# Page 24
@O.k
def test24():
    """Generators and Iterators"""
    import types

    def lazy_odds(n):
        i = 1
        while i < n:
            yield i
            i += 2
    
    lazy_range_comprehensions = (x for x in range(10))

    assert isinstance(lazy_odds(10), types.GeneratorType)
    assert isinstance(lazy_range_comprehensions, types.GeneratorType)

# Page 25
@O.k
def test25():
    """Randomness"""
    import random

    random.seed(5)
    rand1 = random.random()
    random.seed(5)
    rand2 = random.random()
    assert rand1 == rand2
    assert random.randrange(3,6) < 6

# Page 26
@O.k
def test26():
    """Regular Expression"""
    import re
    assert all([
        not re.match("b", "abc"),
        re.search("not", "not me"),
        4 == len(re.split("[Ee]", "Regular Expression")),
        "NBAK" == re.sub("[0-9]", "", "NBA2K18")
    ])

# Page 27
@O.k
def test27():
    """Object-Oriented Programming"""
    class Rectangle:
        def __init__(self, width=1, height=1):
            self.width = width
            self.height = height
        def __repr__(self):
            return "Rectangle with width = "+self.width+" and height = "+self.height
        def calcArea(self):
            return self.width*self.height

    rec = Rectangle(3, 4)
    area = rec.calcArea()
    assert area == 12

# Page 28
@O.k
def test28():
    """Functional Tools"""
    from functools import partial
    
    def divide(a, b):
        return a/b
    
    divide_2 = partial(divide, 2)
    divide_by_2 = partial(divide, b=2)
    assert divide_2(1) == 2
    assert divide_by_2(6) == 3

# Page 29
@O.k
def test29():
    """Functional Tools --- map, reduce, filter"""
    from functools import reduce 

    def square(x):
        return x*x
    
    def is_even(x):
        return x%2 == 0

    my_list = [1, 2, 3]
    my_list_squared = map(square, my_list)
    my_list_squared_even = filter(is_even, my_list_squared)
    my_list_squared_even_sum = reduce(lambda x, y: x+y, my_list_squared_even)
    assert my_list_squared_even_sum == 4

# Page 30
@O.k
def test30():
    """enumerate"""
    xs = [1, 4, 9, 16]
    sum_index = 0
    sum_value = 0
    for i, x in enumerate(xs):
        sum_index += i
        sum_value += x
    assert [sum_index, sum_value] == [6, 30]

# Page 31
@O.k
def test31():
    """zip and Argument Unpacking"""
    list1 = [1, 2, 3]
    list2 = ["Tyrion", "Sansa", "Jon Snow"]
    list3 = [(1, "Tyrion"), (2, "Sansa"), (3, "Jon Snow")]
    assert list(zip(list1, list2)) == list3
    assert list(zip(*list3)) == [tuple(list1), tuple(list2)]

# Page 32
@O.k
def test32():
    """args and kwargs"""
    def repeat(f):
        def g(*args):
            return f(*args)+f(*args)
        return g

    def concat_str(s1, s2, s3):
        return s1+s2+s3
    
    test_function = repeat(concat_str)
    assert test_function("Python", "Hello", "World") == "PythonHelloWorldPythonHelloWorld"

# Page 33
@O.k
def test33():
    """args and kwargs cont"""
    books = {"Introdution to Algorithms": 160,
            "Database System": 150}
    
    def add_books(**kwargs):
        books.update(kwargs)

    new_books = {"Computer Networks": 175,
                "Chinese History": 155}
    new_books2 = {"Computer Architecture": 185}
    add_books(**new_books)
    add_books(**new_books2)
    assert books["Computer Networks"] == 175

if __name__== "__main__":
    O.report()