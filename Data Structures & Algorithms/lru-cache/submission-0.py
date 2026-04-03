class Node:
    def __init__(self, key: int, val: int, next, prev):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        
        self.left = Node(0, 0, None, None)
        self.right = Node(0, 0, None, self.left)
        self.left.next = self.right

    def insert(self, node):
        # Insert from end
        self.right.prev.next = node
        node.prev = self.right.prev
        self.right.prev = node
        node.next = self.right
        

    def remove(self, node):
        # Adjust ptrs to be before and after current node
        prev, nxt = node.prev, node.next
        node.prev.next, node.next.prev = nxt, prev
        

    def get(self, key: int) -> int:
        if key in self.cache:
            # Update LRU
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            # Return res
            return self.cache[key].val
        else:
            return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value, None, None)
        self.insert(self.cache[key])
        
        
        if len(self.cache) > self.cap:
            # Remove LRU, self.left.next is the first element of list or LRU
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
