class Solution:
    def climbStairs(self, n: int) -> int:

        one,two=1,0
        for i in range (n):
            temp=one
            one=one+two
            two=temp
        return one
'''
assume 
at the nth staircase: neither step can be taken (0);
at n-1th staircase: only 1 step can be taken (1)

at n-2th staircase: 
position n is where 2 steps taken (named two)
position n-1 is where 1 step taken (named one)
'''