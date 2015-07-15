'''
Demos of tips, tricks, and other gotchas writing python code.

* Python doesn't have tail-call recursion optimiaztion (TCO), so recursive call
  stacks grow linearly with input size even when you can repeated do the
  calculation on the last stack frame. Guido explicitly specific this so that
  you can see full stack traces.

'''

#max positive (for python3) int val can be found out by:
import sys
print("max positive int value on this system:", sys.maxsize)
print(2 ** 65) #python3 internaly auto promotes int to long when int overflows.
print()



'''tricky syntax: create a 1 element tuple vs using parenthesis'''
will_eval_to_tuple = (1,)       #use the comma
will_eval_to_int = (1)          #no comma
print(type(will_eval_to_tuple))     #is a tuple
print(type(will_eval_to_int))       #is an int
print()



'''
floats are not exact, there is a small amount of "error".
so never compare floats for equality. instead, you
should check whether they are approximately equal.
'''
0.1 #python2.6 or eariler will eval to 0.10000000000000001

#another example
sum(0.1 for i in range(10)) == 1.0      #will return false

#check if approx equal (like in unittest module)
def almost_equal(x, y, places=7):
    return round(abs(x-y), places) == 0
almost_equal(sum(0.1 for i in range(10)), 1.0)

#for exact decimals use the deciaml module
from decimal import *
sum(Decimal("0.1") for i in range(10)) == Decimal("1.0")    #returns True
print()




'''
==================================================
seperate above and below examples
==================================================
'''


'''
Python functions are "first-class" meaning functions are also objects.
This leads to some interesting things that can be done in Python which can't
be done in Java. Which leads to map-reduce, map-fold.
'''
from math import sqrt, log

list_of_functions = [print, log, sqrt]  #built-n python functions.
data = 100

for func in list_of_functions:
    print("func name: %s result: %s" % (func, func(data)))

data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

def is_even(elmt):
    return (elmt%2) == 0
print("apply is_even() function to data:", end=' ')
map(is_even, data)                      #creates a map object, a generator.
print([i for i in map(is_even, data)])  #iterate map obj to get results.
print("filtering data through is_even():", end=' ')
filter(is_even, data)   #filter a func that takes a func, returns a generator.
print([i for i in filter(is_even, data)])   #iterate filter obj to get results.

print("apply sqrt() on data seq:", end=' ')
print([i for i in map(sqrt, data)])
print()

#zip() built-in returns a tuple where the i-th element comes from the i-th iterable argument
tupA = (1, 2, 3, 4, 5, 6)
tupB = ('a', 'b', 'c')
zip_obj = zip(tupA, tupB)
#zip_obj is <zip object at 0x7fdbafac>
print("zip example:")
for i in zip(tupA, tupB):
    print(i)
# output
#   (1, 'a')
#   (2, 'b')
#   (3, 'c')
print()



'''
==================================================
seperate above and below examples
==================================================
'''

'''
keys for dictionaries can only be hashable (b/c immutable) types: tuples, strs.
can't use mutable types like sets, lists, dicts for keys.

mutable types can used as values in dicts b/c they are allowed to modified.

src: http://stackoverflow.com/questions/8056130/immutable-vs-mutable-types-python
Immutable: python defines certain types as immutable.
numbers: int, float, complex
immutable sequences: str, tuples, bytes, frozensets

Mutable: everything else defaults to mutable.
mutable sequences: list, byte array
set type: sets
mapping type: dict
classes, class instances
etc.

And a trick is to use id() built-in function. For instance,

Using on integer:
>>> n = 1
>>> id(n)       #check id
**704
>>> n += 1      #modify
>>> n
2
>>> id(n)       #id changes because must create a new obj b/c original immutable
**736

Using on list:
>>> m = [1]
>>> id(m)       #check id
**416           
>>> m.append(2) #modify
>>> m
[1, 2]
>>> id(m)       #id remains the same, since internal contents were modified.
**416
'''

#tuples work because they are immutable (implies hashable).
#>>> {(1,2,3): 'a', (1,2): 'b'}             #tuples as keys will work.
#{(1, 2): 'b', (1, 2, 3): 'a'}

