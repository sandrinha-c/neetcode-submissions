class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set()
        for num in nums:
            s.add(num)
        max_len=0
        current_len=1
        if s:
            for i in range (min(s),max(s)+1):
                print ("i=",i)
                if i in s:
                    print (i,"in s")
                    if ((i-1) in s):
                        print ("current_len=", current_len)
                        print(f"(i-1)= {i-1} in s")
                        current_len+=1
                        #print ("current_len+=1=", current_len)
                        max_len = max(max_len, current_len)
                        #print ("max_len=",max_len)
                    else:
                        print(f"(i-1)={i-1} not in s")
                        current_len=1
                        max_len = max(max_len, current_len)
                print ("max_len=",max_len)
                print ("current_len=",current_len)
            
        return max_len
