class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        ans=[0]*len(temperatures)
        for i, temp in enumerate (temperatures):
            while stack and temp> temperatures[stack[-1]]:
                prev_idx=stack.pop()
                ans[prev_idx]=i-prev_idx
            stack.append(i)
        return ans