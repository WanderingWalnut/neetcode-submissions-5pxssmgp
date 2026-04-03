class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Simple binary search

        l, r = 0, len(nums) - 1
        print(l, r)

        while l <= r:
            mid = l + (r - l)//2
            # print("Mid: ", mid) 

            # Found solution
            if nums[mid] == target:
                return mid
            # Answer is on the right side of the array
            elif target > nums[mid]:
                l = mid + 1
            # Answer is on the right side of the array
            else:
                r = mid - 1

        # No solution   
        return -1
        

        