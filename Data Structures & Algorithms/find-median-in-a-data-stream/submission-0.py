import heapq
import math
class MedianFinder:

    def __init__(self):
        self.minHeap = []
        

    def addNum(self, num: int) -> None:
        # Add num to min heap (logn) time
        heapq.heappush(self.minHeap, num)
        print(f"Added {num} to heap: {self.minHeap}")

    def findMedian(self) -> float:
        # Heap sort the heap and then find median based on len
        print(f"Before finding res, heap looks as follows: {self.minHeap}")
        n = len(self.minHeap)
        res = [0] * n
        copyMinHeap = self.minHeap.copy() # We pop from the copy so we dont affect the original

        # Heap sort arr
        for i in range(n):
            curr = heapq.heappop(copyMinHeap)
            res[i] = curr
        
        print(f"Heap sort arr: {res}")

        # Odd len, unqiue median
        if len(res) % 2 == 1:
            print(f"Odd len, unqiue median... returning: {res[int(n/2)]}")
            return res[int(n/2)]
        # Even len, between 2 nums
        else:
            lowerIndex = math.floor(n/2) -1
            upperIndex = math.ceil(n/2)
            print(f"Even len, combined median {lowerIndex} & {upperIndex}... returning: {((res[lowerIndex]+res[upperIndex])/2)}")
            return ((res[lowerIndex]+res[upperIndex])/2)

        
        
        