'''
Implementation of common sorting algs in python.

Selection sort: "selects" min, puts it in correct place.
                avg/worst runtime: O(n^2), aux mem: O(1), stable?

Insertion sort: avg/worst runtime: O(n^2), aux mem: O(1),
                stable: yes, in-place: yes.

Merge sort: avg/worst runtime: O(n lg n), aux mem: O(n),
            stable: yes, in-place: no.

Quick sort: avg runtime: O(n lg n) under the assumption that elements are
            randomized/shuffled and that they are mostly unique/few duplicates,
            if not then you will get worst runtime: O(n^2), aux mem: O(lg n),
            stable: no, in-place: yes (even though it has rec call stacks).

Quick 3-way sort: variant of quicksort (quick3) that is great for data with
                  many duplicates.

Heap sort: avg/worst runtime: O(n lg n), aux mem: O(1). stable?

Timsort: python’s native sorting algorithm, is a naturally adaptive version
         of merge sort. best runtime: O(n), worst O(n lg n).

'''

from random import randrange as randrange

def selectionsort_v1(data):
    '''
    This version is more imperative (translation of Java to Python).
    '''
    N = len(data)

    i = 0
    while i < N:
        minimum = i

        j = i+1
        while j < N:
            if data[j] < data[minimum]:
                minimum = j     #found new minimum.
            j += 1

        data[i], data[minimum] = data[minimum], data[i] #python idiom for swap.
        i += 1

def test_selectionsort_v1():
    print("Testing selectionsort v1...")
    my_list = [randrange(100) for i in range(50)]
    print(my_list)
    print("sorted?", is_sorted(my_list))
    selectionsort_v1(my_list)
    print(my_list)
    print("sorted?", is_sorted(my_list))
    print()

def selectionsort_v2(data):
    '''
    This version of selection sort uses Python idioms and style:
        * use min() to find minimum instead of iterating over array.
        * use enumerate() to return a pair (idx, element) instead of 2 nested
          for-loops.
        * use comma to swap values instead of swap() function.
    '''
    for idx, element in enumerate(data):
        # find min in remaining array using element/value as the key.
        # x.__getitem__(y) <==> x[y]
        mn = min(range(idx, len(data)), key=data.__getitem__) #find min

        data[idx], data[mn] = data[mn], element #swap data[idx] and data[mn].
    return data #is this optional? since sort is in-place, no need to return.
    '''
    what does enumerate do?
    it numbers elmnts from 0 to N-1, in effect assigning idices to elements.
    >>> data = ['a', 'b', 'c', 'd', 'e', 'f']
    >>> for i in enumerate(data):
            print(i)

        (0, 'a')
        (1, 'b')
        (2, 'c')
        (3, 'd')
        (4, 'e')
        (5, 'f')
    '''

def test_selectionsort_v2():
    print("Testing selectionsort v2...")
    my_list = [randrange(100) for i in range(50)]
    print(my_list)
    print("sorted?", is_sorted(my_list))
    selectionsort_v2(my_list)
    print(my_list)
    print("sorted?", is_sorted(my_list))
    print()





def insertionsort(data):
    '''
    avg/worst case runtime: O(n^2), aux mem: O(1), in-place, stable.
    '''
    N = len(data)
    i = 0
    while i < N:
        j = i
        while j > 0 and data[j] < data[j-1]:
            data[j], data[j-1] = data[j-1], data[j] #swap j with j-1
            j -= 1

        i += 1

def test_insertionsort():
    print("Testing insertionsort...")
    my_list = [randrange(100) for i in range(50)]
    print(my_list)
    print("sorted?", is_sorted(my_list))
    insertionsort(my_list)
    print(my_list)
    print("sorted?", is_sorted(my_list))
    print()





def gnomesort(data):
    '''
    Gnomesort is a variant of insertion sort.
    '''
    i = 0
    while i < len(data):
        if i == 0 or data[i-1] <= data[i]:
            i += 1
        else:
            data[i], data[i-1] = data[i-1], data[i] #swap data[i] with data[i-1]
            i -= 1

def test_gnomesort():
    print("Testing gnomesort...")
    my_list = [randrange(100) for i in range(50)]
    print(my_list)
    print("sorted?", is_sorted(my_list))
    gnomesort(my_list)
    print(my_list)
    print("sorted?", is_sorted(my_list))
    print()





