class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # math sol
        #from (0,0) to  (m,n), there are (m+n) Choose (m) unique ways.
        # use a iterative sol NOT factorials
        if m== 1 or n == 1:
            return 1
        if m < n:
            m, n = n, m
        
        res = j = 1
        for i in range(m, m + n - 1):
            res *= i
            res //= j
            j += 1
        return res