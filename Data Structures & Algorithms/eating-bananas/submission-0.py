class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # K is the rate -> banana/hr
        # Goal is to determine most optimal K
        # Mid becomes our K -> eating rate
        # For each pile if we are under the h we move left r = mid - 1
        # If we are above we move right l = mid + 1 -> did not finish in time

        l, r = 1, max(piles)
        
        # Set res to the maximum num i.e [1, 4, 3, 2] --> 4 would take 4 hrs 
        res = max(piles) 

        while l <= r:
            hrs = 0
            k = l + (r-l)//2
            
            # Calculate hrs 
            for p in piles:
                hrs += math.ceil(p/k)
            
            # We can find a smaller K
            if hrs <= h:
                res = min(res, k) # Update res with min value
                r = k - 1
            # Was not a valid solution, k is too small
            else:
                l = k + 1
        
        return res





                



            



        