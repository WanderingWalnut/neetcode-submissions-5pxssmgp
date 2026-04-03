class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #Sort the original array
        nums = set(nums)

        #Keep count of consecutive nums
        count = 1

        if not nums:
            return 0

        for num in nums:
            # Check if sequence
            if num - 1 not in nums:
                localCount = 1
                # Increase local count for every consecutive num
                while (num + localCount) in nums:
                    localCount += 1
                count = max(localCount, count)

        return count

