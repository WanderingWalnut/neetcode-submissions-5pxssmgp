from collections import defaultdict
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Use dijkstra's algorithim
        # Create an adjacency list with each point and its weight
        # Before appending calculate weight using manhattan distance
        # Using a priority queue based on distance we pop and add distance 
        
        adjList = defaultdict(list)
        
        for i in range(len(points)):
            x, y = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]

                dist = abs(x-x2) + abs(y-y2)
                # Dist at front for min heap
                adjList[i].append((dist, j))
                adjList[j].append((dist, i))
            
        print(adjList)
        # Start the min heap with 0 cost for first element + 0 index item
        minHeap = [[0,0]]
        visit = set()
        res = 0

        # Prim's algorithim
        while len(visit) < len(points):
            dist, i = heapq.heappop(minHeap)
            print(f"Processing {i}")

            if (i) in visit:
                continue

            visit.add(i)
            res += dist

            for nborDist, nbor in adjList[i]:
                if nbor not in visit:
                    heapq.heappush(minHeap,[nborDist, nbor])
        
        return res







        
        
        