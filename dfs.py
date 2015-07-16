'''
Implementation of depth-first traversal alg in python.

Traversal and exploration:
    * Depth First Search (DFS):
        * traverses as deep as it can down on path, before trying next path.

    #sample runs
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

#sample graphs used to test algs; they represent the same directed
#unweighted graph (with cycles) using diff python structures.
a, b, c, d, e, f, g, h = range(8)
graph1 = [              #list of sets (dicts without values)
    {b, c, d, e, f},        # a
    {c, e},                         # b
    {d},                            # c
    {e},                            # d
    {f},                            # e
    {c, g, h},                      # f
    {f, h},                         # g
    {f, g}                          # h
]
graph2 = [              #list of lists
    [b, c, d, e, f],        # a
    [c, e],                         # b
    [d],                            # c
    [e],                            # d
    [f],                            # e
    [c, g, h],                      # f
    [f, h],                         # g
    [f, g]                          # h
]
graph3 = {              #dict of string (key), set (value). 
    'a': set('bcdef'),
    'b': set('ce'),
    'c': set('d'),
    'd': set('e'),
    'e': set('f'),
    'f': set('cgh'),
    'g': set('fh'),
    'h': set('fg')
}

def dfs_iterative(G, s):
    '''
    DFS written pure and minimal python to demo the alg not the language.

    Iterative recursive version.

    This alg will start at node s and explore all nodes in the entire
    graph, marking down what node we used to reach the current node.
    Using edge_to we can reconstruct the path from s to any node.

    Finding the "finishing times" (post order) is much harder for iterative
    DFS than recrusive DFS b/c we lose that BACKTRACKING from the call stack.
    src: http://stackoverflow.com/questions/24051386/kosaraju-finding-finishing-time-using-iterative-dfs

    DFS DOES NOT solve shortest path for unweighted graphs, but we
    can still use it to find A PATH from s to t from the edge_to list.

    @type G: list of lists, list of sets, dict of sets
    @param G: the graph we are exploring.

    @type s: string, variable name
    @param s: source/starting node.

    @rtype: list
    @return: list each of the node's predecessor for path starting at s.
    '''
    #visited = []   #don't need this, since edge_to is dynamically resized we can just check for existance to see if we visited node or not.
    edge_to = {s: None}     #list of predecessors (mark how we got to node x).
    stk = [s]               #use list as stack of nodes we need to explore.

    #preorder for iterative is easy.
    #hard to figure out postorder for iterative dfs. where does the post go?

    while stk:                      #simulate recursion with explicit stack.
        x = stk.pop()
        for y in G[x]:
            if y in edge_to:    continue    #skip visited.
            edge_to[y] = x
            stk.append(y)                   #push v onto stack.
    return edge_to

def test_dfs_iterative():
    print("running test_dfs_iterative()...")
    print("h -> d:", find_path(graph3, dfs_iterative, 'h', 'd'))
    print("h -> d:", find_path(graph1, dfs_iterative, h, d))
    print("h -> d:", find_path(graph2, dfs_iterative, h, d))
    print("a -> h:", find_path(graph3, dfs_iterative, 'a', 'h'))
    print("a -> h:", find_path(graph1, dfs_iterative, a, h))
    print("h -> a:", find_path(graph3, dfs_iterative, 'h', 'a'))    #no path.

def dfs_recursive(G, s):
    '''
    For recursive version, you need a seperate "visited" list.
    '''
    edge_to = {s: None} #record the predecessor of node x.
    visited = []    #marked nodes that have been visited and processed.

    def _dfs_recursive(G, x):
        '''
        _def_recursive is the core dfs logic.

        using CLOSURES!!! inner _dfs has access to state of outer dfs.
        so don't need to change _dfs_recursive function signature to pass
        edge_to & visited.
        '''
        visited.append(x)           #mark as visited
        for y in G[x]:
            if y not in visited:    #only process new nodes, skip visited ones.
                edge_to[y] = x
                _dfs_recursive(G, y)    #recursive call.

    _dfs_recursive(G, s) #core DFS function for wrapper.
    #using CLOSURES!!! inner dfs has access to state of outer dfs.
    #so don't need to change _dfs function signature to pass edge_to & visited.

    return edge_to

def test_dfs_recursive():
    print("running test_dfs_recursive()...")
    print("h -> d:", find_path(graph3, dfs_recursive, 'h', 'd'))
    print("h -> d:", find_path(graph1, dfs_recursive, h, d))
    print("h -> d:", find_path(graph2, dfs_recursive, h, d))
    print("a -> h:", find_path(graph3, dfs_recursive, 'a', 'h'))
    print("a -> h:", find_path(graph1, dfs_recursive, a, h))
    print("h -> a:", find_path(graph3, dfs_recursive, 'h', 'a'))    #no path.


def find_path(G, trav_alg, s, t):
    '''
    Used by both DFS and BFS to trace path from source to target.
    TODO: make it a query so that it doesn't have to run trav_alg every
    time. Just run the alg once, and allow for repeated queries.

    @type G: list of lists, list of sets, dict of sets
    @param G: the graph we are exploring.

    @type s: string, variable name
    @param s: source/starting node.

    @rtype: list
    @return: list each of the node's predecessor for path starting at s.
    '''
    x = t                           #x is a "dummy variable"
    path = [x]
    edge_to = trav_alg(G, s)            #dynamic func application explore graph.
    try:
        while edge_to[x] is not None:   #walk backwards from t to s.
            path.append(edge_to[x])
            x = edge_to[x]
    except KeyError:
        return "No path from %s to %s" % (s, t)
    path.reverse()  #reverse() is in-place, path.reverse() returns 'None'.
    return tuple(path)

def main():
    test_dfs_iterative()
    test_dfs_recursive()

if __name__ == "__main__":
    main()
