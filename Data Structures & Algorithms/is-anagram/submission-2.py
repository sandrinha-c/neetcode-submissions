class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_s,seen_t={},{}
        for ss in s:
            seen_s[ss]=seen_s.get(ss,0)+1

        for tt in t:
            seen_t[tt]=seen_t.get(tt,0)+1
        return seen_s == seen_t
        