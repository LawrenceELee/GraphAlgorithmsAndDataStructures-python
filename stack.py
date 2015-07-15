'''
Typical implementation of a stack using a list/array.

This is for academic demo purposes. It is a better idea to use python set()
for stack in DFS, etc. instead b/c sets have faster lookup than list().
'''

class Stack(list):
    #inherits from list.

    push = list.append  #just bind name "push" to the append() fundtion.
    #pop = list.pop #list has a pop() already so we don't have to rebind it

    def is_empty(self):
        '''
        Add a is_empty function that list class didn't have.
        Returns true if no elements in stack, false otherwise.

        #old version
        if self.__len__() <= 0:     #same as len(self) == 0
            return True
        return False
        '''
        #new version: just check for non-existance
        return not self


    def peek(self):
        '''
        Add a peek function that List class doesn't have.
        Look at "top" of stack, but don't remove "top" element.
        '''
        # slicing returns a list, which isn't exactly what we want.
        # we just want the element itself.
        #return self[-1:]   #return last element using python slice syntax

        return self[len(self)-1] #so we just return the last element.

def test1():
    print("Test 1")
    s = Stack()
    print("is empty?", s.is_empty())
    print("pushing...", s.push(100))
    print("pushing...", s.push(200))
    print("pushing...", s.push(300))
    print("pushing...", s.push(400))
    print("pushing...", s.push(500))
    print("pushing...", s.push(600))
    print("peeking... (shouldn't remove \"top\" element)", s.peek())
    print(s)
    print("is empty?", s.is_empty())
    print("popped", s.pop())
    print("popped", s.pop())
    print("popped", s.pop())
    print("is empty?", s.is_empty())
    print(s)
    print("pushing...", s.push(700))
    print("pushing...", s.push(800))
    print("is empty?", s.is_empty())
    print(s)
    print("popped", s.pop())
    print("popped", s.pop())
    print("popped", s.pop())
    print("popped", s.pop())
    print("popped", s.pop())
    print(s)
    print("is empty?", s.is_empty())

def main():
    test1()

if __name__ == "__main__":
    main()
