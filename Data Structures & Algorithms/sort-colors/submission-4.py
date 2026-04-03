class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Sorting in place, that means no new array
        # Can't use extra arrays
        # Can use my old bump alogorithim as this one doesn't have 
        # time constraints

        # Go number by number and push them to the desired location


        i = 1

        while i < len(nums):
            if i > 0 and nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
                
                # Go backwards and check and make sure its sorted
                i -= 1

                if i == 0:
                    i = 1

            else:
                i += 1 
            
    


        