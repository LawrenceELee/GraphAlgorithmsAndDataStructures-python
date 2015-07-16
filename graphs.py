'''
Different ways of representing graphs in python using built-ins.

1) adj list:
    use sets in python because faster.
    space: O(|V| + |E|)
    good for SPARSE (few edges) graphs.

2) adj matrix:
    space: O(|V|^2) (# of nodes/vertices squared), but faster lookup than a typical list.
    good for DENSE (many edges) graphs.

There are also other more complicated representations:
    edge lists or edge sets
    incidence matrices
    incidence list


Traversal and exploration:
    * Depth First Search (DFS):
        * traverses as deep as it can down on path, before trying next path.
    * Breadth First Search (BFS):
        * traverses in outwardly expanding concentric rings from source node.
        * BFS can also solve shortest path problem for unweighted (both directed and undirected) graphs.

    #sample runs
    running test_bfs()...
    h -> d: ('h', 'f', 'c', 'd')    #finds shortest path.
    h -> d: (7, 5, 2, 3)
    h -> d: (7, 5, 2, 3)
    a -> h: ('a', 'f', 'h')
    a -> h: (0, 5, 7)
    h -> a: No path from h to a

    running test_dfs_iterative()...
    h -> d: ('h', 'f', 'c', 'd')    #might find shortest path, in this case yes.
    h -> d: (7, 5, 2, 3)
    h -> d: (7, 5, 2, 3)
    a -> h: ('a', 'f', 'h')
    a -> h: (0, 5, 7)
    h -> a: No path from h to a

    running test_dfs_recursive()...
    h -> d: ('h', 'g', 'f', 'c', 'd') #might find short path, in this case no.
    h -> d: (7, 5, 2, 3)
    h -> d: (7, 5, 2, 3)
    a -> h: ('a', 'c', 'd', 'e', 'f', 'h')
    a -> h: (0, 1, 2, 3, 4, 5, 6, 7)
    h -> a: No path from h to a


Reachability/accessibility:
    only on undirected graphs.
    * Connected Componenets:

    only for directed graphs
    * Topological sort: used to order things with dependencies (graph must be a DAG). For ex, steps to make a cake, order to take school courses, etc.
      topological sorting of a DAG is equivalent to its reverse postordering.

    * Strongly Connected Components: only for directed acyclic graphs (DAG).
      Run DFS 2 times: 1st on G.reverse() then on G.

Minimum spanning tree:
    * Kruskal's
    * Prim's

Shortest path:
    * Dijkstra
    * Bellman-Ford

we can generalize DFS and BFS to a general traverse alg and by passing
in a stack or queue create either a DFS or BFS.

if you think about it:
    DFS, BFS -> a spanning tree (not necessarily minimum)
    then the next refinement is to find the min spanning tree -> Prim, Kruskal
    then the next refinement is to find the shortest path the spanning tree: Dijkstra.

a good implmentation to benckmark your code against in terms of quality and
effciency; it uses CLOSURES instead of classes:
    https://github.com/pmatiello/python-graph/blob/master/core/pygraph/algorithms/searching.py
    https://github.com/networkx/networkx/tree/master/networkx/algorithms/traversal
    http://www.ics.uci.edu/~eppstein/PADS/DFS.py for pre, post order, and class.

more reading on closures:
    http://www.reddit.com/r/Python/comments/1xdigg/nested_function/cfakafe
    http://stackoverflow.com/a/1305633
    http://stackoverflow.com/a/1589606
    http://stackoverflow.com/a/2006017

'''


#associates variable names of nodes with nums/idx.
#(i.e number variables a to h with nums 0 to 7)
a, b, c, d, e, f, g, h = range(8)

#can use longer or more meaningful variable names.
#ex. names of cities.
#(i.e number city names with nums 0 to 4)
new_york, los_angeles, san_francisco, chicago, miami =  range(5)


#UNWEIGHTED DIRECTED graph
#adj list with set/dict(with just keys, no values)
#adj list using list of dicts.
adj_list_of_dicts = [
    {b, c, d, e, f},    # a is idx 0
    {c, e},             # b is idx 1
    {d},                # c is idx 2
    {e},                # d is idx 3
    {f},                # e etc.
    {c, g, h},          # f
    {f, h},             # g
    {f, g}              # h
]

#UNWEIGHTED DIRECTED graph
#adj list with list objects
#adj list using list of lists.
adj_list_of_lists = [
    [b, c, d, e, f],    # a is idx 0
    [c, e],             # b is idx 1
    [d],                # c is idx 2
    [e],                # d is idx 3
    [f],                # e etc.
    [c, g, h],          # f
    [f, h],             # g
    [f, g]              # h
]

