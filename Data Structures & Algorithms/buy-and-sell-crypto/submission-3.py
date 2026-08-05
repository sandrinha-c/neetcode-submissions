class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best=0
        min_price=float("inf")
        for price in prices:
            profit= price-min_price
            best=max(best, profit)
            min_price=min(min_price,price)
        return best