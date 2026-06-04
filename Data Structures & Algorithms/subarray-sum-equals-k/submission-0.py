class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        maps={0:1}
        curr_sum=0
        for num in nums:
            curr_sum+=num
            need=curr_sum-k
            if need in maps:
                count+=maps[need]
            maps[curr_sum]=maps.get(curr_sum,0)+1
        return count
        