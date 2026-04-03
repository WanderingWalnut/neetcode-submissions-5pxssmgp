# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # Go down to the bottom
        # From the bottom up we start based off this
        # If the children are greater than parent then we start with its kids
        # We go up and skip one level each time
        # i.e 4+2 > 3, so we add 4+2 to total and skip 3 then
        # Each call should return rob_this and skip_this 
        # Basically on each call we ask if I rob this node, whats the max
        # If i skip whats the max?

        def dfs(root):
            if not root:
                return [0, 0]
            
            # Grab the pairs for each subtree
            leftPair = dfs(root.left)
            rightPair = dfs(root.right)

            # With root you take current root + without root values of the children below
            withRoot = root.val + leftPair[1] + rightPair[1]

            # Without root you can take either or ebcause if you skip the current root you can also skip the next one if there is a bigger val after
            withoutRoot = max(leftPair) + max(rightPair)

            return [withRoot, withoutRoot]

        return max(dfs(root))
        