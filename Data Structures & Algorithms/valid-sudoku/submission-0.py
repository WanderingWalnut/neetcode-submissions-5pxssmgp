class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = set()
        column_set = set()
        subgrids = {
            (0, 0): set(), (0, 1): set(), (0, 2): set(),
            (1, 0): set(), (1, 1): set(), (1, 2): set(),
            (2, 0): set(), (2, 1): set(), (2, 2): set(),
        }


        for i in range(9):
            row_set.clear()
            column_set.clear()
            for j in range (9):
                currentRowNum = board[i][j]
                currentColumnNum = board[j][i]

                # Check rows
                if (currentRowNum != '.'):
                    if currentRowNum in row_set:
                        return False
                    else:
                        row_set.add(board[i][j])
                # Check columns
                if (currentColumnNum != '.'):
                    if currentColumnNum in column_set:
                        return False
                    else:
                        column_set.add(board[j][i])
                
                # Check subgrids

                if (currentRowNum != "."):
                    grid_key = (i//3,j//3)
                    if currentRowNum in subgrids[grid_key]:
                        return False
                    else:
                        subgrids[grid_key].add(currentRowNum)
                    
        return True

                

                

        
        