class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Same binary search but instead of returning -1
        # Return mid + 1

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r-l)//2

            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        if nums[mid] > target:
            return mid
        else:
            return mid + 1