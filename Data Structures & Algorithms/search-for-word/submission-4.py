class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # For each word in the graph check all possible paths
        # Use a path set to include the current path we are on (we can't take the same letter twice)

        ROWS, COLS = len(board), len(board[0])
        pathSet = set()

        def dfs(i, r, c):
            # Got all letters
            if i == len(word):
                return True

            # Check all terminating cases
            if r >= ROWS or c >= COLS or (r,c) in pathSet or r < 0 or c < 0 or board[r][c] != word[i]:
                return
            
            if board[r][c] == word[i]:
                
                # Add to set so we don't take the same letter
                pathSet.add((r,c))
                print(f"Exploring from {board[r][c]}, currently have {pathSet}")
                
                # Check all directions
                res = (dfs(i+1, r+1, c) or
                    (dfs(i+1, r, c+1) or
                    dfs(i+1, r-1, c) or
                    dfs(i+1, r, c-1)))
                
                # If we found a valid ans
                if res:
                    return res
                
                pathSet.remove((r,c))

        
        # Check from each word as starting points
        for row in range(ROWS):
            for col in range(COLS):
                # start from first letter
                if dfs(0, row, col):
                    return True
        
        return False
                
        
        # return False # If an ans is not found
        
