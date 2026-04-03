class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Goal is to find the split in our binary search
        # If mid > r -> we are in rotated part -> move l = mid + 1
        # If mid < r -> we know we are in smaller partition -> move r = mid - 1

        l, r = 0, len(nums) - 1
        res = float("inf")

        while l <= r:

            mid = l + (r-l)//2

            # In the bigger partition/rotated section
            if nums[mid] > nums[r]:
                l = mid + 1
            # In smaller partition
            else:
                # Update min
                res = min(res, nums[mid])
                print("Current Res: ", res)
                r = mid - 1
        
        return res


            




        