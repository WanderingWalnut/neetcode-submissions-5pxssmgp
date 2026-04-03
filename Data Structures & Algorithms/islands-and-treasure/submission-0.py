from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # For each piece of land find it's nearest treasure
        # Iterate over all possible places, trigger dfs when land
        # DFS function should return the distance and modify that land value
        # Should be BFS -> shortest distance == BFS in unweighted graph


        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        q = deque()

        def addLand(r,c):
            # Invalid cases, do not add to queue
            if r == ROWS or c == COLS or c < 0 or r < 0 or (r,c) in seen or grid[r][c] == -1:
                return
            
            q.append([r,c])
            seen.add((r,c))

        # Put all treasure chests in the queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    seen.add((r,c))
        
        dist = 0

        while q:
            # Iterate over all items in the layer
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                print(f"Changed {(r,c)} to {dist}")

                # Add the land around the chest/subsequent land to the queue
                addLand(r+1, c)
                addLand(r-1, c)
                addLand(r, c+1)
                addLand(r, c-1)
            
            dist += 1

                

        