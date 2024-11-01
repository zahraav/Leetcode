class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a=a[::-1]
        b=b[::-1]
        res=[]
        carry=0
        if len(a)>=len(b):
            l=len(a)
        else :
            l=len(b)
        for i in range(l):
            ai=int(a[i])if i<len(a) else 0
            bi= int(b[i]) if i<len(b)else 0
            t=ai+bi+carry
            
            if t>=2:
                carry=t//2
                t=t%2
            else:
                carry=0
            res.append(t)
        if carry!=0:
            res.append(carry)
        res=res[::-1]

        return "".join(str(i) for i in res)