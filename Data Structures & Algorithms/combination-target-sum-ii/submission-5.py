from collections import defaultdict
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Same as combination sum
        # Sort the array so that you can prune, we can avoid duplicates by not starting from the same number
        # Base cases are the same

        candidates.sort()
        res = []
        startSet = set()

        def dfs(i, sol, total):
            
            # Base case: Valid Solution
            if total == target:
                print(f"Adding {sol} to res")
                res.append(sol.copy())
                return
            
            # Base case: Invalid Solution
            if total > target or i == len(candidates):
                return
            
            for j in range(i, len(candidates)):
                if candidates[j] > target - total:
                    continue
                
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                
                sol.append(candidates[j])
                # Add to starting point hashset
                print(f"Current path is {sol}")
                dfs(j+1, sol, total + candidates[j])
                sol.pop() # Backtrack
        
        
        dfs(0, [], 0)
        return res
            



            
            