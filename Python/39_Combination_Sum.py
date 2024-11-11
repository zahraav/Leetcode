class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]

        def bt(i,sub):
            if sum(sub)==target:
                res.append(sub.copy())
                return
            
            if sum(sub)>target:
                return
            if i>=len(candidates):
                return 
            sub.append(candidates[i])
            bt(i,sub)

            sub.pop()
            bt(i+1,sub)

        bt(0,[])  
        return res