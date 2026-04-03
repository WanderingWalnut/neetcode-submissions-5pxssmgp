# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Put all the nodes into an array
        # Connect the next pointers in the required order, i and j
        # nodes[i].next = node[j] and vice versa

        # No list available 
        if not head:
            return None

        curr = head
        nodes = [] 

        while curr:
            nodes.append(curr)
            curr = curr.next
        
        i, j = 0, len(nodes) - 1


        while i < j:
            nodes[i].next = nodes[j]
            i += 1

            # i and j cross path, all nodes are covered and re-mapped
            if i > j:
                break
            
            nodes[j].next = nodes[i]
            j -= 1

        # Last node now points to null ptr
        nodes[i].next = None
    




        