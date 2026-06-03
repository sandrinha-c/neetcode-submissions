class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1]> nums[0] or len(nums)<=1:
            return nums[0]
        else: 
            l=0
            r=len (nums)-1
            while l <= r:
                mid= (l+r)//2
                if nums[mid-1]<nums[mid]<nums[mid+1]: #爬坡區:判斷mid在左坡or右坡 (應該不會out of index)
                    if nums[mid] < nums[-1]: #mid在右邊那段 那我要更新r 讓mid變小 而且左右比
                        r= mid
                    else: #mid在左邊那段  那我要更新l 讓mid變大 而且左右比   
                        l= mid
                if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                    return nums[mid+1]
                if nums[mid]<nums[mid-1] and nums[mid]<nums[mid+1]:
                    return nums[mid]

                