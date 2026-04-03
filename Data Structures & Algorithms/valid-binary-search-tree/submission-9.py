# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Do DFS inorder
        # On each recrusive call check the simple condition
        # Is left smaller than root and right bigger than root

        def dfs(root, minNum, maxNum):
            if not root:
                return True
            
            # Checking for condition for it to be false
            if not (minNum < root.val < maxNum):
                return False
            
            # Recursively check left and right
            left = dfs(root.left, minNum, root.val)
            right = dfs(root.right, root.val, maxNum)

            return left and right
        
        return dfs(root, float("-inf"), float("inf"))
                

        