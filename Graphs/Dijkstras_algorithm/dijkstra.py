"""
Simple implementation for the dijkstra's algorithm with priority queue
"""
import collections
import heapq


def dijkstra(edges, source_node):
    """
    edges: List[List]
        list of directed edges: start-node, end-node and weight
    source_node: int
        source node
    N: int
        total number of nodes in the graph
    return: dict
        key-value pair for shortest distances for each node from the source
    """
    graph = collections.defaultdict(list)

    for u, v, w in edges:
        graph[u].append((v, w))

    dist = {}  # shortest distance

    heap = [(0, source_node)]
    while heap:
        dd, node = heapq.heappop(heap)
        if node in dist:
            continue
        dist[node] = dd
        for neighbor, w in graph[node]:
            if neighbor not in dist:  #
                heapq.heappush(heap, (dd + w, neighbor))
    return dist


if __name__ == '__main__':
    input_edges = [[1, 2, 3], [1, 3, 1], [3, 2, 1], [3, 4, 4], [2, 4, 1]]
    source = 1

    print(f"the distance from source node {source} to all other nodes in the graph are:")
    for node_idx, dist in dijkstra(input_edges, source).items():
        print(f"the distance from source to {node_idx} is {dist}")
