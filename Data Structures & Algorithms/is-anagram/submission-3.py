class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict,t_dict={},{}
        for s_ch in s:
            s_dict[s_ch]=s_dict.get(s_ch,0)+1
        for t_ch in t:
            t_dict[t_ch]=t_dict.get(t_ch,0)+1
        return s_dict==t_dict
        
        