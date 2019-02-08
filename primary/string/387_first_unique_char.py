class Solution:
    def firstUniqChar(self, s: 'str') -> 'int':
        # solution 1
        # from collections import Counter
        # counter = Counter(s)
        # for i, c in enumerate(s):
        #     if counter.get(c) == 1:
        #         return i
        # return -1

        # solution2
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1
        for i, c in enumerate(s):
            if freq[ord(c) - ord('a')] == 1:
                return i
        return -1


def test_solution():
    s = 'leetcode'
    assert Solution().firstUniqChar(s) == 0

    s = 'loveleetcode'
    assert Solution().firstUniqChar(s) == 2

    s = 'aassdd'
    assert Solution().firstUniqChar(s) == -1
