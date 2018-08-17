"""
Implement basic depth-first search to find all path from source to target.
"""


def DFS(graph, source, target, N):
    """
        graph: defaultdict(list)
            graph as adjacency list
        source: int
            source node id
        target: int
            target node id
        N: int
            number of nodes in the graph
    """
    def search(node, path):
        if node == target:
            res.append(list(path + [node]))
        else:
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    search(neighbor, path + [node])
            # back-tracking to search all paths
            visited[node] = False

    visited = [False] * (N + 1)
    res = []
    search(source, [])
    return res


if __name__=='__main__':
    graph = {1: [2, 3],
            2: [1, 4],
            3: [2, 4],
            4: [3]}
    N = 4
    source = 1
    target = 2

    print(f'The paths from {source} to {target} are: ')
    for path in DFS(graph, source, target, N):
        print(path)
