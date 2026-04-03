# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        # Initialize pointers for the nodes to be swapped
        self.first = self.second = self.prev = None

        def inorder(node):
            if not node:
                return
            
            # Left
            inorder(node.left)

            # Detect swapped nodes
            if self.prev and self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev  # First time we see drop
                self.second = node  # Could be updated later

            self.prev = node  # Move pointer

            # Right
            inorder(node.right)

        inorder(root)

        # Swap values of the wrong nodes
        self.first.val, self.second.val = self.second.val, self.first.val

        
                


             
        