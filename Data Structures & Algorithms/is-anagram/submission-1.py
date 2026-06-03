class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s={}
        count_t={}
        for word in s:
            count_s[word]= count_s.get(word, 0)+1
        print (f"count_s=", count_s)
        for word in t:
            count_t[word]=count_t.get(word, 0) + 1
        print (f"count_t=", count_t)
        if count_s == count_t:
            return True    
        else:
            return False
        