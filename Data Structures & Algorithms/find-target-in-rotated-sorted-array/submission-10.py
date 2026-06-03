class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)<=1:
            if nums[0] == target:
                return 0
            else:
                return -1
        l=0
        r=len(nums)-1
        if nums[-1]> nums[0]: #not rotated
            while l <= r:
                mid=(l+r)//2
                if target>nums[mid]:
                    l=mid+1
                elif target < nums [mid]:
                    r=mid-1
                elif target== nums[mid]:
                    return mid
            return -1
        else:
            while l <= r:
                mid=(l+r)//2
                if target == nums[mid]:
                    return mid
                if nums[mid] >= nums[l]: # mid in left arr (range: l~ mid)
                    if target in range (nums[l],nums[mid]+1):
                        r=mid-1
                    else:  #target on right arr (btwn mid+1 and r)
                        l=mid+1
                else:
                    if target in range(nums[mid],nums[r]+1):
                        l= mid+1
                    else:
                        r=mid-1
            return -1
               
                  


