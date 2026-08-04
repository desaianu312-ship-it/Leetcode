class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [str(i) for i in range(1, n + 1)]
        factorial = [1] * n

        for i in range(1, n):
            factorial[i] = factorial[i - 1] * i

        k -= 1
        ans = []

        for i in range(n, 0, -1):
            index = k // factorial[i - 1]
            ans.append(numbers.pop(index))
            k %= factorial[i - 1]

        return "".join(ans)