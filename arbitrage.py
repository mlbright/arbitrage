"""
http://shriphani.com/blog/2010/07/02/bellman-ford-algorithms-applications-triangular-arbitrage/
"""

from bellman_ford import bellman_ford
from math import log
from collections import defaultdict
import sys

# ---------------------------------------------------------------------------- #

def has_negative_weight_cycle(distances):
    for d in distances:
        if distances[d] == -float('inf'):
            return True
    return False
    
def negative_weight_cycle(predecessor,start,end):
    """ assumes there's a negative weight cycle in predecessor graph """
    path = []
    while True:
        path.append(end)
        if path.count(end) > 1:
            path = path[path.index(end):]
            path.reverse()
            return path
        end = predecessor[end]

symbols = set()
graph = defaultdict(dict)
for line in sys.stdin:
    src,dst,weight = line.strip().split(',')
    symbols.add(src)
    symbols.add(dst)
    rate = float(weight.strip())
    if rate != 0.0:
        graph[src.strip()][dst.strip()] = log(1/rate)

for src in symbols:
    distances,predecessors = bellman_ford(graph,src)
    for dst in distances:
        if dst == src:
            continue
        if distances[dst] == -float('inf'):
            print "%s -> %s" % (src,dst)
            path = negative_weight_cycle(predecessors,src,dst)
            print path
