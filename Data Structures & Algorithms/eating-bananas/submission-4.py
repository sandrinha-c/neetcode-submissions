import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(k,h):
            curr_h=0
            for pile in piles:
                curr_h+= math.ceil(pile/k)
            return curr_h<=h
        l=1
        r=max(piles)
        while l<r:
            mid=(l+r)//2
            if can_finish(mid,h):
                r=mid
            else:
                l=mid+1
        return l