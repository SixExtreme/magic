from typing import List

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        # solution 1
        from collections import Counter

        license = ''.join(c.lower() for c in licensePlate if c.isalpha())
        plate = Counter(license)

        ans = ''
        for word in words:
            if plate & Counter(word) != plate:
                continue
            if ans == '' or len(ans) > len(word):
                ans = word
        return ans

        # solution 2
        # plate = [0] * 26
        # for c in licensePlate:
        #     if not c.isalpha():
        #         continue
        #     c = c.lower()
        #     plate[ord(c) - ord('a')] += 1
        #
        # ans, ref = -1, [0] * 26
        # for i, word in enumerate(words):
        #     for j in range(26):
        #         ref[j] = plate[j]
        #     for c in word:
        #         index = ord(c) - ord('a')
        #         if ref[index] != 0:
        #             ref[index] -= 1
        #     if sum(ref) != 0:
        #         continue
        #     if ans == -1 or len(word) < len(words[ans]):
        #         ans = i
        # return '' if ans == -1 else words[ans]

        # solution 3
        # primes = [
        #     2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
        #     47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103
        # ]
        #
        # def to_val(s: str):
        #     val = 1
        #     for c in s:
        #         if not c.isalpha():
        #             continue
        #         val *= primes[ord(c.lower()) - ord('a')]
        #     return val
        #
        # index, pval = -1, to_val(licensePlate)
        # for i, word in enumerate(words):
        #     if to_val(word) % pval != 0:
        #         continue
        #     if index == -1 or len(word) < len(words[index]):
        #         index = i
        # return '' if index == -1 else words[index]


def test_solution():
    licensePlate = "1s3 PSt"
    words = ["step", "steps", "stripe", "stepple"]
    assert Solution().shortestCompletingWord(licensePlate, words) == 'steps'

    licensePlate = "1s3 456"
    words = ["looks", "pest", "stew", "show"]
    assert Solution().shortestCompletingWord(licensePlate, words) == 'pest'
