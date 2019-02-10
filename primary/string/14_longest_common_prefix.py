class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        # solution 1
        # prefix = ''
        # if len(strs) == 0:
        #     return prefix
        #
        # ptr, min_len = 0, min([len(str) for str in strs])
        # for _ in range(min_len):
        #     ch = strs[0][ptr]
        #     for i in range(1, len(strs)):
        #         if strs[i][ptr] != ch:
        #             return prefix
        #     ptr, prefix = ptr + 1, prefix + ch
        #
        # return prefix

        # solution 2
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]

        prefix, chars = '', zip(*strs)
        for i, group in enumerate(chars):
            ch = group[0]
            for j in range(1, len(group)):
                if group[j] != ch:
                    return prefix
            prefix += strs[0][i]
        return prefix


def test_solution():
    strs = ['flower', 'flow', 'flight']
    assert Solution().longestCommonPrefix(strs) == 'fl'

    strs = ['dog', 'racecar', 'car']
    assert Solution().longestCommonPrefix(strs) == ''



