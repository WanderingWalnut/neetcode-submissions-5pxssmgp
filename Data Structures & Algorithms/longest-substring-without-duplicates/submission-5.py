class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Condition that breaks a substring is a repeating character

        charSet = set() # Check if char is in substring
        substringSize = 0 # Size of substring

        l = 0

        for r in range(len(s)):
            # If duplicate occurs
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            
            charSet.add(s[r])
            substringSize = max(substringSize, r -l +1)
            print(charSet)
        
        return substringSize






        