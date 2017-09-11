from nodes import MSTNode
from heapq import heapify, heappush, heappop
from collections import defaultdict
import sys

class Prims():
    """
    This class implement the Prim's algorithm to find the minimum spanning tree
    in an undirected weighted graph.
    """
    def __init__(self, network):
        """
        params:
            network: a list of Minimum-spanning tree nodes that are connected per graph topology
            n: network size
        """
        self.nodes = network
        self.Q = network
        self.mst = []
        self.cost = 0

    def findMin(self):
        candidate = None
        cost = float('inf')
        for node in self.Q:
            if node.cost <= cost:
                cost = node.cost
                candidate = node
        self.Q.remove(candidate)
        return candidate

    def constructMST(self):
        while self.Q:
            node = self.findMin()
            node.visited = True
            print (node.key)
            for p in node.neighbors:
                if p.visited: continue
                new_dist = node.getDist(p)
                if new_dist < p.cost:
                    p.cost = new_dist
                    p.keyNode = node
            if node.keyNode:
                self.mst.append((node, node.keyNode))

    def MSTCost(self):
        self.constructMST()
        self.cost = sum([x[0].cost for x in self.mst])
        return self.cost

    def printMST(self):
        for edge in self.mst:
            print ("(%d, %d)" % (edge[0].key, edge[1].key))

class Test():
    def __init__(self):
        s = MSTNode(key = 0, data = (0,0))
        a = MSTNode(key = 1, data = (-3, 0))
        b = MSTNode(key = 2, data = (-5,0))
        c = MSTNode(key = 3, data = (5,0))
        d = MSTNode(key = 4, data = (20,0))
        s.addEdges([a, b, c, d])
        a.addEdges([s, b, d])
        b.addEdges([s, a])
        c.addEdges([s, d, a])
        d.addEdges([s, c])
        self.network = [s, a, b, c, d]

    def runAlgorithm(self):
        self.prims = Prims(self.network)
        self.prims.constructMST()
        print ("The edges of minimum spanning tree are: ")
        self.prims.printMST()
        print ("The total cost of building minimum spanning tree is %.2f" % self.prims.MSTCost())

test = Test()
test.runAlgorithm()
