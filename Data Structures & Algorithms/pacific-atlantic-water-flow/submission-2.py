class Solution:
    """
    Idea is to have 2 searches from pacific and atlantic, check for uphill ie n <= n+1 then set this as pac and same for atlantic, set all possible cells in a list of atl
    Then return pac and atlantic, else None
    This then has a time complexity of O(m x n), and space complexity of O(m x n)
    """
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # similar to a backtracking strat
        pac, atl = set(), set()
        ROWS, COLS = len(heights), len(heights[0])

        
        def dfs(r,c, visit, prevHeight):
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                heights[r][c] < prevHeight or (r,c) in visit ):
                return
            visit.add((r,c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
        
        # adding the atlantic and pacific streams
        for c in range(COLS):
            dfs(0 ,c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res
        