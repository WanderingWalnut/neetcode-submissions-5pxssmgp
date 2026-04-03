class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Base case is sum of sol == target
        # 2 other cases
        # Choose another number or choose the same number

        res = []

        def dfs(i, curr, total):

            # Base case 1: found valid solution
            if total == target:
                res.append(curr.copy())
                return
            
            # Base case 2: solution cannot be found
            if i >= len(nums) or total > target:
                return
            
            # Case 1: take the num
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])

            curr.pop()

            # Case 2: don't take the num
            dfs(i+1, curr, total)
        
        
        dfs(0, [], 0)
        return res

        