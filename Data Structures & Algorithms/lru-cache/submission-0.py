class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # key to node

        self.capacity = capacity

        # doubly linked list for LRU functionality
        self.left = Node(-1, -1) # least recently used
        self.right = Node(-1, -1) # most recently used
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node): # insert on the right side
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        self.right.prev = node
        node.next = self.right


    def remove(self, node): # remove from doubly linked list
        prv, nxt = node.prev, node.next
        prv.next = nxt
        nxt.prev = prv


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
        else:
            node = Node(key, value)
            lru = self.left.next
            self.cache[key] = node
            self.insert(node)
            if len(self.cache) > self.capacity:
                self.remove(lru)
                del self.cache[lru.key]

        
