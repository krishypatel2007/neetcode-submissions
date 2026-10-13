class Solution:
    # retry of solution
    def nthFib(self, n, dp):
        # base case:
        if n <= 2:
            return n
        
        # have we seen this subproblem before? if so we return this.
        if dp[n] != -1:
            return dp[n]
        
        # Calculate our value using recursion
        dp[n] = self.nthFib(n - 1, dp) + self.nthFib(n - 2, dp)
        return dp[n]

    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n+1)
        return self.nthFib(n, dp)

        