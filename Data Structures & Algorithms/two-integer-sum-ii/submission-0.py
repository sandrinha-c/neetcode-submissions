class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums={} #index; num
        for i, num in enumerate(numbers):
            comp= target-num
            if comp in nums:
                return [nums[comp]+1, i+1]
            nums[num]=i


