class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Do BFS on each row of the matrix
        # Return true if target exists


        def bfs(l,r, row):
            
            while l <= r:

                mid = l + (r-l)//2

                if matrix[row][mid] == target:
                    print("Found target")
                    return True
                elif matrix[row][mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
                
            return False
        

        for row in range(len(matrix)):

            l, r = 0, len(matrix[0]) - 1
            returnVal = bfs(l, r, row)

            # If target is found
            if returnVal:
                return True
            
        return False
        
        

        


        