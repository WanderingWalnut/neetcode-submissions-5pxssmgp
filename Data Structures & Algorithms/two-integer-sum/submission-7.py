class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}

        for i in range(len(nums)):
            current = nums[i]
            ans = target - current

            #If the missing value is in Dict 
            if ans in numsDict:
                return [numsDict[ans], i]
            else:
                #Store index if value not found
                numsDict[current] = i

                


        