#same with strings                          #strings as keys will work.
#>>> {'1,2,3': 'a', '1,2': 'b'}
#{'1,2': 'b', '1,2,3': 'a'}

#>>> {3: 'a', 2: 'b'}                       #ints work too.
#{2: 'b', 3: 'a'}

#>>> {[1,2,3]: 'a', [1,2]: 'b'}             #trying to use list as key.
#Traceback (most recent call last):         #will raise exception/error.
#File "<stdin>", line 1, in <module>
#TypeError: unhashable type: 'list'

#>>> {set([1,2,3]): 'a', set([1,2]): 'b'}   #trying to use set as key.
#Traceback (most recent call last):
#File "<stdin>", line 1, in <module>
#TypeError: unhashable type: 'set'

#>>> {{1,2,3}: 'a', {1,2}: 'b'}}            #trying to use dict/set as key.
#Traceback (most recent call last):
#File "<stdin>", line 1, in <module>
#TypeError: unhashable type: 'set'





'''
==================================================
seperate above and below examples
==================================================
'''


'''
memebership lookup is faster for sets than lists b/c lookups are
CONSTANT for sets and LINEAR for lists.
'''
from random import randrange as randnum
my_list = [randnum(1000) for i in range(100)]
42 in my_list   #is num 42 in the list?

#convert list to set to have faster lookup.
my_set = set(my_list)
42 in my_set    #is num 42 in the list?
print()

'''
constant for sets matters when you are checking and adding to it
if you did this with a list, it would be quadratic runtime, whereas
for a set would be linear.
'''


'''
==================================================
seperate above and below examples
==================================================
'''

'''
append() vs extend()
src: http://stackoverflow.com/questions/252703/python-append-vs-extend
'''
#append: Appends object at end
x = [1, 2, 3]
x.append([4, 5])
print(x)        #gives you: [1, 2, 3, [4, 5]]

#extend: extends list by appending elements from the iterable
x = [1, 2, 3]
x.extend([4, 5])
print(x)        #gives you: [1, 2, 3, 4, 5]
print()


