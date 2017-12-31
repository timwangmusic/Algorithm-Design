from BinaryNode import BinaryNode as Node

def BT2DoublyLL(root):
    node = root
    stack = []
    prev = None
    head = None     # Doubly-linkedlist head
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if prev == None:
                head = node
            else:
                prev.right = node
                node.left = prev
            prev = node
            node = node.right
    return head

# Test case and print doubly-linked list
root = Node(10)
root.left = Node(12)
root.right = Node(15)
root.left.left = Node(25)
root.left.right = Node(30)
root.right.left = Node(36)

def printDoublyLL(head):
    while head.right != None:
        print (head.key)
        head = head.right

    while head != None:
        print (head.key)
        head = head.left

printDoublyLL(BT2DoublyLL(root))
