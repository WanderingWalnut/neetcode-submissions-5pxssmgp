# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Found the node to delete

            # Case 1: No children
            if not root.left and not root.right:
                return None
            
            # Case 2: One child
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # Case 3: Two children
            # Find the smallest value in the right subtree (inorder successor)
            successor = self.findMin(root.right)
            root.val = successor.val  # Replace value
            root.right = self.deleteNode(root.right, successor.val)  # Delete successor

        return root

    def findMin(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node




        