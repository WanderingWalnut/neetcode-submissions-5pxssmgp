class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Calcualte profit at each window interval
        # l and r ptrs for our window
        # If currentProfit is greater than maxProfit move only R 
        # Basically find a better day to sell
        # If currentProfit is less than maxProfit move both ptrs

        maxProfit = 0


        for i in range(1, len(prices)):
            buyPrice = min(prices[:i])
            print("Buy Price: ", buyPrice)
            
            currentProfit = prices[i] - buyPrice
            print("Current Price: ", currentProfit)
            
            maxProfit = max(maxProfit, currentProfit)

        
        return maxProfit

                




           