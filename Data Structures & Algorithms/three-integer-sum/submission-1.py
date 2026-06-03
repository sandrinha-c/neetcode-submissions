class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #cleaver: same idea as 2 sum
        memo=set()
        nums.sort()
        for num in nums : #num + 2 sum ==0 num=-2 sum  = target
            temp_nums=nums.copy()
            temp_nums.remove(num)
            l=0
            r=len(temp_nums)-1
            while l<r :
                two_sum = temp_nums[l] + temp_nums[r]
                if two_sum==(-num):
                    temp_list=[num, temp_nums[l],temp_nums[r]]
                    memo.add(tuple(sorted(temp_list)))
                    l=l+1
                    r=r-1
                elif two_sum<(-num):
                    l=l+1
                elif two_sum>(-num):
                    r=r-1
        final_list=list(memo)
        return final_list



                

            
            

        