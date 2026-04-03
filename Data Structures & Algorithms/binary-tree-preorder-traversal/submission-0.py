# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        def preorder(root):
            if not root:
                return
            
            res.append(root.val) # Visit root first
            preorder(root.left) # GO down left
            preorder(root.right) # Go down right
        
        preorder(root)
        return res

        