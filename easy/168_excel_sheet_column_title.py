from string import ascii_uppercase

class Solution:
    def convertToTitle(self, n: int) -> str:
        stk = []
        while n:
            k = n % 26
            stk.append(ascii_uppercase[k - 1])
            if k == 0:
                n -= 26
            n //= 26
        return ''.join(reversed(stk))


def test_solution():
    assert Solution().convertToTitle(1) == 'A'
    assert Solution().convertToTitle(28) == 'AB'
    assert Solution().convertToTitle(701) == 'ZY'
    assert Solution().convertToTitle(702) == 'ZZ'
