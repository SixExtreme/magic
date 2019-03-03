class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ms, mt = dict(), dict()
        for i in range(len(s)):
            if ms.get(s[i], '') != mt.get(t[i], ''):
                return False
            ms[s[i]], mt[t[i]] = i, i
        return True


def test_solution():
    s, t = 'egg', 'add'
    assert Solution().isIsomorphic(s, t)

    s, t = 'foo', 'bar'
    assert not Solution().isIsomorphic(s, t)

    s, t = 'paper', 'title'
    assert Solution().isIsomorphic(s, t)

    s, t = 'ab', 'aa'
    assert not Solution().isIsomorphic(s, t)
