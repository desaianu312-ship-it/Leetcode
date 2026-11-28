
from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        min_price = min(price for factor, price in items)
        max_factor = max(factor for factor, price in items)

        
        freq = [0] * (max_factor + 1)

        for factor, price in items:
            freq[factor] += 1

        
        for i in range(1, max_factor + 1):
            for j in range(2 * i, max_factor + 1, i):
                freq[i] += freq[j]

        
        opportunities = []

        for factor, price in items:
            gain = freq[factor] - 1

            if gain > 0 and price <= 2 * min_price:
                opportunities.append((price, gain))

        
        opportunities.sort()

        ans = 0

        for price, gain in opportunities:
            take = min(gain, budget // price)

            ans += 2 * take
            budget -= take * price

        
        ans += budget // min_price

        return ans
