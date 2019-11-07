"""
Simple dijkstra's algorithm implementation with priority queue
"""


def dijkstra(edges, source, nodes=1):
    """
    edges: List[List]
        list of edges: start-node, end-node and weight
    source: int
        source node
    N: int
        total number of nodes in the graph
    """
    import collections, heapq
    graph = collections.defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        # shortest distance
        dist = {}
        # priority queue
        heap = [(0, source)]
    while heap:
        dd, node = heapq.heappop(heap)
        if node in dist:
            continue
        dist[node] = dd
        for neighbor, w in graph[node]:
            if neighbor not in dist:
                heapq.heappush(heap, (dd + w, neighbor))
    return dist


if __name__ == '__main__':
    edges = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    source = 2
    N = 4
    from pprint import pprint as pp

    pp(dijkstra(edges, source, nodes=N))
