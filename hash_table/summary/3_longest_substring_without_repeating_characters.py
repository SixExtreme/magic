class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # solution 1
        # ans, hset = 0, set()
        #
        # i = 0
        # for j in range(len(s)):
        #     if s[j] in hset:
        #         while i < j and s[i] != s[j]:
        #             hset.remove(s[i])
        #             i += 1
        #         i += 1
        #     hset.add(s[j])
        #     ans = max(ans, j - i + 1)
        #
        # return ans

        # solution 2
        ans, hmap = 0, dict()
        i = 0
        for j in range(len(s)):
            if s[j] in hmap:
                i = max(i, hmap[s[j]] + 1)
            hmap[s[j]] = j
            ans = max(ans, j - i + 1)
        return ans


def test_solution():
    s = "abcabcbb"
    assert Solution().lengthOfLongestSubstring(s) == 3

    s = "bbbbb"
    assert Solution().lengthOfLongestSubstring(s) == 1

    s = "pwwkew"
    assert Solution().lengthOfLongestSubstring(s) == 3

