class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]

        def bt(i,sub):
            if len(sub)==k:
                res.append(sub.copy())
                return
            if i>n:
                return
            sub.append(i)
            bt(i+1,sub)
            
            sub.pop()
            bt(i+1,sub)
        
        bt(1,[])
        return res