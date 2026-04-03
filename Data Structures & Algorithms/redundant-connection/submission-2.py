class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # We do nodes + 1 where len(edges) is nodes, +1 since nodes == edges
        par = [i for i in range(len(edges) + 1)] 
        # Rank helps re-arrange our trees so that our tree flattens out
        rank = [1] * (len(edges)+1)

        def find(n):
            # Only the root is the parent of itself
            if par[n] != n:
                par[n] = find(par[n])
            
            return par[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            # If the parents are the same then that is second occurence of that link (extra edge)
            if p1 == p2:
                return False
            
            # Re-arrange tree to keep find efficient
            if rank[p1] > rank[p2]:
                par[p2] = p1 # Since p1 is a greater rank, par of p2 = p1 now
                rank[p1] += rank[p2] # Increment it's rank by rank 2's val
            else:
                par[p1] = p2 # par of p1 = p2
                rank[p2] += rank[p1] # Increment rank

            return True

        # Iterate over all pairs of edges 
        for n1, n2 in edges:
            # If any repeating connection
            if not union(n1, n2):
                return [n1, n2]
        
        return []


