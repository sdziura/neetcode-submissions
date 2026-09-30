# DP
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        best_profit = 0
        for i in prices[1:]:
            if i < min_buy:
                min_buy = i
            else:
                best_profit = max(best_profit, i - min_buy)
        return best_profit
