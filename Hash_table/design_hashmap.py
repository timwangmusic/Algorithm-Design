class MyHashMap:

    def __init__(self):
        """
        The value range for keys will be [1, 1000000]. 
        Use simple residual hash function to map keys to buckets.
        Since each bucket contains at most 100 keys, search and insert can be considered O(1).
        Remove is also O(1).
        """
        self.buckets = 10000
        self.hashmap = [list() for _ in range(self.buckets)]
        

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        bucket = key % self.buckets
        for ix, (k, v) in enumerate(self.hashmap[bucket]):
            if k == key:
                self.hashmap[bucket][ix] = key, value
                return
        self.hashmap[bucket].append((key, value))
            

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        bucket = key % self.buckets
        for k, v in self.hashmap[bucket]:
            if k == key:
                return v
        return -1
        
        
    def swap(self, l, left, right):
        l[left], l[right] = l[right], l[left]
        
        
    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        bucket = key % self.buckets
        for ix, (k, v) in enumerate(self.hashmap[bucket]):
            if k == key:
                self.swap(self.hashmap[bucket], ix, len(self.hashmap[bucket])-1)
                self.hashmap[bucket].pop()
                return
                
