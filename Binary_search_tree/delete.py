# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        def find_successor(node):
            cur = node.right
            while cur and cur.left:
                cur = cur.left
            return cur
        
        if root is None:
            return None
        
        if root.val == key:
            if root.left is None:
                return root.right
            
            if root.right is None:
                return root.left
            
            p = find_successor(root)
            root.val = p.val
            root.right = self.deleteNode(root.right, p.val)
            return root
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        return root
