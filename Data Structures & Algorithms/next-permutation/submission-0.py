class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2 # -1 for the second last no, another -1 for the index in python
        # find oour "pivot point"
        while i >= 0 and nums[i] >= nums[i +1]:
            i -= 1
        # found our pivot!!
        #replace with least diff one
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # reverse the string from i + 1 afterwards
        l, r = i + 1, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


        