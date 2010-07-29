"""
http://shriphani.com/blog/2010/07/02/bellman-ford-algorithms-applications-triangular-arbitrage/
"""

from bellman_ford import bellman_ford
from math import log
from collections import defaultdict
import sys

# ---------------------------------------------------------------------------- #

def find_path(predecessor,start,end):
    path = []
    while True:
        path.append(end)
        if end == start:
            print "found simple path..."
            path.reverse()
            return path
        if path.count(end) > 1:
            print "found cycle!"
            cycle = path[path.index(end):]
            cycle.reverse()
            return cycle 
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
    print "source %s ..." % (src),
    distances,predecessors,has_negative_weight_cycle = bellman_ford(graph,src)
    if has_negative_weight_cycle:
        print " has negative weight cycle"
    else:
        print " does not have negative weight cycle"
    """
        continue
        for dst in distances:
            if dst == src or distances[dst] == float('inf'):
                continue
            path = find_path(predecessors,src,dst)
            print path
    """
