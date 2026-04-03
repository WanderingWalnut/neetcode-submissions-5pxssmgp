from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A cycle means it is invalidated as 2 nodes connect to the same one node

        adjList = defaultdict(list)

        for prnt, chld in edges:
            adjList[prnt].append(chld)
            adjList[chld].append(prnt)
        print(adjList)

        seen = set()

        def dfs(node, parent):

            if node in seen:
                return False

            seen.add(node)
            for nbor in adjList[node]:
                if nbor == parent:
                    continue
    
                if not dfs(nbor, node):
                    print(f"{nbor} violates")
                    return False

            return True
        
        return dfs(0, -1) and len(seen) == n
            