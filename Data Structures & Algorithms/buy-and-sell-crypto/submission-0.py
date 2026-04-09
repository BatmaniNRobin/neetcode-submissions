class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1 # starts at one because selling it same day probably wont make you profit

        profit = 0 # stores max

        while r<len(prices):
            tmp = 0 # tmp max variable
            # if left > right 
            if prices[l] > prices[r]:
                l = r
            else:
                tmp = prices[r] - prices[l]
                r+=1
            profit = max(profit, tmp)

        return profit