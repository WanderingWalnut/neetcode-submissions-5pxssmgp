class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) == 0:
            return list([])
        
        
        #Stores all the patterns for the anagrams
        anagramDict={}
        #List to store sorted words
        sortedList = []

        for i in range(len(strs)):
            #Grabs current word
            currentWord = strs[i]
            # Sorts the letters in the word
            sortedWord = ''.join(sorted(currentWord))
            # Create list with sorted words
            sortedList.append(sortedWord)
            
            # Grabs the index of each word
            if sortedWord in anagramDict:
                anagramDict[sortedWord].append(currentWord)
            else:
                anagramDict[sortedWord] = [currentWord]
            
        anagramList = list(anagramDict.values())

        return anagramList

        
        
            



        