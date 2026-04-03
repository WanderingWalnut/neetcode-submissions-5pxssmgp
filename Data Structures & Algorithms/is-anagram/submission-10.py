class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Iterate over the 2 strings
        # Track counts of each letter in a dict
        # End of for loop check if dictS = dictT -> return True
        # Else return False

        dictS = {}
        dictT = {}

        # Edge case for when one str is smaller than the other
        lenStr = max(len(s), len(t))

        if len(t) != len(s):
            return False

        for i in range(lenStr):
            charS = s[i]
            charT = t[i]

            # If current char in str does not exist in dict -> init,
            # Otherwise add 1 to count
            if charS not in dictS:
                dictS[charS] = 1
            else:
                dictS[charS] += 1

            if charT not in dictT:
                dictT[charT] = 1
            else:
                dictT[charT] += 1

        if dictS == dictT:
            return True
        
        return False
        