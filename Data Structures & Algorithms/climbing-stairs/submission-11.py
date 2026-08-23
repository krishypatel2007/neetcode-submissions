class Solution:
    def nthFib(self, n, dp):
        # Base Case
        if n <= 2:
            return n
        
        # If we have solved this subproblem, we return it.
        if dp[n] != -1:
            return dp[n]
        
        # Calculate and return fib vlaue
        dp[n] = self.nthFib(n-1, dp) + self.nthFib(n-2, dp)
        return dp[n]
        
    def climbStairs(self, n: int) -> int:
        # Dynamic Programming approach
        dp = [-1] * (n+1)
        return self.nthFib(n,dp)
