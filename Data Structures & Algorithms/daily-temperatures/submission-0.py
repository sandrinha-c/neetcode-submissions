class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack= []
        result=[0]*len(temperatures)
        for i,t in enumerate(temperatures):
            if i == 0:
                stack.append(i)
            else:
                while stack and t> temperatures[stack[-1]]:
                    print("i=",i, "t=",t)
                    print("stack-before=",stack)
                    prev_day_idx=stack.pop()
                    result[prev_day_idx]=i-prev_day_idx
                    print("result[",i-1,"]=",result[i-1])
                stack.append(i)
                print("stack-after=",stack)
            print("result=",result)
        return result    

                
