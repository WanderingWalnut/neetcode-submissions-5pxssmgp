class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0

        for r in range(len(s)):
            # Keep track of the occurence of each char
            count[s[r]] = 1 + count.get(s[r], 0)

            # Checks if its a valid substring
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            # Update res if current substring is larger
            res = max(res, r - l + 1)
        
        return res
        