class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        
        memo=[0]*len(nums)
        for i in range(len(nums)):
            memo[i]= max(memo[i-2]+nums[i],memo[i-1])
        return memo[len(nums)-1]