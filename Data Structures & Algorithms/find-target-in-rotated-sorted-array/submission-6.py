class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary search problem, 2 sorted portions due to rotations
        # Find the pivot between the 2 sorted segments
        # If nums[l] < nums[mid] means we are in left sorted portion, move based on target
        # If nums[l] > nums[mid] means we are in right sorted portion, move based on target

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r)//2

            
            if nums[mid] == target:
                return mid
            # In left sorted portion, if nums[l] is less than target then target is right sorted portion
            elif nums[l] <= nums[mid]:
                # If target is between l and mid, narrow down left portion
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                # Otherwise in right portion
                else:
                    l = mid + 1
                # In right sorted portion, if nums[r] is greater than or equal to target then it is in left sorted portion
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
                    



         
