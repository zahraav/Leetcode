class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res=0
        for i in columnTitle:
            res=(ord(i) - ord('A') + 1) + res*26
        return res
