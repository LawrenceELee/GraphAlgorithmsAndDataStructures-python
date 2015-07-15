'''
Implementation of various graph algs in python.

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

from collections import deque

#these ths sample graph that we are going to test algs on; they are represent
#the same directed unweighted graph (with cycles) using diff python structures.
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


def bfs(G, s):
    '''
    BFS written pure and minimal python to demo the alg not the language.

    Only iterative, no recursive version of BFS.

    This alg will start at node s and explore all nodes in the entire
    graph, marking down what node we used to reach the current node.
    Using edge_to we can reconstruct the path from s to any node.

    Since BFS solves the shorest path for unweighted graphs, we keep
    track of "edge_to" of node v so that we can reconstruct path from
    s to t.

    @type G: list of lists, list of sets, dict of sets
    @param G: the graph we are exploring.

    @type s: string, variable name
    @param s: source/starting node.

    @rtype: list
    @return: list each of the node's predecessor for path starting at s.
    '''

    #visited = []   #don't need this, since edge_to is dynamically resized we can just check for existance to see if we visited node or not.
    edge_to = {s: None}     #list of predecessors (mark  how we got to node x.)
    que = deque([s])        #queue of nodes we still need to explore.

    while que:
        x = que.popleft()                   
        for y in G[x]:                      #explore all neighbors of node u.
            if y in edge_to:    continue    #already visited/explore, so skip.
            edge_to[y] = x                  #record that got to v from u.
            que.append(y) #queue every unvisited neighbor.
    return edge_to
def test_bfs():
    print("running test_bfs()...")
    print("h -> d:", find_path(graph3, bfs, 'h', 'd')) #graph3, call with strs.
    print("h -> d:", find_path(graph1, bfs, h, d)) #graph1, call with var names.
    print("h -> d:", find_path(graph2, bfs, h, d))
    print("a -> h:", find_path(graph3, bfs, 'a', 'h'))
    print("a -> h:", find_path(graph1, bfs, a, h))
    print("h -> a:", find_path(graph3, bfs, 'h', 'a'))  #no path.


def dfs_iterative(G, s):
    '''
    DFS written pure and minimal python to demo the alg not the language.

    Iterative recursive version.

    This alg will start at node s and explore all nodes in the entire
    graph, marking down what node we used to reach the current node.
    Using edge_to we can reconstruct the path from s to any node.

    We can use DFS to create a pre and post order of the nodes starting from
    source node.

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
    edge_to = {s: None}     #list of predecessors (mark  how we got to node x.)
    stk = [s]               #use list as stack of nodes we need to explore.

    #preorder for iterative is easy.
    #hard to figure out postorder for iterative dfs. where does the post go?

    while stk:                      #simulate recursion with explicit stack.
        x = stk.pop()
        for y in G[x]:
            if y not in edge_to:    #only process new nodes, skip visited ones.
                edge_to[y] = x
                stk.append(y)       #push v onto stack.
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




def dfs_ordering(G):
    '''
    Even though this has similar idea to dfs_recursive, we need a separate
    dfs to process orderings.
    
    We don't take source as args b/c we need to discover ALL nodes.

    We can't wrap dfs_order around dfs_recursive because we don't share the
    same "space" so we can't "get" pre, post, revpost unless we embed it inside.
    Once the dfs_recusion terminates, all the "space" is torn down.

    TODO: how do refactor this code to return a specific ordering.
    '''
    edge_to = {} #record the predecessor of node x.
    visited = []    #marked nodes that have been visited and processed.
    pre     = []    #pre-order traversal, what application?
    post    = []    #post-order traversal, what application?
    revpost = []    #revpost order is used for strongly conn componet alg.
    #note: revpost is NOT the same as pre order!

    def _dfs_recursive(G, x):   #for graph2, x is a list not an int
        pre.append(x)
        visited.append(x)               #mark as visited
        print("G[x]:", G[x])
        for y in G[x]:
            if y not in visited:
                edge_to[y] = x
                _dfs_recursive(G, y)    #recursive call.
        post.append(x)
        revpost.append(x)

    for x in G:
        if x not in visited:
            _dfs_recursive(G, x)

    revpost.reverse()
    print("pre:\t\t", pre)
    print("post:\t\t", post)
    print("revpost:\t", revpost)
