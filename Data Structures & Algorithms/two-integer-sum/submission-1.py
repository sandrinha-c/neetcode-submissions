class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_track={}
        for i, num in enumerate(nums):
            comp= target- num
            if comp in num_track:
                return [num_track[comp], i]
            num_track[num]=i   

            

        
        