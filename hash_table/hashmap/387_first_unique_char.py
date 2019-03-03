class Solution:
    def firstUniqChar(self, s: str) -> int:
        # solution 1
        # hmap = dict()
        # for i, c in enumerate(s):
        #     hmap[c] = hmap.get(c, 0) + 1
        # for i, c in enumerate(s):
        #     if hmap[c] == 1:
        #         return i
        # return -1

        # solution 2
        counter = [0] * 26
        for c in s:
            counter[ord(c) - ord('a')] += 1
        for i, c in enumerate(s):
            if counter[ord(c) - ord('a')] == 1:
                return i
        return -1


def test_solution():
    s = 'leetcode'
    assert Solution().firstUniqChar(s) == 0

    s = 'loveleetcode'
    assert Solution().firstUniqChar(s) == 2

    s = 'aassdd'
    assert Solution().firstUniqChar(s) == -1
