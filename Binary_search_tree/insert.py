# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None: return TreeNode(val)
        
        prev = None
        node = root

        while node:
            prev = node
            if node.val < val:
                node = node.right
            else:
                node = node.left

        if prev.val < val:
            prev.right = TreeNode(val)
        else:
            prev.left = TreeNode(val)
            
        return root
        
