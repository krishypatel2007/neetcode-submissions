class Solution:
    def rob(self, nums: List[int]) -> int:
        # We use a memoization approach in which we store past subproblems in a dp table. 
        # Then use a recursive approach
        n = len(nums)
        # initialise dp table as n+1 of -1's
        dp = [-1] * (n+1)

        def dfs(i):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            # Calculate our value using recursion
            dp[i] = max(dfs(i+1), nums[i] + dfs(i+2) )
            return dp[i]
        return dfs(0)
        
            

        