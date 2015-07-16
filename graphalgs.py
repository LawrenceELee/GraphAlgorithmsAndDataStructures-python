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
    'd': set('efgh'),
    'e': set('fghd'),
    'f': set('ghde'),
    'g': set('h'),
    'h': set('')
}
def scc(G):
    '''
    Kosaraju's Strongly Connected Component alg.

    The outline of the alg: run DFS two times.
    1) run dfs_ordering on reverse(G), yielding a reverse post ordering on G rev
    2) for every node x in dfs_ordering.revpost(), run dfs.

    Dependencies:
        topological sort
        reverse graph
    '''

    visited = []    #faster to check memebership than list.
    sccs    = {}

    #iterative dfs without extra path finding stuff.
    def _traverse(G, s, storage=[]):        
        #dynically make alg dfs or bfs by specifiying what storage to use.
        #if queue/list/deque -> bfs. if stack -> dfs.
        #default is set() b/c faster to check membership.
        left_to_explore = storage   
        left_to_explore.append(s)

        while left_to_explore:
            x = left_to_explore.pop()
            print("G:", G)
            print("x: ", x)
            print("G[x]: ", G[x])
            for y in G[x]:
                if y not in visited:        #node process prior, skip.
                    continue

                sccs[x] = y                 #record the parent scc.
                visited.append(y)               #we know this scc, skip in future.
                left_to_explore.append(y)

    #run dfs_ordering on G.reverse() to get reverse post ordering, 1st dfs run.
    #(i.e. run topsort on G_reverse)
    G_reverse = reverse(G)
    topsort_order = topsort(G_reverse)      #topsort_order is just reverse post.
    print("HERE topsort order:", topsort_order)
    
    #for every node x in dfs_ordering.revpost(), run dfs. 2nd dfs run.
    for x in topsort_order:
        if x in visited: continue
        c = _traverse(G_reverse, x, visited)
        visited.append(c)
        sccs[x] = c
    '''
    for x in topsort_order:
        #get a node in the order
        print("x:", x)
        for y in G[x]:              #get adj list, list of edges.
            #print("sccs:", scc)
            print("y:", y)
            if y in visited: continue   #processed before, skip.
            comp = _traverse(G, y, visited)
            visited.add(comp)
            sccs[y] = comp
    '''

    return sccs
def test_scc():
    my_sccs = scc(graph_scc)
    print("sccs:", my_sccs)
    '''
    for node in scc(graph3):
        for i in node:
            print("i:", i)
    '''

def traverse(G, s, storage=set()):      
    '''
    Generalized graph traversal algorithm.

    If you use queue for storage, traversal turns into BFS.
    If you use stack for storage, traversal turns into DFS.

    Default is to use list as a stack. Using set is faster to check for
    membership, but it doesn't have the same API functions as list(), deque().

    Forget BFS for now.
    '''
    to_explore = storage    
    to_explore.add(s)

    predecessors = {s: None}

    while to_explore:
        x = to_explore.pop()
        for y in G[x]:
            if y in predecessors:   continue    #node process prior, skip.

            predecessors[y] = x
            to_explore.add(y)
            #visited.append(y)              #we know this scc, skip in future.

    return predecessors
def test_traverse():
    predecessors = traverse(graph3, 'a')
    x = 'h'
    path = [x]
    while predecessors[x] is not None:  #walk backwards from t to s.
        path.append(predecessors[x])
        x = predecessors[x]
    path.reverse()
    print("test traversal path:", path)




'''
The 3 below graph algs are slightly buggy. They are only examples used for
comparison and reference.

They seem to work with lists of lists, which is good for inverse/reverse graphs.

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
    test_dfs_ordering()
    test_topsort()
    test_reverse()
    test_scc()
    #test_traverse()

    #test_recursive_dfs()   #a little buggy, path has extra nodes.
    #test_iterative_dfs()   #a little buggy, path has extra nodes.
    #test_iterative_bfs()   #a little buggy, path has extra nodes.

if __name__ == "__main__":
    main()
