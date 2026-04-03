# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Recursively traverse the tree
        # If val is greater than root then traverse right
        # If val is less than root then traverse left
        # Within each traversal block put a condition to check if its insertion point

        if not root:
            node = TreeNode(val)
            return node

        def dfs(root):
            if not root:
                return
            
            # Target is bigger than current
            if val > root.val:
                if not root.right:
                    node = TreeNode(val)
                    root.right = node
                else:
                    return dfs(root.right)
            
            else:
                # If val is less than root and left node does not exist
                if not root.left:
                    node = TreeNode(val)
                    root.left = node
                # Traverse if not insertion point
                else:
                    return dfs(root.left)
                
        dfs(root)

        return root


        