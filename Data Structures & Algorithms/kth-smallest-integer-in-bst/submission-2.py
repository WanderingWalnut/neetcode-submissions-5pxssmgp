# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Go down to the smallest element (node.left)
        # No go back up, and each time increment count (starts at 1)
        # We should be going back up as follows:
        # left, root, right -> inorder
        # if count == k
        # return node.val

        count = 0

        def dfs(root):
            if not root:
                return
            
            # Traverse to smallest element
            left = dfs(root.left)

            # Res is found in left
            if left is not None:
                return left
            
            # Current node is res
            nonlocal count
            count += 1
            print(f"Current Count: {count}")
            
            if count == k:
                return root.val
            
            right = dfs(root.right)
            
            # res is found in right
            if right is not None:
                return right
            # If not on the left side, check right side

        res = dfs(root)

        return res
        

        

            
            