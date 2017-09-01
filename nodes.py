from math import sqrt
import sys, heapq
class node():
    """
    Basic node class for Undirected Graphs.
    Params:
        : key: node ID
        : data: data the node holds, such as location or other high dimensional data
        : neighbors: references to neighbors of the current node
        : nodes: a list of nodes to be added/removed as neighbors
    """
    def __init__(self, key = 0, data = None):
        self.key = key
        self.data = data
        self.neighbors = {self}

    def addEdges(self, nodes):
        for node in nodes:
            self.neighbors.add(node)

    def removeEdges(self, nodes):
        for node in nodes:
            # using discard does not to worry about key error
            if node is not self:
                self.neighbors.discard(node)

    def isNeighbor(self, node):
        return node in self.neighbors

class MSTNode(node):
    """
    Node class for minimum-spanning tree (MST)
    Params:
        : keyNode: type: MstNode, node via which the node is connected to MST
        : cost: type: float, distance to keyNode
    """
    def __init__(self, keyNode = None, key = 0, data = None):
        node.__init__(self, key, data)
        self.keyNode = keyNode
        self.cost = float('inf')
        self.visited = False

    def getDist(self, w):
        """
        Calculate the distance from node to neighbor w
        If w is not a neighbor, return infinity
        rtype: float
        """
        if w not in self.neighbors: return float('inf')
        x, y = self.data
        x_w, y_w = w.data
        return sqrt((x-x_w)**2 + (y-y_w)**2)
