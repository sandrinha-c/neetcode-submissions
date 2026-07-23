class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False

        s1_maps,s2_window={},{}
        for s in s1:
            s1_maps[s]=s1_maps.get(s,0)+1
        
        #inititate window
        for i in range (len(s1)):
            s2_window[s2[i]]=s2_window.get(s2[i],0)+1
        
        l=0
        if s1_maps== s2_window:
            return True

        for r in range(len(s1),len(s2)):
            s2_window[s2[r]]=s2_window.get(s2[r],0)+1
            #rm element
            if s2_window[s2[l]]==1:
                del s2_window[s2[l]]
            else:
                s2_window[s2[l]]=s2_window[s2[l]]-1
            if s1_maps== s2_window:
                return True
            l+=1
        
        return False
                

