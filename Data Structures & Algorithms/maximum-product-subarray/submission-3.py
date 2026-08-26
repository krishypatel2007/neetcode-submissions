class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMax, currMin = 1,1 # since products, 1 doesnt matter

        for num in nums:
            
            # either carry on subarray produtct, start a new one, or carry on the min ie the curr is -ve
            temp = currMax * num
            currMax = max(num, currMax * num, currMin * num)
            currMin = min(num, temp, currMin * num)
            res = max(res, currMax)
        return res


