class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = nums[0]
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            # Sorted left half --> left is increasing to mid
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1 # Move search to the right half
                else:
                    r = mid - 1 # stay in the left half 
            # Sorted right half --> mid to right is increasing
            else:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1  # Stay in the right half
                else:
                    r = mid - 1  # Move search to the left half
        return -1
            
            




        