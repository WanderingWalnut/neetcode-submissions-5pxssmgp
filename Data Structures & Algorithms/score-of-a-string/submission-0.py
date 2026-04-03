class Solution:
    def scoreOfString(self, s: str) -> int:
        # Iterate over each char and then subtract and add to res
        # Go backwards to avoid indexing issues
        res = 0
        for i in range(len(s)-2, -1, -1):
            res += abs(ord(s[i]) - ord(s[i+1]))
        
        return res
            
            
        
        