'''
furthermore, extend() a list is more efficient (fast) than append()
since strings are immutable (can't be changed one they are created,
this is analogous to the String() & '+' vs StringBuilder() in Java.
even though lists are mutable, they behave like immutable when appending.
'''
my_list=["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
results = []
for item in my_list:
    results.extend(item)

'''
demoing inefficient (you can get away with it for small input b/c of internal optimizations b/c appending allows you to overallocate with a percentage so that the available space grows exponentially, and the append() cost is constant when averaged (amortized) over all the operations.)
'''
#my_list=["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
my_string = ""
for item in my_list:
    my_string += item   #BAD! the += operator creates a new string everytime

#slightly better
my_items = []
for item in my_list:
    my_items.append(item)
my_string = ''.join(my_items)

#condensing above code (still bad)
my_string = ''.join(my_list)

#VERY BAD
my_list=[["the", "quick"], ["brown", "fox", "jumps"], ["over"], ["the", "lazy", "dog"]]
results = sum(my_list, [])  #same as sum(my_str, '') == sum(my_strs, ''.join())
#b/c under the covers sum() doesn't know what you are summing and has to
#do additions one after another, meaning you get the analogous below
#behavior with strings.
#sum() on strings is concatenation (i.e. +=)


'''list comprehension'''
#print("list comp ex1:", [[i for j in range(5)] for i in range(10)])
# how efficient is list comprehension? i dont know.
# is it just 2 nested for loops?
# are there some optimziations under the hood?
# how well does it scale?

# action for i in outerloop for j in innerloop
#print("list comp ex2:", [(i, j) for i in range(5) for j in range(10)])

# equivalent to above
#lst = []
#for i in range(5):
    #for j in range(10):
        #lst.append((i, j))
#print("equivalent:", lst)

# list of (x, y, z) 3d coordinatese
#print("list comp ex3:", [(x,y,z) for x in range(2) for y in range(3) for z in range(5)])

#using dict comprehension to reverse/inverse a dict/map available in v2.7+/3+
m = {'a':1, 'b':'2', 'c':3, 'd':(3,1), 'e':'0' }
inv_m = dict((v,k) for k,v in m.items()) #or inv_m = {v:k for k,v in m.items()}
print("inverse:", inv_m)

'''
#for-loop syntactic sugar:
for x in ..a..:
    ..code..

#turns into

my_iter = iter(..a..)
while (my_iter is not empty):
    x = my_iter.next()
    ..code..
'''


'''
==================================================
seperate above and below examples
==================================================
'''

'''
creating own iterable class
src: https://wiki.python.org/moin/ForLoop
'''

class Iterable(object):
    def __init__(self,values):
        self.values = values
        self.location = 0

    def __iter__(self):
        return self

    def next(self):
        if self.location == len(self.values): raise StopIteration

        value = self.values[self.location]
        self.location += 1
        return value

'''
creating (inefficent) range generator from scratch.
python's range() under the hood is MUCH MUCH more efficient. allowing for
constant 'memebership check' runtime regardless of the size of input.
(i.e. '99 in range(100)' is as fast as '99999999 in range(1000000000)')
further reading:
http://stackoverflow.com/questions/30081275/why-is-1000000000000000-in-range1000000000000001-so-fast-in-python-3
http://stackoverflow.com/questions/102535/what-can-you-use-python-generator-functions-for

this is because range() isn't a generator it is a sequence obj like list obj.
the difference between a range and a list is that a range is a LAZY or DYNAMIC sequence; it DOESN'T REMEMBER ALL OF ITS VALUES, it just remembers its start, stop, and step, and creates the values on demand on __getitem__.
'''
import timeit
def my_inefficent_range(start, end, step=1):
    while start <= end:
        yield start     #yield keyword is the thing that makes it generator.
        start += step

#for functions you define, you can pass setup parameter.
time_own = timeit.timeit("10 in my_inefficent_range(0, 11)", setup="from __main__ import my_inefficent_range")
time_python = timeit.timeit("10 in range(0, 11)")
print("own:", time_own, "python:", time_python)
time_own = timeit.timeit("100 in my_inefficent_range(0, 101)", setup="from __main__ import my_inefficent_range")
time_python = timeit.timeit("100 in range(0, 101)")
print("own:", time_own, "python:", time_python)
print("time_python (checking if element in range object) should be about CONSTANT same time even though 10x increase in input size, time_own (using for-loop and yield) should be LINEAR with input size.\n")
#runtimes: note that checking membership is near constant with python's range()
#and LINEAR with your own inefficient range function.
#own: 3.2441859245300293 python: 0.8330478668212891
#own: 25.80547595024109 python: 0.8650491237640381



#this is the wrong approach, we don't have want to have to iterate over
#all the elements. if we do then runtime is linear with input size regardless
#of how fast we can check memebership in range()/my_range().
#as implied by the timing data.
#time_own = timeit.timeit("for x in my_inefficent_range(1, 100): pass", setup="from __main__ import my_inefficent_range")
#time_python = timeit.timeit("for x in range(1, 100): pass")
#print("own:", time_own, "python:", time_python)
#print("both time_python and time_own should iterate 'for x in range(): pass' at linear with input size")
#run1
#own: 2.7101550102233887 python: 0.9570538997650146
#own: 22.949312925338745 python: 3.2081828117370605
#own: 243.6319351196289 python: 44.67555594444275
#run2
#own: 2.855163097381592 python: 0.8890509605407715
#own: 23.555346965789795 python: 3.5112011432647705
#own: 236.8995499610901 python: 45.933626890182495



#calling/invoking fucntions my_inefficent_range() and range() are constant.
time_own = timeit.timeit("my_inefficent_range(0, 101)", setup="from __main__ import my_inefficent_range")
time_python = timeit.timeit("range(0, 101)")
print("own:", time_own, "python:", time_python)
print("calling/invoking fucntions my_inefficent_range() and range() are constant.\n")
#runtimes
#own: 0.5690329074859619 python: 0.6820387840270996
#own: 0.5380301475524902 python: 0.6560380458831787
#own: 0.6080348491668701 python: 0.8090457916259766





'''
==================================================
seperate above and below examples
==================================================
'''

'''
what is metaclass?
more info:
    stackoverflow.com/questions/100003/what-is-a-metaclass-in-python
'''
