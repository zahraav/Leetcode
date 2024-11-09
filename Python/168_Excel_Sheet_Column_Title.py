class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res=[]

        while columnNumber>0:
            columnNumber-=1
            reminder=columnNumber%26
            res.append(chr(reminder + ord('A')))
            columnNumber=columnNumber//26
        
        
        return "".join(reversed(res))