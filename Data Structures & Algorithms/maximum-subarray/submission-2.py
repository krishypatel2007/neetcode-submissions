class Solution:
    # Retry of solution
    def maxSubArray(self, nums: List[int]) -> int:
        # Use of Kandades Algorithm:
        res = maxEnding = nums[0]
        for i in range(1, len(nums)):
            maxEnding = max(maxEnding + nums[i], nums[i])
            res = max(res, maxEnding)
        return res
        