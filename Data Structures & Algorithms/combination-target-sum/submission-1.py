class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Binary decision tree, at each stage we can reuse the same num or use the next num
        # Base case: if i == len(nums) -> return
        # Base case: if curTotal > target -> return
        # An optimization we can use is to sort the nums that way we 

        nums.sort()
        res = []       

        def dfs(i, sol, total):
            
            if total == target:
                print(f"Adding {sol} to res")
                res.append(sol.copy())
                return
            
            if total > target:
                return
            
            if i == len(nums):
                return

            # Take the current num
            sol.append(nums[i])
            print(f"Trying with {nums[i]} on {sol}")
            dfs(i, sol, total + nums[i])
            print(f"Backtrack, removing {nums[i]}")
            sol.pop()  
            
            # Take the next num
            print(f"Taking only {nums[i]}")
            dfs(i+1, sol, total)
            

        dfs(0,[], 0)
        return res


        