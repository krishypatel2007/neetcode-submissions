class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Use Kadanes Algorithm, where we go through nums, and res is max of eiterh current subarray, or we start again.
        res = nums[0]
        # store max of potential sub array
        maxEnding = nums[0]

        for i in range(1, len(nums)):
            # We either extend current subarray, or we start a new one.
            maxEnding = max(maxEnding + nums[i], nums[i])
            # update res
            res = max(res, maxEnding)
        return res
        