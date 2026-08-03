class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(index, total, path):
            # Base case, ie we have found a sum == target
            if total == target:
                res.append(path.copy())
                return
            # We have found an invalid path
            if index >= len(nums) or total > target: 
                return

            # Decision 1: include nums[index]
            path.append(nums[index])
            backtrack(index, total + nums[index], path)
            path.pop()

            # Decision 2: skip nums[index]
            backtrack(index + 1, total, path)
        backtrack(0, 0, [])
        return res
