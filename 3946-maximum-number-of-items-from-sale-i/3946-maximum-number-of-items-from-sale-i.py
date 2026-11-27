
from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        dp = [0] * (budget + 1)
        min_price = min(price for _, price in items)

        for factor, price in items:
            count = sum(
                f % factor == 0
                for f, _ in items
            )

            # 0/1 Knapsack: activate each item type once
            for b in range(budget, price - 1, -1):
                dp[b] = max(dp[b], dp[b - price] + count)

        # Spend remaining budget on cheapest items
        return max(
            dp[b] + (budget - b) // min_price
            for b in range(budget + 1)
        )
