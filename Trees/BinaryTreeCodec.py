# Iterative version
from BinaryNode import BinaryNode
from collections import deque
class BinaryTreeCodec:
    def __init__(self):
        self.vals = []

    def Encode(self, root):
        """
        type root: BinaryNode
        rtype: str
        """
        if root == None: return ""
        self.vals.clear()
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node == None:
                self.vals.append("*")
                continue
            self.vals.append(str(node.key))
            q.append(node.left)
            q.append(node.right)
        return " ".join(self.vals)


    def Decode(self, code):
        """
        type code: str
        rtype: BinaryNode
        """
        code = code.split(" ")
        if len(code) == 0 or code[0] == '*': return None
        q = deque()
        root = BinaryNode(code[0])
        q.append(root)
        idx = 1
        while idx < len(code):
            node = q.popleft()
            if code[idx] != '*':
                node.left = BinaryNode(int(code[idx]))
                q.append(node.left)
            if code[idx+1] != '*':
                node.right = BinaryNode(int(code[idx+1]))
                q.append(node.right)
            idx += 2
        return root

codec = BinaryTreeCodec()
root = BinaryNode(20)
root.left = BinaryNode(10)
root.right = BinaryNode(200)
root.left.right = BinaryNode(50)
root.right.left = BinaryNode(75)

print (codec.Encode(root))
root = codec.Decode(codec.Encode(root))

def preorder(root):
    if root == None: return
    print (root.key)
    preorder(root.left)
    preorder(root.right)

preorder(root)
