class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:

        result = []
        count = 0

        for ch in reversed(s):

            if ch == "-":
                continue

            if count == k:
                result.append("-")
                count = 0

            result.append(ch.upper())
            count += 1

        return "".join(result[::-1])