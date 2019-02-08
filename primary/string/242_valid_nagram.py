class Solution:
    def isAnagram(self, s: 'str', t: 'str') -> 'bool':
        # solution 1
        # from collections import Counter
        # return Counter(s) == Counter(t)

        # solution2
        if len(s) != len(t):
            return False

        freq = [0] * 26
        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')] += 1
            freq[ord(t[i]) - ord('a')] -= 1
        for i in range(26):
            if freq[i] != 0:
                return False
        return True


def test_solution():
    assert Solution().isAnagram('anagram', 'nagaram')
    assert not Solution().isAnagram('rat', 'car')
