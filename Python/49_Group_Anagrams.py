class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedList=[]
        result={}
        for s in strs:
            word=''.join(sorted(s))
            if word in result:
                result[word].append(s)
            else:
                result[word]=[s]
        
        return result.values()