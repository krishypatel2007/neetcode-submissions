class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        offset = 1

        for i in range(1, n+1):
            # we at 1,2,4,8,... ie the 2^n numbers, we reset!
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp

            
                