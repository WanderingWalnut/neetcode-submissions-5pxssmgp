# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Perform BFS, go level by level
        # The last node in the level add to res

        if not root:
            return []
        
        res = []
        queue = deque([root])

        while queue:
            level_len = len(queue)

            for i in range(level_len):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                # If its the last element in the level 
                if i == level_len - 1:
                    print(f"Adding {node.val} to res")
                    res.append(node.val)
        
        return res
            