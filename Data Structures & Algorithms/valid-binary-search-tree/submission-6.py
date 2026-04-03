# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Use DFS, user pre-order traversal
        # Compare current node to left and right tree
        # If left is bigger or right is smaller than current node, return false
        # Go through entire tree, if we dont find fault return True

        if root is None:
            return True
        
        stack = [(root, float('-inf'), float('inf'))]  # (node, lower_bound, upper_bound)



        while stack:
            node, lower, upper = stack.pop()

            if not node:
                continue
            
            val = node.val

            # If BST policy is violated
            if val <= lower or val >= upper:
                return False

            stack.append((node.right, val, upper))
            stack.append((node.left, lower, val))

        return True            

            