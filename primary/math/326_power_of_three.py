import sys
import math

class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 3 ** math.floor(math.log(n, 3)) % n == 0


def test_solution():
    print(1162261467 * 3)
    assert Solution().isPowerOfThree() == True
