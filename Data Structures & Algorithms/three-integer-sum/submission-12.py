class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Use the same concept of end and beginning of list
        # Create outer for loop for each index
        # utilize 2 pointers to get O(n^2) solution instead of O(n^3)
        # Inner loop utilizes indices l and r to move along the array
        # and find a match
        # make sure array is sorted so we can use that property in our logic
        # e.g [-4, -1, -1, 0, 1, 2]
        # first loop i = 4
        # l = -1, r = 2
        # compute -4 + (-1) + 2 does it equal 0?
        # if not check if greater or less than, move pointers based on that

        nums = sorted(nums)
        res = []
        seen = set()

        for i in range(len(nums)):
            r = len(nums) - 1
            l = i + 1

            while l < r: 
                currSum = nums[i] + nums[l] + nums[r]
                if currSum == 0 and l != r and i != r and i != l:
                    triplet = (nums[i], nums[l], nums[r])
                    if triplet not in seen:
                        res.append([nums[i], nums[l], nums[r]])
                        seen.add(triplet)
                        print("Added the following: ", nums[i], nums[l], nums[r])
                    # res.append(nums[i])
                    # res.append(nums[l])
                    # res.append(nums[r])
                
                # Num is too big, lower it
                if currSum > 0:
                    r -= 1
                else:
                    l += 1
        return res


