class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=3:
            return max(nums)
        memo=[0]*(len(nums)-1)
        # 0-> nums-1
        for i in range(len(nums)-1):
            memo[i]=max(memo[i-2]+nums[i], memo[i-1])


        memo2=[0]*(len(nums)-1)
        for i in range(1,len(nums)):
            memo2[i-1]=max(memo2[i-3]+nums[i], memo2[i-2])


        return max(memo[len(nums)-2],memo2[len(nums)-2])