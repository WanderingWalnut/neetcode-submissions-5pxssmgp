class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        pathSet = set()

        def dfs(r, c, i):
            # If we have found the entire word (base case)
            if i == len(word):
                return True
            
            # All conditions that invalidate the current char
            if (r < 0 or c < 0 or
            r >= ROWS or c >= COLS
            or board[r][c] != word[i]
            or (r,c) in pathSet):
                return False
            
            # Add current path to set
            pathSet.add((r,c))
            # Check all possible adjacent neighbours
            res = (dfs(r + 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r-1, c, i + 1) or dfs(r, c-1, i + 1))
            # Remove path we just explored
            pathSet.remove((r,c))

            return res
        # Iterate over each char and check all possible paths for solution
        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0):
                    return True
        
        return False

