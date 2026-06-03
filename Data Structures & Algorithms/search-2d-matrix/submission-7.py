class Solution:
    def find_mid(self,x,y)-> int:
        return (x+y)//2
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #final_optimal
        #start indx:
        row_upper=0
        row_btm=len(matrix)-1
        #print("row_btm=",row_btm)
        row= self.find_mid(row_upper,row_btm)
   
        while row_upper <= row_btm:
            value_l=matrix[row][0]
            value_r=matrix[row][len(matrix[0])-1]
            if target not in range (value_l, value_r):
                if target>value_r:
                    row_upper=row+1
                    row=self.find_mid(row_upper, row_btm)
                elif target< value_l:
                    row_btm=row-1
                    row=self.find_mid(row_upper, row_btm)
                else: #target == value_R
                    return True
            else: #target in range
                l=0
                r=len(matrix[0])-1
                while l<=r:
                    mid=self.find_mid(l,r)
                    value_mid= matrix[row][mid] 
                    print ("l_now:",l,"r_now",r,"mid:", mid, "value_mid:",value_mid)
                    if target> value_mid: #l 往右移
                        l=mid+1
                        print ("L got update to:",l)
                    elif target <value_mid:
                        r=mid-1
                        print ("R got update to:",r)
                    else:#target == value_mid
                        return True
                return False
                    
        return False             




