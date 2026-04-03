class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dict={}

        #Loop through all elements in array
        for i in range(len(nums)):
            # Current is set to the current number in the iteration
            current = nums[i]
            # Complement is the number we are trying to find
            complement = target-nums[i]
            # If complement is in the dict then return th current index and the index of the complement
            if complement in index_dict:
                return [index_dict[complement], i]
            # Or else just add the num and its index to the dict
            else:
                index_dict[nums[i]]= i




            



        