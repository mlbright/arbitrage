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
            print "reached v..."
        if end in path:
            path = path[path.index(end):]
            break
        end = previous[end]
    path.reverse()
    return path

rates = defaultdict(dict)
fd = open("test_data")
for line in fd:
    src,dst,weight = line.strip().split(',')
    rates[src.strip()][dst.strip()] = weight.strip()
fd.close()

symbols = []
for line in currencies.split("\n"):
    elements = line.strip().split()
    if elements:
        symbols.append(elements[-1])

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
                print "%s, %s, %.2f" % (a,b,rate)
                graph[a][b] = log(1/rate)
            else:
                continue

for src in symbols:
    d,p,cycle = bellman_ford(graph,src)
    if cycle:
        print negative_weight_cycle(p,src,src)
