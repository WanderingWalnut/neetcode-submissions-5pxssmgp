from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Keep a char count of s2
        # We have another res dict storing counts of s1
        # Add to s2 on each pass, if count matches return true

        if len(s1) > len(s2):
            return False

        
        res = defaultdict(int)
        count = defaultdict(int)
        
        l = 0
        r = 0

        # Create count of res
        for char in s1:
            res[char] += 1
        
        print(res)
            
        while r < len(s2):
            char = s2[r]
            # part of our res window
            if char in res:
                count[char] += 1
            
            r += 1
            
            # Window bigger than result
            if (r-l) > len(s1):
                left_char = s2[l]
                # Remove counts of items being removed
                if left_char in count:
                    count[left_char] -= 1
                    if count[s2[l]] == 0:
                        del count[s2[l]]
                l += 1
            
            if (r-l) == len(s1) and res == count:
                return True

            print("Count & Res: ", res, count)
        
        return False
                    

