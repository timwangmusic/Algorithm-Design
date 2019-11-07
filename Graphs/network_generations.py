from Graphs.nodes import Node
import random


class generateNetwork:
    def __init__(self):
        self.lastKey = -1

    def generateRandomNodes(self, numNodes=8, dim=2, val_start=0, val_end=100):
        """
        Return a list of nodes with random values, using random.uniform function.
        """
        random.seed()
        cur_key = self.lastKey + 1
        nodes = []
        for i in range(numNodes):
            new_data = [random.uniform(val_start, val_end) for _ in range(dim)]
            nodes.append(Node(key=cur_key, data=new_data))
            cur_key += 1
        self.lastKey += numNodes
        return nodes

    def constructNetwork(self, nodes):
        pass


class generateTree(generateNetwork):
    """
    Derived from generate network class.
    Construct network function constructs a tree with random connection, given a list of nodes.
    The collection of trees created is saved in the forest variable.
    """

    def __init__(self):
        generateNetwork.__init__(self)
        self.forest = []

    def constructNetwork(self, nodes):
        random.seed()
        random.shuffle(nodes)  # randomization
        root = None
        tree = []
        parent = None
        while nodes:
            n = nodes.pop()
            if tree:
                parent = random.choice(tree)
                parent.addEdges([n])
            else:
                root = n
            tree.append(n)
        self.forest.append(root)

    def _print(self, node):
        if node is None:
            return
        print(node.key)
        for n in node.neighbors:
            self._print(n)


class Test:
    def __init__(self):
        pass

    @staticmethod
    def generatePrint(numTrees=3):
        gt = generateTree()
        for i in range(numTrees):
            gt.constructNetwork(gt.generateRandomNodes())
            gt._print(gt.forest[-1])


Test.generatePrint()
