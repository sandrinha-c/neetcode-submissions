class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_window,s2_window={},{}
        if len(s1) > len(s2):
            return False
        for s in s1:
            s1_window[s]=s1_window.get(s,0)+1
        
        window_size=len(s1)
        for r,ss in enumerate(s2):
            s2_window[ss]=s2_window.get(ss,0)+1

            
            if r>=window_size:
                l_ch=s2[r-window_size]

                s2_window[l_ch]-=1
                if s2_window[l_ch]==0:
                    del s2_window[l_ch]
        
            if s1_window==s2_window:
                return True
        return False    
