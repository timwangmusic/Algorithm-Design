# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root == None: return None
        first = None
        stack = []
        cur = root
        prev = None
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if not first:
                    first = cur
                cur.left = prev
                if prev: 
                    prev.right = cur
                prev = cur
                cur = cur.right
        first.left = prev
        prev.right = first
        return first
