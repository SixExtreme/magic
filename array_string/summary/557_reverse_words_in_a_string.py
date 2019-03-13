class Solution:
    def reverseWords(self, s: str) -> str:
        # solution 1
        # words = s[::-1].split(' ')
        # words.reverse()
        # return ' '.join(words)

        # solution 2
        ans, stk = [], []
        for ch in reversed(s):
            if ch != ' ':
                stk.append(ch)
            elif len(stk) > 0:
                ans.append(''.join(stk))
                stk.clear()
        ans.append(''.join(stk))
        return ' '.join(reversed(ans))


def test_solution():
    s = "Let's take LeetCode contest"
    assert Solution().reverseWords(s) == "s'teL ekat edoCteeL tsetnoc"
