class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        s=s.lower()

        while l<=r:
            if s[r].isalnum() and s[l].isalnum():
                if s[r]!=s[l]:
                    return False
                r-=1
                l+=1
            elif not s[r].isalnum():
                r-=1
            elif not s[l].isalnum():
                l+=1
           
        return True