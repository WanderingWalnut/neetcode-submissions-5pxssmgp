class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Store char counts
        sDict = {}
        tDict = {}

        #Iterate through first str
        for char in s:
            # Increment count by 1 if char exists in dict
            if char in sDict:
                sDict[char] += 1
            # If its the first occurence then initialize with 1
            else:
                sDict[char] = 1

        for char in t:
            if char in tDict:
                tDict[char] += 1
            else:
                tDict[char] = 1

        
        if sDict == tDict:
            return True
        
        return False

        