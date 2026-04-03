from collections import defaultdict
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 2 Terminating cases(Base Cases):
        # i >= target or total > target
        # total == target
        # In the case it's not a valid or invalid solution we have 2 cases
        # Take the number & do not take the number just stick with itself only
        # dfs(i+1) and dfs(i) -> if we take dfs(i) we don't move further we evaluate if that's a sol
        # Basically exploring all possible combos with the num at index i

        candidates.sort()
        res = []


        def dfs(i, cur, total):
            # Valid solution
            if total == target:
                if cur not in res:
                    res.append(cur.copy())
                return
            
            # Invalid solution
            if i == len(candidates) or total > target:
                return
            
            # Do not take any other nums
            dfs(i+1, cur, total)

            # Take the num
            cur.append(candidates[i])
            dfs(i+1, cur, total + candidates[i])

            cur.pop()
        
        dfs(0, [], 0)

        return res


            
            