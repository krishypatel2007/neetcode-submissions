class Solution:
    
    def hasDuplicate(self, nums: List[int]) -> bool:
        repeats = []
        for num in nums:
            if num in repeats:
                return True
            else:
                repeats.append(num)
        return False
        