class TimeMap:
    def __init__(self):
        self.store={}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key]=[(value, timestamp)]
        else:
            self.store[key].append((value, timestamp))
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        key_list=self.store[key]
        print (key_list,"; target time=",timestamp)
        l,r=0,len(key_list)-1
        best_mood=""
        while l<=r:
            mid= (l+r)//2
            mid_tme,  mid_mood = key_list[mid][1], key_list[mid][0]
            print ("l:",l,"; r:",r,"mid:",mid,"; mid_tme=",mid_tme,"; mid_mood=",mid_mood)
            if mid_tme == timestamp:
                return mid_mood
            elif mid_tme > timestamp:
                r= mid-1
                print (mid_tme,">",timestamp , "r=mid-1=",r)
            elif mid_tme < timestamp:
                best_mood=key_list[mid][0]
                l=mid+1
                print (mid_tme,"<",timestamp , " l!=r  l=mid+1=",l)
            #print("mood:", mood)
        return best_mood
    
