class Solution:
    def wordPattern(self, pattern: str, words: str) -> bool:
        # solution 1
        # words = words.split(' ')
        # if len(pattern) != len(words):
        #     return False
        # mp, mw = dict(), dict()
        # for i, ch in enumerate(pattern):
        #     if mp.get(ch, -1) != mw.get(words[i], -1):
        #         return False
        #     if ch not in mp and words[i] not in mw:
        #         mp[ch] = mw[words[i]] = i
        # return True

        # solution 2
        # words = words.split(' ')
        # if len(pattern) != len(words):
        #     return False
        # lsp = len(set(pattern))
        # lsw = len(set(words))
        # lsz = len(set(zip(pattern, words)))
        # return lsp == lsw == lsz

        # solution 3
        words = words.split(' ')
        if len(pattern) != len(words):
            return False
        hmap = dict()
        for i, ch in enumerate(pattern):
            if hmap.setdefault(ord(ch), i) != hmap.setdefault(words[i], i):
                return False
        return True


def test_solution():
    pattern, words = 'abc', "b c a"
    assert Solution().wordPattern(pattern, words)

    pattern, words = 'abba', "dog cat cat dog"
    assert Solution().wordPattern(pattern, words)

    pattern, words = 'abba', "dog cat cat fish"
    assert not Solution().wordPattern(pattern, words)

    pattern, words = 'aaaa', "dog cat cat dog"
    assert not Solution().wordPattern(pattern, words)

    pattern, words = 'abba', "dog dog dog dog"
    assert not Solution().wordPattern(pattern, words)
