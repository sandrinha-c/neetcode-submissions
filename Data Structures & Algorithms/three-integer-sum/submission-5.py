class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()

        for i in range (0,len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            target= -nums[i]
            while l<r:
                s=nums[l]+nums[r]
                if s == target :
                    elements=[nums[i],nums[l],nums[r]]
                    result.append(elements)
                    l+=1
                    r-=1
                    # 內層去重（關鍵在這裡）
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif s< target :
                    l+=1
                elif s> target:
                    r-=1
        return result            