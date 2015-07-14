'''
Typical implementation of a queue using a list/array.

TODO: implement some unit testing or TDD/BDD.
'''

class Queue(list):
    #inherits from list.

    #simply rename the function by
    #binding new name "enqueue" to the append() fundtion.
    enqueue = list.append

    def dequeue(self):
        try:
            return self.pop(0)  #returns the 1st elmt and removes it from list.
        #don't want remove(elmt) b/c it will search for elmt and list and del it
        except:
            pass        #quietly do nothing if no more elmnts to pop.

    def is_empty(self):
        '''
        Add a is_empty function that list class didn't have.
        Returns true if no elements in stack, false otherwise.
        '''
        if self.__len__() <= 0:     #same as len(self) == 0
            return True
        #else is optional, more efficent without the else clause?
        return False

def test1():
    print("Test 1")
    q = Queue()
    print("is empty?", q.is_empty())
    print("enqueueing...", q.enqueue(100))
    print("enqueueing...", q.enqueue(200))
    print("enqueueing...", q.enqueue(300))
    print("enqueueing...", q.enqueue(400))
    print("enqueueing...", q.enqueue(500))
    print("enqueueing...", q.enqueue(600))
    print(q)
    print("is empty?", q.is_empty())
    print("dequeued", q.dequeue())
    print("dequeued", q.dequeue())
    print("dequeued", q.dequeue())
    print("is empty?", q.is_empty())
    print(q)
    print("enqueueing...", q.enqueue(700))
    print("enqueueing...", q.enqueue(800))
    print("is empty?", q.is_empty())
    print(q)
    print("dequeued", q.dequeue())
    print("dequeued", q.dequeue())
    print("dequeued", q.dequeue())
    print("dequeued", q.dequeue())
    print("dequeued", q.dequeue())
    print(q)
    print("is empty?", q.is_empty())
    print("dequeued", q.dequeue())
    print("is empty?", q.is_empty())

def main():
    test1()

if __name__ == "__main__":
    main()
