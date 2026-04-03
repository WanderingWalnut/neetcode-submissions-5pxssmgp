class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # If the length of strings does not match then it cannot be an anagram
        if (len(s) != len(t)):
            return False

        # Turn strings into a list of letters 
        s = list(s)
        t = list(t)

        # Dictionary to store the key/value pairs of the letters
        firstString = {}
        secondString = {}

        # Updates dictionary with count of each letter
        for i in range(len(s)):
            if s[i] in firstString:
                firstString[s[i]] += 1
            else:
                firstString[s[i]] = 1
            if t[i] in secondString:
                secondString[t[i]] += 1
            else:
                secondString[t[i]] = 1

        # Returns bool value if both dictionaries have the same count
        if (firstString == secondString):
            return True
        
        return False



