class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Base case is when i == len(nums)
        # For each num in nums create all permutations
        # So for 1,2,3 we start with 1 and so we can create 1,2,3 and 1,3,2


        res = []

        def dfs(i, path):
            if i == len(nums):
                res.append(path.copy())

            # Iterate over each num
            for j in range(len(nums)):
                # If it already is in current res skip it
                if nums[j] in path:
                    continue
                
                path.append(nums[j])
                print(f"Creating path: {path}")
                dfs(i+1, path)
                path.pop()

        dfs(0, [])
        return res
