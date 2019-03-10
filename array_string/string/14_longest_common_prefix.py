class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> str:
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]

        ans, chars = [], zip(*strs)
        for i, group in enumerate(chars):
            for j in range(1, len(group)):
                if group[j] != group[0]:
                    return ''.join(ans)
            ans.append(group[0])
        return ''.join(ans)


def test_solution():
    strs = ['flower', 'flow', 'flight']
    assert Solution().longestCommonPrefix(strs) == 'fl'

    strs = ['dog', 'racecar', 'car']
    assert Solution().longestCommonPrefix(strs) == ''


