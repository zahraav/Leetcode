class Solution {
    public boolean isValidSudoku(char[][] board) {
        for(int i=0;i<9;i++){
            if(isValidRow(board,i)==false){
                return false;
            }
            if(isValidColumn(board,i)==false){
                return false;
            }
        }
        for(int i=0;i<3;i++){
            for(int j=0;j<3;j++){
                if(isValidCube(board,i*3,j*3)==false){
                    return false;
                }
            }
        }
        return true;
    }
    private boolean isValidColumn(char[][] board,int column){
        HashSet<Character> nums=new HashSet<>();
        for(int r=0;r<9;r++){
            if(nums.contains(board[r][column])&& board[r][column]!='.'){
                return false;
            }
            nums.add(board[r][column]);
        }
        return true;
    }
    private boolean isValidRow(char[][]board,int row){
        HashSet<Character> nums=new HashSet<>();
        for(int c=0;c<9;c++){
            if(nums.contains(board[row][c])&& board[row][c]!='.'){
                return false;
            }
            nums.add(board[row][c]);
        }
        return true;
    }
    private boolean isValidCube(char[][]board, int row,int column){
        HashSet<Character> nums=new HashSet<>();
        for(int r=0;r<3;r++){
            for(int c=0;c<3;c++){
                if(nums.contains(board[row+r][column+c])&& board[row+r][column+c]!='.'){
                    return false;
                }
                nums.add(board[row+r][column+c]);
            }
        }
        return true;
    }

}
