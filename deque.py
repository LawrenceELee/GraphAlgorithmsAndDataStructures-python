'''
Implementation of a deque data structure using a python built-in list.

This is for academic demo purposes. It is a better idea to use deque
from the collections library.
'''

class Deque(list):
    
    #by default, operations are done on the end/right of list
    #just rebind the function name to something else.
    #pop = list.pop             #function name rebindings are optional.
    #append = list.append       #function name rebindings are optional.
    #extend = list.extend       #function name rebindings are optional.

    popright = list.pop         #bind pop function to another name.
    '''
    ex.
    >>> data = ['b', 'c', 'd', 'e', 'f']
    >>> data.pop()
    'f'
    >>> data
    ['b', 'c', 'd', 'e']
    '''

    appendright = list.append       #bind append function to another name.
    '''
    ex.
    >>> data = ['b', 'c', 'd', 'e']
    >>> data.append([1, 2, 3])
    >>> data
    ['b', 'c', 'd', 'e', [1, 2, 3]]
    '''

    extendright = list.extend       #bind extend function to another name.
    '''
    ex.
    >>> data = ['a', 'b', 'c', 'd', 'e', 'f']
    >>> data.extend([1, 2, 3, 4, 5])
    >>> data
    ['a', 'b', 'c', 'd', 'e', 'f', 1, 2, 3, 4, 5]
    '''

    #operations on the front/left of list.
    def popleft(self):
        popped_elmt = self.pop(0)           #remove and return 1st element.
        return popped_elmt

    def appendleft(self, element):
        '''
        appends adds a single element (other) to the beginning of this list.
        the element can be an int, list, or something else since list
        can hold multiple data types.
        ex.
        >>> data
        ['b', 'c', 'd', 'e']
        >>> data.appendleft([1, 2, 3])
        >>> data
        [[1, 2, 3], 'b', 'c', 'd', 'e']
        '''
        self.insert(0, element)         #insert before 1st idx.
        

    def extendleft(self, otherlist):
        '''
        extend joins/combines this list with other, with other before self.
        extend will return a new list, won't "add" in-place.
        '''
        otherlist.reverse()             #reverse list to make next step easier
        #append each elmt in other list
        return [self.appendleft(i) for i in otherlist]


    def is_empty(self):
        return len(self) <= 0

def test1():
    print("Deque test 1")
    d = Deque()
    print("is empty?", d.is_empty())
    print("appending left...", d.appendleft(200))
    print("appending right...", d.appendright(300))
    print("appending right...", d.append(400))
    print("appending left...", d.appendleft(100))
    print("appending right...", d.appendright(500))
    print("appending right...", d.append(600))
    print("extending right...", d.extendright([700, 800, 900]))
    print("extending left...", d.extendleft([0, 1, 2, 3, 4, 5]))
    print(d)
    print("is empty?", d.is_empty())
    print("popping right...", d.pop())
    print("popping left...", d.popleft())
    print("popping right...", d.popright())
    print("is empty?", d.is_empty())
    print(d)
    print("appending...", d.append(1000))
    print("appending...", d.appendleft(-1))
    print("is empty?", d.is_empty())
    print(d)
    print("popping right...", d.pop())
    print("popping left...", d.popleft())
    print("popping left...", d.popleft())
    print("popping right...", d.popright())
    print("popping left...", d.popleft())
    print(d)
    print("is empty?", d.is_empty())

def main():
    test1()

if __name__ == "__main__":
    main()
