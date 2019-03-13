class Solution:
    def reverseWords(self, s: str) -> str:
        ans, stk = [], []
        for i, ch in enumerate(s):
            if ch != ' ':
                stk.append(ch)
            elif len(stk) > 0:
                ans.append(''.join(stk))
                stk.clear()
        if len(stk) > 0:
            ans.append(''.join(stk))
        return ' '.join(reversed(ans))


def test_solution():
    assert Solution().reverseWords("   hello world!  ") == "world! hello"
    assert Solution().reverseWords("the sky is blue") == "blue is sky the"
    assert Solution().reverseWords("a good   example") == "example good a"


if __name__ == '__main__':
    test_solution()


