# Implement solution to the Merge K-sorted Lists Problem
import heapq
def merge(lists):
    """
    input: k sorted lists List[List[int]], each containing at least one element
    output: a merged sorted list List[int]
    """
    heap = []
    k = len(lists)
    l = [0] * k
    res = []
    s = set(range(k))
    for i, ind in enumerate(l):
        heapq.heappush(heap, (lists[i][ind], i))
    while s:
        # while there is any element left in any list
        cur_min = heapq.heappop(heap)
        num, list_ind = cur_min
        res.append(num)
        if l[list_ind] == len(lists[list_ind]) - 1:
            s.remove(list_ind)
        else:
            l[list_ind] += 1
            temp = lists[list_ind][l[list_ind]]
            heapq.heappush(heap, (temp, list_ind))
    return res

# Tests
l1 = list(range(40,50))
l2 = list(range(5))
l3 = list(range(7))
print (merge([l1,l2,l3]))
