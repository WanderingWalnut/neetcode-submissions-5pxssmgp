class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Base case is when we have created the entire board
        # if i and j == n
        # Constraint is the movements of queens
        # Create a for loop to iterate over all starting positions within the board

        # Setup board
        board = [["."]*n for row in range(n)]
        print(board)

        col = set()
        negDiag = set() # (r-c)
        posDiag = set() # (r+c)
        res = []
        
        def backtrack(r):

            # Base case
            if r == n:
                res.append(["".join(r) for r in board])
                return
            
            # Run a for loop to try and place each Q at every position
            # Check each position
            for c in range(n):
                # If it invalidates our condition skip to next pos
                if c in col or (r-c) in negDiag or (r+c) in posDiag:
                    continue
                
                # If valid update pos and add to constraint set
                board[r][c] = "Q"
                col.add(c)
                negDiag.add(r-c)
                posDiag.add(r+c)

                backtrack(r+1) 
                
                # Backtracking step
                board[r][c] = "."
                col.remove(c)
                negDiag.remove(r-c)
                posDiag.remove(r+c)
        
        backtrack(0)
        return res


        