"""
Given a binary tree, return True if it is a complete tree else False.
"""
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

from collections import deque
def completeTree(root):
    if root == None: return True
    q = deque()
    q.append(root)
    level = 0
    while q:
        count = len(q)
        prev = q[0]
        has_next_level = False
        for _ in range(count):
            cur = q.popleft()
            if prev == None and cur != None:
                return False
            prev = cur
            if cur.left:
                has_next_level = True
                q.append(cur.left)
            if cur.right:
                has_next_level = True
                q.append(cur.right)
        if has_next_level:
            if count != 2 ** level: return False
        level += 1
    return True

# Tests
root = Node(1)
a = Node(2)
b = Node(3)
c = Node(4)
d = Node(5)
e = Node(6)
root.left = a
root.right = b
a.left = c
a.right = d
b.left = e
if completeTree(root):
    print ("Complete tree!")
else:
    print ("not a Complete tree!")
