class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # Its basically a rotated array
        # Ideally find your answer in the left poriton (lower index)
        # K is our mid
        # Use l and r to figure out mid
        # Looking for the first instance of true (min index)
        # Approach -> find the peak, split the array into 2
        # Binary search on both portions, find peak
        # Do so on both sides
        
        if mountainArr.length() < 3:
            return -1 

        l, r = 0, mountainArr.length() - 1
        res = -1 

        # Find peak
        while l < r:
            mid = l + ((r-l) // 2)

            # Climbing up still
            if mountainArr.get(mid) < mountainArr.get(mid+1):
                l = mid + 1
                # peak = max(peak, mountainArr.get(mid))
            # Going down
            else:
                r = mid 
        
        peak_index = r      
        
        l, r = 0, peak_index
        
        # Search ascending side
        while l <= r:

            mid = l + ((r-l)//2)

            if mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get(mid) > target:
                r = mid - 1
            else:
                l = mid + 1
        
        # Target was not found
        if res == -1:
            l, r = peak_index, mountainArr.length() - 1

            while l <= r:

                mid = l + (r-l)//2
                # Reversed as its descending side
                if mountainArr.get(mid) == target:
                    res = mid
                    # Conintue searching for smaller index
                    r = mid -1
                elif mountainArr.get(mid) < target:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return res
    
                



        