class Solution:
    # retry of solution
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        # what this dfs search does is once it sees an island, it just clears it from the map
        def dfs(r, c):
            # are we out of bounds, or is there no island next to us?
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or 
                grid[r][c] == "0"):
                return
            # mark the one we are on (which is an island) as seen
            grid[r][c] = "0"
            # check recursively for other islands
            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r - 1, c)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1
        return islands
        
                
            
            

        