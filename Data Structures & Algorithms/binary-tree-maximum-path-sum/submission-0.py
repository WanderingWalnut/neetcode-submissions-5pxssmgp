# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Track a res var
        # Traverse from bottom up
        # Each call returns its maxPathSum
        # Either with root, without root or only root
        # If the total of the path is greater than res
        # Then update it

        res = float("-inf")

        def dfs(root):
            
            # If node does not exist, account to 0 for path sum
            if not root:
                return 0

            # Do not use negative numbers
            leftPathSum = max(0, dfs(root.left))
            rightPathSum = max(0, dfs(root.right))

            fullPathSum = root.val + leftPathSum + rightPathSum

            nonlocal res
            res = max(res, fullPathSum)
            print(f"Updating res: {res}")

            # Return the best path up, we can only take one path for it to stay valid 
            return root.val + max(leftPathSum, rightPathSum)

            # # If without root is the biggest val
            # if withoutRoot > withRoot and withoutRoot > root.val:
            #     res = max(res, withoutRoot)
            #     print(f"Returning to parent: {root.val + max(leftPathSum, rightPathSum)}")
            #     print(f"Updating res with: {root.val + leftPathSum + rightPathSum}")
            #     return root.val + max(leftPathSum, rightPathSum)
            # # If with root is the biggest val
            # else:
            #     res = max(res, withRoot)
            #     print(f"Returning to parent: {root.val + max(leftPathSum, rightPathSum)}")
            #     print(f"Updating res with: {root.val + leftPathSum + rightPathSum}")
            #     return root.val + max(leftPathSum, rightPathSum)
            # # Root is the biggest val
            # else:
            #     res = max(res, root.val)
            #     print(f"Returning to parent: {root.val + max(leftPathSum, rightPathSum)}")
            #     print(f"Updating res with: {root.val + leftPathSum + rightPathSum}")
            #     return root.val + max(leftPathSum, rightPathSum)

        dfs(root)      
        return res




        
        

        