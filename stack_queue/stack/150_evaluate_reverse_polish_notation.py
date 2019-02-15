class Solution:
    def evalRPN(self, tokens: 'List[str]') -> 'int':
        stack = []
        for token in tokens:
            if token is '+':
                a, b = stack.pop(), stack.pop()
                stack.append(b + a)
            elif token is '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif token is '*':
                a, b = stack.pop(), stack.pop()
                stack.append(b * a)
            elif token is '/':
                a, b = stack.pop(), stack.pop()
                pa = a if a > 0 else -a
                pb = b if b > 0 else -b
                res = pb // pa
                stack.append(res if a * b > 0 else -res)
            else:
                stack.append(int(token))
        return stack.pop()


def test_solution():
    tokens = ['2', '1', '+', '3', '*']
    assert Solution().evalRPN(tokens) == 9

    tokens = ['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+']
    assert Solution().evalRPN(tokens) == 22


if __name__ == '__main__':
    test_solution()
