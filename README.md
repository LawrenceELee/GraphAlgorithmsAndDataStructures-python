# Data structures and Algorithms (Python)
Typical data structures and algorithms implemented in python.

Python built-ins: Lists, Dicts, Sets.

Data structures:
- [ ] LinkedList: TODO: add(), remove().
- [x] Stack: add to "top" of stack, remove from "top" of stack.
- [x] Queue: add to "back" of queue, remove from "front" of queue.
- [x] Deque: a "double-ended queue" aka circular buffer (i.e. and queue that you can push/pop from both the "front" and "back"). It is implemented in the python collections library.
- [ ] Priority Queue (Heap): minimum (minheap) is on top, everything else is greater in value below.
- [ ] Fibonacci Heaps are more efficent in theory, but are complicated to implement, so they are used in real life.

Trees (special case of graphs):
- [x] Binary tree:
- [ ] d-ary tree: more general case of binary tree with d children instead of just 2 children.
- [ ] Binary search tree (BST): binary tree with property that leftchild.data < curr.data < rightchild.data throughout tree.

Self-balancing trees:
- [ ] B-tree: sort of like a self-balancing BST.
- [ ] Red-Black tree:
- [ ] Splay tree:
- [ ] AVL tree:

Misc:
- [ ] Trie (pronounced "try", from re'tri'val):
- [ ] Treap:
- [ ] Rope:

Comparison based sorts (best case limit is O(n lg n)):
- [x] Selection sort: pick min. avg/worst runtime: O(n^2), aux mem: O(1), stable?
- [x] Insertion sort: avg/worst runtime: O(n^2), aux mem: O(1), stable: yes, in-place: yes.
- [ ] Insertion sort (Binary search variant): reduces num of comparisons to ceil(log(n)) but num of swaps still O(n^2). https://en.wikipedia.org/wiki/Insertion_sort#Variants
- [x] Merge sort: avg/worst runtime: O(n lg n), aux mem: O(n), stable: yes, in-place: no.
- [x] Quick sort: avg runtime: O(n lg n) under the assumption that elements are randomized/shuffled and that they are mostly unique/few duplicates, if not then you will get worst runtime: O(n^2), aux mem: O(lg n), stable: no, in-place: yes (even though it has rec call stacks).
- [ ] Quick 3-way sort (variant of quicksort) that is great for data with many duplicates.
- [ ] Heap sort: avg/worst runtime: O(n lg n), aux mem: O(1). stable?
- [ ] Timsort: python’s native sorting algorithm, is a naturally adaptive version of merge sort. best runtime: O(n), worst O(n lg n).
- [x] Gnomesort: a variant of insertion sort.
- [ ] Shell sort: a variant of insertion sort that compares 3+ elmts at a time.

Non-Comparison based sorts:
- [ ] Counting sort:
- [ ] Bucket sort: avg runtime: O(n+k), worst O(n^2), aux mem: O(n).
- [ ] MSD radix sort: avg/worst runtime: O(nk) where n is # of bits/digits starting with most signif digit. aux mem: O(n+k), stable: yes, in-place: no.
- [ ] LSD radix sort: like MSD but starting from least signif digit, stable: yes, in-place: no.

- [x] Graph representations

Unweighted (all edges have implicited same weight), Undirected Graph:
- [ ] Depth first search (DFS):
- [ ] Breadth first search (BFS):
- [ ] Connected Components:

Unweighted (all edges have implicited same weight), Directed Graph:
- [ ] DFS
- [ ] BFS
- [ ] Strongly Connection Components
- [ ] Topological sort
- [ ] Cycle Detection

Minimum Spanning Tree (Weighted (explicit weight required), Undirected Graphs):
- [ ] Prim
- [ ] Kruskal

Shortest Path (Weighted (explicit weight required), Directed Graphs):
- [ ] Dijkstra (no negative edge weights, faster than Bellman-Ford if you know all edges are non-negative ahead of time.)
- [ ] Bellman-Ford (allows negative edge weights)
