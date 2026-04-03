class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Similar to yesterday's problem but instead we update a res var which represents max size 
        # Keep a size varibale and when we hit our base case we update our res variable
        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        seen = set()

        def dfs(r, c):
            nonlocal res

            # All invalid conditions
            if r >= ROWS or c >= COLS or c < 0 or r < 0 or (r,c) in seen or grid[r][c] == 0:
                return 0
            
            # Add to path
            seen.add((r,c))
            print(f"Checking all paths from {(r,c)}")
            
            # Check all directions and add their sizes
            size = 1 + (dfs(r+1, c) +
            dfs(r-1, c) + 
            dfs(r, c+1) + 
            dfs(r, c-1))

            print(f"Returning {size}")
            return size


        for r in range(ROWS):
            for c in range(COLS):
                # Beginning of a sequence
                if grid[r][c] == 1 and (r,c) not in seen:
                    size = dfs(r, c)
                    res = max(res, size)
                    print(f"Size is {size} and res is {res}")
        
        return res