class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Similar concept to combination sum II
        # Order the array that way we don't have repeats
        # Run a while loop to start at only unique numbers
        # Remaining solution is the same as subsets
        # Don't pick the num and pick the num

        res = []
        nums.sort()

        def backtrack(i, cur):
            
            # Base case
            if i == len(nums):
                # if cur not in res:
                res.append(cur.copy())  
                return
            
            # Inlcude num path
            cur.append(nums[i])
            backtrack(i+1, cur)
            cur.pop()
            
            # Skip any repetitive elements 
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            # Do not include path
            backtrack(i+1, cur)
        
        backtrack(0, [])
        return res



        