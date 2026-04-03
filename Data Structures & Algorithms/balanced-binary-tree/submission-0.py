# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Grab height of each subtree
        # If the max height of each sub tree is greater than 1 
        # return false
        # otherwise return true
        
        isBalanced = True

        def dfs(root):
            if not root:
                return 0
            
            # Get height
            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)

            print(f"L Height: {leftHeight}, R Height: {rightHeight}")
            # Compare heights
            nonlocal isBalanced
            if abs(leftHeight - rightHeight) > 1:
                isBalanced = False
                return (1 + max(leftHeight, rightHeight))
            else:
                return (1 + max(leftHeight, rightHeight))

        dfs(root)
        
        return isBalanced





        