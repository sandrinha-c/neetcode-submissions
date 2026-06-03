class TimeMap:
    def __init__(self):
        self.store = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key]=[(value, timestamp)]      
        else:
            self.store[key].append ((value, timestamp))  
    def get(self, key: str, timestamp: int) -> str:
        if key in self.store: 
            key_list= self.store[key]
            #print ("key list=",key_list,"self.store[key][1][1]=",self.store[key][0][1])
            for i in range (len(self.store[key])-1,-1,-1):
                tme=self.store[key][i][1]
                print (tme)
                if tme <=timestamp: 
                    print (self.store[key][i][0])
                    return self.store[key][i][0]
            return ""
        else:
            return ""     
                    
# tmemap= TimeMap()
# tmemap.set("alice", "happy", 1)
# print (tmemap.store["alice"][0][1])
