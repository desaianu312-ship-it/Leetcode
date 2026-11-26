
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        # Build original tree
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        # Track nodes with each character on current DFS path
        path = [[] for _ in range(26)]

        ans = [1] * n

        # Iterative DFS: (node, parent, state)
        stack = [(0, -1, 0)]

        while stack:
            node, par, state = stack.pop()
            c = ord(s[node]) - ord('a')

            if state == 0:
                path[c].append(node)

                stack.append((node, par, 1))

                for child in children[node]:
                    stack.append((child, node, 0))

            else:
                # Find closest ancestor with same character
                if len(path[c]) > 1:
                    new_parent = path[c][-2]
                else:
                    new_parent = par

                # Add completed subtree size to its new parent
                if new_parent != -1:
                    ans[new_parent] += ans[node]

                path[c].pop()

        return ans
