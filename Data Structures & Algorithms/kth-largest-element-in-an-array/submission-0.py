import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Solving without sorting is simple -> use a heap
        # Create a max heap and then just pop the elements k times

        res = k

        # Make all nums negative to simulate a max heap
        for i in range(len(nums)):
            nums[i] = -nums[i]

        heapq.heapify(nums)
        print(nums)
        
        # Pop k elements
        for i in range(k):
            res = -heapq.heappop(nums)
            print(f"Current largest k is {res}")
        
        return res

        