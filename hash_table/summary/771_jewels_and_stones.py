class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # solution 1
        # ans, hset = 0, set(J)
        # for ch in S:
        #     if ch in hset:
        #         ans += 1
        # return ans

        # solution 2
        hmap = [None] * 26
        for ch in J:
            key = ord(ch.lower()) - ord('a')
            if hmap[key] is None:
               hmap[key] = []
            hmap[key].append(ch)
        ans = 0
        for ch in S:
            chars = hmap[ord(ch.lower()) - ord('a')]
            if chars and ch in chars:
                ans += 1
        return ans


def test_solution():
    J, S = 'aA', 'aAAbbbb'
    assert Solution().numJewelsInStones(J, S) == 3

