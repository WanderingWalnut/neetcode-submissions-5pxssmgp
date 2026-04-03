# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # It is a BST, utilize that property
        # 3 cases
        # Ancestor is parent of P & Q
        # Ancestor is P
        # Ancestor is Q
        # if root.left and root.right == p and q, return root
        # if root and root.left == p or root.right == q, return root
        # if root and root.left == q or root.right == q, return root
        # Otherwise compare and search a certain segment of the tree

        if p.val < root.val and q.val < root.val:
            print(f"Both nums are greater, going to {root.left.val}")
            return self.lowestCommonAncestor(root.left, p, q)

        elif p.val > root.val and q.val > root.val:
            print(f"Both nums are greater, going to {root.right.val}")
            return self.lowestCommonAncestor(root.right, p, q)
        
        else:
            print(f"Ancestor is {root.val}")
            return root
        
        # if root.left and root.right:
        #     if root.left.val == p.val and root.right.val == q.val:
        #         return root
        
        #     elif root.val == p.val and root.left.val == q.val or root.right.val == q.val:
        #         print(f"P is ancestor and Q is descendant, returning {root.val}")
        #         return root
        
        #     elif root.val == q.val and root.left.val == p.val or root.right.val == p.val:
        #         print(f"Q is ancestor and P is descendant, returning {root.val}")
        #         return root
        
        # # No solution found, binary search based on p and q
        #     else:
        #         if root.val > p.val:
        #             print(f"Moving to branch with {root.left.val}")
        #             return self.lowestCommonAncestor(root.left, p, q)
        #         else:
        #             print (f"Moving to branch with {root.left.val}")
        #             return self.lowestCommonAncestor(root.right, p, q)
        



        