class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int n=cost.length;
        if(n<2){return cost[n];}
        int[]dp=new int[n+1];
        dp[0]=cost[0];
        dp[1]=cost[1];
        for(int i=2;i<=n;i++){
            if (i<n){
                dp[i]=Math.min(dp[i-1]+cost[i],dp[i-2]+cost[i]);
            }else{
                dp[i]=Math.min(dp[i-1],dp[i-2]);
            }
        }
        return dp[n];
    }
}
/*
class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int n=cost.length;
        if(n<2){return cost[n];}
        int prev1=cost[0];
        int prev2=cost[1];
        for(int i=2;i<=n;i++){
            int cur=Math.min(prev1,prev2)+ (i < n ? cost[i] : 0);
            prev1=prev2;
            prev2=cur;
        }
        return prev2;
    }
}

*/
