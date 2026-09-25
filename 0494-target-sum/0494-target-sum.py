from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}

        for num in nums:
            new_dp = {}

            for total, ways in dp.items():
                new_dp[total + num] = new_dp.get(total + num, 0) + ways
                new_dp[total - num] = new_dp.get(total - num, 0) + ways

            dp = new_dp

        return dp.get(target, 0)