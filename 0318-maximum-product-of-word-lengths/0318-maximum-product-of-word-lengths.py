class Solution:
    def maxProduct(self, words: List[str]) -> int:
        masks = {}
        ans = 0

        for word in words:
            mask = 0

            for ch in word:
                mask |= 1 << (ord(ch) - ord('a'))

            masks[mask] = max(masks.get(mask, 0), len(word))

        keys = list(masks.keys())

        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                if keys[i] & keys[j] == 0:
                    ans = max(ans, masks[keys[i]] * masks[keys[j]])

        return ans
        