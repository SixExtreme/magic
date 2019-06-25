from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set = set(banned)
        chars = []
        for ch in paragraph:
            if not ch.isalpha():
                chars.append(' ')
            else:
                chars.append(ch.lower())
        words = ''.join(chars).strip().split()

        ans, counter = '', dict()
        for word in words:
            if word in banned_set:
                continue
            counter[word] = counter.get(word, 0) + 1
            if counter[word] > counter.get(ans, 0):
                ans = word

        return ans


def test_solution():
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ['hit']
    assert Solution().mostCommonWord(paragraph, banned) == 'ball'
