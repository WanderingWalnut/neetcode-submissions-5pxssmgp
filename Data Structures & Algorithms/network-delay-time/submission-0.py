from collections import defaultdict
import heapq
from math import inf
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra's algorithim
        
        adjList = defaultdict(list)

        for u,v,t in times:
            adjList[u].append((v,t))
        
        print(adjList)

        dist = [inf] * (n+1)
        dist[k] = 0 # Set starting point time as 0
    
        pq = [(0, k)] # (distance_so_far, node)
        visited = [False] * (n+1)
        
        while pq:

            # Pop the element with the lowest distance
            d, u = heapq.heappop(pq)

            # If already visited, skip
            if visited[u]:
                continue
            
            visited[u] = True

            # For all nodes and their weights that are neighbours of u
            for v,w in adjList[u]:
                # Grab the new distance of the path to it's neighbour (v)
                nd = dist[u] + w
                # If it happens to be less than dist[v], then update with new distance
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v)) # Add to heap so we consider this nd as our point of calculation
        
        ans = max(dist[1:])  # ignore index 0
        return -1 if ans == inf else int(ans)

            

