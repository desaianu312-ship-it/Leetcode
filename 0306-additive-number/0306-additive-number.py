class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        n = len(num)

        def valid(start, length):
            return length == 1 or num[start] != "0"

        for i in range(1, n):
            if not valid(0, i):
                break

            for j in range(i + 1, n):
                if not valid(i, j - i):
                    break

                a = int(num[:i])
                b = int(num[i:j])
                k = j

                while k < n:
                    c = a + b
                    s = str(c)

                    if not num.startswith(s, k):
                        break

                    k += len(s)
                    a, b = b, c

                if k == n:
                    return True

        return False
        