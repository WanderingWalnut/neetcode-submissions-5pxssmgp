# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Traverse the list, add each node to a set
        # If next node already exists in list then it is a cycle
        # If list is traveresed and no loop exists, return false

        visited = set() # Set to store visited nodes


        current = head

        while current is not None:
            if id(current) not in visited:
                visited.add(id(current)) # Add current node to set
            # If the node already exists in the set that means we have a cycle
            else:
                return True
            print("Current node val is: ", current.val)
            current = current.next # Traverse to next node
        return False

            

        