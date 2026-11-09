from collections import defaultdict

class Solution:
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda a: a[1])

        q = sorted((time, i) for i, time in enumerate(queries))

        count = defaultdict(int)
        ans = [0] * len(queries)

        left = right = 0

        for time, idx in q:
            start = time - x

            while right < len(logs) and logs[right][1] <= time:
                server = logs[right][0]
                count[server] += 1
                right += 1

            while left < right and logs[left][1] < start:
                server = logs[left][0]
                count[server] -= 1

                if count[server] == 0:
                    del count[server]

                left += 1

            ans[idx] = n - len(count)

        return ans