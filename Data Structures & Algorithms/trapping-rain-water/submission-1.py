class Solution:
    def trap(self, height: List[int]) -> int:
        water=[]
        for i in range (0, len(height)):
            print ("i=",i, "; height_i=",height[i])
            h_i= height[i]
            h_left_max=0
            h_right_max=0
            l = i-1
            r=i+1
            while l>=0:
                #print ("old l=",l, "; old h_left_max=",h_left_max)
                h_l=height[l]
                h_left_max=max(h_left_max, h_l)
                l-=1
                #print ("new l=",l, "; new h_left_max=",h_left_max)
            #print ("h_left_max final=",h_left_max)
            while r<=len(height)-1:
                #print ("old l=",l, "; old h_left_max=",h_left_max)
                h_r=height[r]
                h_right_max=max(h_right_max, h_r)
                r+=1
            print ("h_right_max final=",h_right_max)
            h_final_i=min (h_left_max, h_right_max)
            water_i= max (h_final_i-h_i,0)

            water.append (water_i)
        print ("water",water)
        return sum(water)

