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


class UnionFind:
    def __init__(self, graph=None):
        self.graph = graph

    def makeUnionFind(self):
        for node in self.graph:
            node.parent = node
            node.rank = 0

    @staticmethod
    def find(x: UF_node) -> UF_node:
        # x is a UF_node object, find the disjoint parent of x
        r = x
        while r.parent != r:
            r = r.parent
        return r

    def union(self, x: UF_node, y: UF_node) -> None:
        # x, y are UF_node objects, join x and y to the larger parent
        ds_x = self.find(x)
        ds_y = self.find(y)

        if ds_x == ds_y:
            return

        if ds_x != ds_y:
            if ds_x.rank > ds_y.rank:
                ds_y.parent = ds_x
                y.parent = ds_x  # path compression
            elif ds_x.rank < ds_y.rank:
                ds_x.parent = ds_y
                x.parent = ds_y  # path compression
            else:
                ds_y.parent = ds_x
                ds_x.rank += 1
                y.parent = ds_x


# Testing
if __name__ == "__main__":
    a = UF_node('a')
    b = UF_node('b')
    c = UF_node('c')
    d = UF_node('d')
    e = UF_node('e')
    f = UF_node('f')
    graph = [a, b, c, d, e, f]

    # Union-find Object
    uf = UnionFind(graph)
    uf.makeUnionFind()

    # Unions
    uf.union(a, b)
    uf.union(b, c)
    uf.union(b, d)
    uf.union(d, e)
    uf.union(e, f)

    for node in graph:
        print("The node %s has rank %d" % (node.key, node.rank))
