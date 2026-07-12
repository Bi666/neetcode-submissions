class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_in = float('inf')
        for p in prices:
            max_profit = max(max_profit, p - min_in)
            min_in = min(min_in, p)
        return max_profit