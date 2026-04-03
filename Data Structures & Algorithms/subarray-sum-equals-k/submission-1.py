from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Sort the array
        # Go through each num 
        # Add prior nums, if current total < target
        # Move to the next element and add to total
        # Once a subarray is complete start from the next num
        # Increment res by 1 for every subarray

        res, currSum = 0, 0

        prefixSums = defaultdict(int)
        prefixSums[0] = 1

        for num in nums:
            currSum += num
            diff = currSum - k

            res += prefixSums[diff]
            prefixSums[currSum] += 1
        
        return res






        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(i, len(nums)):
        #         sum += nums[j]
        #         print("Current Total: ", sum)
        #         if sum == k:
        #             res += 1
        
            # current += nums[i]
            # print("Current Total: ", current)
            # if current == k:
            #     res += 1
            #     current = 0

        
        return res
        




        