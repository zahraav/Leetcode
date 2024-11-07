class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result=[]
        def isPalindrome(substr):
            return substr==substr[::-1]
                
        def bt(i,partition):
            if i==len(s):
                result.append(partition.copy())
                return

            for j in range(i+1,len(s)+1):
                substr=s[i:j]
                if isPalindrome(substr):
                    partition.append(substr)
                    bt(j,partition)
                    partition.pop()
        bt(0,[])
        return result                