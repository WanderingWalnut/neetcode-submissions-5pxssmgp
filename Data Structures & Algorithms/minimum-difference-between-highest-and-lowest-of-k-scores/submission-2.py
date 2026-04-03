class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # Sort the arr
        # Iterate over the entire array
        # Window should be size k
        # If min is smaller than res update
        
        # If only 1 element just return 0
        if k == 1:
            return 0
        
        nums.sort()
        
        l, r = 0, k-1
        res = float("inf")

        while r < len(nums):
            difference = nums[r] - nums[l]

            res = min(difference, res)

            l += 1
            r += 1
        
        return res