class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #optimal
        l=0
        r=len(heights)-1
        area=[]
        while l<r:
            area.append( min(heights[l],heights[r])*(r-l))
            if heights[l]< heights[r]:
                l+=1
            elif heights[l] > heights[r]:
                r-=1
            else: # heights[l]== heights[r] 還是要往下走
                l+=1
                r-=1
        return max(area)
