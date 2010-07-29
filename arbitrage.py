"""
http://shriphani.com/blog/2010/07/02/bellman-ford-algorithms-applications-triangular-arbitrage/
"""

from bellman_ford import bellman_ford
from math import log
from collections import defaultdict
import sys

# ---------------------------------------------------------------------------- #

def find_path(predecessor,start,end):
    """ assumes path exists from start to end """
    path = []
    while True:
        path.append(end)
        if end == start:
            path.reverse()
            return path
        end = predecessor[end]

def negative_weight_cycle(predecessor,end):
    path = []
    while True:
        path.append(end)
        if path.count(end) > 1:
            path = path[path.index(end):]
            path.reverse()
            path = path[path.index(end):]
            return path 
        end = predecessor[end]

symbols = set()
graph = defaultdict(dict)
for line in sys.stdin:
    src,dst,weight = (s.strip() for s in line.split(','))
    symbols.add(src)
    symbols.add(dst)
    rate = float(weight)
    if rate != 0.0:
        graph[src][dst] = log(1/rate)

for src in symbols:
    distances,predecessors,cycle_vertex = bellman_ford(graph,src)
    if cycle_vertex is not None:
        print negative_weight_cycle(predecessors,cycle_vertex)
        sys.exit()
    else:
        # debugging stuff, delete this
        print " does not have a negative weight cycle"
        for dst in distances:
            if src == dst or distances[dst] == float('inf'):
                continue
            print find_path(predecessors,src,dst)
