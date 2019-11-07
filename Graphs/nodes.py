from math import sqrt


class Node:
    """
    Basic node class for Undirected Graphs.
    Params:
        : key: node ID
        : data: data the node holds, can be 2-d vector as such location or other high dimensional vector
        : neighbors: references to neighbors of the current node
        : nodes: a list of nodes to be added/removed as neighbors
    """

    def __init__(self, key=0, data=None):
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


class MSTNode(Node):
    """
    Node class for minimum-spanning tree (MST)
    Params:
        : keyNode: type: MstNode, node via which the node is connected to MST
        : cost: type: float, distance to keyNode
    """

    def __init__(self, keyNode=None, key=0, data=None):
        Node.__init__(self, key, data)
        self.keyNode = keyNode
        self.cost = float('inf')
        self.visited = False

    def getDist(self, w):
        """
        Calculate the distance from node to neighbor w
        If w is not a neighbor, return infinity
        rtype: float
        """
        if w not in self.neighbors:
            return float('inf')
        x, y = self.data
        x_w, y_w = w.data
        return sqrt((x - x_w) ** 2 + (y - y_w) ** 2)
