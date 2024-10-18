class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res=[]
        subset=[]

        def helper(i):
            if i>= len(s):
                res.append("".join(subset))
                return
            subset.append(s[i])
            helper(i+1)
            subset.pop()
            if s[i].isalpha():
                subset.append(s[i].swapcase())
                helper(i+1)
                subset.pop()
        helper(0)
        return res
