'''
Explaination of dynammic programming (DP).

DP is a way to solve a group of problems.
In this context, "programming" refers to making a set of changing (dynamic) choices. Analogous to linear programming where you "walk" along a (linear) path making a set of choices.

1) memoization (caching) recursion (e.g caching fibonacci numbers).
2) relaxtion iteration (i.e. Dijkstra's algorithm).

DP is an extension of greedy algorithm paradigm (pick the best choice at this
current moment, e.g. kruskal, prim) but instead DP picks the best choice in
the context of future choices down the line.

At its core, DP is just a normal recursive/inductive function, but because
there are overlapping subproblems (unnesscessary repeated work) we can can
cache the results. This means that even for exponential input, we can trim away
the ineffciencies (repeated work) and get a solution in "reasonable" time.
This is referred to as top-down DP.

We can translate top-down DP into an iterative version, and filling out some data structure (such as a multidimensional array) step by step.
This is referred to as bottom-up DP.

Another option is to implement the recursive formulation directly but to cache
the return values. If a call is made more than once with the same arguments,
the result is simply returned directly from the cache.
This is called memoization.

progression:
(naive recursive fibonacci -> recursive fib w/ memo (cache) -> convert rec
fib to iterative fib with cache).
Fibonacci just fills in a 1d array, but there are other problems that require
multidimensional arrays.
other examples: longest increasing subsequence.
some languages (like python) have decorators (which are?)

DP can been model as a DAG (directed acyclic graph).
For Iterative version, you also have two choices: you can relax the edges out of each node (in topologically sorted order), or you can relax all edges into each node. The latter more obviously yields a correct result but requires access to nodes by following edges backward. This isn't as far-fetched as it seems when you're working with an implicit DAG in some nongraph problem. For example, the longest increasing subsequence problem, looking at all backward "edges" can be a useful perspective.

'''

import timeit



def fib_naive(N):
    '''
    Canonical recursive naive fib function.

    Very inefficient because fib(4) is needlessly recalculated
    when on fib(N), where N > 4 (i.e. over-lapping subproblems).

    runtime: O(2^N) b/c each problem is divided into 2 sub-problems.
    it might actually be worst thatn 2^N since you do unessceasary repeated
    work.

    first 20 fib nums, with seeds f(0)=0, f(1)=1
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597,
    2584, 4181, 6765
    '''

    #refactored old version code into more concise version, but doesn't
    #account for negative N's.
    if N < 2:       return N
    else:           return fib_naive(N-1) + fib_naive(N-2)

    '''
    #old version, more verbose, but accounts for negative N's.
    if N <= 0:          #base case 1
        return 0
    elif N == 1:        #base case 2
        return 1
    else:
        return fib_naive(N-1) + fib_naive(N-2)
    '''
def test_fib_naive():
    print("\nrunning test_fib_naive...")
    print("fib_naive(0) =", fib_naive(0))
    print("fib_naive(1) =", fib_naive(1))
    print("fib_naive(2) =", fib_naive(2))       #should equal 1
    print("fib_naive(3) =", fib_naive(3))       #should equal 2
    print("fib_naive(4) =", fib_naive(4))       #should equal 3
    print("fib_naive(10) =", fib_naive(10))     #should equal 55
    print("fib_naive(15) =", fib_naive(15))     #should equal 610
    print("fib_naive(20) =", fib_naive(20))     #should equal 6765
    #print("fib_naive(25) time:", timeit.timeit("fib_naive(25)", setup="from __main__ import fib_naive"))
    print("will start running into performance problems starting around fib_naive(21)") #fib(21) is really inefficient and slow





def memo(func):
    cache = {}          #hash to store prev calc results (sub-problems).
    #"wrap" the memo/caching function around whatever func is passed in.
    #and return it.

    def _memo(*args):                   #memoized wrapper
        if args not in cache:           #not already computed?
            cache[args] = func(*args)   #compute and cache soln.
        return cache[args]              #return cached solun.
    return _memo


'''
#this syntax wasn't memoizing the function. don't know why, so switched syntax.
def fib_memo(N):
    #memo is function that wraps (decorates) other functions.
    #it takes a function as input, and returns a function as output.
    fib_wrapped_with_memo = memo(fib_naive)
    return fib_wrapped_with_memo(N)
    #return memo(fib_naive)     #is not the same, it doesn't evaluate with args.
'''
@memo       #'@' is syntax to decorate fib_memo() with memo()
def fib_memo(N):
    '''
    A clone/copy of fib that we can memoize.
    '''
    if N < 2:       return N
    else:           return fib_memo(N-1) + fib_memo(N-2)
