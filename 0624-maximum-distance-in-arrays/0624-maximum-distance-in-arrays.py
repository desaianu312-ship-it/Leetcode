from typing import List

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        ans = 0

        for i in range(1, len(arrays)):
            first = arrays[i][0]
            last = arrays[i][-1]

            ans = max(
                ans,
                abs(last - min_val),
                abs(max_val - first)
            )

            min_val = min(min_val, first)
            max_val = max(max_val, last)

        return ans
        