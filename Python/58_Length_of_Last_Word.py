class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s[::-1]
        s=s.strip()
        for i in range(len(s)):
            if s[i] ==" ":
                return i

        return len(s)