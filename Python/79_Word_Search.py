class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

    
        def dfs(row,column,index)-> bool:
            if index==len(word):
                return True
            
            if 0<= row< len(board) and 0<= column< len(board[0]) and board[row][column]==word[index]:
                temp = board[row][column]
                board[row][column]='#'
                if dfs(row+1 , column , index+1) or dfs(row,column+1, index+1) or dfs(row-1, column, index+1) or dfs(row, column-1, index+1):
                    return True
                board[row][column]=temp
                    
            return False
            
            

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0] and dfs(i,j,0)==True:
                    return True
        return False