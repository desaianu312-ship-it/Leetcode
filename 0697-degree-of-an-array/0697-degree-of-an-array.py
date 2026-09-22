from typing import List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first = {}
        count = {}
        degree = 0
        ans = len(nums)

        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i

            count[num] = count.get(num, 0) + 1

            if count[num] > degree:
                degree = count[num]
                ans = i - first[num] + 1
            elif count[num] == degree:
                ans = min(ans, i - first[num] + 1)

        return ans