"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Traverse the graph DFS, for each of it's children create your own copy
        
        oldToNew = {}

        def dfs(node):
            # If our current node is already mapped
            if node in oldToNew:
                return oldToNew[node]

            # Otherwise create the copy and map it
            copy = Node(node.val)
            oldToNew[node] = copy
            # Put all neighbours inside the children of copy
            for nbor in node.neighbors:
                copy.neighbors.append(dfs(nbor))
            
            return copy
        
        return dfs(node) if node else None
        