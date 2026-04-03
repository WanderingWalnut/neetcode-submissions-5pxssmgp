class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Brute for solution first
        res = 0

        # Set indices for 2 pointers
        l = 0 
        r = len(heights) - 1

        for i in range(len(heights)):
            while l < r:
                area = (r - l) * min(heights[l], heights[r])
                res = max(area, res) # Update res variable

                if heights[l] > heights[r]:
                    r -= 1
                else:
                    l += 1

            

            
            

        return res
            


        