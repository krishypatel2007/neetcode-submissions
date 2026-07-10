class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for num in numSet:
            if (num - 1) not in numSet: # check for start
                length = 1
                while (num + length) in numSet:
                    length += 1
                # reached max length
                res = max(length, res)
        return res