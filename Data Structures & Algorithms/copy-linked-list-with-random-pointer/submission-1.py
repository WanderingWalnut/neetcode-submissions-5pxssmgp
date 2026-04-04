"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import defaultdict
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Create a hashmap of current list nodes random ptrs
        # To existing nodes, and then 
        # Iterate through the linkedlist to create our deep copy
        # Once we create a copy the next ptr of that original node
        # Points to the newly created node
        # Now we can do the following op -> random_dict[old_node] -> random ptr to old_random
        # old_random.next -> new_node

        node_dict = {}
        dummy = Node(0)
        new_cur = dummy
        cur = head

        while cur:
            # Create new node
            new_cur.next = Node(cur.val)
            node_dict[cur] = new_cur.next

            new_cur = new_cur.next
            cur = cur.next
        
        for cur_node, new_node in node_dict.items():
            print(cur_node.val, new_node.val)
            if cur_node.random:
                new_node.random = node_dict[cur_node.random]
            else:
                new_node.random = None
        
        return dummy.next
        
        
        