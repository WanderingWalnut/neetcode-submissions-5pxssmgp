# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Traverse the list for n times
        # Remove the node, and fix pointers
        # Use while i <= n in order to traverse and if i == n for the node removal condition

        curr = head

        nodes = []

        while curr:
            nodes.append(curr)
            curr = curr.next

        removeIndex = len(nodes) - n

        if removeIndex == 0:
            return head.next

        # Connect the prev node to the node after removed node
        nodes[removeIndex - 1].next = nodes[removeIndex].next

        return head

        