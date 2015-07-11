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
        #pop (return and remove) element at idx 0.
        return self.pop(0)  #by default pop() removes last element.
        #don't want my_list.remove(element) will see if element is in
        #list and remove it.

    def is_empty(self):
        '''
        Add a is_empty function that list class didn't have.
        Returns true if no elements in stack, false otherwise.
        '''
        if self.__len__() <= 0:     #same as len(self) == 0
            return True
        else:
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

def main():
    test1()

if __name__ == "__main__":
    main()
