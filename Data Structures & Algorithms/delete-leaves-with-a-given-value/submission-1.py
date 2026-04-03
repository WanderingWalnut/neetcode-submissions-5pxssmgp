# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # Start from bottom up
        # 2 cases
        # If node is leaf
        # If node becomes leaf
        # Since we are oing bottom up each call should update the tree with left and right values/subtrees
        # If node == target and left and right do not exist we delete

        if not root:
            return None
        
        # Update tree as we go up
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        # Leaf node
        if not root.left and not root.right:
            
            if root.val == target:
                print(f"Removing {root.val}")
                return None
            
            else:
                # Stays part of tree
                print(f"Keep {root.val}")
                return root
        
        return root



        