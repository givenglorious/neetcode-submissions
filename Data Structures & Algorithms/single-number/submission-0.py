class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        maps = set()
        for i in nums:
            if i in maps:
              maps.remove(i) 
            else:
              maps.add(i)
        return list(maps)[0]

