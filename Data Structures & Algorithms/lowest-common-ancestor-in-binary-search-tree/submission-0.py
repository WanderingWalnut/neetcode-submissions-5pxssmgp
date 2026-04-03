# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # If p and q are smaller than current node, ancestor is in left tree
        # If p and q are bigger than current node, ancestor is in right tree
        # If ancestor is between p and q, then current node is ancestor
        
        
        if root is None:
            return None

        

        queue = [root]

        while queue:

            node = queue.pop()
            print('Current Node: ', node.val)

            if p.val < node.val and q.val < node.val:
                queue.append(node.left)
            elif p.val > node.val and q.val > node.val:
                queue.append(node.right)
            else:
                return node
        



        