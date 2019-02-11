class Solution:
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans, s = 0, s.strip()
        if len(s) == 0:
            return ans

        i, positive = 0, True
        if s[0] == '+' or s[0] == '-':
            i, positive = 1, s[i] == '+'

        while i < len(s):
            if not s[i].isdigit():
                break
            else:
                ans = ans * 10 + (ord(s[i]) - ord('0'))
            i += 1

        min_i32, max_i32 = -2 ** 31, 2 ** 31 - 1
        return  min(ans, max_i32) if positive else max(min_i32, -ans)


def test_solution():
    assert Solution().myAtoi('42') == 42
    assert Solution().myAtoi('-42') == -42
    assert Solution().myAtoi('words and 987') == 0
    assert Solution().myAtoi('4193 with words') == 4193
