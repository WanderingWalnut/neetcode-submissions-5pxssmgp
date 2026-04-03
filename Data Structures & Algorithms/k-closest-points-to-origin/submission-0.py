import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Create distance calculator helper function
        # Helper function basically will calculate points distance from 0
        # Now store each distance in a min heap mapped with its points as a tuple
        # Pop k times from heap to get closest points to origin

        # Calc distance
        def calcFromOrigin(x, y):
            distance = math.sqrt((x - 0)**2 + (y - 0)**2)
            return distance
        
        heap = []
        res = []

        # Heapify the coordinates & distance
        for i in range(len(points)):
            distance = calcFromOrigin(points[i][0], points[i][1])
            heapq.heappush(heap, (distance, points[i]))
            print(f"Heap is current {heap} and the size is {len(heap)}")
        
        # Pop k elements to create res
        for j in range(k):
            distance, coordinates = heapq.heappop(heap)
            print(f"For {j} iteration we have {distance} and following coordinates: {coordinates}")
            res.append(coordinates)
        
        return res

        
        