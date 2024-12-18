class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
            
        for i,elem in enumerate(nums):
            if elem>0:
                break
            if i>0 and elem==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                s=nums[i]+nums[l]+nums[r]
                if s<0:
                    l+=1
                elif s>0:
                    r-=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                    
        return res