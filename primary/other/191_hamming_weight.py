class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # return bin(n).count('1')

        sum = 0
        while n:
            sum += 1
            n &= n - 1
        return sum


def test_solution():
    n = 4
    assert Solution().hammingWeight(n) == 1
