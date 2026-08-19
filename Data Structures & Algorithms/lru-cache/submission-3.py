class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        # key => Node
        self.store = {}
        self.left = Node(-1, -1) # LRU pointer
        self.right = Node(-1, -1) # MRU/insertion pointer
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        prv = self.right.prev
        prv.next = node
        node.prev = prv
        self.right.prev = node
        node.next = self.right

    def remove(self, node):
        prv, nxt = node.prev, node.next
        nxt.prev = prv
        prv.next = nxt

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        self.remove(self.store[key])
        self.insert(self.store[key])
        return self.store[key].value


    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.remove(self.store[key])
        node = Node(key, value)
        self.store[key] = node
        self.insert(node)
        if len(self.store) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.store[lru.key]

