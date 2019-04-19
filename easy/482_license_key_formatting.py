class Solution:
    # solution 1
    # def licenseKeyFormatting(self, S: str, K: int) -> str:
    #     count, i, ans = 0, len(S) - 1, []
    #     while i >= 0:
    #         if S[i].isalpha() or S[i].isdigit():
    #             ans.append(S[i].upper())
    #             count = (count + 1) % K
    #             if count == 0:
    #                 ans.append('-')
    #         i -= 1
    #     if ans and ans[-1] is '-':
    #         ans.pop()
    #     return ''.join(reversed(ans))

    # solution 2
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        ans = []
        for i in reversed(range(len(S))):
            if S[i] is not '-':
                if len(ans) % (K + 1) == K:
                    ans.append('-')
                ans.append(S[i].upper())
        return ''.join(reversed(ans))


def test_solution():
    S, K = '5F3Z-2e-9-w', 4
    assert Solution().licenseKeyFormatting(S, K) == '5F3Z-2E9W'

    S, K = '2-5g-3-J', 2
    assert Solution().licenseKeyFormatting(S, K) == '2-5G-3J'

    S, K = '--a-a-a-a--', 2
    assert Solution().licenseKeyFormatting(S, K) == 'AA-AA'

    S, K = '---', 3
    assert Solution().licenseKeyFormatting(S, K) == ''


if __name__ == '__main__':
    test_solution()
