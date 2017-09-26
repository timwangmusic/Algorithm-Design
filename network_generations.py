from nodes import node
from random import choice
class generateNetwork:
    def __init__(self, nodes):
        self.nodes = nodes

    def constructNetwork(self):
        pass

class generateTree(generateNetwork):
    """
    Subclass of generate network.
    Construct a random tree, given a list of disjoint nodes.
    """
    def __init__(self, nodes):
        generateNetwork.__init__(self, nodes)
        self.node_set = set(self.nodes)
        self.root = None
        self.tree = []

    def constructNetwork(self):
        parent = None
        while self.node_set:
            n = self.node_set.pop()
            if self.tree:
                parent = choice(self.tree)
                parent.addEdges([n])
            else:
                self.root = n
            self.tree.append(n)

    def _print(self, node):
        if node == None: return
        print (node.key)
        for n in node.neighbors:
            self._print(n)

class Test:
    def __init__(self):
        s = node(key = 0, data = (0,0))
        a = node(key = 1, data = (-3, 0))
        b = node(key = 2, data = (-5,0))
        c = node(key = 3, data = (5,-10))
        d = node(key = 4, data = (20,100))
        self.node_list = [s, a, b, c, d]

    def generate(self):
        gt = generateTree(self.node_list)
        gt.constructNetwork()
        gt._print(gt.root)

Tester = Test()
Tester.generate()
