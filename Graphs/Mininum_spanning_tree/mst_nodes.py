from Graphs.nodes import Node
from math import sqrt


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
