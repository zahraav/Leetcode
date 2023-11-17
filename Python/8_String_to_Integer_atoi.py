class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.lstrip()
        if len(s)==0:
            return 0
        sign=1
        if s[0]=='-':
            sign=-1
            s=s[1:]
        elif s[0]=='+':
            sign=1
            s=s[1:]
        snum=""
        for i in range(len(s)):
            if s[i] in "0123456789":
                snum+=s[i]
            else:
                break
        if len(snum)==0:
            return 0
        num=int(snum)*sign
        if num> 2**31-1:
            num=2**31-1
        elif num< -2**31:
            num=-2**31
        return num