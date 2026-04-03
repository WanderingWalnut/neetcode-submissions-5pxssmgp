class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Cannot sort as x axis matters here
        # i is our X axis
        # heights[i] is our Y axis
        # Create a rectangle/container that has the largest area
        # Go through the entire array, update only if new contianer is bigger
        # For heights[i] we take the lower as the max height
        # i.e 6 and 7 we would use 6 as the height
        # Move 2 pointers based on:
        # if current container is bigger move right ptr
        # if current container is smaller move left ptr

        l = 0
        r = len(heights) - 1

        res = 0
        
        while l < r:
            height = min(heights[l], heights[r])
            area = (r-l)*height
            
            # Update res with bigger container
            res = max(area, res)

            # Move pointer with smaller height
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return res


        
            


            


        