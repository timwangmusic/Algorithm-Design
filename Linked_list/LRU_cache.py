"""
Implement a basic least recently used cache with linked list.

Keys are used by put and get operations.
When new keys are inserted, check if capacity is reached. If so, evict the least recently used key.
"""


class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity

        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.nodes = {}  # store key --> node map

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        self.moveToHead(key)
        return self.nodes[key].val

    def evict(self) -> None:
        node = self.tail.prev
        node.prev.next = self.tail
        self.tail.prev = node.prev

        self.nodes.pop(node.key)

    def insertToHead(self, node: Node) -> None:
        # insert node to the head
        tmp = self.head.next

        self.head.next = node
        node.prev = self.head

        tmp.prev = node
        node.next = tmp

    def moveToHead(self, key) -> None:
        node = self.nodes[key]
        next_node = node.next
        prev_node = node.prev
        prev_node.next = next_node
        next_node.prev = prev_node
        self.insertToHead(node)

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            self.nodes[key].val = value
            self.moveToHead(key)
            return
        new_node = Node(key, value)
        if len(self.nodes) == self.cap:
            self.evict()

        self.insertToHead(new_node)

        self.nodes[key] = new_node
