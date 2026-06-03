class Solution:  #key idea: create 2 list that has all the answers. 
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L=[1]
        R=[1]*len(nums)
        result=[1]*len(nums)
        product_R=1

        for i in range(1,len(nums)):
            L.append(L[i-1]*nums[i-1])
        
            print (L)
        for j in range (len(nums)-1,-1,-1):
            print (j)
            R[j]=product_R
            product_R= product_R*nums[j]
            result[j]=(R[j]*L[j])
            print ( R, result)
        return result
