'''
Implementation of various graph algs in python.

Traversal and exploration:
    * Depth First Search (DFS):
        * traverses as deep as it can down on path, before trying next path.
    * Breadth First Search (BFS):
        * traverses in outwardly expanding concentric rings from source node.
        * BFS can also solve shortest path problem for unweighted (both directed and undirected) graphs.

Reachability:
    * Connected Componenets
    * Strongly Connected Components
    * Topological sort (graph must be a directed acyclical graph (DAG))

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
graph3 = {      #dict of string keys and set values
    'a': set('bcdef'),
    'b': set('ce'),
    'c': set('d'),
    'd': set('e'),
    'e': set('f'),
    'f': set('cgh'),
    'g': set('fh'),
    'h': set('fg')
}

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
        u = que.popleft()                   
        for v in G[u]:                      #explore all neighbors of node u.
            if v in edge_to:    continue    #already visited/explore, so skip.
            edge_to[v] = u                  #record that got to v from u.
            que.append(v) #queue every unvisited neighbor.
    return edge_to 

def dfs_iterative(G, s):
    '''
    '''
    #visited = []   #don't need this, since edge_to is dynamically resized we can just check for existance to see if we visited node or not.
    edge_to = {s: None}     #list of predecessors (mark  how we got to node x.)
    que = [s]               #use list as stack of nodes we need to explore.


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
    edge_to = trav_alg(G, s)                #explore graph.
    try:
        while edge_to[x] is not None:   #walk backwards from t to s.
            path.append(edge_to[x])
            x = edge_to[x]
    except KeyError:
        return "No path from %s to %s" % (s, t)
    path.reverse()  #reverse() is in-place, can't return path.reverse().
    return tuple(path)

def test_bfs():
    print("running test_bfs()...")
    print(find_path(graph3, bfs, 'h', 'd')) #for graph3, call with strings.
    print(find_path(graph1, bfs, h, d)) #for graph1, call with variable names.
    print(find_path(graph3, bfs, 'a', 'h'))
    print(find_path(graph3, bfs, 'h', 'a'))  #no path.






def main():
    #test_dfs_iterative()
    test_recursive_dfs()    #a little buggy, path has extra nodes.
    test_iterative_dfs()    #a little buggy, path has extra nodes.
    test_iterative_bfs()    #a little buggy, path has extra nodes.
    test_bfs()


if __name__ == "__main__":
    main()
