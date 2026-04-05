import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Keep a max heap of size k
        # Add a point to the max heap if the size of max heap < k or the top of the max heap is greater than the new one coming in
        # Idea is basically max heap keeps our furthest k point at the top and we replace it with the nearest
        # Store [distance, [x,y]] in max heap

        def calc_distance(x, y):
            res = ((x)**2 + (y)**2)**0.5
            return res

        max_heap = []

        for i in range(len(points)):
            x, y = points[i]
            dist = calc_distance(x, y)

            if not max_heap or len(max_heap) < k:
                heapq.heappush(max_heap, [-dist, [x,y]])

            elif max_heap and len(max_heap) == k and abs(max_heap[0][0]) > dist:
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, [-dist, [x,y]])
            
        # Build our res
        res = []

        while max_heap:
            dist, points = heapq.heappop(max_heap)
            res.append(points)

        print(res)      
        return res  

            




        