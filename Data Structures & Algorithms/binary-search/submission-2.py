class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #optimal 
        l=0
        r=len (nums)
        while (l-r)!=0:
            mid= round ((l+r)/2)
            print ("mid_idx=",mid,"nums[mid]=",nums[mid])
            if nums[mid] >target: #dont go right anymore, update r index
                print ("nums[mid] > target=",target) 
                r=mid
                print ("new nums list =", nums[l:r+1])
            elif nums[mid] <target:#dont go left anymore, update l index
                print ("nums[mid] <target=",target)
                l=mid +1
                print ("new nums list =", nums[l:r+1])
            else:
                return mid
        return -1
