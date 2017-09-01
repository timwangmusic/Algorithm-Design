from nodes import MSTNode
from collections import defaultdict

class Kruskals():
    def __init__(self, network):
        self.nodes = network
        self.networkSize = len(self.nodes)
        self.edges = defaultdict(list)
        self.clusters = [-1] * self.networkSize
        for i, node in enumerate(network):
            for j in range(i+1, self.networkSize):
                if node.isNeighbor(network[j]):
                    dist = node.getDist(network[j])
                    self.edges[dist].append((node, network[j]))
        self.mst = []
        # iterator for generating next shortest edge, together with self.edges
        self._iter = iter(sorted(list(self.edges)))
        self.last_dist = next(self._iter)

    def next(self):
        if self.hasNext():
            return self.edges[self.last_dist].pop()
        return None

    def hasNext(self):
        if self.edges[self.last_dist]:
            return True
        try:
            self.last_dist = next(self._iter)
        except StopIteration:
            return False
        return True

    def findCluster(self, node):
        if self.clusters[node.key] == -1:
            return node.key
        parent = self.nodes[self.clusters[node.key]]
        return self.findCluster(parent)

    def union(self, x, y):
        cluster_x = self.findCluster(x)
        cluster_y = self.findCluster(y)
        if cluster_x != cluster_y:
            self.clusters[cluster_x] = cluster_y
            self.mst.append((x,y))

    def constructMST(self):
        while self.hasNext():
            x,y = self.next()
            # Union-Find
            self.union(x,y)

    def MSTCost(self):
        self.cost = 0
        for x,y in self.mst:
            self.cost += x.getDist(y)
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
        self.kruskals = Kruskals(self.network)
        self.kruskals.constructMST()
        print ("The edges of minimum spanning tree are: ")
        self.kruskals.printMST()
        print ("The total cost of building minimum spanning tree is %.2f" % self.kruskals.MSTCost())

test = Test()
test.runAlgorithm()
