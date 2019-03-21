class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, ans = 5, 0
        while n // i > 0:
            ans += n // i
            i *= 5
        return ans


def test_solution():
    assert Solution().trailingZeroes(3) == 0
    assert Solution().trailingZeroes(5) == 1
