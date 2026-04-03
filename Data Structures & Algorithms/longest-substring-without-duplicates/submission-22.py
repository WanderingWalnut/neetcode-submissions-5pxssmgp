class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Create a sliding window
        # Increase on every iteration
        # Decrease on a duplicate detected
        # On each pass, update max (res)

        l = 0
        res = 0

        charSet = set()

        print("Len of S: ", len(s))



        for r in range(len(s)):
            # currStr = s[l:r] # Current window

            # If new char is a duplicate
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            
            charSet.add(s[r])
            res = max(r - l + 1, res)

            print("currStr: ", charSet)
        
        return res
