class Solution:
    def climbStairs(self, n: int) -> int:
        memo_dict={}
        return self.helper(n,memo_dict)

    def helper(self, n:int, memo_dict: dict[int,int])-> int:
        if n==1 or n==0:
            return 1
        
        if n not in memo_dict:
            memo_dict[n]=self.helper(n-1,memo_dict)+self.helper(n-2,memo_dict)
        
        return memo_dict[n] 