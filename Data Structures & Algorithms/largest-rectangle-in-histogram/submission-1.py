class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Iterate through the array, store height & width on stack
        # If height is greater than top most element pop
        # Dynamically add width's --> e.g heights = [7,1,7,2,2,4]
        # At stack = [[7,1],[2,1],[2,1]] when we add 4, we pop both the 2's
        # So we use width to update it for 4 so our stack looks like this
        # stack = [[7,1], [2,3]]
        # We just add the width and take the min of heights and calc area
        
        stack = []
        max_area = 0

        # Allows final pop to happen
        heights.append(0)


        for i in range(len(heights)):
            curr = heights[i]
            width_accum = 0

            # Next bar is smaller i.e end of block
            while stack and curr <= stack[-1][0]:
                height, width = stack.pop()
                area = height * (width_accum + width)

                # Accumulate width --> part of next block
                width_accum += width
                
                # Update max area
                max_area = max(area, max_area)
                print("Max Area: ", max_area)
            
            stack.append([curr, width_accum + 1])
            print("Added: ", stack[-1])
            print("Stack Currently: ", stack)

        return max_area

        