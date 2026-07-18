class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums[i] + nums[j] = -nums[k] -> use a 2 pointer method to go through i,j and check for -nums[k]
        # [-1, -4, -1, 0, 1, 2]
        #  l    m             r
        res = []
        nums.sort()

        for l in range(len(nums)):
            if l>0 and  nums[l] == nums[l-1]:
                continue
            m,r = l + 1, len(nums) - 1
            
            while m < r:
                currSum = nums[l] + nums[m] + nums[r]
                if currSum < 0:
                    m += 1
                elif currSum > 0:
                    r -= 1
                elif currSum == 0:
                    res.append([nums[l],nums[m], nums[r]])
                    m += 1
                    r -= 1
                    while m < r and nums[m] == nums[m -1]:
                        m += 1
                    while m < r and nums[r] == nums[r+1]:
                        r -= 1
        return res

            