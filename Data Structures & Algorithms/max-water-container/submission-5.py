class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Brute for solution first
        res = 0

        for i in range(len(heights)):
            # Current num in the loop
            current = heights[i]
            for j in range(i+1, len(heights)):
                height = min(current, heights[j])
                # print("This is height: ", height)
                length = j - i
                # print("This is length: ", length)
                area = height * length
                res =max(area, res)
                #print("Current max area: ", res)

        return res
            


        