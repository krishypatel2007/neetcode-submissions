class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # using a dynamic programming approach, in which we iterate backwards and use prev answers
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            # check for LIS from i
            for j in range(i+1, len(nums)):
                #check for strictly increasing
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)