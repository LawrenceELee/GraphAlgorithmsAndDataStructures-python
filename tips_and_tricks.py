'''
Demos of tips and tricks using python syntax.

'''


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
extend() a list is more efficient (fast) than append()
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


#how efficient is list comprehension?
[[j for j in range(5)] for i in range(10)]
#is it just 2 nested for loops?
#are here some optimziations?
#how well does it scale?
