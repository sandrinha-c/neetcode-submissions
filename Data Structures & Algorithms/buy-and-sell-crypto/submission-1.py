class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best=0
        l=0
        while l <= len(prices)-1:
            for i in range(l,len(prices)):
                curr= prices[i]-prices[l]
                best=max(best, curr)
            l+=1
        return best