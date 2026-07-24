class Solution:
    def isPalindrome(self, s: str) -> bool:
        left,right=[],[]
        for i in range (len(s)):
            if s[i].isalnum():
                left.append(s[i].lower())
        for j in range(len(s)-1,-1,-1):
            if s[j].isalnum():
                right.append(s[j].lower())
        return left==right