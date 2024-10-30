class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        res=[""]*numRows
        i=0
        flag=True
        for ch in s:
            if flag:
                if i<numRows-1:
                    res[i]+=ch
                    i+=1
                elif i==numRows-1:
                    res[i]+=ch
                    i-=1
                    flag=False
            else:
                if i>0:
                    res[i]+=ch
                    i-=1
                elif i==0:
                    res[i]+=ch
                    i+=1
                    flag=True
        return "".join(res)