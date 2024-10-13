class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        curmin=nums[0]
        while l<=r:
            mid=l+(r-l)//2
            curmin=min(curmin,nums[mid])
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid-1
        
        return curmin

    def findMin2(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        if len(nums)==1:
            return nums[0]

        def helper(l,r):
            if l>r:
                return -1
            mid=l+(r-l)//2
            if nums[mid]<nums[mid-1]:
                return nums[mid]
            elif nums[mid]<nums[r]:
                return helper(l,mid-1)
            else:
                return helper(mid+1,r) 
        
        return helper(0,len(nums)-1)