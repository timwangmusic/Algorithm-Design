from math import sqrt


class Node:
    """
    Basic node class for directed graphs.
    Params:
        : key: integer, node ID
        : data: data the node holds, can be 2-d vector as such location or other high dimensional vector
        : neighbors: references to neighbors of the current node
        : nodes: a list of nodes to be added/removed as neighbors
    """

    def __init__(self, key: int = 0, data=None):
        self.key = key
        self.data = data
        self.neighbors = set()

    def addEdges(self, nodes):
        for node in nodes:
            self.neighbors.add(node)

    def removeEdges(self, nodes):
        for node in nodes:
            # using discard does not to raise key error
            self.neighbors.discard(node)

    def isNeighbor(self, node):
        return node in self.neighbors



