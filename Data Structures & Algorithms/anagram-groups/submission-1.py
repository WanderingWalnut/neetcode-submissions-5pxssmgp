from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Iterate through all the strings
        # Sort the strings i.e cat --> act == act
        # Store in dictionary with index
        # At the end append to res by grabbing index from dict


        # Stores anagrams and their count
        strDict = {}

        res = []

        if strs is None:
            return list([""])
        
        for i in range(len(strs)):
            letters = sorted((strs[i]))
            word = "".join(letters)
            print(word)
            # If the sorted word is not in dict, init
            if word not in strDict:
                strDict[word] = []
                strDict[word].append(strs[i])
            else:
                strDict[word].append(strs[i]) # Add the word directlyg anagram


        return list(strDict.values())



        