class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Helper to count total length
        def getLength(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length
        
        dummy = ListNode(0)
        dummy.next = head
        prev_group_tail = dummy
        curr = head

        total_length = getLength(head)
        while total_length >= k:
            tail = curr
            for _ in range(k - 1):
                tail = tail.next
            
            next_group_head = tail.next

            # Reverse current group
            new_head = self.reverse(curr, tail)

            # Connect previous group to new head
            prev_group_tail.next = new_head
            # Old start becomes new tail, connect to next group
            curr.next = next_group_head

            # Move pointers forward
            prev_group_tail = curr
            curr = next_group_head
            total_length -= k

        return dummy.next

    def reverse(self, curr, tail):
        prev = None
        stop = tail.next
        while curr != stop:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev  # New head of reversed segment
