# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = collections.deque([root])
        level = 0
        next_layer_count = 1
        while q:
            count = next_layer_count
            last = -1
            next_layer_count = 0
            for _ in range(count):
                node = q.popleft()
                if node is None and last != None:
                    return False
                last = node
                if node is None: continue
                if node.left:
                    q.append(node.left)
                    next_layer_count += 1
                else:
                    q.append(None)
                if node.right:
                    q.append(node.right)
                    next_layer_count += 1
                else:
                    q.append(None)
                    
            if count < 2**level and next_layer_count > 0:
                return False
            elif next_layer_count == 0:
                break
            level += 1
        return True
    
