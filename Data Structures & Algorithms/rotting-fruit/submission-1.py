from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS, rot spreads level by level
        # Expand each level and change values from 1 to 2
        # Add all rotten fruits to queue first, similar to walls and gates

        seen = set()
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                # Add all rotten fruits to queue first
                if grid[r][c] == 2:
                    q.append([r,c])
                    seen.add((r,c))
        
        def addNext(r, c):
            # Inavlid conditions do not add to q
            if r == ROWS or c == COLS or c < 0 or r < 0 or (r,c) in seen or grid[r][c] == 0:
                return
            
            q.append([r,c])
            seen.add((r,c))
        
        time = -1 # Set to -1 because we have to init with rotten fruits
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                
                print(f"Checking (r,c) which is {grid[r][c]}")
                # Fresh fruit or rotten set to rotten
                if grid[r][c] == 2 or grid[r][c] == 1:
                    grid[r][c] = 2
                
                print(f"Now {(r,c)} is {grid[r][c]}")
                
                addNext(r+1, c)
                addNext(r-1, c)
                addNext(r, c+1)
                addNext(r, c-1)

            time += 1
            print(f"Current time is {time}")
        
        total = (sum(sum(row) for row in grid))
        print(f"Total: {total}")

        # If all 0's
        if total == 0:
            return 0

        # Check if any fresh fruit is left
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        
        # All fruit is rotten, return time
        return time

        