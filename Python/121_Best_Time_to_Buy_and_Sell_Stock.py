class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        if len(prices)==1:
            return 0
        max_profit=0
        while r<len(prices):
            if prices[l]<prices[r]:
                p=prices[r]-prices[l]
                max_profit=max(p,max_profit)
            else:
                l=r
            r+=1
        return max_profit
        