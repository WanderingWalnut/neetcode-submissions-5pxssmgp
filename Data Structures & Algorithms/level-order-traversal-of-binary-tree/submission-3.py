# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Level order traversal -> has to be BFS
        # Each level has i^height nodes, so height = 0 has 1 node (2^0)
        # So if i == max for height, append to res and reset
        # Use a queue, for each level add to res list
        # return res
        # How do we calculate height?


        if not root:
            return []

        queue = deque([root])
        res = []
        current = []
        level = 0

        while queue:
            nodes = len(queue) # Total nodes in the level
            
            # Traverse the entire level
            for i in range(nodes):
                node = queue.popleft()
                
                current.append(node.val)
                print(f"Added {node.val} to current res")

                if node.left:
                    queue.append(node.left)
                    print(f"Added {node.left.val} to queue")
                if node.right:
                    queue.append(node.right)
                    print(f"Added {node.right.val} to queue")
           
            res.append(current)
            current = [] # Reset curr array for next iteration
            level += 1
        
        return res










        