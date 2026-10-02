class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                curr = prices[j] - prices[i]
                if curr > max:
                    max = curr
        return max
                