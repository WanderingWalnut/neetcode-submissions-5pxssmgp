class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Start from all O edges
        # Add all the O's it can get, add to visit
        # If they can do not change
        # If they can't, change to X's
        # Iterate over the grid at the end, if (r,c) in visit then leave as O otherwise X

        ROWS, COLS = len(board), len(board[0])

        visit = set()
        
        def dfs(r,c, visit):
            if r == ROWS or c == COLS or r < 0 or c < 0 or (r,c) in visit or board[r][c] == "X":
                return
            
            visit.add((r,c))
            dfs(r+1, c, visit)
            dfs(r-1, c, visit)
            dfs(r, c+1, visit)
            dfs(r, c-1, visit)
        

        for r in range(ROWS):
            for c in range(COLS):
                # Call on each edge that is an O
                if (r == 0 or c == 0 or r == ROWS-1 or c == COLS-1) and board[r][c] == "O":
                    dfs(r,c,visit)
        
        print(f"This is visit {visit}")
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    # If the edge wasn't able to reach it, it is surrounded
                    if (r,c) not in visit:
                        print(f"Changing {(r,c)} to X")
                        board[r][c] = "X"
                




        