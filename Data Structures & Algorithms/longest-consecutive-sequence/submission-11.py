class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 1 # count of consecutive elements
        max_count = 1

        # Removes duplicates and sorts the nums
        nums = list(set(nums))
        nums.sort()
        len_nums = len(nums)

        # If list is empty return 0
        if (len(nums) == 0):
                max_count = 0
                return max_count

        # Loop thru all elements and find the longest sequence

        for i in range(1,len(nums)):
            # Comapre if current number is consecutive to the previous one
            if (nums[i] == nums[i-1] + 1):
                count += 1
            # If consecutive streak ends, update max_count
            else:
                max_count = max(max_count, count)
                count = 1
        # Update max_count one last time to ensure the last sequence was considered 
        max_count = max(max_count, count)

        return max_count