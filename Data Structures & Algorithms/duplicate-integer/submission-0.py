class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        current = 0

        for i in range(len(nums)):
            current = nums[i]
            counter = 0

            for n in range(len(nums)): 
                if (current == nums[n]):
                    counter = counter + 1

                if (counter >= 2):
                    return True
        
        return False
            
         