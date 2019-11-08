"""
Implement Tarjan's algorithm to find strongly connected components (SCC) in a directed graph

low_link of a node v represents the smallest index of any node known to be reachable from v through v's DFS subtree
"""
from typing import List

from Graphs.Tarjans_algorithm.tarjan_node import TarjanNode


class Tarjan:
    def __init__(self, nodes: List[TarjanNode]):
        self.nodes = nodes
        self.sccs = []  # each strongly connected components is stored as a list of nodes
        self.next_idx = 1  # starting index being 1 to avoid not 0 == True
        self.stack = []

    def find_sccs(self):
        for node_ in self.nodes:
            if not node_.key:
                self.__strong_connect(node_)

    def __strong_connect(self, node_: TarjanNode):
        node_.key = self.next_idx
        self.next_idx += 1
        self.stack.append(node_)
        node_.on_stack = True
        node_.low_link = node_.key  # initialize low_link with key value

        for neighbor in node_.neighbors:
            if not neighbor.key:
                self.__strong_connect(neighbor)
            elif neighbor.on_stack:
                node_.low_link = min(node_.low_link, neighbor.key)

        if node_.low_link == node_.key:
            new_scc = []
            while self.stack[-1] != node_:
                last_node_on_stack = self.stack[-1]
                last_node_on_stack.on_stack = False
                new_scc.append(self.stack.pop())
            new_scc.append(self.stack.pop())
            node_.on_stack = False
            self.sccs.append(new_scc)


if __name__ == "__main__":
    a = TarjanNode(None, "a")
    b = TarjanNode(None, "b")
    c = TarjanNode(None, "c")
    d = TarjanNode(None, "d")
    e = TarjanNode(None, "e")
    f = TarjanNode(None, "f")
    a.addEdges([b, c])
    b.addEdges([c, a])
    c.addEdges([b])
    d.addEdges([c, e])
    e.addEdges([d, f])
    tarjan = Tarjan([a, b, c, d, e])
    tarjan.find_sccs()
    # expected output:
    # Strongly connected component #1 ['c', 'b', 'a']
    # Strongly connected component #2 ['e', 'd']
    for idx, scc in enumerate(tarjan.sccs, 1):
        print(f"Strongly connected component #{idx}", [node.data for node in scc])