#WEIGHTED DIRECTED graph
#adj list with set/dict. nodes are the keys, edge weights are values.
#adj list using list of dicts.
adj_list_of_dicts = [
    {b:2, c:1, d:3, e:9, f:4},      # a is node/idx 0.
    {c:4, e:3},                     # b is node/idx 1.
    {d:8},                          # c is node/idx 2.
    {e:7},                          # d etc.
    {f:5},                          # e
    {c:2, g:2, h:2},                # f
    {f:1, h:6},                     # g
    {f:9, g:8}                      # h
]
#>>> b in adj_dict_of_sets[a]   #is node b a neighbor/adj to node a?
#True                           #yes.

#>>> len(adj_dict_of_sets[f])   #total edges going out from f to neighbor nodes?
#3                              #node f has 3 outgoing edges.

#>>> adj_dict_of_sets[a][b]     #edge weight of edge (a,b)?
#2                              #the edge from node a to node b has weight 2.


#adj list using a dict of sets.
adj_dict_of_sets = {
    'a': set('bcdef'),
    'b': set('ce'),
    'c': set('d'),
    'd': set('e'),
    'e': set('f'),
    'f': set('cgh'),
    'g': set('fh'),
    'h': set('fg')
}


#adj matrix using list of lists
#UNWEIGHTED, DIRECTED graph b/c weights are either 1 (edge) or 0 (no edge) and
#the matrix is not symmetric (implying directed).
adj_matrix_directed_unweighted = [
        [0,1,1,1,1,1,0,0], # a
        [0,0,1,0,1,0,0,0], # b
        [0,0,0,1,0,0,0,0], # c
        [0,0,0,0,1,0,0,0], # d
        [0,0,0,0,0,1,0,0], # e
        [0,0,1,0,0,0,1,1], # f
        [0,0,0,0,0,1,0,1], # g
        [0,0,0,0,0,1,1,0]  # h
]
#>>> adj_matrix_directed_unweighted[a][b]   #check if b is a neighbor of a.
#1                                          #can't use 'b in adj[a]'.

#>>> sum(adj_matrix_directed_unweighted[f]) #can't use len() to find out degree 
#3                                          #b/c all lists are the same length,
                                            #so use sum() instead.

#weighted, directed graph using adj matrix
_ = float('inf')    #use underscore as infinity (for shortest path algorithms).
adj_matrix_directed_weighted = [
        [0,2,1,3,9,4,_,_], # a
        [_,0,4,_,3,_,_,_], # b
        [_,_,0,8,_,_,_,_], # c
        [_,_,_,0,7,_,_,_], # d
        [_,_,_,_,0,5,_,_], # e
        [_,_,2,_,_,0,2,2], # f
        [_,_,_,_,_,1,0,6], # g
        [_,_,_,_,_,9,8,0]  # h
]
'''
we can make it undirected by making matrix symmetric. also note, that the diagonal from upper left to lower right is always 0 (no self-loops).
we can make graph weighted by putting non-zero integers as weights and 0 or infity as no edge. we need infinity for shortest path algs, if it were 0 then it would pick all the 0 edges.
'''
#>>> inf = float('inf')                         #define infinity

#>>> adj_matrix_directed_weighted[a][b] < inf   
#is there an edge from a to b? (i.e. is b a neighbor of a?)
#True  #yes, is a neighbor

#>>> adj_matrix_directed_weighted[c][e] < inf   
#is there an edge from c to e? (i.e. is )
#False  #not a neighbor

#>>> sum(1 for w in adj_matrix_directed_weighted[a] if w < inf) - 1
#out degree of node a. add 1 to count for each edge that has val less than inf.
#remember to subtract 1 so that it doesn't count the self-loop from a to a.
#5  #5 edges going out of node a.



#sample graphs used to test algs; they represent the same directed
#unweighted graph (with cycles) using diff python structures.
a, b, c, d, e, f, g, h = range(8)
graph1 = [      #list of sets (dicts without values)
    {b, c, d, e, f},    # a
    {c, e},             # b
    {d},                # c
    {e},                # d
    {f},                # e
    {c, g, h},          # f
    {f, h},             # g
    {f, g}              # h
]
graph2 = [      #list of lists
    [b, c, d, e, f],    # a
    [c, e],             # b
    [d],                # c
    [e],                # d
    [f],                # e
    [c, g, h],          # f
    [f, h],             # g
    [f, g]              # h
]
graph3 = {      #dict of string (key), set (value). 
    'a': set('bcdef'),
    'b': set('ce'),
    'c': set('d'),
    'd': set('e'),
    'e': set('f'),
    'f': set('cgh'),
    'g': set('fh'),
    'h': set('fg')
}
graph_scc = {       #2 scc's {a,b,c} and {d,e,f,g,}
    'a': set('b'),
    'b': set('c'),
    'c': set('a'),
    'd': set('e'),
    'e': set('fd'),
    'f': set('gde'),
    'g': set('d'),
    'h': set('')
}

