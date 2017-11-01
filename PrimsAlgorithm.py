from nodes import MSTNode
from heapq import heappush, heappop

class Prims:
    """
    This class implement the Prim's algorithm to find the minimum spanning tree
    in an undirected weighted graph.
    """
    def __init__(self, network = [MSTNode(data = (0, 0))]):
        """
        params:
            network: a list of Minimum-spanning tree nodes that are connected per graph topology
            n: network size
        """
        self.nodes = network
        self.networkSize = len(network)
        self.heap = [(0, self.nodes[-1])]
        self.mst = []
        self.mst_cost = 0

    def findMin(self):
        cost, candidate = heappop(self.heap)
        while self.heap and candidate.visited:
            cost, candidate = heappop(self.heap)
        return candidate

    def constructMST(self):
        while len(self.mst) < self.networkSize - 1:
            node = self.findMin()
            node.visited = True
            for p in node.neighbors:
                if not p.visited:
                    new_dist = node.getDist(p)
                    if new_dist < p.cost:
                        p.cost = new_dist
                        p.keyNode = node
                        heappush(self.heap, (p.cost, p))
            if node.keyNode:
                self.mst.append((node, node.keyNode))

    def MSTCost(self):
        """
        Construct minimum-spanning tree and calculate cost.
        """
        self.constructMST()
        self.mst_cost = sum([x[0].cost for x in self.mst])
        return self.mst_cost

    def printMST(self):
        for edge in self.mst:
            print ("(%d, %d)" % (edge[0].key, edge[1].key))

class Test():
    def __init__(self):
        s = MSTNode(key = 0, data = (0,10))
        a = MSTNode(key = 1, data = (-3, 0))
        b = MSTNode(key = 2, data = (-5,10))
        c = MSTNode(key = 3, data = (5,0))
        d = MSTNode(key = 4, data = (20,-5))
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
