class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Iterate over input array
        # Add to count dict
        # Check count, if count > 1 return true
        # else return false

        count = {}

        for i in range(len(nums)):
            cur = nums[i]
            if cur not in count:
                count[cur] = 1
            
            else:
                return True
        
        print(count)
        return False


         