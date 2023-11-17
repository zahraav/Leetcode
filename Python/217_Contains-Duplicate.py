class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numset=set()
        for i in nums:
            if i in numset:
                return True
            else:
                numset.add(i)
        return False