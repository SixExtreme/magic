class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '[':
                stack.append(']')
            elif c == '{':
                stack.append('}')
            elif len(stack) == 0 or stack.pop() != c:
                return False
        return len(stack) == 0


def test_solution():
    s = '()'
    assert Solution().isValid(s)

    s = '()[]{}'
    assert Solution().isValid(s)

    s = '{[()]}'
    assert Solution().isValid(s)

    s = '(]'
    assert not Solution().isValid(s)

    s = '([)]'
    assert not Solution().isValid(s)

