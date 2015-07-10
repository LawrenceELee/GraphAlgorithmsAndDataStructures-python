# GraphAlgorithmsAndDataStructures-python
Typical data structures and algorithms implemented in python.

Data structures:
- [ ] LinkedList: lists are built-in to python.
- [ ] Stack: add to "top" of stack, remove from "top" of stack.
- [ ] Queue: add to "back" of queue, remove from "front" of queue.
- [ ] Priority Queue (Heap): minimum (minheap) is on top, everything else is greater in value below.
[ ] Fibonacci Heaps are more efficent in theory, but are complicated to implement, so they are used in real life.

Trees (special case of graphs):
- [ ] Binary tree:
- [ ] d-ary tree: more general case of binary tree with d children instead of just 2 children.
[ ] Binary search tree (BST): binary tree with property that leftchild.data < curr.data < rightchild.data throughout tree.

Self-balancing trees:
- [ ] B-tree: sort of like a self-balancing BST.
- [ ] Red-Black tree:
- [ ] Splay tree:
- [ ] AVL tree:

Misc:
- [ ] Trie:
- [ ] Treap:
- [ ] Rope:

Comparison based sorts (best case limit is O(n lg n)):
- [ ] Insertion sort: avg/worst runtime: O(n^2), aux mem: O(1), stable: yes, in-place: yes.
- [ ] Selection sort: avg/worst runtime: O(n^2), aux mem: O(1), stable?
- [ ] Merge sort: avg/worst runtime: O(n lg n), aux mem: O(n), stable: yes, in-place: no.
- [ ] Quick sort: avg runtime: O(n lg n) under the assumption that elements are randomized/shuffled and that they are mostly unique/few duplicates, if not then you will get worst runtime: O(n^2), aux mem: O(lg n), stable: no, in-place: yes (even though it has rec call stacks).
- [ ] There is a variant of quicksort (quick3) that is great for data with many duplicates.
- [ ] Heap sort: avg/worst runtime: O(n lg n), aux mem: O(1). stable?

Non-Comparison based sorts:
- [ ] Counting sort:
- [ ] Bucket sort: avg runtime: O(n+k), worst O(n^2), aux mem: O(n).
- [ ] MSD radix sort: avg/worst runtime: O(nk) where n is # of bits/digits starting with most signif digit. aux mem: O(n+k), stable: yes, in-place: no.
- [ ] LSD radix sort: like MSD but starting from least signif digit, stable: yes, in-place: no.

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
