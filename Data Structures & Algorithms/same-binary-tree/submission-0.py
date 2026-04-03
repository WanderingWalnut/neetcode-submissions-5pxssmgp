# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Use bfs and iterate through each level
        # 2 Queues for each tree
        # Compare each node, if they dont match return False
        # If entire tree goes without being false, return True


        q1 = [p]
        q2 = [q]

        while q1 and q2:
                
            # Grab the current node
            node1 = q1.pop(0)
            node2 = q2.pop(0)


            # If both are none, continue
            if not node1 and not node2:
                continue 
            
            # If one is none and other exists
            if not node1 and node2 or node1 and not node2:
                return False

            if node1 and node2:
                print("Queue 1 current node is: ", node1.val)
                print("Queue 2 current node is: ", node2.val)
                # Check if values match
                if node1.val != node2.val:
                    return False
            
            # If nodes exist, add to queue
            if node1:
                q1.append(node1.left)
                q1.append(node1.right)

            if node2:
                q2.append(node2.left)
                q2.append(node2.right)

        return True




        
        