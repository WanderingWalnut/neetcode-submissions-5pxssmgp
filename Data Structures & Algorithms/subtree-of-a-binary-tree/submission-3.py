# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 3 cases
        # Root is not subroot -> False continue traversing
        # Root is subroot -> True, isSameTree called
        # Root is part of subroot -> True, continue calling isSameTree

        res = False

        def dfs(root):
            # Main tree or subTreedoes not exist
            if not root or not subRoot:
                return False
            
            # On each pass, check if its the same tree
            # This solves the edge cases where the leaf nodes are different
            if isSameTree(root, subRoot):
                return True

            return dfs(root.left) or dfs(root.right)

        def isSameTree(root, subRoot):
            # Both are None
            if not root and not subRoot:
                return True
            # All possible false cases
            elif not root or not subRoot or root.val != subRoot.val:
                return False
            else:
                return (isSameTree(root.left, subRoot.left) and
                isSameTree(root.right, subRoot.right))

        return dfs(root)


        
            




        