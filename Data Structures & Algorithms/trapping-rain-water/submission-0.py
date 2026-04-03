class Solution:
    def trap(self, height: List[int]) -> int:
        # Builds on container with most water
        # In order for it to be a valid container it must
        # Have 2 walls around it
        # So a container starts when we have 2 walls
        # Start l pointer at first wall
        # r pointer moves from l all the way till the next wall 
        # to calculate water being trapped use same formula
        # indices measure length and take min of heights[i]
        # Do so for all containers possible 
        # Edge case: there must be atleast 1 empty space between 
        # 2 walls to form a container

        # e.g non zero num, zero, non zero num --> container
        # Blocks in between a container must be subtracted

        res = 0

        minHeights = {}
        l = 0
        r = 0

        # Find max heights to l and r for each index
        for i in range(1, len(height)):
            l = max(height[:i])
            r = max(height[i:])
            smallest = min(l, r)
            minHeights[i] = smallest
        
        print(minHeights)
        
        
        for i in range(1, len(height)):
            area = minHeights[i] - height[i]

            if area > 0:
                res += area
        
        return res

        # # Run till end of the array
        # for i in range(1, len(height)):
        #     l = 0
        #     r = 0

        #     # Skip empty spaces
        #     if height[l] == 0:
        #         l += 1
        #         r += 1
            
        #     if height[l] > 0:
        #         # r pointer must go till next valid wall
        #         if height[r] == 0:
        #             r += 1
        #         else:




            


