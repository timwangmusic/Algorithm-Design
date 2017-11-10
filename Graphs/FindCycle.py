"""
For a simplified undirected graph represented by edges [(a, b), (b, d), (d, a), (k, e)],
in which (x, y) means node with key x connects to node with key y.
Find cycle function answers the question if the graph has cycle.
Using Union-find data structure, we can create multiple disjoint sets.
"""
from Union_Find import UF_node, Union_Find

def findCycle(graph):
    vertex_set = set()          # get vertex keys
    for x, y in graph:
        vertex_set.add(x)
        vertex_set.add(y)
    nodes = {n: UF_node(n) for n in vertex_set}
    uf = Union_Find()
    for x, y in graph:
        ds_x = uf.find(nodes[x])
        ds_y = uf.find(nodes[y])
        if ds_x == ds_y:
            return True
        else:
            uf.union(nodes[x], nodes[y])
    return False

# Testing
graph1 = [(1, 2), (3, 4), (1, 4), (2, 4), (5, 6)]
graph2 = [(1, 2), (3, 4), (4, 5), (5, 1), (2, 6)]
for graph in [graph1, graph2]:
    if findCycle(graph):
        print ('There is cycle in graph %s.' % str(graph))
    else:
        print ('No cycle detected in graph %s.' % str(graph))
