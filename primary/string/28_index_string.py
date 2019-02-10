class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # solution 1
        # if needle == '':
        #     return 0
        #
        # m, n = len(haystack), len(needle)
        # if m < n:
        #     return -1
        #
        # i = 0
        # while i < m:
        #     if haystack[i] == needle[0]:
        #         for j in range(1, n):
        #             if i + j >= m:
        #                 return -1
        #             elif haystack[i + j] != needle[j]:
        #                 break
        #         else:
        #             return i
        #     i += 1
        # return -1

        # solution 2
        # if needle == '':
        #     return 0
        #
        # m, n = len(haystack), len(needle)
        # if m < n:
        #     return -1
        #
        # i = 0
        # while i < m:
        #     if haystack[i] == needle[0]:
        #         if haystack[i:i+n] == needle:
        #             return i
        #     i += 1
        # return -1

        return haystack.index(needle) if needle in haystack else -1


def test_solution():
    haystack, needle = 'hello', 'll'
    assert Solution().strStr(haystack, needle) == 2

    haystack, needle = 'aaaaa', 'bba'
    assert Solution().strStr(haystack, needle) == -1


if __name__ == '__main__':
    for i in range(5):
        if i == 3:
            break
    else:
        print(i)
