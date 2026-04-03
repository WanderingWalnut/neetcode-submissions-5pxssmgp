# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Add all nodes to an arr to be easily indexed
        # Iterate through the arr till n
        # On the nth index change ptrs
        # Save next ptr as temp_next
        # Set nth index node to None
        # Set prev index n - 1 to temp_next
        # If popping first index, just set next to none
        # If not then set next to n + 1, if n + 1 does not exist set to None

        curr = head
        arr = []

        # Populate arr
        while curr is not None:
            arr.append([curr, curr.val])
            curr = curr.next
        
        print(arr)
        index_to_remove = len(arr) - n

        # If removing first index
        if index_to_remove == 0:
            return head.next
        
        prev_node = arr[index_to_remove-1][0]

        # In between node
        if index_to_remove < len(arr) -1:
            prev_node.next = arr[index_to_remove + 1][0]
        # End node
        else:
            prev_node.next = None
        
        return head

                
                


                






        