class BSTIterator:
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.node = root
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack or self.node

    def next(self):
        """
        :rtype: int
        """      
        while self.node:
            self.stack.append(self.node)
            self.node = self.node.left
        cur = self.stack.pop()
        self.node = cur.right
        return cur.val
