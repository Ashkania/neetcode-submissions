class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sol1:
        # price_min = prices[0]
        # ans = 0
        # for price in prices:
        #     price_min = min(price_min, price)
        #     # profit = price - price_min
        #     ans = max(ans, price - price_min)
        # return ans

        # sol2: 2 pointer
        if len(prices) == 1:
            return 0
        
        profit_max = 0
        l_i, r_i = 0, 1 

        while r_i < len(prices):
            if prices[r_i] > prices[l_i]:
                profit_max = max(profit_max, prices[r_i] - prices[l_i])
            else:
                l_i = r_i
            r_i +=1
        return profit_max


