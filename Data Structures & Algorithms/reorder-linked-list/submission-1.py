# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # The pattern is one element from beginning and then one from end
        # If head is the beginning and tail is the end, the pattern is head, tail, head, tail etc
        # We can't go backwards in a singly linked list
        # Add all nodes to an array
        # Start from the beginning and end
        # Move the next ptrs accordinly
        # Stop loop once all elements in the arr have been processed
        
        curr = head
        arr = []
        
        # Populate arr with all nodes
        while curr is not None:
            arr.append([curr, curr.val])
            curr = curr.next
        
        print(arr)

        l, r = 0, len(arr) - 1

        while l < r:
            # Left node points to right most element
            arr[l][0].next = arr[r][0]
            l += 1

            if l == r:
                break
            # Right most element points to left most element
            arr[r][0].next = arr[l][0]
            r -= 1

        # Set last node to none
        print("Final Value: ", arr[r][0].val)
        arr[l][0].next = None        
        
        for i in range(len(arr)):
            print(arr[i][0].val, arr[i][0].next.val if arr[i][0].next else "None")
            
            if arr[i][0].next is None:
                break

        head = arr[0][0]
            






        