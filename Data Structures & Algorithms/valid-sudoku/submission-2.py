class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Look at each 3x3 box, validate and keep going
        # 2 for loops, as follows: i -> 0-2 and j -> 0-2
        # If we spot a duplicate return false
        # else return true
        # Create seperate isValid3x3 function, we'll call it isValid

        # Brute force: Check each condition seperately
        # If any issue return False

        n = len(board)

        # Check all rows 
        for i in range(n):
            seen = set()
            for row in range(n):
                if board[i][row] == ".":
                    continue
                if board[i][row] in seen:
                        print("Row False")
                        return False
                else:
                    seen.add(board[i][row])
            print("Row Seen", seen)
        
        # Check each column
        for j in range(n):
            seen = set()
            for col in range(n):
                if board[col][j] == ".":
                    continue
                if board[col][j] in seen:
                    print("Column False")
                    return False
                else:
                    seen.add(board[col][j])
            print("Column Seen: ", seen)

        # Check each sqaure (3x3) --> 9 squares
        for square in range(n):
            seen = set()
            # Iterate over each square
            for i in range(3):
                for k in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + k

                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        print(seen)
                        print("Current Num in 3x3: ", board[row][col])
                        print("Box False")
                        return False
                    else:
                        seen.add(board[row][col])
            print("Sqaure Seen: ", seen)
        return True
        

        


            

        