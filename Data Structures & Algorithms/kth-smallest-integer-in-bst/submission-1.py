# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Traverse the tree K times using DFS
        # Use in-order traversal
        # Intuition: Traverse all the way down left, pop K elements
        # return the Kth value

        arr = []

        def inorder(node):

            if not node:
                return None
            
            inorder(node.left)

            arr.append(node.val)

            inorder(node.right)

        inorder(root)

        return arr[k-1]


        

            
            