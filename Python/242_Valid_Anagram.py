class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letterdict={}
        for c in s:
            if c in letterdict.keys():
                letterdict[c]+=1
            else:
                letterdict[c]=1
        for c in t:
            if c in letterdict.keys() and letterdict[c]>0:
                letterdict[c]-=1
            else:
                return False
        for i in letterdict.keys():
            if letterdict[i]>0:
                return False
        return True