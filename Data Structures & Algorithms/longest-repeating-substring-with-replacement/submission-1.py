class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        maps={}
        max_len=0
        #window=[]
        for r,a in enumerate(s):
            maps[a]=maps.get(a,0)+1
            max_freq=max(maps.values())


            while(r - l + 1) - max(maps.values()) > k:
                a_del= s[l]
                maps[a_del]=maps.get(a_del,0)-1
                l+=1 
            window_len=r-l+1
            max_len=max(max_len, window_len)


        return max_len


        
