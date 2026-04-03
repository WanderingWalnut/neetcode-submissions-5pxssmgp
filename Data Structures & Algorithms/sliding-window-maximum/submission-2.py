class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Create a decreasing queue
        # Always grab the first element in the queue (maxNum)
        # If current num is greater than num in queue, keep popping
        # If current num is less than or equal to num in queue return left element
        # Ensure we are always grabbing maxNum
        # Make sure to remove elements outside of window

        res = []
        q = collections.deque() # Store indices
        l = r = 0

        while r < len(nums):
            
            # Before adding new num ensure biggest num is left most element
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)
            
            # Remove left most element from window when it is out of window
            if l > q[0]:
                q.popleft()
            
            # Valid window
            if (r-l+1) == k:
                res.append(nums[q[0]])
                l += 1
            
            r += 1

        return res






        