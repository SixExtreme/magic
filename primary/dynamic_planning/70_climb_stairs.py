class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        f1, f2 = 1, 2
        for i in range(2, n):
            f1, f2 = f2, f1 + f2
        return f2


def test_solution():
    assert Solution().climbStairs(2) == 2
    assert Solution().climbStairs(3) == 3
