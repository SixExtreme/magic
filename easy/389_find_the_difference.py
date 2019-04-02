class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # solution 1
        # _counter = [0] * 36
        # for ch in t:
        #     _counter[ord(ch) - ord('a')] += 1
        # for ch in s:
        #     _counter[ord(ch) - ord('a')] -= 1
        # for i in range(26):
        #     if _counter[i] != 0:
        #         return chr(97 + i)
        # return ''

        # solution 2
        # _map = dict()
        # for ch in t:
        #     _map[ch] = _map.get(ch, 0) + 1
        # for ch in s:
        #     _map[ch] -= 1
        # for k, v in _map.items():
        #     if v != 0:
        #         return k
        # return ''

        # solution 3
        # from collections import Counter
        # ans, _ = (Counter(t) - Counter(s)).popitem()
        # return ans

        # solution 4
        # ans = 0
        # for ch in s:
        #     ans ^= ord(ch)
        # for ch in t:
        #     ans ^= ord(ch)
        # return chr(ans)

        # solution 5
        ans = ord(t[-1])
        for i in range(len(s)):
            ans ^= ord(s[i])
            ans ^= ord(t[i])
        return chr(ans)


def test_solution():
    s, t = 'a', 'aa'
    assert Solution().findTheDifference(s, t) == 'a'

    s, t = 'abcd', 'abcde'
    assert Solution().findTheDifference(s, t) == 'e'
