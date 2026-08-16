class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(x):
            if x in memo:
                return memo[x]
            

            if x==1:
                return 1
            if x==2:
                return 2

            ans=dfs(x-1)+dfs(x-2)
            memo[x]=ans
            return ans
        return dfs(n)