class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        length = 0

        for ch in s:
            if ch in seen:
                seen.remove(ch)
                length += 2
            else:
                seen.add(ch)

        if seen:
            length += 1

        return length