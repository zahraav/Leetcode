class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispalindrome(left,right):
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True
        
        left,right=0,len(s)-1
        while left<right:
            if s[left]!=s[right]:
                print(ispalindrome(left+1,right))
                print(ispalindrome(left,right-1))
                return ispalindrome(left+1,right) or ispalindrome(left,right-1)
            left+=1
            right-=1
        return True
