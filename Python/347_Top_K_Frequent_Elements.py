class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt={}
        for i in nums:
            if i not in cnt.keys():
                cnt[i]=0
            cnt[i]+=1

        sorted_counts=sorted(cnt.items(), key= lambda y:y[1],reverse=True)
        res=[]
        for i in range(k):
            res.append(sorted_counts[i][0])

        return res