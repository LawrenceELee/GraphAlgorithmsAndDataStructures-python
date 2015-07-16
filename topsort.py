'''
Implementation of depth-first ordering. Get orderings, we don't care as much
about finding a path from source node to target node.

* Topological sort: used to order things with dependencies (graph must be a DAG). For ex, steps to make a cake, order to take school courses, etc.
topological sorting of a DAG is equivalent to its reverse postordering.

This is needed by SCC alg.
'''

from graphs import *
#why does this have a different effect than 'import graphs' ?

from dfs import dfs_recursive

def reverse(G):
    '''
    Reverses all edges in a directed graph.

    Need by Kosaraju's SCC alg.
    '''
    if type(G) == list:
        #print("graph is a list")
        pass
    elif type(G) == set:
        #print("graph is a set")
        pass
    elif type(G) == dict:
        #print("graph is a dict")
        rev = {}
        for u in G: rev[u] = set()
        for u in G:
            for v in G[u]:
                rev[v].add(u)
        return rev
def test_reverse():
    print("\nrunning test_reverse()...")                    
    #print("graph:\n", graph1)                  
    #print("graph reverse:\n", reverse(graph1))     #won't work, can't have a set of sets b/c lists aren't hashable (b/c they are mutable)).
    #print("graph:\n", graph2)
    #print("graph reverse:\n", reverse(graph2))
    print("graph:\n", graph3)
    print("graph reverse:\n", reverse(graph3))





def dfs_ordering(G):
    '''
    This is exactly like dfs_recursive, except with a few extra lists to
    records pre, post, and revpost orderings.
    Can't import b/c need to embed pre, post, and revpost into alg.
    
    We don't take source as args b/c we run DFS on ALL nodes in graph.

    We can't wrap dfs_order around dfs_recursive because we don't share the
    same "space" so we can't "get" pre, post, revpost unless we embed it
    inside. Once the dfs_recusion terminates, all the "space" is torn down.
    SOLVED this by returning a dict of all orderings, so now
    pre, post, revpost are inside function instead of globals.

    Alternatively, you can use TIMESTAMPS instead of pre, post, revpost.

    @type G: list of lists, list of sets, dict of sets
    @param G: the graph we are exploring.

    @type choice: string
    @param choice: 'pre', 'post', or 'revpost' ordering.

    @rtype: tuple
    @return: tuple of the nodes in the ordering of your choice.
    '''

    pre     = []    #pre-order traversal, what application?
    post    = []    #post-order traversal, what application?
    revpost = []    #revpost order is used for strongly conn componet alg.
    #note: revpost is NOT the same as pre order!

    #edge_to = {}   #record the predecessor of node x.
    #don't need path/route, so this is not important here.

    visited = []    #marked nodes that have been visited and processed.

    def dfs(G, x):
        pre.append(x)
        visited.append(x)                       #mark as visited
        for y in G[x]:
            if y in visited:    continue        #skip visited nodes.
            #edge_to[y] = x
            dfs(G, y) #recursive call.
        post.append(x)
        revpost.append(x)

    #run dfs on every node in graph to get forest.
    for x in G:
        if x not in visited:
            dfs(G, x)

    revpost.reverse()   #reverse post traversal to get revpost.

    all_orderings = {'pre': tuple(pre), 'post': tuple(post), 'revpost': tuple(revpost)}
    return all_orderings

def test_dfs_ordering():
    print("\nrunning test_dfs_ordering()...")
    #print("graph1:", dfs_ordering(graph1)) #doesn't work on list of sets, why?
    #print("graph2:", dfs_ordering(graph2)) #doesn't work on list of lists, why?
    orderings = dfs_ordering(graph3)
    print("graph3 pre:\t\t", orderings['pre'])
    print("graph3 post:\t\t", orderings['post'])
    print("graph3 rev post:\t", orderings['revpost'])

    orderings = dfs_ordering(graph_scc)
    print("\ngraph_scc rev post:\t", orderings['revpost'])





def topsort(G):
    '''
    Topological sort: used to order things with dependencies.

    Only works on directed acyclic graphs (DAG's).

    For ex, steps to make a cake, order to take school courses, etc.


    Dependencies:
        dfs_ordering
    '''
    #check if G is a DAG. if G has CYCLE, exit.
    #TODO

    #run dfs_ordering on G for EVERY node to get a complete topsort.
    orderings = dfs_ordering(G)

    '''
    result = []     #have to use list!
    #can't use a dict, b/c need the appending order. dict will reorder it.

    #node_order = []
    #get REVERSEPOST (of adj list) ordering of nodes from dfs_ordering.
    for node in orderings['revpost']:
        result.append(G[node])
    #   node_order.append(node)
    #print("graph:", G)
    #print("node_order:", node_order)
    return result
    '''
    return orderings['revpost']

def test_topsort():
    print("\nrunning test_topsort()...")                    
    print("\ngraph3")
    print("topsort graph3:", topsort(graph3))
    print("\ngraph_scc")
    print("topsort graph_scc:", topsort(graph_scc))





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

    sccs    = {}
    visited = []
    list_of_sccs    = []

    def dfs(G, x):
        visited.append(x)                       #mark as visited
        for y in G[x]:
            if y in visited:    continue        #skip visited nodes.
            dfs(G, y)                           #recursive call.

    #run dfs_ordering on reverse(G)) to get rev post ordering, 1st dfs run.
    #(i.e. run topsort on G_reverse)
    G_reverse = reverse(G)
    topsort_order = topsort(G_reverse)  #topsort_order is just reverse post.
    
    #for every node x in dfs_ordering.revpost(), run dfs. 2nd dfs run.
    count = 0
    for node in topsort_order:
        if node in visited: continue    #belongs to another SCC, skip over.
        dfs(G_reverse, node)
        sccs[node] = count
        count += 1

    return sccs


    

def test_scc():
    my_sccs = scc(graph3)
    print("\nsccs graph3:", my_sccs)

    my_sccs = scc(graph_scc)
    print("\nsccs graph_scc:", my_sccs)
    '''
    output: graph3 only has 1 strongly connected component, the entire graph
    sccs graph3: {'c': 0}

    output: graph3 has 3 strongly connected component: 
    1st) node 'h' and its' SCC (just node 'h' by itself)
    2nd) node 'e' and it's SCC.
    3rd) node 'a' and its' SCC
    sccs graph_scc: {'a': 2, 'h': 0, 'e': 1}
    '''

    tmp = []
    for node in my_sccs:
        #print(dfs_recursive(graph_scc, node))
        print((dfs_recursive(graph_scc, node)))
        #tmp.append(dfs_recursive(graph_scc, node))
    print("tmp:", tmp)

    #for node in sccs:
        #list_of_sccs.append(dfs_recursive(graph_scc, node))
    #return list_of_sccs




def main():
    #test_reverse()
    #test_dfs_ordering()
    #test_topsort()
    test_scc()

if __name__ == "__main__":
    main()
