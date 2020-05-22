import collections
import heapq
from typing import List

"""
Skyline problem

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed
from a distance. Now suppose you are given the locations and height of all the buildings,
output the skyline formed by these buildings collectively.

Computational complexity:
O(N*logN) where N is number of buildings
"""


def getSkyline(buildings: List[List[int]]) -> List[List[int]]:
    points = []
    for left, right, height in buildings:
        # x-axis, height and if the event is building starts
        points.append((left, height, True))
        points.append((right, height, False))

    heap = []  # max heap
    points.sort(key=lambda p: p[:1])

    counter = collections.Counter()  # tracking valid elements in heap
    start, end = 0, 0
    res = []
    prev_h = None
    # for each unique x-axis value, compute a height
    while start < len(points):
        x, h, _ = points[start]
        while end < len(points):
            ex, eh, end_building_start = points[end]
            if ex > x:
                break
            if end_building_start:
                counter[eh] += 1
                heapq.heappush(heap, -eh)
            else:
                counter[eh] -= 1
            end += 1

        # remove invalid elements from heap
        while heap and counter[-heap[0]] == 0:
            heapq.heappop(heap)

        cur_h = -heap[0]
        if cur_h != prev_h:
            res.append([x, cur_h])
            prev_h = cur_h
        start = end
    return res
