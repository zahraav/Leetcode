class Solution:
    def isNumber(self, s: str) -> bool:
        if s[0]=='+'or s[0]=='-':
            s=s[1:]
        if not s or (len(s)==1 and not s.isdigit()):
            return False
        isdot,ise=False,False
        i=0
        while i < len(s):
            if s[i]=='.':
                if isdot or ise :
                    return False
                if (i==0 or not s[i-1].isdigit()) and (i+1>len(s) or not s[i+1].isdigit()):
                    return False
                isdot=True
            elif s[i]=='e' or s[i]=='E':
                if ise or i==0:
                    return False
                ise=True
                i=i+1
                if i<len(s) and (s[i]=='-' or s[i]=='+'):
                    i=i+1
                if i>=len(s) or not s[i].isdigit():
                    return False
            elif not s[i].isdigit():
                return False
            i+=1            
        return True