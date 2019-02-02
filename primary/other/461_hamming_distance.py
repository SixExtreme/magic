class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # return bin(x ^ y).count('1')

        sum, xor = 0, x ^ y
        while xor != 0:
            sum += 1
            xor &= xor - 1
        return sum


def test_solution():
    x, y = 1, 4
    assert Solution().hammingDistance(x, y) == 2
