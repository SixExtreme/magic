class Solution:
    def isIsomorphic(self, s: 'str', t: 'str') -> 'bool':
        # solution 1
        # st, ts = dict(), dict()
        # for i in range(len(s)):
        #     if s[i] not in st and t[i] not in ts:
        #         st[s[i]] = t[i]
        #         ts[t[i]] = s[i]
        #     if st.get(s[i], '') != t[i] or ts.get(t[i], '') != s[i]:
        #         return False
        # return True

        # solution 2
        st, ts = dict(), dict()
        for i in range(len(s)):
            if st.get(s[i], '') != ts.get(t[i], ''):
                return False
            st[s[i]], ts[t[i]] = i, i
        return True


def test_solution():
    s, t = 'egg', 'add'
    assert Solution().isIsomorphic(s, t)

    s, t = 'foo', 'bar'
    assert not Solution().isIsomorphic(s, t)

    s, t = 'paper', 'title'
    assert Solution().isIsomorphic(s, t)

    s, t = 'ab', 'aa'
    assert Solution().isIsomorphic(s, t)


if __name__ == '__main__':
    test_solution()
