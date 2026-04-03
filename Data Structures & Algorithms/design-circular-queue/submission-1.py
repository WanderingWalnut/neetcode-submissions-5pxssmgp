class Node:

    def __init__(self, val = 0, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev


class MyCircularQueue:

    def __init__(self, k: int):
        self.space = k
        
        self.left = Node(0, None, None)
        self.right = Node(0, None, self.left)
        self.left.next = self.right

    def enQueue(self, value: int) -> bool:
        # If list is full return False
        if self.isFull():
            return False
        
        curr = Node(value, self.right, self.right.prev) # Init node from end (right dummy node)
        self.right.prev.next = curr # Old end of list now points to new end
        self.right.prev = curr # Dummy node marking end of list now points to the end
        self.space -= 1
        return True

    def deQueue(self) -> bool:
        # If list is empty return False
        if self.isEmpty():
            return False
        
        # Get the current front node (first real node after the dummy head)
        curr = self.left.next

        # Remove the front node by updating pointers
        self.left.next = curr.next
        curr.next.prev = self.left

        # Clear the removed node's pointers 
        curr.next, curr.prev = None, None

        # Increment available space
        self.space += 1

        return True

    def Front(self) -> int:
        # If a node past left dummy node exists return the val (front)
        if self.left.next != self.right:
            return self.left.next.val
        else:
            return -1    

    def Rear(self) -> int:
        if self.right.prev != self.left:
            return self.right.prev.val
        else:
            return -1
        
    def isEmpty(self) -> bool:
        # If only the dummy nodes exusr
        return self.left.next == self.right
        
    def isFull(self) -> bool:
        # If all space is taken
        if self.space == 0:
            return True
        
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()