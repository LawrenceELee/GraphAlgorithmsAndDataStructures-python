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
    #test_traverse()

    #test_recursive_dfs()   #a little buggy, path has extra nodes.
    #test_iterative_dfs()   #a little buggy, path has extra nodes.
    #test_iterative_bfs()   #a little buggy, path has extra nodes.
    pass

if __name__ == "__main__":
    main()
