class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        resList = []
        # Sort the nums
        nums = sorted(nums)

        n = len(nums)

        # Current num, L pointer is +1 current and right pointer
        for i in range(n):
            current = nums[i]
            r = n - 1
            l = i + 1

            # Skip duplicates for the current number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while l < r:
                # Sum of the nums
                res = current + nums[l] + nums[r]
                if res > 0:
                    r -= 1
                elif res < 0:
                    l += 1
                else:
                    ans = [current, nums[r], nums[l]]
                    # Add list to result list if it doesn't exist
                    if ans not in resList:
                        resList.append(ans)
                    # Move pointers
                    l += 1
                    while nums[i] == nums[i-1] and l < r:
                        l += 1

        return resList
