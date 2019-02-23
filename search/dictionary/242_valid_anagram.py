class Solution:
    def isAnagram(self, s: 'str', t: 'str') -> 'bool':
        counter = [0] * 26
        for c in s:
            counter[ord(c) - ord('a')] += 1
        for c in t:
            counter[ord(c) - ord('a')] -= 1
        for c in counter:
            if c != 0:
                return False
        return True
