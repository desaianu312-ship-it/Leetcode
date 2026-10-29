from typing import List

class Solution:
    def palindromePath(self, n: int, edges: List[List[int]],
                       s: str, queries: List[str]) -> List[bool]:
        from collections import defaultdict

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        stack = [(0, -1, False)]
        while stack:
            u, p, exit_node = stack.pop()

            if not exit_node:
                parent[u] = p
                tin[u] = timer
                timer += 1
                stack.append((u, p, True))

                for v in reversed(graph[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, False))
            else:
                tout[u] = timer

        LOG = n.bit_length()
        up = [parent[:]]

        for _ in range(1, LOG):
            prev = up[-1]
            up.append([
                prev[prev[i]] if prev[i] != -1 else -1
                for i in range(n)
            ])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            for j in range(LOG):
                if diff & (1 << j):
                    u = up[j][u]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u, v = up[j][u], up[j][v]

            return parent[u]

        class BIT:
            def __init__(self, size):
                self.bit = [0] * (size + 2)

            def add(self, i, val):
                i += 1
                while i < len(self.bit):
                    self.bit[i] ^= val
                    i += i & -i

            def query(self, i):
                ans = 0
                i += 1
                while i > 0:
                    ans ^= self.bit[i]
                    i -= i & -i
                return ans

            def range_xor(self, l, r, val):
                self.add(l, val)
                if r + 1 < n:
                    self.add(r + 1, val)

        chars = list(s)
        bit = BIT(n)

        for u in range(n):
            mask = 1 << (ord(chars[u]) - ord('a'))
            bit.range_xor(tin[u], tout[u] - 1, mask)

        ans = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                delta = (1 << (ord(chars[u]) - ord('a'))) ^ \
                        (1 << (ord(c) - ord('a')))

                bit.range_xor(tin[u], tout[u] - 1, delta)
                chars[u] = c

            else:
                u, v = int(parts[1]), int(parts[2])
                w = lca(u, v)

                mask = bit.query(tin[u]) ^ bit.query(tin[v])
                mask ^= 1 << (ord(chars[w]) - ord('a'))

                ans.append(mask == 0 or (mask & (mask - 1)) == 0)

        return ans