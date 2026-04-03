class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        l, r = 0, 1
        
        while r < len(prices):
            currentPrice = prices[l]
            sellPrice = prices[r]
            
            # When profit is greater than current maxProfit
            if sellPrice - currentPrice >= maxProfit:
                maxProfit = sellPrice - currentPrice
                r += 1
            # Found a better day to buy
            elif prices[r] < prices[l]:
                l = r
            # continue the process by increasing r pointer
            else:
                r += 1
        
        return maxProfit
            
        