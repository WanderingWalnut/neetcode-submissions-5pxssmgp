class Solution:
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Use heap, pop
        # Check conditions
        # If equal destroy both
        # Otherwise create new node and add to heap

        if len(stones) == 1:
            return stones[0]

        min_heap = []

        for stone in stones:
            heapq.heappush(min_heap, -stone)
        
        while len(min_heap) > 1:
            stone1 = -heapq.heappop(min_heap)
            stone2 = -heapq.heappop(min_heap)
            print(f"Heaviest stones being used are {stone1} and {stone2}")

            if stone1 == stone2:
                continue # Both are gone
            
            else:
                newStone = stone1 - stone2
                print(f"New stone is: {newStone}")
                heapq.heappush(min_heap, -newStone)
        
        if min_heap:
            return -min_heap[0]
        else:
            return 0
        