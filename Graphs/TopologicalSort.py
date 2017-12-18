"""
* For directed graphs, topological sort tries to find a topological order so that the nodes visited
earlier does not depend on nodes visited later.
* This is a highly simplified implementation, suitable for quick usage in functions.
"""
from collections import defaultdict, deque
def TopologicalSort(edges, nodes = None):
    """
    :type edges: List[List[String]]
    :type nodes: List[String]
    :rtype: List[String]
    """
    indegrees = {node: 0 for node in nodes}
    graph = defaultdict(set)
    queue = deque()
    res = []

    for x, y in edges:
        if x in graph[y]: return []                 # Loop found, no topological sort possible
        indegrees[y] += 1
        graph[x].add(y)

    for node in indegrees:
        if indegrees.get(node, 0) == 0:
            queue.append(node)

    while queue:
        node = queue.popleft()                      # current node to visit
        res.append(node)
        for neighbor in graph[node]:
            if indegrees.get(neighbor, 0) > 0:      # node has not been visited
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
    return res

nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
edges = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['C', 'D'], ['C', 'E'], ['E', 'G'], ['D', 'F'], ['F', 'G']]
print (TopologicalSort(edges, nodes))               # Prints ['A', 'B', 'C', 'E', 'D', 'F', 'G']
