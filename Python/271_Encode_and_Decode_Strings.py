from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        sizes=[]
        for i in strs:
            res+=str(len(i))+"#"+i
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        word=""
        i=0
        while i <len(s):
            j=i
            while s[j]!='#':
                j+=1
            size=int(s[i:j])
            i=j+1
            word=s[i:i+size]
            res.append(word)
            i+=size
        return res


test_case = ["neet", "code", "love", "you"]

solution = Solution()
encoded = solution.encode(test_case)
decoded = solution.decode(encoded)

print("Encoded:", encoded)
print("Decoded:", decoded)