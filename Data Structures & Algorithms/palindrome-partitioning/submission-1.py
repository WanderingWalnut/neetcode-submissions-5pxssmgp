class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Base case is: i == len(s)
        # For each starting variation in s
        # We check all possible palindromes
        # So for aab we can create "a", "aa", and "aab"
        # If the inital starting point is valid 
        # keep creating nested recursive calls

        res = []

        def dfs(i, part):

            if i == len(s):
                res.append(part.copy())
                return
            

            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    part.append(s[i:j+1])
                    dfs(j+1, part)
                    part.pop()
                
        dfs(0, [])
        return res

        