# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Do BFS, iterate through the level and add to list
        # Empty iteration list on completion of one

        if root is None:
            return []
        
        res = []

        queue = [root]


        while queue:
            # Current list for the level
            current = []
                
            # Iterate through the level
            for i in range(len(queue)):
                node = queue.pop(0)

                current.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            res.append(current) # Update res list
            

        return res





        