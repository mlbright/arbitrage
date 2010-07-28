"""
http://shriphani.com/blog/2010/07/02/bellman-ford-algorithms-applications-triangular-arbitrage/
"""

from bellman_ford import bellman_ford
from math import log
from collections import defaultdict
import sys

# ---------------------------------------------------------------------------- #

def negative_weight_cycle(previous,start,end):
    """ assumes there's a negative weight cycle in predecessor graph """
    path = []
    while True:
        path.append(end)
        if end == start:
            path.reverse()
            return path
        if path.count(end) > 1:
            path = path[path.index(end):]
            path.reverse()
            return path
        end = previous[end]

rates = defaultdict(dict)
symbols = set()
fd = open("test_data")
for line in fd:
    src,dst,weight = line.strip().split(',')
    symbols.add(src)
    rates[src.strip()][dst.strip()] = weight.strip()
fd.close()

graph = defaultdict(dict)

for a in symbols:
    for b in symbols:
        if a == b:
            continue
        if a in rates and b in rates[a]:
            rate = rates[a][b]
        else:
            continue
        if rate:
            rate = float(rate)
            if rate != 0.0:
                #print "%s, %s, %.2f" % (a,b,rate)
                graph[a][b] = log(1/rate)
            else:
                continue

for src in symbols:
    distances,previous,cycle = bellman_ford(graph,src)
    if cycle:
        for dst in distances:
            if dst == src:
                continue
            path = negative_weight_cycle(previous,src,dst)
            print "%s %s" % (src,dst)
            print path
