class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p=float("inf")
        max_profit=0
        for price in prices:
            profit= price-min_p
            max_profit=max(profit, max_profit)
            min_p=min(min_p, price)
        return max_profit