def test_dfs_ordering():
    print("running test_dfs_ordering()...")
    #print("graph1:", dfs_ordering(graph1)) #doesn't work on list of sets, why?
    #print("graph2:", dfs_ordering(graph2)) #doesn't work on list of lists, why?
    print("graph3:", dfs_ordering(graph3))





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




def topsort(G):
    '''
    Topological sort: used to order things with dependencies.

    Only works on directed acyclic graphs (DAG's).

    For ex, steps to make a cake, order to take school courses, etc.
    '''
    #check if G is a DAG. if G has CYCLE, exit.
    #run dfs_ordering on G for EVERY node to get a complete topsort.
    #get REVERSEPOST ordering of nodes from dfs_ordering. this is the topsort.

def test_topsort():
    print("topsort:", topsort(graph3))

def reverse(G):
    '''
    Reverses all edges in a directed graph.

    Need by Kosaraju's SCC alg.
    '''
    if type(G) == list:
        print("graph is a list")
    elif type(G) == set:
        print("graph is a set")
    elif type(G) == dict:
        print("graph is a dict")
        rev = {}
        for u in G: rev[u] = set()
        for u in G:
            for v in G[u]:
                rev[v].add(u)
        return rev
def test_reverse():
    print("graph:\n", graph1)                   
    print("graph reverse:\n", reverse(graph1))      #won't work, can't have a set of sets b/c lists aren't hashable (b/c they are mutable)).
    print("graph:\n", graph2)
    print("graph reverse:\n", reverse(graph2))
    print("graph:\n", graph3)
    print("graph reverse:\n", reverse(graph3))

def walk(G, s, S=None):     #recursive dfs without extra path finding stuff.
    if S is None: S = set()
    S.append(s)
    for u in G[s]:
        if u in S: continue
        walk(G, u, S)
def scc(G):
    '''
    Kosaraju' Strongly Connected Component alg.

    Dependencies:
        topological sort
        reverse graph
    '''

    #alg
    #run dfs_ordering on G.reverse(), 1st dfs run.
    #for every node x in dfs_ordering.revpost(), run dfs. 2nd dfs run.
    rev = reverse(G)
    sccs, visited = [], []
    for u in topsort(G):
        if u in visited:        continue
        C = walk(rev, u, visited)
        visited.append(C)
        sccs.append(C)
    return sccs
def test_scc():
    print("scc:",scc(graph3))




'''
The 3 below graph algs are slightly buggy. They are only examples used for
comparison and reference.
src: http://code.activestate.com/recipes/576723-dfs-and-bfs-graph-traversal
'''
def recursive_dfs(graph, start, path=[]):
    '''recursive depth first search from start'''
    path = path + [start]
    for node in graph[start]:
        if not node in path:
            path = recursive_dfs(graph, node, path)
    return path
def test_recursive_dfs():
    print("dfs:", recursive_dfs(graph1, h))

def iterative_dfs(graph, start, path=[]):
    ''' iterative depth first search from source.  '''
    #to_explore is a stack in DFS. add to top, remove from top.
    to_explore = [start]

    while to_explore:
        v = to_explore.pop(0)
        if v not in path:
            path = path + [v]
            to_explore.extend(graph[v])
    return path
def test_iterative_dfs():
    print("test_iterative_dfs:", iterative_dfs(graph3, 'h'))

def iterative_bfs(graph, start, path=[]):
    '''iterative breadth first search from start'''
    #to_explore is a queue in BFS. add and back, remove from front.
    to_explore = [start]

    while to_explore:
        v = to_explore.pop(0)
        if not v in path:
            path = path + [v]           #add to path to node v.
            to_explore.extend(graph[v]) #add neighbor nodes to back of queue.
    return path
def test_iterative_bfs():
    print("test_iterative_bfs:", iterative_bfs(graph3, 'h'))



def main():
    test_bfs()
    test_dfs_iterative()
    test_dfs_recursive()
    test_dfs_ordering()
    test_topsort()
    test_reverse()
    #test_scc()

    #test_recursive_dfs()   #a little buggy, path has extra nodes.
    #test_iterative_dfs()   #a little buggy, path has extra nodes.
    #test_iterative_bfs()   #a little buggy, path has extra nodes.

if __name__ == "__main__":
    main()
