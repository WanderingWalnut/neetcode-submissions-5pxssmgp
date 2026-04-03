class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        l,r = 0,1

        while r < len(prices):
            # If buy price is lower than sell price
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(profit, maxProfit) # Update maxprofit if higher
                r += 1
            # If buy price is higher than sell price
            else:
                l = r # Set buy price to sell price
                r += 1
        
        return maxProfit
         

                




           