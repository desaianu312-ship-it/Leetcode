class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = float("-inf")
        sold = 0
        rest = 0

        for price in prices:
            prevHold = hold
            prevSold = sold
            prevRest = rest

            hold = max(prevHold, prevRest - price)
            sold = prevHold + price
            rest = max(prevRest, prevSold)

        return max(sold, rest)
        