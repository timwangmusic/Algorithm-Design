# Implement solution to the Merge K-sorted Lists Problem
from heapq import heapify, heappush, heappop
def merge(lists):
    """
    input: k sorted lists List[List[int]], each containing at least one element
    output: a merged sorted list List[int]
    """
    k = len(lists)
    l = [0] * k     # list indexes
    res = []
    s = set(range(k))
    heap = [(lists[i][0],i) for i in range(k)]
    heapify(heap)
    while s:
        # while there is any element left in any list
        cur_min = heappop(heap)
        num, list_ind = cur_min
        res.append(num)
        if l[list_ind] == len(lists[list_ind]) - 1:
            s.remove(list_ind)
        else:
            l[list_ind] += 1
            temp = lists[list_ind][l[list_ind]]
            heappush(heap, (temp, list_ind))
    return res

# Tests
l1 = list(range(40,50))
l2 = list(range(5))
l3 = list(range(5,7))
print (merge([l1,l2,l3]))