def mergesort(data):        #data is a more general than list object.
    '''
    Typical mergesort with a recursive dividing portion, then a merging portion.
    '''
    
    #mid = len(data)//2     #integer division, truncate after decimal pt.
    #under the hood, it might covert // into >>
    mid = len(data) >> 1        #fast way to divide by 2. just bitshift left.
    #do we have to worry about the sign bit since >> carries sign bit?

    left, right = data[:mid], data[mid:]    #split at midpoint into 2 subarrays.

    #if subarray size is greater than 1 (more than 1 element), then...
    if len(left) > 1:
        left = mergesort(left)      #recurse on left subarray.

    if len(right) > 1:
        right = mergesort(right)    #recurse on right subarray.

    #merge portion of mergesort
    aux = []                #auxilary space
    while left and right:   #while left and right sublists not empty...
        #easier to keep track of last elmnt than pointers for curr left/right.
        if left[-1] >= right[-1]:
            aux.append(left.pop())  #take last element of left subarray.
        else:
            aux.append(right.pop()) #take last element of right subarray.

    aux.reverse()   #currently sorted descending, so need to reverse.
    return (left or right) + aux    #concat aux with whatever is not empty, [].

def test_mergesort():
    print("Testing mergesort...")
    my_list = [randrange(100) for i in range(50)]
    print(my_list)
    print("sorted?", is_sorted(my_list))
    my_list = mergesort(my_list)            #not in-place?
    print(my_list)
    print("sorted?", is_sorted(my_list))
    print()





def quicksort_v1(data):
    shuffle(data)   #make sure all data is randomized so that pivot is near mid.
    _quicksort(data, 0, len(data)-1)
def _quicksort(data, lo, hi):
    '''
    This version uses the same array and just swaps elements as needed.
    '''
    if lo < hi: #if not base case, where size is greater than or equal to 1.
        pivot, i, j = data[lo], lo, hi  #i is ptr for left subarry, j for right.
        while i <= j:
            while data[i] < pivot:      #find elmnt less than pivot
                i += 1
            while data[j] > pivot:      #find elmnt less than pivot
                j -= 1

            if i <= j:
                data[i], data[j] = data[j], data[i] #swap
                i += 1
                j -= 1

        _quicksort(data, lo, j)
        _quicksort(data, i, hi)

def quicksort_v2(data):
    '''
    This doesn't do it in-place, it creates a new list everytime when it
    concatenates less, pivot, more.
    '''
    if len(data) <= 1: return data          #base case
    less, pivot, more = partition(data)
    #sort lo up to pivot then concat with pivot then sort pivot+1 up to hi.
    return quicksort(less) + [pivot] + quicksort(more)
def partition(data):
    '''
    Partition will divide data into 2 lists: less (all elmts less than or equal
    to pivot), more (all elemts more than pivot), and 1 pivot elmnt.

    This doesn't do it in-place, it creates a new list everytime.
    '''
    #use first elmt as pivot, split into pivot and rest of data.
    pivot, data = data[0], data[1:]
    less = [i for i in data if i <= pivot] #create new list filtered from old.
    more = [i for i in data if i > pivot]   #create new list filtered from old.
    return less, pivot, more                #return lo list, pivot, hi list.

def test_quicksort():
    print("Testing quicksort...")
    my_list = [randrange(100) for i in range(50)]
    print(my_list)
    print("sorted?", is_sorted(my_list))
    quicksort_v1(my_list)   #in-place sort, no new array is returned.
    print(my_list)
    print("sorted?", is_sorted(my_list))
    print()




def shuffle(data):
    '''
    Helper function to randomize/shuffle elements in list.
    This is important for quicksort because this helps to make the pivot element
    somewhere near the middle of list and probablistic guarentee of
    O(n lg n) avg runtime.
    '''
    N = len(data)
    for idx, elmt in enumerate(data):
        randIdx = idx + randrange(N - idx)
        data[idx], data[randIdx] = data[randIdx], elmt
def test_shuffle():
    print("Testing shuffle()...")
    my_list = [i for i in range(100)]
    shuffle(my_list)
    return is_sorted(my_list)
    



def is_sorted(data):
    '''
    Helper function to check that sort algs are working correctly.
    '''
    N = len(data) - 1
    i = 0
    while i < N:
        if data[i] > data[i+1]: return False #if out of order, return false
        i += 1
    
    return True         #if no errors, then it is sorted.

def main():
    test_selectionsort_v1()
    test_selectionsort_v2()
    test_insertionsort()
    test_gnomesort()
    test_mergesort()
    test_quicksort()


if __name__ == "__main__":
    main()
