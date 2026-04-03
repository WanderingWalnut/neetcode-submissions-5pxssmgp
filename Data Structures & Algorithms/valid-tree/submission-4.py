from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A cycle means it is invalidated as 2 nodes connect to the same one node

        adjList = defaultdict(list)

        # Create adjlist
        for prnt, chld in edges:
            adjList[prnt].append(chld)
            adjList[chld].append(prnt)
        print(adjList)

        seen = set()

        def dfs(node, parent):

            seen.add(node)
            for nbor in adjList[node]:
                
                if nbor == parent:
                    continue
                
                if nbor in seen:
                    return False
    
                if not dfs(nbor, node):
                    print(f"{nbor} violates")
                    return False

            return True
        
        return dfs(0, -1) and len(seen) == n
            