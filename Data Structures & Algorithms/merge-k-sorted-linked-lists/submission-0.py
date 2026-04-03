# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Store all vals in an array
        # Sort the array, turn array into a linked list after
        # Also can store nodes themselves but re-arranging ptrs will take more time

        arr = []
        for i in range(len(lists)):
            curr = lists[i]

            while curr:
                arr.append(curr.val)
                curr = curr.next
            
        arr.sort()
        print(arr)
        head = ListNode(0)
        curr = head
        for i in range(len(arr)):
            curr.next = ListNode(arr[i])
            curr = curr.next
        
        return head.next
