class Solution:
    """
    Idea is to have a backtracking strategy for each cell, only traversing when the current one == 1. Once we have visited a cell, we change to a 0. This will have a time complecity of O(n*m), and space complexity of O(m*n), m,n being number of rows, columsn
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(r,c): # check if valid -> mark as visited -> check others recursively
            if (r < 0 or c < 0 or
                r >= ROWS or c>= COLS or 
                grid[r][c] == "0"):
                return
            grid[r][c] = "0"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r    , c + 1)
            dfs(r    , c - 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1
        return islands




