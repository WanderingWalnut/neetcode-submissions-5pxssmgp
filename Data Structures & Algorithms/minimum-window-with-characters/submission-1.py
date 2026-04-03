class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # if t is empty string
        if t == "":
            return ""

        countT, window = {}, {}

        #Populate countT dictionary
        for char in t:
            countT[char] = 1 + countT.get(char, 0)
        # initilialize res and resLen
        res, resLen = [-1, -1], float("infinity")

        have, need = 0, len(countT)

        l = 0

        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)

            if char in countT and window[char] == countT[char]:
                have += 1

            while have == need:
                # Update our result
                if (r-l+1) < resLen:
                    res = l,r
                    resLen = r-l+1
                
                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l,r = res

            
        return s[l:r+1] if resLen != float("infinity") else ""






        
        