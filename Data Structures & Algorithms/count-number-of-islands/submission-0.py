class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Create a for loop that iterates over all starting points
        # Then recursively build your island
        # Our base case is when we return from the function i.e no more land pieces connect

        seen = set()
        res = 0
        ROWS, COLS = len(grid), len(grid[0])


        def dfs(r, c):

            # If that path has already been taken, don't pursue or we have hit water/out of bounds
            if (r,c) in seen or r >= ROWS or c >= COLS or c < 0 or r < 0 or grid[r][c] == "0":
                return
            
            # Add to path we have past
            seen.add((r,c))

            # Recursively explore all paths
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            

        # Check all starting island points 
        for r in range(ROWS):
            for c in range(COLS):
                # Beginning of island
                if grid[r][c] == "1" and (r,c) not in seen:
                    res += 1
                    dfs(r,c)

        return res        