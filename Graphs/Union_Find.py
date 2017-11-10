"""
Implement a general union-find/disjoint parent data structure.
Params:
    graph: a list of union-find node objects, which have pointers to their component nodes.
"""
class UF_node:
    def __init__(self, val):
        self.key = val
        self.parent = self
        self.rank = 0

class Union_Find:
    def __init__(self, graph = None):
        self.graph = graph

    def makeUnionFind(self):
        for node in self.graph:
            node.parent = node
            node.rank = 0

    def find(self, x):
        # x is a UF_node object, find the disjoint parent of x
        r = x
        while r.parent != r:
            r = r.parent
        return r

    def union(self, x, y):
        # x, y are UF_node objects, join x and y to the larger parent
        ds_x = self.find(x)
        ds_y = self.find(y)
        if ds_x == ds_y:
            return

        if ds_x != ds_y:
            if ds_x.rank > ds_y.rank:
                ds_y.parent = ds_x
            elif ds_x.rank < ds_y.rank:
                ds_x.parent = ds_y
            else:
                ds_y.parent = ds_x
                ds_x.rank += 1

# Testing
a = UF_node(10)
b = UF_node(20)
c = UF_node(40)
d = UF_node(55)
e = UF_node(100)
graph = [a, b, c, d, e]

# Union-find Object
uf = Union_Find(graph)
uf.makeUnionFind()

# Unions
uf.union(a, b)
uf.union(b, c)
uf.union(b, d)
uf.union(d, e)

# for node in graph:
    # print ("The node %d has rank %d" % (node.key, node.rank))
