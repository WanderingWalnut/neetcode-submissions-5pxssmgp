class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute force sol:
        # Iterate over the list of nums
        # For each iteration, loop over all the nums (second for loop)
        # i == j, same num do not add to res

        # Optimized solution:
        # Compute prefix's and postfix
        # Add them to get res
        # if no prefix to num i.e for first index, default to 1
        prefix = [1] * len(nums) # array of 1's (default val)
        postfix = [1] * len(nums)
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            # Multiply prefix total from before with new num
            print("Multiply: ", prefix[i-1], nums[i-1])
            prefix[i] = nums[i-1] * prefix[i-1]
            print("Prefix: ", prefix)

        post_product = 1
        for i in range(len(nums) - 2, -1, -1):
            # Create postfix opposite to prefix
            postfix[i] = nums[i+1] * postfix[i+1] 
            print(postfix)
        
        for i in range(len(nums)):
            res[i] = postfix[i] * prefix[i]
        return res




        




            





        