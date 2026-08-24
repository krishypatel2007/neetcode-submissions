class Solution:
    # using a dynamic programming approach, O(n^2) time complexity and O(n) space complex.
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        resLen  = 0

        # helper function to check for panidrome substring
        def checkPalindrome(l, r):
            nonlocal res, resLen
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1


        for i in range(len(s)):
            # even case
            l, r = i, i
            checkPalindrome(l,r)

            # odd case
            l, r = i, i + 1
            checkPalindrome(l,r)
        return res
        
        