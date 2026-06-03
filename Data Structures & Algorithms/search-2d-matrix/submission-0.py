class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #naive:
        for row in matrix:
            for i in range (0,len(row)):
                value=row[i]
                if value== target:
                    return True
        return False 
        