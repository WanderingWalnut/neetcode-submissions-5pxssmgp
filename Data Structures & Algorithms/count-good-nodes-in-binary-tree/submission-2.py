# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Brute force solution is that for each node we check the full path
        # If the path has no nums greater than itself increment res by 1
        # If the path has a num greater than itself then just return false
        # If a node is bigger than its parent increment res by 1

        if not root:
            return 0
        
        res = 0 

        def dfs(root, maxVal):
            if not root:
                return
 
            nonlocal res
            if root.val >= maxVal:
                res += 1
            
            if root.val > maxVal:
                maxVal = root.val
                print("New Max Val is: ", maxVal)
            
            dfs(root.left, maxVal)
            dfs(root.right, maxVal)
        

        dfs(root, float("-inf") )
        return res