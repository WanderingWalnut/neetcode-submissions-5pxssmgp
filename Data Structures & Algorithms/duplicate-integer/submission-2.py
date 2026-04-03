class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Iterate over input array
        # Add to count dict
        # Check count, if count > 1 return true
        # else return false

        count = {}

        # Iterate over all nums
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1
            # Check if count is greater than 1
            if count[nums[i]] > 1:
                return True
        
        return False


         