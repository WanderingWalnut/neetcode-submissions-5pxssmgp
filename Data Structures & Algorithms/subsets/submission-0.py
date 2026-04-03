class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Base case is i == len(nums)
        # Other 2 cases are if we pick the num at index i and we dont
        n = len(nums)
        res, sol = [], []
        

        def backtrack(i):

            if i == n:
                res.append(sol[:]) # Append a copy -> res.append(sol) this just adds a referecne
                return
            
            # Do not pick the num, next func
            backtrack(i+1)

            # Pick the num
            sol.append(nums[i])
            backtrack(i+1)

            # Pop that num after
            sol.pop()
        
        backtrack(0)
        return res