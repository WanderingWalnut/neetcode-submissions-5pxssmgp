from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Same as Permuatation in string --> builds on it
        # Slide across the str, keep track of window
        # Once the counts match up for each letter use len to update res
        # We want to get the min result
        # When window == len(t), check the dict to see if its valid res
        # Just those letters need to be a part of the str 
        # i.e we can have extras --> Input: s = "OUZODYXAZV", t = "XYZ"
        # "YXAZ" is the solution we're allowed to have A in the res

        # Standardize the strs
        s.lower()
        t.lower()

        if len(s) < len(t):
            return ""

        res = len(s) # Entire str
        resStr = "" # Only update if min(window) < res

        target = defaultdict(int)

        # Create our target dict
        for i in range(len(t)):
            target[t[i]] += 1
        
        required = len(target) # Unique characters in s
        formed = 0 # How many valid chars do we have

        l = 0

        window = defaultdict(int)

        for r in range(len(s)):
            char = s[r]
            window[char] += 1
            
            # Beginning of a valid sequence
            if char in target and window[char] == target[char]:
                formed += 1

                # Reduce the window from the left till we achieve smallest res
                while formed == required:

                    # Update res
                    if (r-l) < res:
                        res = r-l
                        resStr = s[l:r+1]
                        print("New resStr: ", resStr)
                    
                    # Pop element we are moving away from
                    window[s[l]] -= 1
                    
                    if s[l] in target and window[s[l]] < target[s[l]]:
                        formed -= 1 # Not matching anymore, so lower count
                    
                    l += 1
                    
        return resStr
                
                    






        



        