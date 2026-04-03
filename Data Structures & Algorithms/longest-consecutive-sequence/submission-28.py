class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Init current num
        # Iterate over the list of nums
        # if the next num minus current == 1
        # increment counter
        # Otherwise restart
        # Have a global consecutive count and local, use max to update

        nums = sorted(set(nums))
        print(nums)

        count = 0
        currentCount = 0

        for i in range(len(nums)):
            # Beginning of a sequence
            if nums[i] - 1 not in nums:
                while i < len(nums) and nums[i] in nums:
                    currentCount += 1
                    i += 1
                    print("Current Count: ", currentCount)
                    if i < len(nums) and nums[i] - nums[i-1] != 1:
                        count = max(currentCount, count) # Update count 
                        currentCount = 0
                        break
                    
                    count = max(count, currentCount)
                    
                
        return count

            




