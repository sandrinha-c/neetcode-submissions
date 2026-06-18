class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps={}
        for i, num in enumerate(nums):
            need= target-num
            if need in maps:
                return [maps[need],i]
            else:
                maps[num]=i

