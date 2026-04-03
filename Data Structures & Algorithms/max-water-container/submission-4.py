class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        i, j = 0, len(heights)-1

        for n in range(len(heights)):
            # Calculate area
            currentArea = min(heights[i], heights[j]) * (j-i)
            
            if currentArea > area:
                area = currentArea
                if heights[i] < heights[j]:
                    i += 1
                elif heights [i] >= heights[j]:
                    j -= 1


            else:
                if heights[i] < heights[j]:
                    i += 1
                elif heights [i] >= heights[j]:
                    j -= 1
            
        return area