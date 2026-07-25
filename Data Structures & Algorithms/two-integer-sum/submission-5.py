class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need_map={}
        for i,num in enumerate(nums):
            need=target-num
            if need in need_map:
                return [need_map[need],i]
            else:
                need_map[num]=i
        