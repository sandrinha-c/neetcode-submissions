class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #naive:
        l=0
        area=[]
        for l in range (0, len(heights)-1):
            r=len(heights)-1
            while l<r:
                w=r-l
                h= min(heights[r], heights[l])
                area.append(w*h)
                r-=1
        return max(area)
        
        