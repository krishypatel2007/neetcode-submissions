class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums): # create hashmap as we go along of nums[i] : index
            if target - nums[i] in hashmap:
                return sorted([i, hashmap[target-nums[i]]])
            hashmap[num] = i
        
