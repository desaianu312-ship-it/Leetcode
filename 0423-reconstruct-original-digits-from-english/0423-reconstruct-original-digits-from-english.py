class Solution:
    def originalDigits(self, s: str) -> str:
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        digit = [0] * 10

        # Unique letters
        digit[0] = count[ord('z') - ord('a')]
        digit[2] = count[ord('w') - ord('a')]
        digit[4] = count[ord('u') - ord('a')]
        digit[6] = count[ord('x') - ord('a')]
        digit[8] = count[ord('g') - ord('a')]

        # Remaining digits
        digit[3] = count[ord('h') - ord('a')] - digit[8]
        digit[5] = count[ord('f') - ord('a')] - digit[4]
        digit[7] = count[ord('s') - ord('a')] - digit[6]
        digit[1] = count[ord('o') - ord('a')] - digit[0] - digit[2] - digit[4]
        digit[9] = count[ord('i') - ord('a')] - digit[5] - digit[6] - digit[8]

        ans = []

        for i in range(10):
            ans.append(str(i) * digit[i])

        return ''.join(ans)