def test_fib_memo():
    print("\nrunning test_fib_memo...")
    print("fib_memo(0) =", fib_memo(0))
    print("fib_memo(1) =", fib_memo(1))
    print("fib_memo(2) =", fib_memo(2))     #should equal 1
    print("fib_memo(3) =", fib_memo(3))     #should equal 2
    print("fib_memo(4) =", fib_memo(4))     #should equal 3
    print("fib_memo(10) =", fib_memo(10))   #should equal 55
    print("fib_memo(15) =", fib_memo(15))   #should equal 610
    print("fib_memo(20) =", fib_memo(20))   #should equal 6765
    print("now, can even quickly calculate fib_memo(100) =", fib_memo(100))
    #should be 354224848179261915075
    print("fib_memo(100) time:", timeit.timeit("fib_memo(100)", setup="from __main__ import fib_memo"))





def fib_iter(N):
    '''
    Convert recurisve memo fib to iterative.
    '''
    cache = {0: 0, 1: 1}        #seed cache with f(0)=0, f(1)=1
    #if you are calling fib a lot, might be a good idea to make cache
    #global or persist across multiple function calls.

    i = 2
    while i <= N:
        cache[i] = cache[i-1] + cache[i-2]
        i += 1
    return cache[N]
def test_fib_iter():
    print("\nrunning test_fib_iter...")
    print("fib_iter(0) =", fib_iter(0))
    print("fib_iter(1) =", fib_iter(1))
    print("fib_iter(2) =", fib_iter(2))     #should equal 1
    print("fib_iter(3) =", fib_iter(3))     #should equal 2
    print("fib_iter(4) =", fib_iter(4))     #should equal 3
    print("fib_iter(10) =", fib_iter(10))   #should equal 55
    print("fib_iter(15) =", fib_iter(15))   #should equal 610
    print("fib_iter(20) =", fib_iter(20))   #should equal 6765
    print("now, can even quickly calculate fib_iter(100) =", fib_iter(100))
    #should be 354224848179261915075
    print("fib_iter(100) time: about 55 seconds.") #really slow when timed, don't know why.
        









from math import sqrt, floor
def fib_formula(N):
    '''
    There is a closed-form formula to calculate the fib nums.

    runtime: O(1) assuming arithmetic (mult, sqrt) are O(1) operations.

    You can extend this further to matrices.

    fib(N) = (phi^N - pho^N) / (phi - pho) = (phi^N - pho^N)/sqrt(5),
    where phi = (1 + sqrt(5))/2 and pho = (1 - sqrt(5))/2 = 1 - phi
    phi is also known as the "golden ratio".

    '''
    sqrt5 = sqrt(5)         #store as var so don't have to recalc everytime.
    phi = (1 + sqrt5)/2
    pho = (1 - sqrt5)/2
    return int((phi**N - pho**N) / sqrt5)   #trucate the portion after decimal.
def test_fib_formula():
    print("\nrunning test_fib_formula...")
    print("fib_formula(0) =", fib_formula(0))
    print("fib_formula(1) =", fib_formula(1))
    print("fib_formula(2) =", fib_formula(2))       #should equal 1
    print("fib_formula(3) =", fib_formula(3))       #should equal 2
    print("fib_formula(4) =", fib_formula(4))       #should equal 3
    print("fib_formula(10) =", fib_formula(10)) #should equal 55
    print("fib_formula(15) =", fib_formula(15)) #should equal 610
    print("fib_formula(20) =", fib_formula(20)) #should equal 6765
    print("ans starting to get imprecise ... fib_formula(100) =", fib_formula(100)) #should be 354224848179261915075
    print("fib_formula(100) time:", timeit.timeit("fib_formula(100)", setup="from __main__ import fib_formula"))
        


def test_fib():
    '''
    Sample runtimes:
    running test_fib_memo...
    fib_memo(0) = 0
    fib_memo(1) = 1
    fib_memo(2) = 1
    fib_memo(3) = 2
    fib_memo(4) = 3
    fib_memo(10) = 55
    fib_memo(15) = 610
    fib_memo(20) = 6765
    now, can even quickly calculate fib_memo(100) = 354224848179261915075
    fib_memo(100) time: 0.46602702140808105

    running test_fib_iter...
    fib_iter(0) = 0
    fib_iter(1) = 1
    fib_iter(2) = 1
    fib_iter(3) = 2
    fib_iter(4) = 3
    fib_iter(10) = 55
    fib_iter(15) = 610
    fib_iter(20) = 6765
    now, can even quickly calculate fib_iter(100) = 354224848179261915075
    fib_iter(100) time: 53.15003991127014

    running test_fib_formula...
    fib_formula(0) = 0
    fib_formula(1) = 1
    fib_formula(2) = 1
    fib_formula(3) = 2
    fib_formula(4) = 3
    fib_formula(10) = 55
    fib_formula(15) = 610
    fib_formula(20) = 6765
    ans starting to get imprecise ... fib_formula(100) = 354224848179263111168
    fib_formula(100) time: 3.1901819705963135

    Why is fib_iter so much slower than fib_memo? Why does it compute
    fib_iter(100) so quickly, but really slowly when timed?
    '''
    test_fib_naive()
    test_fib_memo()
    test_fib_iter()
    test_fib_formula()


if __name__ == '__main__':
    test_fib()
