class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1

        ans, carry = [], 0
        while i >= 0 or j >= 0:
            s = 0
            if i >= 0:
                s += ord(num1[i]) - ord('0')
            if j >= 0:
                s += ord(num2[j]) - ord('0')
            i -= 1
            j -= 1

            s += carry
            s, carry = s % 10, s // 10

            ans.append(str(s))

        if carry > 0:
            ans.append('1')

        return ''.join(reversed(ans))


def test_solution():
    assert Solution().addStrings('12', '13') == '25'
    assert Solution().addStrings('123', '12') == '135'
    assert Solution().addStrings('12', '123') == '135'


if __name__ == '__main__':
    test_solution()
