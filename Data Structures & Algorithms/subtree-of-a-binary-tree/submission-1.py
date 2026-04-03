# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Use DFS recursively to check if subtree is in tree
        # Similar to same tree
        # Check all subtrees and see if they match subRoot

        # No subroot means its True
        if not subRoot:
            return True
        # If main tree does not exist then no subtree can exist
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))



    def sameTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # If both roots are none
        if not root1 and not root2:
            return True

        # If both roots exist and match
        if root1 and root2 and root1.val == root2.val:
            return (self.sameTree(root1.left, root2.left) and self.sameTree(root1.right, root2.right))

        # Otherwise return false
        return False


        
            




        