"""
Analysis:

Take the idea from LRU cache, inc freq of an item and move the node to the list with new freq.
Track linked-list node reference with hash table
Track linked-list head with frequency count
For evictions, we need to track the least frequency
If the current LF = 3, and there are 2 items with freq=3. After eviction LF = 1.
If the current LF = 3, and there are just 1 item with freq=3. After eviction LF = 1.
If current LF = 1, after eviction LF = 1.

"""
import collections


class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.heads = {}  # freq-->(head, tail) mapping
        self.nodes = {}  # key-->node mapping
        self.least_freq = 0
        self.frequencies = {}  # node-->freq mapping
        self.counter = collections.Counter()

    def insert_to_head(self, node: Node, freq: int):
        if freq not in self.heads:
            self.create_list(freq)

        head, tail = self.heads[freq]
        tmp = head.next

        node.prev = head
        node.next = tmp

        head.next = node
        tmp.prev = node

        self.counter[freq] += 1
        self.frequencies[node] = freq

    def remove_from_tail(self, freq: int):
        _, tail = self.heads[freq]
        last = tail.prev
        self.counter[freq] -= 1
        if self.counter[freq] == 0:
            self.counter.pop(freq)
        self.nodes.pop(last.key)
        self.frequencies.pop(last)

        tmp = last.prev
        tmp.next = tail
        tail.prev = tmp

    def remove_node(self, node: Node):
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def create_list(self, freq: int):
        head, tail = Node(-1, -1), Node(-1, -1)
        head.next = tail
        tail.prev = head
        self.heads[freq] = (head, tail)

    def inc_key(self, key: int):
        node = self.nodes[key]

        self.remove_node(node)

        prev_freq = self.frequencies[node]
        self.counter[prev_freq] -= 1
        if self.counter[prev_freq] == 0:
            self.counter.pop(prev_freq)

        self.frequencies[node] += 1
        freq = self.frequencies[node]

        self.insert_to_head(node, freq)

        if self.least_freq not in self.counter:
            self.least_freq += 1

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1

        self.inc_key(key)

        return self.nodes[key].val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.nodes:
            self.inc_key(key)
            self.nodes[key].val = value
            return

        if len(self.nodes) == self.capacity:
            self.remove_from_tail(self.least_freq)

        self.least_freq = 1
        new_node = Node(key, value)

        self.insert_to_head(new_node, 1)
        self.nodes[key] = new_node
