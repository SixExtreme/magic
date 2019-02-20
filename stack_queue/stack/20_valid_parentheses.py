class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # solution 1
        stack, pairs = [], {'(': ')', '[': ']', '{': '}'}
        for c in s:
            if len(stack) == 0:
                stack.append(c)
            else:
                peek = stack[-1]
                if peek in pairs and c == pairs[peek]:
                    stack.pop()
                else:
                    stack.append(c)
        return len(stack) == 0

        # solution 2
        # stack = []
        # for c in s:
        #     if c == '(':
        #         stack.append(')')
        #     elif c == '[':
        #         stack.append(']')
        #     elif c == '{':
        #         stack.append('}')
        #     elif len(stack) == 0 or stack.pop() != c:
        #         return False
        # return len(stack) == 0


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

