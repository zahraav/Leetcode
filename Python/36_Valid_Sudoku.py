class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row,col=9,9

        def isValidRow(r):
            res=set()
            for c in range(9):
                if board[r][c] != '.' and board[r][c] in res:
                    return False
                res.add(board[r][c])
            return True
        def isValidCol(c):
            res=set()
            for r in range(9):
                if board[r][c] !='.' and board[r][c] in res:
                    return False
                res.add(board[r][c])
            return True
        def isValidBox(r,c):
            res=set()
            for i in range(r,r+3):
                for j in range(c,c+3):
                    if board[i][j] !='.' and board[i][j] in res:
                        return False
                    res.add(board[i][j])
            return True
        
        for i in range(9):
            if isValidRow(i)==False:
                return False
            if isValidCol(i)==False:
                return False
        for i in range(3):
            for j in range(3):
                if isValidBox(i*3,j*3)==False:
                    return False
        return True

