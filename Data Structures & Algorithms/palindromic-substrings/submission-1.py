class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        # helper function to check for panidrome substring
        def checkPalindrome(l, r):
            nonlocal res
            while l >= 0 and r < len(s) and s[l] == s[r]: # ie a valid palindrom
                res += 1
                l -= 1
                r += 1
        
        for i in range(len(s)):
            # odd case
            l, r = i, i
            checkPalindrome(l,r)

            # even case
            l, r = i, i + 1
            checkPalindrome(l,r)
        return res
       


