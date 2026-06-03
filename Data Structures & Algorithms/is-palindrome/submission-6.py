class Solution:
    def isPalindrome(self, s: str) -> bool:
        L_idx=0
        R_idx=len(s)-1
        while (L_idx< R_idx) :
            while L_idx != len(s)-1 and not s[L_idx].isalnum()   :
                L_idx+=1
            while R_idx != 0 and not s[R_idx].isalnum() :
                R_idx-=1
            if L_idx>=R_idx:
                return True # complete all the elements scanned
            elif s[L_idx].lower()!=s[R_idx].lower():
                return False
            else:
                L_idx+=1
                R_idx-=1
             
        return True
        