from BinaryTrees import TreeNode
# All algorithms are implemented iteratively

def IterativePreorder(node):
    stack = [node]
    traversal_res = []
    while stack:
        node = stack.pop()
        traversal_res.append(node.key)
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
    return traversal_res


def IterativeInorder(node):
    stack = []
    traversal_res = []
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            traversal_res.append(node.key)
            node = node.right
    return traversal_res


def IterativePostorder(node):
    stack = []
    lastVisited = None
    traversal_res = []
    while (stack or node):
        if node:
            stack.append(node)
            node = node.left
        else:
            peekNode = stack[-1]
            if (peekNode.right and peekNode.right != lastVisited):
                node = peekNode.right
            else:
                traversal_res.append(peekNode.key)
                lastVisited = stack.pop()
    return traversal_res

# build a tree and testing
# Postorder shall output: [100, 200, 300, 500]
# Preorder shall output: [500, 300, 200, 100]
# Inorder shall output: [300, 200, 100, 500]
root = TreeNode(500)
a = TreeNode(300)
b = TreeNode(200)
c = TreeNode(100)
root.left = a
a.right = b
b.right = c
print ("The postorder traversal result is: ", IterativePostorder(root))
print ("The preorder traversal result is: ", IterativePreorder(root))
print ("The inorder traversal result is: ", IterativeInorder(root))
