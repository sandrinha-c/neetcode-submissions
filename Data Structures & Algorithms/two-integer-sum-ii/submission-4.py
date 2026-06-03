class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #2 pointer
        
        for i_L in range(0,len(numbers)):
            print (i_L)
            i_R=len(numbers)-1
            while i_L < i_R:
                print ("l_indx=", i_L,"; R_idx=", i_R)
                print ("L:",numbers[i_L], "; R:",numbers[i_R])
                result= numbers[i_L]+ numbers[i_R]
                if result== target:
                    return [i_L+1, i_R+1]
                else:
                    i_R-=1
