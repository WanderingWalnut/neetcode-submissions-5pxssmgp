class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            # If current iteration is a duplicate
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            # Keep adding every iteration to set and calc'ing res length
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res