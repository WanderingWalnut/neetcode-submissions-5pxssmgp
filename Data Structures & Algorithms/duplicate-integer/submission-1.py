class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Create dict to store occurences 
        numsDict = {}

        for num in nums:
            #Check if in dict
            if num in numsDict:
                return True
            else:
                numsDict[num] = 1
            
        return False

        


         