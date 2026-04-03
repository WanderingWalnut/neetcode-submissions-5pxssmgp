# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step by step approach
        # Save next node
        # Current points to prev
        # prev pointer moves to current node, prepare for next iteration
        # Move current pointer to next node

        prev = None
        curr = head
        nextNode = None

        while (curr != None):
            nextNode = curr.next # Save next node 
            curr.next = prev # Current node points to prev value (reversing part)
            prev = curr # prev is points to current as we move on to the next iteration
            curr = nextNode # current finally moved to nextNode for next iteration

        return prev


        