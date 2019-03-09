class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if len(haystack) < len(needle):
            return -1
        i = 0
        while i < len(haystack):
            if haystack[i] != needle[0]:
                i += 1
            else:
                if i + len(needle) > len(haystack):
                    break
                cnt, k = 0, i
                for j in range(len(needle)):
                    if k == i and haystack[i + j] == needle[0]:
                        k = i + j
                    if haystack[i + j] != needle[j]:
                        break
                    else:
                        cnt += 1
                if cnt == len(needle):
                    return i
                elif k > i:
                    i = k
                else:
                    i += cnt
        return -1


def test_solution():
    assert Solution().strStr("hello", "ll") == 2
    assert Solution().strStr("aaaaa", "bba") == -1
    assert Solution().strStr("mississippi", "issip") == 4
    assert Solution().strStr("mississippi", "issipi") == -1


if __name__ == '__main__':
    test_solution()
