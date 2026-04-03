# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Traverse both linked lists (curr1 and curr2)
        # Keep track of prev node 
        # If curr2 > curr1 --> swap
        # prev1.next = curr2
        # curr2.next = curr1
        # If one becomes None (end of list) add the rest to the end
        
        # Edge cases
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        prev1, curr1 = None, list1
        prev2, curr2 = None, list2

        if curr2.val < curr1.val:
            head = list2
        else:
            head = list1

        while curr1 and curr2:

            if curr2.val < curr1.val:
                next_temp = curr2.next
                prev2 = curr2 # Save curr2 
                
                if prev1:
                    prev1.next = curr2 # Since the new curr1 is bigger than curr2 we connect prev to curr2

                curr2.next = curr1 # curr2 val mpoints to bigger val now
                prev1 = curr2
                curr2 = next_temp
            
            else:
                prev1 = curr1 # Save prev val
                curr1 = curr1.next # Traverse forward
            
        if curr1 or curr2:
            prev1.next = curr1 if curr1 else curr2 # Add remaining part
        
        return head

        



        



                  




        