# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Use fast and slopw ptr approach
        # If fast ptr meets with slow ptr then we have a cycle
        # if fast ptr hits None then no cycle exists
        # Increment index for each slow and only update if we have a match otherwise return -1

        slow, fast = head, head.next

        while fast is not None and fast.next is not None:
            
            # Fast ptr catches up to the slow ptr
            if fast == slow:
                return True
            # Traverse
            fast = fast.next.next
            slow = slow.next

        return False



        