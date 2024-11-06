class Solution:
    def simplifyPath(self, path: str) -> str:
        temp=path.split("/")
        res=['/']
        for i in temp:
            if i=='..':
                if len(res)>=3:
                    res.pop()
                    res.pop()
                    
            elif i=='...' or i=='....':
                res.append(i)
                res.append('/')
            elif i=='.':
                pass
            elif i=='/' or i=='':
                pass
            else:
                res.append(i)
                res.append('/')
        if res[-1]=='/' and len(res)>1:
            res.pop()
        return "".join(res)