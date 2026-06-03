class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #optimal
        row_num=len(matrix)-1
        col_num=len(matrix[row_num])-1
        row=0
        l=0
        r=col_num
        while row<=row_num and l<= col_num and r<= col_num :
            value_r= matrix[row][r]
            print ("row:",row, "; l:",l,"; r:",r)
            print ("value_r=",value_r)
            if value_r < target:#jump to next row
                row+=1
            elif value_r > target: # 看看那個row 有沒有答案
                value_l=matrix[row][l]
                if value_l <target:
                    l+=1
                elif value_l >target:
                    return False
                else: #value_l== target
                    return True
            else: #value_r== target
                return True
            
        return False     

