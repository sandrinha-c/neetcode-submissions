class Solution:
    def isPalindrome(self, s: str) -> bool:
        L_=[]
        R_=[]
        for L in range (0, len(s)):
            if s[L].isalnum() :
                l= s[L].lower()
                L_.append(l)
        print ("L_=",L_)

        for R in range (len(s)-1,-1 ,-1):
            if s[R].isalnum() :
                r= s[R].lower()
                R_.append(r)
        print ("R_=",R_)
            
        if L_== R_:
            return True
        else:
            return False