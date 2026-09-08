class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # idea is to find the substring in s, then reduced from left side to only get substring t
        if t == "":
            return ""
        
        window, countT = {}, {}
        # create our base answer foro countT
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        # no of unique letters in window and countT
        have, need = 0, len(countT)

        res, resLen = [-1,-1], float("infinity")
        l = 0
        
        for r in range(len(s)):
            c = s[r]
            # add c to our hashmap
            window[c] = 1  + window.get(c,0)

            # check if this c is in t ie we have found ONE matching letter
            # note checking if in the HASHMAP not s itself ensures we check for duplicates
            if c in countT and window[c] == countT[c]:
                have += 1
            
            # say we have reached a substring that is viable as an answer
            while have == need:
                # update res if better than before:
                if (r - l + 1) < resLen:
                    res = [l,r]
                    resLen = (r - l + 1)
                # pop from left of window to see if we can get a min window substring
                window[s[l]] -= 1
                # check if new string is NOT viable, if not reduce have by 1.
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r+1] if resLen != float("infinity") else ""


        
