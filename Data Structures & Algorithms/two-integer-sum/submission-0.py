class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dict={}

        for i in range(len(nums)):
            current = nums[i]
            complement = target-nums[i]
            if complement in index_dict:
                return [index_dict[complement], i]
            else:
                index_dict[nums[i]]= i




            



        