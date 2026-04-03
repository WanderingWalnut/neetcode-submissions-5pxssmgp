from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # We want distinct components, traverse over each possible point
        # Since it is undirected, we need to account for back edge in dfs
        # When a DFS returns completely, that is one connected component
        # We can differentiate by using the seen set, if it's not in seen then it is a new beginning of a new set

        adjList = defaultdict(list)

        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        print(adjList)

        visit = set()

        def dfs(node, prev):
            if node in visit:
                return

            visit.add(node)
            for nbor in adjList[node]:
                if nbor == node:
                    continue
                
                dfs(nbor, node)
            
            return
        
        res = 0
        for i in range(n):
            if i not in visit:
                res += 1
                print(f"{i} and it's graph has not been seen, {res} graphs so far")
                dfs(i, -1)
        
        return res