from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Create a grid of no connections (all false)
        # If any points have both pacific and atlantic we add to res
        
        ROWS, COLS = len(heights), len(heights[0])
        pac = [[False]*COLS for _ in range(ROWS)]
        atl = [[False] *COLS for _ in range(ROWS)]

        directions = [[1,0], [-1,0], [0, 1], [0, -1]]

        # Mark it's maximum path for each edge in source
        def bfs(source, ocean):
            q = deque(source)

            while q:
                r, c = q.popleft()
                ocean[r][c] = True # The position has been traversed
                print(f"Marked {heights[r][c]} with coordinates {(r,c)} as True")

                # Grab all subsequent possible directions
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < ROWS and 0 <= nc < COLS 
                    and not ocean[nr][nc] and heights[nr][nc] >= heights[r][c]):
                
                        q.append([nr, nc])
                        # print(f"Added {(nr, nc)}")  
            
            # Return updated map of ocean
            return ocean      
        
        pacific = []
        atlantic = []

        # Grab all edges for each ocean
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    pacific.append([r,c])
                
                if r == ROWS -1 or c == COLS-1:
                    atlantic.append([r,c])
        
        pacific = bfs(pacific, pac)
        atlantic = bfs(atlantic, atl)

        res = []

        for r in range(ROWS):
            for c in range(COLS):
                # If they both are traversable on both maps
                if pacific[r][c] and atlantic[r][c]:
                    res.append([r,c])
                    print(f"{(r,c)} is part of res")
        
        return res
            





