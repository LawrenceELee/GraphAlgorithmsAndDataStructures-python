'''
Implementation of breadth first traversal algs in python.

* BFS can also solve shortest path problem for unweighted (both directed and undirected) graphs.

#sample runs
running test_bfs()...
h -> d: ('h', 'f', 'c', 'd')    #finds shortest path.
h -> d: (7, 5, 2, 3)
h -> d: (7, 5, 2, 3)
a -> h: ('a', 'f', 'h')
a -> h: (0, 5, 7)
h -> a: No path from h to a
'''

from collections import deque

from graphs import *
#why does this have a different effect than 'import graphs' ?


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
    edge_to = {s: None}             #list of predecessors (mark  how we got to node x.)
    que = deque([s])                #queue of nodes we still need to explore.

    while que:
        x = que.popleft()                                       
        for y in G[x]:                      #explore all neighbors of node u.
            if y in edge_to:    continue    #already visited/explore, so skip.
            edge_to[y] = x                  #record that got to v from u.
            que.append(y)                   #queue every unvisited neighbor.
    return edge_to

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

def test_bfs():
    print("running test_bfs()...")
    print("h -> d:", find_path(graph3, bfs, 'h', 'd')) #graph3, call with strs.
    print("h -> d:", find_path(graph1, bfs, h, d)) #graph1, call with var names.
    print("h -> d:", find_path(graph2, bfs, h, d))
    print("a -> h:", find_path(graph3, bfs, 'a', 'h'))
    print("a -> h:", find_path(graph1, bfs, a, h))
    print("h -> a:", find_path(graph3, bfs, 'h', 'a'))      #no path.

def main():
    test_bfs()

if __name__ == "__main__":
    main()
