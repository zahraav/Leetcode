class Solution:
    def grayCode(self, n: int) -> List[int]:
        res=[0]

        for i in range(n):
            temp = []
            for x in reversed(res):
                temp.append((1 << i) | x)
            res.extend(temp)
        return res