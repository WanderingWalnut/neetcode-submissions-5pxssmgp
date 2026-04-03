# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Go down the left leaf process it all then root then right
        
        res = []

        def inorder(root):
            if not root:
                return
            
            inorder(root.left) # Go left first
            res.append(root.val) # then root
            inorder(root.right) # then right

        inorder(root)
        return res
        