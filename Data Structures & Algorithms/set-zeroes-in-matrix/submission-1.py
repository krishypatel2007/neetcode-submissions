class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        # store the flag for first col!
        flag = False
        # check for 0s, check for flag. change top row/ left col to mark
        for r in range(ROWS):
            for c in range(COLS):
                # mark top row as 0
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        flag = True
                
        # change rest of matrix
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        # check top left entry and adjist left col
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        if flag:
            for c in range(COLS):
                matrix[0][c] = 0

        

        
        