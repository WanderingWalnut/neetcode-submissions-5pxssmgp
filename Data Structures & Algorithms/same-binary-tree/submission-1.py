# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # DFS on both trees, at each node compare --> preorder traversal
        # If any node does not match return false
        # Otherwise return true
        
        # All base cases
        if not p and not q:
            return True
        
        elif not p and q:
            return False
        
        elif p and not q:
            return False
        
        elif p.val != q.val:
            return False
        
        # Recursively check l and r branches for both trees
        else:
            left = self.isSameTree(p.left, q.left)
            print("Left: ", left, p.val, q.val)
            right = self.isSameTree(p.right, q.right)
            print("Right: ", right, p.val, q.val)
            return left and right
        

        # def dfs(rootP, rootQ):
        #     if not rootP and not rootQ:
        #         return 
            
        #     nonlocal isSame
            
        #     print(f"Comparing {rootP.val} and {rootQ.val}")
        #     if rootP.val != rootQ.val:
        #         isSame = False
        #         dfs(rootP.left, rootQ.left)
        #         dfs(rootP.right, rootQ.right)
            
        #     else:
        #         dfs(rootP.left, rootQ.left)
        #         dfs(rootP.right, rootQ.right)
        
        # dfs(p, q)

        # return isSame
        





        
        