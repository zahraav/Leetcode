class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')  
        min_diff = float('inf') 

        for i, num in enumerate(nums[:-2]):
            l, r = i + 1, len(nums) - 1

            while l < r:
                x = num + nums[l] + nums[r]
                diff = abs(target - x) 

                if diff < min_diff:
                    min_diff = diff
                    closest = x 

                if x < target:
                    l += 1  
                elif x > target:
                    r -= 1 
                else: 
                    return x
        
        return closest
