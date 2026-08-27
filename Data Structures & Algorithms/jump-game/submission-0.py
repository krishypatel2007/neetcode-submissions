class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # lets be greedy!!
        # we work backwards, checking if we can acc make the last one
        # if not return false
        goal  = len(nums) - 1 # ie the index we want to reach
        for i in range(len(nums) - 2, -1, -1):
            # check if our jump is valid
            if i + nums[i]>= goal:
                goal = i
        return True if goal == 0 else False
