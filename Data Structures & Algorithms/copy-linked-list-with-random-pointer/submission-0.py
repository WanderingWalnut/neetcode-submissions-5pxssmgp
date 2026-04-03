"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Create a copy, traverse the pass list
        # Create a new node on each instance and add the val to the new ndoe
        # Utilize an arr to change ptrs down the road
        # Initially set to None, update as it is found

        curr = head
        OldToCopy = {None: None}

        while curr:
            copy = Node(curr.val)
            OldToCopy[curr] = copy # Map old node to new node
            curr = curr.next
        
        curr = head # Reset for 2nd pass

        while curr:
            copy = OldToCopy[curr] # Load copy
            copy.next = OldToCopy[curr.next] # Set next to the new copy
            copy.random = OldToCopy[curr.random] # Set random to the copy of random ptr node
            curr = curr.next

        
        return OldToCopy[head]



                
            







        