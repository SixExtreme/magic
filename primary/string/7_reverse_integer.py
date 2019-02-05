class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sum, tmp = 0, x if x > 0 else -x
        while tmp != 0:
            sum = sum * 10 + tmp % 10
            tmp //= 10

        if sum < -2**31 or sum > 2**31:
            return 0
        return sum if x > 0 else -sum


def test_solution():
    x = 123
    assert Solution().reverse(x) == 321

    x = -123
    assert Solution().reverse(x) == -321

    x = 120
    assert Solution().reverse(x) == 21


if __name__ == '__main__':
    test_solution()

