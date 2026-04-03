class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Treat the arr as a linked list
        # Each num is an index
        # First loop gets first intersection
        # Second loop gets the 2nd intersection which is our beginning of cycle (duplicate)
        # Floyd's cycle detection problem

        slow, fast = 0, 0

        # Find first overlap
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        # Find second overlap
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        
        

        