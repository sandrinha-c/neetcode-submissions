class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area_list=[]
        for L in range(0,len(heights)):
            print ("L=",heights[L])
            min_H= +10000
            max_area=0
            
            for R in range(L, len(heights)):
                print ("R=",heights[R])
                min_H=min(heights[R], min_H)
                print ("min_H",min_H)
                width= (R-L)+1
                area= min_H* width
                print("area=",area)
                max_area=max(max_area, area)
                max_area_list.append(max_area)
                print("max area=",max_area)
                print("max area list=",max_area_list)
        return int(max(max_area_list))