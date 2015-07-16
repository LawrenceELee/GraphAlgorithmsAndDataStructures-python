'''
Implementation of depth-first ordering. Get orderings, we don't care as much
about finding a path from source node to target node.

* Topological sort: used to order things with dependencies (graph must be a DAG). For ex, steps to make a cake, order to take school courses, etc.
topological sorting of a DAG is equivalent to its reverse postordering.

This is needed by SCC alg.
'''


#put these here for global scope, so that SCC can use the orderings.
pre             = []    #pre-order traversal, what application?
post    = []    #post-order traversal, what application?
revpost = []    #revpost order is used for strongly conn componet alg.
#note: revpost is NOT the same as pre order!

edge_to = {} #record the predecessor of node x.
visited = []    #marked nodes that have been visited and processed.
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

        def _dfs_recursive(G, x):       #for graph2, x is a list not an int
                pre.append(x)
                visited.append(x)                               #mark as visited
                #print("G[x]:", G[x])
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
        #print("pre:\t\t", pre)
        #print("post:\t\t", post)
        #print("revpost:\t", revpost)
def test_dfs_ordering():
        print("running test_dfs_ordering()...")
        #print("graph1:", dfs_ordering(graph1)) #doesn't work on list of sets, why?
        #print("graph2:", dfs_ordering(graph2)) #doesn't work on list of lists, why?
        dfs_ordering(graph3)
        print("graph3 pre:\t\t", pre)
        print("graph3 post:\t\t", post)
        print("graph3 rev post:\t", revpost)

def topsort(G):
    '''
    Topological sort: used to order things with dependencies.

    Only works on directed acyclic graphs (DAG's).

    For ex, steps to make a cake, order to take school courses, etc.
    '''
    #check if G is a DAG. if G has CYCLE, exit.
    #TODO


    #run dfs_ordering on G for EVERY node to get a complete topsort.
    for node in G:
        dfs_ordering(G)

    return revpost
    
    #result = []
    #get REVERSEPOST (of adj list) ordering of nodes from dfs_ordering.
    #for node in revpost:
    #   result.append(G[node])
    #return result

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
