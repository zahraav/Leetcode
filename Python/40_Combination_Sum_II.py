class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()

        def helper(i,sub,curSum):
            if curSum==target:
                res.append(sub.copy())
                return
            if i>=len(candidates):
                return
            if curSum>target:
                return 
            for j in range(i,len(candidates)):
                if j > i and candidates[j-1]==candidates[j]:
                    continue 
                sub.append(candidates[j])
                helper(j+1,sub,curSum+candidates[j])
                sub.pop()
        helper(0,[],0)
        return res

