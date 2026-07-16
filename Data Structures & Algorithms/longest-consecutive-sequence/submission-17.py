class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # put everything into hashmap -> iterate through nums, checking for start of a possible subsqeunce -> count possible length and compare with max -> after loop, return max.
        hashmap = set(nums)
        res =  0
        for num in nums:
            if (num-1) not in hashmap: # ie we have found a possible start
                length = 1
                while (num+length) in hashmap:
                    length += 1
                res = max(res, length)
        return res
                


        