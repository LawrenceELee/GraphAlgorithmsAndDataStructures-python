'''
Demo how to represent trees in python using built-ins.

Trees are just a special/specific case of graphs.

'''

#general tree using lists of lists
tree1 = [["a", "b"], ["c"], ["d", ["e", "f"]]]

tree1[0][1]             #2nd child of 1st child of root returns node 'b'
tree1[2][1][0]          #1st child 2nd child of 3rd child of root returns node 'e'


#binary tree class
class BinaryTree:
    def __init__(self, l, r):
        self.left = l           #self.left variable is dynamically created.
        self.right = r          #same with self.right variable.
    
    '''
    TODO:
    #need to define this in order for 'for-loop' to work.
    def __iter__():
        pass
    '''

def test_binary_tree():
    t = BinaryTree(BinaryTree("a", "b"), BinaryTree("c", "d"))
    '''
    print("binary tree:")
    for i in t:
        print(i)
    '''
    print("root's right child's left child is:", t.right.left) #returns 'c'

def main():
    test_binary_tree()

if __name__ == "__main__":
    main()
