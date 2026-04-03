class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Dict = {}
        s2Dict = {}
        l = 0
        
        for char in s1:
            if char in s1Dict:
                s1Dict[char] += 1
            else:
                s1Dict[char] = 1
        
        for r in range(len(s2)):
            s2Dict[s2[r]] = s2Dict.get(s2[r], 0) + 1

            # When len of substring reaches s1
            if r - l + 1 == len(s1):
                # Checks if substrings match
                if s1Dict == s2Dict:
                    return True

                # Decrement the count of letters while moving the window
                s2Dict[s2[l]] -= 1
                #Delete the key if it equals 0
                if s2Dict[s2[l]] == 0:
                    del s2Dict[s2[l]]
                # Move left pointer
                l += 1
        return False


        
        