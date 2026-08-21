class Solution:
    def climbStairs(self, n: int) -> int:
        # Note that for n > 2, we have that f(n) = f(n-1) + f(n-2), f(1) =1, 
        # f(2) = 2. Hence we can work backwards from here.
        
        if n<= 2:
            return n

        f2, f1 = 1, 2

        for i in range(3, n+1):
            current = f1 + f2
            f2 = f1
            f1 = current
        return current



            
