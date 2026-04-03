class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Similar to a past binary search problem we did
        # L is set to 1 which is the minimum weight possible
        # R is the maximum weight possible
        # Calculate mid, if mid can do all weights in under X days
        # Update res and find smaller mid -> r = mid - 1
        # If it takes more than X days then we need bigger mid update l = mid + 1

        l, r = max(weights), sum(weights)
        res = float("inf")

        while l <= r:
            mid = l + (r-l)//2
            print("Weight Capacity Being Used: ", mid)

            curr_capacity = 0
            days_taken = 0

            for weight in weights:
                # Full truck
                if curr_capacity + weight > mid:
                    days_taken += 1
                    curr_capacity = 0

                curr_capacity += weight
            
            if curr_capacity > 0:
                days_taken += 1 
                
            print("Days Taken: ", days_taken)

            
            # Valid res, try to find smaller weight capacity
            if days_taken <= days:
                res = min(res, mid)
                print("Updating res: ", res)
                r = mid - 1
            
            # Invalid res
            else:
                l = mid + 1
            
        return res


              
            


        