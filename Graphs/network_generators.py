from Graphs.nodes import Node
import random


class NodeGenerator:
    def __init__(self):
        self.lastKey = -1

    def generate_nodes(self, numNodes=10, dim=2, val_start=0, val_end=100):
        """
        Return a list of nodes with random values, using random.uniform function.
        Each call to generate_nodes generates a list of nodes with unique keys.
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

    def construct_graph(self, nodes):
        pass


class TreeGenerator(NodeGenerator):
    """
    Construct network function constructs a tree with random connections.
    The number of children for any node in the tree is random as well.
    The collection of trees created is saved in the forest variable.
    """

    def __init__(self):
        NodeGenerator.__init__(self)
        self.forest = []

    def construct_graph(self, nodes):
        random.seed()
        random.shuffle(nodes)  # randomization
        root = None
        tree = []
        while nodes:
            n = nodes.pop()
            if len(tree) > 0:
                # grow new tree from randomly selected node already added to the tree
                parent = random.choice(tree)
                parent.addEdges([n])
            else:
                root = n
            tree.append(n)
        self.forest.append(root)

    # pre-order printing with depth-first search
    def print_tree(self, node):
        if node is None:
            return
        print(node.key)
        for n in node.neighbors:
            self.print_tree(n)


class Test:
    def __init__(self):
        pass

    @staticmethod
    def test_tree_construction(numTrees=2):
        tree_generator = TreeGenerator()
        for idx in range(1, numTrees + 1):
            print(f"printing tree #{idx}")
            tree_generator.construct_graph(tree_generator.generate_nodes(numNodes=5))
            tree_generator.print_tree(tree_generator.forest[-1])


Test.test_tree_construction()
