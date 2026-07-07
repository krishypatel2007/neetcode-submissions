class Solution:
    # Idea is to create a hashmap with the key as number, and value as number of repeats.
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1

        # now create empty nested array st in order of freq.
        arr = []
        for num, cnt in hashmap.items():
            arr.append([cnt, num])
        arr.sort() # sort by freq.
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
        
        

        
        

        