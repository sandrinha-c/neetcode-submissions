class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=[]
        right=[]

        for ch in s:
            if ch.isalnum():
                asc_L=ord(ch.lower())
                l=asc_L if ch.isalpha() else ch
                left.append(l)
        print (f"left:{left}")

        for k in reversed(s):
            if k.isalnum():
                asc_R=ord(k.lower())
                R=asc_R if k.isalpha() else k
                right.append(R)
        print (f"right:{right}")
        if left!= right:
            return False
        return True
                        


        