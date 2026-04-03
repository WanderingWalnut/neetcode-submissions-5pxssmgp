class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # Our l ptr is max(nums), this is the lowest possible sum we can have in a sub array
        # Our r ptr is sum(nums), this is the largest sum we can have (one split only)
        # Binary search decides our ans, we check if its valid by the following
        # Run a sliding window to create a sub array that matches the value
        # If the sliding window is bigger than our max size per sub array
        # Move r to find a smaller num that fits within the constraint
        # If valid move l to find a bigger num with the right window -> possibly not needed
        l, r = max(nums), sum(nums)
        res = float("inf")

        while l <= r:

            mid = l + (r-l)//2
            print("Mid: ", mid)
            
            curr_sum = 0
            split = 0
            # Calc total splits 
            for num in nums:    
                if curr_sum + num > mid:
                    curr_sum = 0
                    split += 1
                curr_sum += num
            # Any remaining nums become the last sub array
            if curr_sum:
                split += 1
            # If our splits is less than or equal to k, valid ans
            if split <= k:
                res = min(mid, res)
                print("Updated Res: ", res)
                r = mid - 1
            # Invalid ans, find a larger mid
            else:
                l = mid + 1
            
        return res



            

        