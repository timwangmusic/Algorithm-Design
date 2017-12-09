# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from heapq import heapify, heappush, heappop
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        elementLeft = [True] * len(lists)
        for i, l in enumerate(lists):
            if l != None:
                heap.append((l.val, i))
            else:
                elementLeft[i] = False
        res = ListNode(0)   # dummy node
        p = res
        heapify(heap)
        while any(elementLeft):
            val, listind = heappop(heap)
            p.next = lists[listind]
            p = p.next
            lists[listind] = lists[listind].next
            if lists[listind] == None:
                elementLeft[listind] = False
            else:
                heappush(heap, (lists[listind].val, listind))
        return res.next
