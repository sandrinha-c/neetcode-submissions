class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row check:
        for row in board:
            #print (f"row is {row}" )
            check_row=set()
            for num in row:
                #print (f"num is {num}")
                if num!= ".":
                    if num in check_row:
                        return False
                    check_row.add(num)
                        
        #col check:
        for col in range (9):
            check_col=set()
            for row_i in range (9):
                #print (f"board [{row_i}][{col}] is {board[row_i][col]}")
                if board[row_i][col] != ".":
                    if board[row_i][col] in check_col:
                        return False
                    check_col.add(board[row_i][col])
                        
            #print (f"check_col= {check_col}")
        # grid check:
        start_col=[0,3,6]
        start_row=[0,3,6]



        for start_row in [0,3,6] :
            for start_col in [0,3,6]:
                check=set()
                for row in range(3):
                    for col in range (3):
                        num=board[start_row+row][start_col+col]
                        print(f"board[{start_row+row}][{start_col+col}] = {num}")
                        if num != ".":
                            if num in check:
                                print (f"false: {num}")
                                return False
                        check.add( num )
                        print (f" check = {check}")
        return True





        