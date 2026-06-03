class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set()
        for num in nums:
            s.add(num)
        max_len=0
        current_len=0
        if s:
            for i in s:
                print (f"i={i}")
                if ((i-1) not in s):
                    print(f"(i-1)= {i-1} not in s")
                    current_len=1
                    print(f"(current_len)= {current_len}")
                    k=i+1
                    while k in s:
                        print(f"(k)= {k}")
                        current_len+=1
                        k+=1
                        print(f"(current_len)= {current_len}")
                    max_len = max(max_len, current_len)

                # print ("max_len=",max_len)
                # print ("current_len=",current_len)
            
        return max_len
