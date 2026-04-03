class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Use binary search to find element
        # Array is sorted but theres multiple sorted segments
        # Divide those segments and then search them

        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            mid = (l+r) // 2

            # If its rotated n times for array size n
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            res = min(res, nums[mid])

            #In left sorted portion if mid is increaing from l
            if nums[mid] >= nums[l]:
                # Search right portion to find min
                l = mid + 1
            # Mid is between left and right sorted portions, min is somewhere in between
            else:
                r = mid - 1
        
        return res

            




        