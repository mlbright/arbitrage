"""
The Bellman-Ford algorithm

Graph API:

    iter(graph) gives all nodes
    iter(graph[u]) gives neighbours of u
    graph[u][v] gives weight of edge (u, v)
    
props to: http://hetland.org/coding/python/bellman_ford.py
"""

def initialize(graph, source):
    d = {}
    p = {}
    for node in graph:
        d[node] = float('inf')
        p[node] = None
    d[source] = 0
    return d, p

def relax(u, v, graph, d, p):
    if d[v] > d[u] + graph[u][v]:
        d[v] = d[u] + graph[u][v]
        p[v] = u

def bellman_ford(graph, source):
    d, p = initialize(graph, source)
    start = None
    for i in range(len(graph)-1):
        for u in graph:
            for v in graph[u]:
                relax(u, v, graph, d, p)
    # one more relaxation to find negative weight cycle
    for u in graph:
        for v in graph[u]:
            if d[v] > d[u] + graph[u][v]:
                #relax(u, v, graph, d, p)
                start = u
                return d,p,start
    return d,p,start

def test():

    graph = {
        'a': {'b': -1, 'c':  4},
        'b': {'c':  3, 'd':  2, 'e':  2},
        'c': {},
        'd': {'b':  1, 'c':  5},
        'e': {'d': -3}
        }
    
    d, p, _ = bellman_ford(graph, 'a')
    
    assert d == {
        'a':  0,
        'b': -1,
        'c':  2,
        'd': -2,
        'e':  1
        }
    
    assert p == {
        'a': None,
        'b': 'a',
        'c': 'b',
        'd': 'e',
        'e': 'b'
        }

if __name__ == '__main__':
    test()
