"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # We have 2 cases
        # If values are all the same it becomes a leaf node
        # If they aren't we recurse until they are
        # Use a set to check if all values are the same or not


        if not grid or not grid[0]:
            print("💥 Empty or invalid grid passed:", grid)
            return None
        
        rowSize = len(grid)
        print(f"row size for grid: {rowSize}")
        uniqueVals = set()

        start_row, end_row = 0, len(grid)
        start_col, end_col = 0, len(grid[0])

        rMid = len(grid) // 2
        cMid = len(grid[0]) // 2

        # Grab unqiue vals in grid
        for i in range(start_row, end_row):
            for j in range(start_col, end_col):
                if grid[i][j] not in uniqueVals:
                    uniqueVals.add(grid[i][j])
                    print(f"Added {grid[i][j]}")
        
        # Is a leaf node
        if len(uniqueVals) == 1:
            if bool(list(uniqueVals)[0]) == 0:
                val = False
            else:
                val = True
            
            node = Node(val, True, None, None, None, None)
        
        # Not a leaf node
        else:
            topLeft = [row[start_col:cMid] for row in grid[start_row:rMid]]
            topRight = [row[cMid:end_col] for row in grid[start_row:rMid]]
            bottomLeft = [row[start_col:cMid] for row in grid[rMid:end_row]]
            bottomRight = [row[cMid:end_col] for row in grid[rMid:end_row]]

            
            node = Node(False, False, self.construct(topLeft), self.construct(topRight), 
                        self.construct(bottomLeft), self.construct(bottomRight))

        return node