from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        wordLen = len(words[0])
        wordCount = len(words)
        totalLen = wordLen * wordCount

        wordFreq = Counter(words)
        ans = []

        for i in range(wordLen):
            left = i
            count = 0
            window = {}

            for right in range(i, len(s) - wordLen + 1, wordLen):
                word = s[right:right + wordLen]

                if word in wordFreq:
                    window[word] = window.get(word, 0) + 1
                    count += 1

                    while window[word] > wordFreq[word]:
                        leftWord = s[left:left + wordLen]
                        window[leftWord] -= 1
                        left += wordLen
                        count -= 1

                    if count == wordCount:
                        ans.append(left)

                        leftWord = s[left:left + wordLen]
                        window[leftWord] -= 1
                        left += wordLen
                        count -= 1

                else:
                    window.clear()
                    count = 0
                    left = right + wordLen

        return ans