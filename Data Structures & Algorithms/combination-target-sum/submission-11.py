class Solution:
    #retry
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(index, total, path):
            # base case : ie we have found a valid path
            if target - total == 0:
                res.append(path.copy())
                return
            # check if our path is valid
            if index >= len(nums) or total > target:
                return
            # do we retry again from here, or do we skip it?
            # Decision 1: we add the next one
            path.append(nums[index])
            backtrack(index , total + nums[index], path)
            path.pop()
            # Decision 2: skip the curr one
            backtrack(index + 1, total, path)
        backtrack(0, 0, [])
        return res
            
            
            
        

        
        