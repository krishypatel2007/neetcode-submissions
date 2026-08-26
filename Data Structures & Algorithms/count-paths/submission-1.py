class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # top down dynamic programming approach
        # m*n table of -1, show that we havent reached this point yet
        memo = [[-1] * n for _ in range(m)]
        def dfs(i,j):
            # reached 1 away from end
            if (i == m-1) and (j == n-1):
                return 1
            # chekc if out of bounds
            if (i >= m) or (j >= n):
                return 0
            # note that without line below, it would be a recursion method not using top down approach
            # check if we have seen this way before
            if memo[i][j] != -1:
                return memo[i][j]

            #return ways up and ways down
            memo[i][j] = dfs(i+1, j) + dfs(i, j+1)
            return memo[i][j]
        return dfs(0,0)
            

        