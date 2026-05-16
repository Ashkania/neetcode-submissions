class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price_min = prices[0]
        ans = 0
        for price in prices:
            price_min = min(price_min, price)
            profit = price - price_min
            ans = max(ans, profit)
        return ans



