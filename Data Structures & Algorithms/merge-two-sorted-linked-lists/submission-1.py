# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Traverse both lists, at each node comapre values
        # Append values accordingly onto list1 (merge list 2 in-order)
        # If a val from list2 < list1 add it before its val (use a prev pointer)
        # Else move current pointer to next node for next comparison
        # Intial thoughts above 

        dummy = node = ListNode()


        while list1 and list2:
            # If l1 node is smaller
            if list1.val < list2.val:
                node.next = list1 # Adds it to our list
                list1 = list1.next # Moves to the next node
            # If l2 node is smaller or equal to
            else:
                node.next = list2 
                list2 = list2.next
            
            # Setup for next iteration, always happens
            node = node.next


            

        #If l1 has remaining nodes
        if list1:
            node.next = list1
        # If l2 has remaining nodes 
        elif list2:
            node.next = list2

        return dummy.next


        



                  




        