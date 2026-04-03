class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # ⌊n / 2⌋ means it has to appear n//2 times
        # e.g for an array of size 9 the majority element
        # has to show up 9//2 times which is 4
        # Solution as follows: 
        # Creat a dictionary to store nums and their counts
        # Grab the max count, we don't need to verify the count
        # because the majority element always exist

        count = {}

        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1
        print(count)
        
        print(max(count, key=count.get))
        
        return max(count, key=count.get)