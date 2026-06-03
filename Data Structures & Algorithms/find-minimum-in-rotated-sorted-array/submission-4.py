class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)<=1 or nums[-1]> nums[0]:
            return nums[0]
        else: 
            l=0
            r=len (nums)-1
            while l < r:
                mid= (l+r)//2
                if nums[mid]> nums[r]:# mid min, l moves to right
                    l=mid+1
                else: # min mid , r moves to left
                    r=mid
            return nums[r]
