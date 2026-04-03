class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # Updating result
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            mid = (l+r)//2
            # If mid is minimum value
            res = min(res, nums[mid])
            
            # Which side to search (binary search part)
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid -1
        return res 
        